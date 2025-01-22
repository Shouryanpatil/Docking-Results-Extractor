import os
import pandas as pd

# Define the main folder containing all the 14 folders
main_folder = "E:/Project/Colon Cancer"
output_excel = "E:/Project/Colon Cancer/docking_results.xlsx"

# List to store the extracted information
results = []

# Traverse through each main folder (like AKT)
for main_subfolder in os.listdir(main_folder):
    main_subfolder_path = os.path.join(main_folder, main_subfolder)

    # Check if it is a directory
    if os.path.isdir(main_subfolder_path):
        for subfolder in os.listdir(main_subfolder_path):
            subfolder_path = os.path.join(main_subfolder_path, subfolder)

            # Check if it is a directory
            if os.path.isdir(subfolder_path):
                dlg_file = os.path.join(subfolder_path, "dock.dlg")

                # Check if dock.dlg exists in the subfolder
                if os.path.exists(dlg_file):
                    cluster_rank = ""
                    free_energy = ""
                    inhibition_constant = ""

                    # Parse the dock.dlg file
                    with open(dlg_file, "r") as file:
                        lines = file.readlines()
                        for i, line in enumerate(lines):
                            # Look for Cluster Rank = 1
                            if "Cluster Rank = 1" in line:
                                # Extract the Estimated Free Energy of Binding
                                for j in range(i, i + 10):  # Scan the next few lines for relevant data
                                    if "Estimated Free Energy of Binding" in lines[j]:
                                        free_energy = lines[j].split("=")[1].strip()
                                        free_energy = free_energy.split("[")[0].strip()  # Remove extra info
                                    if "Estimated Inhibition Constant, Ki" in lines[j]:
                                        inhibition_constant = lines[j].split("=")[1].strip()
                                        inhibition_constant = inhibition_constant.split("[")[0].strip()  # Remove extra info
                                break

                    # Append the extracted information to the list
                    results.append({
                        "Main Folder": main_subfolder,
                        "Subfolder": subfolder,
                        "Cluster Rank": "1",
                        "Estimated Free Energy of Binding": free_energy,
                        "Estimated Inhibition Constant (Ki)": inhibition_constant
                    })

# Create a DataFrame and save it as an Excel file
df = pd.DataFrame(results)
df.to_excel(output_excel, index=False)

print(f"Docking results have been saved to {output_excel}")
