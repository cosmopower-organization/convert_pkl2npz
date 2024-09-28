# script adapated from @dpiras: https://github.com/dpiras/cosmopower-jax/blob/main/convert_tf214.py

# script to take a .pkl file containing a trained model with CP TF<2.14, 
# and convert it to a numpy format that is readable even if the TF version is >=2.14,
# namely, avoiding pickle.
# You only need to run this once using TF<2.14 (was tested on TF=2.13), 
# and this creates the numpy file replacing the pickle file.
# After running this script you should be able to run CPJ with TF>=2.14.
# Inputs are name of the pkl file to convert, and whether pca was used or not.
# NOTE: if you want to use `filepath` with TF>=2.14, make sure you adapt this script
# so that you have the .npz dictionary in your `filepath` folder.
import numpy as np
import pickle
import sys, ast, os

def convert_pkl_to_npz(pkl_filepath, pca=False):
    # Load the pickle file
    with open(pkl_filepath, 'rb') as f:
        pickle_file = pickle.load(f)

    # Select the variable names based on PCA flag
    if pca:
        variable_names = ['weights_', 'biases_', 'alphas_', 'betas_', \
                          'param_train_mean', 'param_train_std', \
                          'pca_mean', 'pca_std', \
                          'feature_train_mean', 'feature_train_std', \
                          'parameters', 'n_parameters', \
                          'modes', 'n_modes', \
                          'n_pcas', 'pca_transform_matrix', \
                          'n_hidden', 'n_layers', 'architecture']
    else:
        variable_names = ['weights_', 'biases_', 'alphas_', 'betas_', \
                          'param_train_mean', 'param_train_std', \
                          'feature_train_mean', 'feature_train_std', \
                          'n_parameters', 'parameters', \
                          'n_modes', 'modes', \
                          'n_hidden', 'n_layers', 'architecture']

    # Check if the number of variables is consistent with the pickle file
    assert len(variable_names) == len(pickle_file), \
        "Length of loaded variables is inconsistent, make sure the PCA flag is used only if loading a PCA model"

    # Create the new dictionary
    new_dict = {name: value for name, value in zip(variable_names, pickle_file)}

    # Save as .npz file in the same directory
    npz_filepath = pkl_filepath.replace('.pkl', '.npz')
    np.savez(npz_filepath, new_dict)
    print(f"Converted {pkl_filepath} to {npz_filepath}")

if __name__ == "__main__":
    # Expecting 2 arguments: pkl file path and PCA flag
    if len(sys.argv) < 2:
        print("Usage: python convert_pkl2npz.py <pkl_file> [pca_flag]")
        sys.exit(1)

    pkl_filepath = sys.argv[1]
    pca = ast.literal_eval(sys.argv[2]) if len(sys.argv) > 2 else False

    convert_pkl_to_npz(pkl_filepath, pca)

