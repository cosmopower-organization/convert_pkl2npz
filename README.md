# convert_pkl2npz

## Instructions to Convert `.pkl` Files to `.npz` Format

Follow these steps to convert all `.pkl` files in the `cosmopower-organization` directory to `.npz` format using the provided Python and shell scripts.

### Steps

1. **Download the Python Script:**
   Save the `convert_pkl2npz.py` script in the root directory.

2. **Download the Shell Script:**
   Save the `convert_all_pkl2npz.sh` script in the same directory.

3. **Make the Python Script Executable:**
   Run the following command in the terminal:
   ```bash
   chmod +x convert_pkl2npz.py
   ```

4. **Make the Shell Script Executable:**
   Run the following command in the terminal:
   ```bash
   chmod +x convert_all_pkl2npz.sh
   ```

5. **Run the Shell Script:**
   Execute the shell script to process all `.pkl` files in the `cosmopower-organization` directory:
   ```bash
   ./convert_all_pkl2npz.sh
   ```

This will automatically convert all `.pkl` files to `.npz` files. Note that for the TE models, the script will apply PCA as specified.
