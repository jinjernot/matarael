import os
import json
import pandas as pd
from datetime import datetime

# Directory containing the granular JSON files
JSON_DIR_GRANULAR = os.path.join('app', 'data', 'json_granular')

# Directory to save the reports
REPORTS_DIR = os.path.join('app', 'reports')
# Ensure the reports directory exists
os.makedirs(REPORTS_DIR, exist_ok=True)

def clean_granular_json_files():
    """
    Identifies and removes duplicate entries in granular JSON files.

    This function scans through JSON files in the JSON_DIR_GRANULAR directory.
    It identifies duplicates based on both 'Component' and 'ContainerValue' fields,
    removes them, and saves the cleaned data back to the original files.
    A report of all duplicates found is saved as an Excel file.
    """
    # List to hold all duplicated rows found across all files
    all_duplicates = []

    # Check if the granular JSON directory exists
    if not os.path.isdir(JSON_DIR_GRANULAR):
        print(f"Error: Directory not found at '{JSON_DIR_GRANULAR}'")
        return

    # Iterate over each file in the granular JSON directory
    for filename in os.listdir(JSON_DIR_GRANULAR):
        if filename.endswith('.json'):
            file_path = os.path.join(JSON_DIR_GRANULAR, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Could not read or parse {filename}: {e}")
                continue

            # Flag to check if the file was modified
            file_modified = False

            # Iterate over each key (e.g., 'Chassis', 'HDD') in the JSON data
            for key in data:
                # Ensure the value is a list
                if not isinstance(data[key], list):
                    continue
                
                # Convert the list of dictionaries to a DataFrame
                df = pd.DataFrame(data[key])

                # Check if DataFrame is empty or doesn't have the required columns
                if df.empty or not all(col in df.columns for col in ['Component', 'ContainerValue']):
                    continue

                # Identify duplicates based on both 'Component' and 'ContainerValue'
                # keep=False marks all occurrences of duplicates
                duplicates = df[df.duplicated(subset=['Component', 'ContainerValue'], keep=False)].copy()

                if not duplicates.empty:
                    duplicates['SourceFile'] = filename
                    duplicates['Group'] = key
                    all_duplicates.append(duplicates)
                    
                    # Remove duplicates, keeping the first instance
                    df.drop_duplicates(subset=['Component', 'ContainerValue'], keep='first', inplace=True)
                    
                    # Convert DataFrame back to a list of dictionaries
                    data[key] = df.to_dict('records')
                    file_modified = True

            # If duplicates were found and removed, write the cleaned data back to the file
            if file_modified:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    print(f"Cleaned duplicates in {filename}")
                except IOError as e:
                    print(f"Could not write to {filename}: {e}")


    # Generate a report if any duplicates were found
    if all_duplicates:
        # Concatenate all duplicate DataFrames into one
        duplicates_df = pd.concat(all_duplicates, ignore_index=True)
        
        # Reorder columns for clarity
        duplicates_df = duplicates_df[['SourceFile', 'Group', 'Component', 'ContainerValue']]
        
        # Generate timestamp for the report file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(REPORTS_DIR, f'duplicated_granular_report_{timestamp}.xlsx')
        
        # Save the report to an Excel file
        duplicates_df.to_excel(report_path, index=False)
        print(f"Generated duplicate report at: {report_path}")
    else:
        print("No duplicates found in any granular JSON files.")

if __name__ == '__main__':
    print("Starting granular JSON cleaning process...")
    clean_granular_json_files()
    print("Process finished.")
