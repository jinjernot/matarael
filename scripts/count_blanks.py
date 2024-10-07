import os
import json

def count_blank_values(folder_path):
    blank_count = 0

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            # Load JSON data from the file with explicit encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

            # Iterate over the pairs of values and count '[BLANK]' occurrences
            filename_without_extension = os.path.splitext(filename)[0]
            if filename_without_extension in json_data:
                for pair in json_data[filename_without_extension]:
                    if pair['ContainerValue'] == '[BLANK]':
                        blank_count += 1

    print(f'Total number of "[BLANK]" values: {blank_count}')
    return blank_count

# Specify the folder path
folder_path = './app/data/json_granular'
count_blank_values(folder_path)