import sys
import os

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.utilities.utilities import load_gcnn_model


hlm_model_file_url = os.path.abspath(os.path.join(root, '../../../checkpoints/gcnn_model.pt'))
hlm_model_file_path = os.path.abspath(os.path.join(root, '../../../checkpoints/gcnn_model.pt'))
rlm_model_file_url = os.path.abspath(os.path.join(root, '../../../checkpoints/rlm_gcnn_model.pt'))
rlm_model_file_path = os.path.abspath(os.path.join(root, '../../../checkpoints/rlm_gcnn_model.pt'))


print(f'Loading Human Liver Microsomal Stability model', file=sys.stdout)
hlm_gcnn_scaler, hlm_gcnn_model = load_gcnn_model(hlm_model_file_path, hlm_model_file_url)
rlm_gcnn_scaler, rlm_gcnn_model = load_gcnn_model(rlm_model_file_path, rlm_model_file_url)

del hlm_model_file_url
del hlm_model_file_path
del rlm_model_file_url
del rlm_model_file_path

print(f'Finished loading Human Liver Microsomal Stability model', file=sys.stdout)