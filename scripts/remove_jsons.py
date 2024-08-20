import os
import json

# Folder containing the JSON files
folder_path = 'app/data/json'

# Function to remove duplicates in a JSON file and update it
def remove_duplicates_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Track whether the file was updated
    updated = False

    # Loop through each section in the JSON file
    for section_name, items in data.items():
        # Extract pairs from each section
        seen_pairs = set()
        unique_items = []
        for item in items:
            pair = (item["PhwebDescription"], item["ContainerValue"])
            if pair not in seen_pairs:
                unique_items.append(item)
                seen_pairs.add(pair)
            else:
                updated = True  # Mark the file as updated if a duplicate was found

        # Update the section with only unique items
        data[section_name] = unique_items

    # If the file was updated, overwrite it with the updated data
    if updated:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# Iterate over all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        remove_duplicates_in_file(file_path)

print("Duplicate pairs have been removed and JSON files updated.")
