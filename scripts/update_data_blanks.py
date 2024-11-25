import json
import os

def update_json_files(json_folder, update_folder):
    # Get a list of JSON files in the json_folder
    json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]
    
    # Loop through each update JSON file
    for update_file in os.listdir(update_folder):
        if update_file.endswith('.json'):
            update_path = os.path.join(update_folder, update_file)
            with open(update_path, 'r', encoding='utf-8') as update_f:
                update_data = json.load(update_f)
            
            # Check if the corresponding JSON file exists in json_folder
            target_file = os.path.join(json_folder, update_file)
            if target_file in json_files:
                with open(target_file, 'r', encoding='utf-8') as target_f:
                    target_data = json.load(target_f)
                
                # Create a mapping for easy look-up of update values
                update_dict = {item["Component"]: item["ContainerValue"] for item in update_data[update_file]}
                
                # Loop through the target data and update ContainerValue where needed
                for item in target_data[update_file]:
                    component = item["Component"]
                    if component in update_dict and item["ContainerValue"] == "[BLANK]":
                        item["ContainerValue"] = update_dict[component]

                # Save the updated data back to the target file
                with open(target_file, 'w', encoding='utf-8') as target_f:
                    json.dump(target_data, target_f, indent=4)

if __name__ == "__main__":
    json_folder = 'app/data/new_json'  # Change this to your JSON folder path
    update_folder = 'update'  # Change this to your update folder path
    
    update_json_files(json_folder, update_folder)