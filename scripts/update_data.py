import json
import os

def update_json_files(json_folder, update_folder):
    # Get a list of JSON files in the json_folder
    json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]
    print(f"Found {len(json_files)} JSON files in {json_folder}")

    # Loop through each update JSON file in the update_folder
    for update_file in os.listdir(update_folder):
        if update_file.endswith('.json'):
            update_path = os.path.join(update_folder, update_file)
            print(f"Processing update file: {update_file}")
            
            # Open and read the update file
            try:
                with open(update_path, 'r', encoding='utf-8') as update_f:
                    update_data = json.load(update_f)
                print(f"Successfully loaded update file: {update_file}")
                
                # Remove the file extension and use it as the key (e.g., 'batterytype')
                key = os.path.splitext(update_file)[0]  # 'batterytype' for 'batterytype.json'
                
                # Check if the key exists in the update data
                if key not in update_data:
                    print(f"Warning: '{key}' does not exist in the update data.")
                    continue  # Skip this file if it doesn't have the expected structure
                else:
                    print(f"Key '{key}' found in update data.")

                # Check if the corresponding JSON file exists in json_folder
                target_file = os.path.join(json_folder, update_file)
                if update_file in json_files:
                    with open(target_file, 'r', encoding='utf-8') as target_f:
                        target_data = json.load(target_f)
                    print(f"Successfully loaded target file: {update_file}")
                    
                    # Create a mapping for easy look-up of update values
                    update_dict = {item["Component"]: item["ContainerValue"] for item in update_data[key]}
                    print(f"Created update_dict with {len(update_dict)} items.")

                    # Track new insertions and updates
                    updated_count = 0
                    inserted_count = 0

                    # Loop through the target data and update ContainerValue where needed
                    for item in target_data.get(key, []):  # Use get to avoid KeyError if key is missing
                        component = item.get("Component")  # Use get to avoid KeyError
                        if component:  # If a component is found
                            # If the component exists in update_dict, update the ContainerValue
                            if component in update_dict:
                                if item.get("ContainerValue") != update_dict[component]:  # Only update if different
                                    item["ContainerValue"] = update_dict[component]
                                    updated_count += 1

                    # Insert new items from update_dict that don't already exist in target_data
                    existing_components = {item.get("Component") for item in target_data.get(key, [])}
                    for component, container_value in update_dict.items():
                        if component not in existing_components:
                            new_item = {"Component": component, "ContainerValue": container_value}
                            target_data[key].append(new_item)  # Insert the new item
                            inserted_count += 1

                    # Log the counts
                    if updated_count > 0:
                        print(f"Updated {updated_count} components in {update_file}")
                    if inserted_count > 0:
                        print(f"Inserted {inserted_count} new components into {update_file}")

                    # Save the updated data back to the target file
                    with open(target_file, 'w', encoding='utf-8') as target_f:
                        json.dump(target_data, target_f, indent=4)
                        print(f"Saved updated data to {target_file}")

            except json.JSONDecodeError as e:
                print(f"Error reading '{update_file}': {e}")
            except KeyError as e:
                print(f"KeyError: Missing key '{e}' in update file '{update_file}'")
            except Exception as e:
                print(f"Unexpected error with '{update_file}': {e}")

if __name__ == "__main__":
    json_folder = 'app/data/new_json'  # Change this to your JSON folder path
    update_folder = 'update'  # Change this to your update folder path
    
    print("Starting the update process...")
    update_json_files(json_folder, update_folder)
    print("Update process completed.")
