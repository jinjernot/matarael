import os
import json
import pandas as pd

# Folder containing the JSON files
folder_path = 'app/data/json'

# Initialize a list to store duplicate information
duplicates_info = []

# Function to identify duplicates in a JSON file
def find_duplicates_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
        data = json.load(file)

    # Loop through each section in the JSON file
    for section_name, items in data.items():
        # Extract pairs from each section
        item_pairs = [(item["PhwebDescription"], item["ContainerValue"]) for item in items]

        # Identify duplicates
        seen_pairs = set()
        duplicates = []
        for pair in item_pairs:
            if pair in seen_pairs:
                duplicates.append(pair)
            else:
                seen_pairs.add(pair)

        # Store duplicates with section information
        for pair in duplicates:
            duplicates_info.append({
                "FileName": os.path.basename(file_path),
                "Section": section_name,
                "PhwebDescription": pair[0],
                "ContainerValue": pair[1]
            })

# Iterate over all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        find_duplicates_in_file(file_path)

# Convert duplicates info to a DataFrame
df = pd.DataFrame(duplicates_info)

# Save DataFrame to an XLSX file
output_file = 'duplicates_info.xlsx'
df.to_excel(output_file, index=False)

print(f"Duplicates information has been saved to {output_file}")
