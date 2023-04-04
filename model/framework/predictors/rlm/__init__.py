import sys
import os

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.utilities.utilities import load_gcnn_model

rlm_model_file_url = os.path.abspath(os.path.join(root, '../../../checkpoints/rlm_model.pt'))
rlm_model_file_path = os.path.abspath(os.path.join(root, '../../../checkpoints/rlm_model.pt'))

print(f'Loading RLM graph convolutional neural network model', file=sys.stdout)

rlm_gcnn_scaler, rlm_gcnn_model = load_gcnn_model(rlm_model_file_path, rlm_model_file_url)

del rlm_model_file_url
del rlm_model_file_path

print(f'Finished loading RLM model files', file=sys.stdout)
