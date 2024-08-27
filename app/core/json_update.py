import json
import os
from app.config.paths import JSON_PATH

def process_json_input(tag, component, value):
    # Construct the file path using the tag as the file name
    file_path = os.path.join(JSON_PATH, f"{tag}.json")

    # Check if the JSON file exists
    if os.path.exists(file_path):
        with open(file_path, 'r+', encoding='utf-8') as json_file:
            data = json.load(json_file)

            # The root key of the JSON is the same as the tag
            root_key = tag

            # Check if the component and value are already present
            for entry in data.get(root_key, []):
                if entry.get('PhwebDescription') == component and entry.get('ContainerValue') == value:
                    raise ValueError("Value already in JSON")  # Raise an error if the component and value are already in the file

            # If not present, add the new component and value
            data[root_key].append({
                'PhwebDescription': component,
                'ContainerValue': value
            })

            # Move the cursor to the beginning and truncate the file before writing
            json_file.seek(0)
            json_file.truncate()
            json.dump(data, json_file, indent=4)

    else:
        # If the file doesn't exist, raise an error
        raise FileNotFoundError("JSON file not found. Please ensure the file exists before attempting to update it.")
