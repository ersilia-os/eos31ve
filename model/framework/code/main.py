# imports
import os
import pandas as pd
import csv
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.hlm.hlm_predictor import HLMPredictor 
from predictors.utilities.utilities import addMolsKekuleSmilesToFrame 


# pass the input file
input_file = sys.argv[1]
# pass the output file
output_file = sys.argv[2]


def predict_df(
    smiles_list, 
    smi_column_name='smiles', 
    models=['hlm']
    ):
    
    df = pd.DataFrame({smi_column_name: smiles_list})    
    response = {} 
    working_df = df.copy() 
    addMolsKekuleSmilesToFrame(working_df, smi_column_name) 
    working_df = working_df[~working_df['mols'].isnull() & ~working_df['kekule_smiles'].isnull()] 

    for model in models:
        response[model] = {}        
        if model.lower() == 'hlm': 
            predictor = HLMPredictor(
                kekule_smiles = working_df['kekule_smiles'].values, 
                smiles=working_df[smi_column_name].values
                )
        else:
            break

        pred_df = predictor.get_predictions()
        pred_df = working_df.join(pred_df)
        pred_df.drop(
            ['mols', 'kekule_smiles'], 
            axis=1, 
            inplace = True
            )

        # columns not present in original df
        diff_cols = pred_df.columns.difference(df.columns)
        df_res = pred_df[diff_cols]

        # making sure the response df is of the exact same length (rows) as original df
        response_df = pd.merge(
            df, 
            df_res, 
            left_index=True, 
            right_index=True, 
            how='inner'
            )
        return response_df
      
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output_df = predict_df(smiles_list)
print(output_df)

OUTPUT_COLUMN_NAME = "Predicted Class (Probability)"


outputs = []
for x in list(output_df[OUTPUT_COLUMN_NAME]):
    c = x.split(" ")[0]
    p = float(x.split("(")[1].split(")")[0])
    outputs += [p]


# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["proba1"]) # header
    for o in outputs:
        writer.writerow([o])