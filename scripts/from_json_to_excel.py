import os
import json
import pandas as pd
from openpyxl import Workbook

def load_json_file(json_path):
    """
    Load and validate the structure of a JSON file.
    Returns the parsed JSON data if the structure is valid, otherwise returns None.
    """
    try:
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

            # Validate structure: Ensure each entry has 'Component' and 'ContainerValue'
            for key, value in data.items():
                if isinstance(value, list):
                    for item in value:
                        if "Component" not in item or "ContainerValue" not in item:
                            raise ValueError(f"Unexpected structure in {json_path}: missing 'Component' or 'ContainerValue'.")
            
            return data

    except (json.JSONDecodeError, ValueError) as e:
        print(f"Skipping {json_path} due to error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred with {json_path}: {e}")
        return None

def gather_json_data_to_excel(json_directory, output_excel_file):
    """
    Gather data from all JSON files in the specified directory, validate them, and save them to an Excel file.
    Each JSON file's data is stored in a separate sheet.
    """
    # Create a list to store data for each sheet
    all_dataframes = {}

    # Iterate through all files in the specified directory
    for filename in os.listdir(json_directory):
        if filename.endswith('.json'):
            json_path = os.path.join(json_directory, filename)
            
            # Load and validate the JSON file
            data = load_json_file(json_path)
            
            if data:
                # Convert JSON data to a pandas DataFrame
                for key, value in data.items():
                    df = pd.DataFrame(value)

                    # Create a valid Excel sheet name from the filename (remove extension)
                    sheet_name = os.path.splitext(filename)[0]

                    # Add DataFrame to the dictionary
                    all_dataframes[sheet_name] = df

    # Create a new Excel file and write each DataFrame to a separate sheet
    with pd.ExcelWriter(output_excel_file, engine='openpyxl') as writer:
        for sheet_name, dataframe in all_dataframes.items():
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Data has been successfully saved to {output_excel_file}")

# Example usage:
json_directory = './app/data/json_granular'  # Directory containing the JSON files
output_excel_file = 'output_data.xlsx'  # Output Excel file path

gather_json_data_to_excel(json_directory, output_excel_file)
