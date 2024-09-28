#!/bin/bash

# Base directory containing the models
BASE_DIR="./cosmopower-organization"

# Loop over all subdirectories in the cosmopower-organization
find "$BASE_DIR" -name "*.pkl" | while read -r pkl_file; do
    # Check if the file is from a TE model, for which PCA should be used
    if [[ "$pkl_file" == *"TE_"* ]]; then
        echo "Converting TE model with PCA: $pkl_file"
        python convert_pkl2npz.py "$pkl_file" True
    else
        echo "Converting non-TE model: $pkl_file"
        python convert_pkl2npz.py "$pkl_file" False
    fi
done
