import pandas as pd
import os
import json

def search_json_files(value, container_names):
    json_folder = "new_jsons"  # Folder containing JSON files
    # Use os.walk to iterate over all directories and files within the json_folder
    for root, _, files in os.walk(json_folder):
        for filename in files:
            if filename.endswith(".json") and filename.split(".")[0] in container_names:
                file_path = os.path.join(root, filename)
                with open(file_path, encoding="utf-8") as json_file:
                    data = json.load(json_file)  # Load JSON data
                    for item in data:  # Iterate through items in the JSON data
                        for entry in data[item]:  # Iterate through entries in each item
                            container_value = entry.get("ContainerValue", "")  # Get the container value
                            if isinstance(container_value, str) and value.lower() in container_value.lower():
                                # Check if the search value is a substring of the container value (case-insensitive)
                                return filename.split(".")[0], container_value  # Return matching file and value
    return None, None  # Return None if no match is found

def load_component_groups():
    with open('app/data/component_groups.json', 'r', encoding='utf-8') as json_file:
        component_groups = json.load(json_file)  # Load component groups data
    # Create a dictionary mapping component groups to container names
    return {group['ComponentGroup']: group['ContainerName'] for group in component_groups['Groups']}

def clean_characteristic(value):
    # List of substrings to remove
    to_remove = ["0.00,", "2.00,", "6.00,", "8.00,", "4.00,", "16.00,", "2.00G"]
    for substring in to_remove:
        value = value.replace(substring, "")  # Replace each substring with an empty string
    return value.strip()  # Remove leading/trailing whitespace

def sanitize_sheet_name(name):
    # Remove or replace invalid characters from sheet name
    invalid_chars = ['\\', '/', '*', '?', ':', '[', ']', ']']
    for char in invalid_chars:
        name = name.replace(char, '_')  # Replace invalid characters with an underscore or any other character
    return name

def matrix_file():
    try:
        component_groups = load_component_groups()  # Load component groups

        df = pd.read_excel("compo.xlsx", engine='openpyxl', skiprows=1)  # Load the Excel file into a DataFrame
        df = df.dropna(subset=["Characteristic"])  # Drop rows with NaN values in the "Characteristic" column
        
        # Clean the "Characteristic" column
        df["Characteristic"] = df["Characteristic"].apply(clean_characteristic)

        group_data = {group: [] for group in component_groups}  # Dictionary to store data for each group

        # Search for data in JSON files and add new columns
        for index, row in df.iterrows():
            scs_group = row["SCS Component Group"]  # Get the SCS component group
            if scs_group in component_groups:
                container_names = component_groups[scs_group]  # Get the container names for the group
                json_name, container_value = search_json_files(row["Characteristic"], container_names)
                if json_name is not None and container_value is not None:
                    # If found, create a dictionary with the row data and the found value
                    found_row = {
                        "Component": row["Component"],
                        "SCSGroup": scs_group,
                        "ContainerType": "Prism",
                        json_name: container_value
                    }
                    group_data[scs_group].append(found_row)  # Append to the list of found data

        # Create a Pandas Excel writer object
        with pd.ExcelWriter("matrix_output.xlsx", engine='openpyxl') as writer:
            for group, data in group_data.items():
                if data:
                    group_df = pd.DataFrame(data)  # Convert the list of dictionaries to a DataFrame for each group
                else:
                    group_df = pd.DataFrame(columns=["Component", "SCSGroup", "ContainerType"])  # Create an empty DataFrame with the specified columns if no data is found
                
                # Sanitize the sheet name before writing
                sanitized_group_name = sanitize_sheet_name(group)
                group_df.to_excel(writer, sheet_name=sanitized_group_name, index=False)  # Write each DataFrame to a different sheet named after the sanitized ComponentGroup

        print("Matrix Excel completed.")  # Print success message

    except Exception as e:
        print("An error occurred:", e)  # Print the error if any exception occurs

if __name__ == "__main__":
    matrix_file()  # Run the main function if the script is executed directly
