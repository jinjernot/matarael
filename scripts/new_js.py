import pandas as pd
import json
import os

def sanitize_folder_name(name):
    # Replace slashes and other special characters with underscores
    return name.replace('/', '_').replace('\\', '_').replace(':', '_')

def excel_to_json_grouped_by_scs_group(file_path):
    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Remove extra spaces from the 'tag' column
        df['tag'] = df['tag'].str.strip()
        
        # Convert all values in 'val' column to strings (including numbers)
        df['val'] = df['val'].astype(str).str.strip()

        # Base directory to store all JSON files
        base_output_dir = 'new_OS_KB'

        # Create the base directory if it doesn't exist
        if not os.path.exists(base_output_dir):
            os.makedirs(base_output_dir)

        # Iterate over unique SCSGroup values
        for scs_group in df['SCSGroup'].unique():
            # Sanitize the SCSGroup name for folder creation
            sanitized_scs_group = sanitize_folder_name(scs_group)

            # Define the folder path for the SCSGroup
            scs_group_folder = os.path.join(base_output_dir, sanitized_scs_group)

            # Create the folder for the SCSGroup if it doesn't exist
            if not os.path.exists(scs_group_folder):
                os.makedirs(scs_group_folder)

            # Iterate over each unique "tag" in the current SCSGroup
            for tag in df[df['SCSGroup'] == scs_group]['tag'].unique():
                # Sanitize the tag name for file naming
                sanitized_tag = sanitize_folder_name(tag)

                # Filter the DataFrame for the current tag within the SCSGroup
                tag_df = df[(df['SCSGroup'] == scs_group) & (df['tag'] == tag)]

                # Create the JSON structure for each pair of Component and ContainerValue
                tag_json = {
                    sanitized_tag: []  # Use the sanitized tag value as the key
                }

                for _, row in tag_df.iterrows():
                    component_data = {
                        "Component": row['Component'],
                        "ContainerValue": row['val']
                    }
                    tag_json[sanitized_tag].append(component_data)

                # Define the file name based on the sanitized "tag"
                file_name = f"{sanitized_tag}.json"
                file_path = os.path.join(scs_group_folder, file_name)

                # Write the JSON structure to a file with UTF-8 encoding
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(tag_json, json_file, indent=4, ensure_ascii=False)

                print(f"JSON file created: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
excel_to_json_grouped_by_scs_group('Keyboard_OS (1).xlsx')
