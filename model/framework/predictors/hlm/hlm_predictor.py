import numpy as np
import pandas as pd
from pandas import DataFrame
import pickle
import warnings
warnings.filterwarnings('ignore')
import sys
import os
from ..utilities.utilities import get_processed_smi
from numpy import array
from chemprop.chemprop.data.utils import get_data, get_data_from_smiles
from chemprop.chemprop.data import MoleculeDataLoader, MoleculeDataset
from chemprop.chemprop.train import predict
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, "../predictors"))

from hlm import hlm_gcnn_scaler, hlm_gcnn_model
from ..rlm import rlm_gcnn_scaler, rlm_gcnn_model
from base.gcnn import GcnnBase
import time

class HLMPredictor(GcnnBase):
    """
    Makes HLM stability preditions

    Attributes:
        df (DataFrame): DataFrame containing column with smiles
        smiles_column_index (int): index of column containing smiles
        predictions_df (DataFrame): DataFrame hosting all predictions
    """

    def __init__(self, kekule_smiles: array = None, smiles: array = None):
        """
        Constructor for HLMPredictior class
        Parameters:
            kekule_smiles (Array): numpy array of RDkit molecules
        """
        GcnnBase.__init__(self, kekule_smiles, column_dict_key='Predicted Class (Probability)', columns_dict_order = 1, smiles=smiles)

        # add RLM predictions as additional features along with SMILES
        rlm_predictions, rlm_labels = self.gcnn_predict(rlm_gcnn_model, rlm_gcnn_scaler)
        if rlm_predictions is not None:
            self.additional_features = rlm_predictions.tolist()
        else:
            print(f'No RLM Predictions')


        self._columns_dict['Prediction'] = {
            'order': 2,
            'description': 'class label',
            'isSmilesColumn': False
        }

        self.model_name = 'hlm'

    def get_predictions(self) -> DataFrame:
        """
        Function that calculates consensus predictions
        Returns:
            Predictions (DataFrame): DataFrame with all predictions
        """

        if len(self.kekule_smiles) > 0:

            start = time.time()
            gcnn_predictions, gcnn_labels = self.gcnn_predict(hlm_gcnn_model, hlm_gcnn_scaler)
            end = time.time()
            print(f'HLM: {end - start} seconds to predict {len(self.predictions_df.index)} molecules')

            self.predictions_df['Prediction'] = pd.Series(
                pd.Series(np.where(gcnn_predictions>=0.5, 'unstable', 'stable'))
            )

            # if not intrprt_df.empty:
            #     intrprt_df['final_smiles'] = np.where(intrprt_df['rationale_score']>0, intrprt_df['smiles'].astype(str)+'_'+intrprt_df['rationale_smiles'].astype(str), intrprt_df['smiles'].astype(str))
            #     self.predictions_df['mol'] = pd.Series(intrprt_df['final_smiles'].tolist())

        return self.predictions_df