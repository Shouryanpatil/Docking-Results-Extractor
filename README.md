# Docking Results Extractor

This repository contains a Python script for parsing and extracting key information from docking result files (`dock.dlg`). The script is designed to navigate through a structured folder hierarchy, locate `dock.dlg` files, and extract details such as:

- **Cluster Rank = 1**
- **Estimated Free Energy of Binding**
- **Estimated Inhibition Constant (Ki)**

The extracted data is saved into an Excel file for further analysis.

## Folder Structure

The script assumes the following folder structure:

```
main_folder
|-- Protein1
|   |-- Ligand1
|   |   |-- dock.dlg
|   |-- Ligand2
|       |-- dock.dlg
|-- Protein2
    |-- Ligand1
    |   |-- dock.dlg
    |-- Ligand2
        |-- dock.dlg
```

- `main_folder`: Contains subfolders named after proteins.
- Each protein folder contains subfolders named after ligands.
- Each ligand folder contains a `dock.dlg` file with docking results.

## Script Overview

The Python script performs the following steps:

1. **Traverse Folder Hierarchy**: Iterates through all protein and ligand folders.
2. **Check for `dock.dlg` File**: Verifies the presence of the docking result file in each ligand folder.
3. **Extract Information**:
   - Reads the `dock.dlg` file.
   - Searches for **Cluster Rank = 1**.
   - Extracts:
     - **Estimated Free Energy of Binding**
     - **Estimated Inhibition Constant (Ki)**
4. **Save to Excel**: Consolidates the extracted data into an Excel file (`docking_results.xlsx`).

## Requirements

- Python 3.x
- pandas

Install the required library using pip:
```bash
pip install pandas
```

## Usage

1. Place your protein and ligand folders inside the working directory of the script.

2. Open IDLE Shell, press `Ctrl+N`, and open the `docking_results_extractor.py` file.

3. Update the following variables in the script with your folder paths:
   ```python
   main_folder = "E:/Project/Colon Cancer"
   output_excel = "E:/Project/Colon Cancer/docking_results.xlsx"
   ```

4. Run the Python file.

5. The extracted results will be saved to `docking_results.xlsx` in the specified output path.

## Output Format

The Excel file contains the following columns:

- **Main Folder**: Name of the protein folder.
- **Subfolder**: Name of the ligand folder.
- **Cluster Rank**: Cluster rank (default is 1).
- **Estimated Free Energy of Binding**: Extracted value from the docking file.
- **Estimated Inhibition Constant (Ki)**: Extracted value from the docking file.

## Example Output

| Main Folder | Subfolder | Cluster Rank | Estimated Free Energy of Binding | Estimated Inhibition Constant (Ki) |
|-------------|-----------|--------------|----------------------------------|-----------------------------------|
| Protein1    | Ligand1   | 1            | -7.8 kcal/mol                   | 1.2 µM                            |
| Protein1    | Ligand2   | 1            | -6.5 kcal/mol                   | 2.3 µM                            |
| Protein2    | Ligand1   | 1            | -8.1 kcal/mol                   | 0.9 µM                            |

## Notes

- Ensure that all `dock.dlg` files follow the standard format expected by the script.
- Modify the script as needed for custom folder structures or additional data extraction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute by submitting issues or pull requests!
