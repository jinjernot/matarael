import os
import json

# Define the folder path where the JSON files are located
folder_path = './app/data/json_granular'

# Function to clean up the JSON file
def clean_json_file(file_path):
    # Read the JSON content
    with open(file_path, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file {file_path}: {e}")
            return

    # Check if the data is a dictionary
    if not isinstance(data, dict):
        print(f"Unexpected structure in {file_path}, skipping...")
        return

    # Function to recursively replace the Unicode sequence and common encoding issues
    def replace_unicode(obj):
        if isinstance(obj, dict):
            return {key: replace_unicode(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [replace_unicode(item) for item in obj]
        elif isinstance(obj, str):
            # Replace common problematic characters
            return (obj
                    .replace('\u00c2\u00ae', '®')  # Specific Unicode to registered trademark
                    .replace('â„¢', '®')           # Common encoding error for registered trademark
                   )
        return obj

    # Replace the Unicode sequences in the data
    cleaned_data = replace_unicode(data)

    # Write the cleaned data back to the file
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(cleaned_data, json_file, indent=4, ensure_ascii=False)

# Loop through the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):  # Check if the file is a JSON file
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            print(f"Cleaning file: {file_path}")
            clean_json_file(file_path)
        else:
            print(f"File not found: {file_path}")

print("Cleanup completed.")
