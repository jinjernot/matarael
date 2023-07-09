import os
import json

def find_duplicates_in_folder(folder_path):
    # Dictionary to store encountered pairs per file
    file_pairs = {}

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            # Load JSON data from the file with explicit encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

            # Iterate over the pairs of values and check for duplicates
            filename_without_extension = os.path.splitext(filename)[0]
            if filename_without_extension in json_data:
                file_pairs[filename] = set()
                for pair in json_data[filename_without_extension]:
                    phweb_description = pair['PhwebDescription']
                    container_value = pair['ContainerValue']
                    value_pair = (phweb_description, container_value)

                    # Check for duplicates within the same file
                    if value_pair in file_pairs[filename]:
                        print(f'Duplicate pair found in {filename}: {value_pair}')
                    else:
                        file_pairs[filename].add(value_pair)

folder_path = './json'
find_duplicates_in_folder(folder_path)
