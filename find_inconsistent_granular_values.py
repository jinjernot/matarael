import os
import json
import pandas as pd
from datetime import datetime

# Define the directory containing the granular JSON files
JSON_DIR_GRANULAR = os.path.join('app', 'data', 'json_granular')

# Define the directory to save the reports
REPORTS_DIR = os.path.join('app', 'reports')
# Ensure the reports directory exists; create it if it doesn't
os.makedirs(REPORTS_DIR, exist_ok=True)

def find_inconsistent_values():
    """
    Identifies components with multiple different ContainerValues within each granular JSON file.

    This function scans each JSON file in the specified granular directory individually.
    It finds any "Component" that has been assigned more than one unique "ContainerValue"
    within the same file. A consolidated report of all such inconsistencies is saved as an
    Excel file, showing the conflicting entries, their values, and their source files.
    """
    all_inconsistent_records = []

    # Check if the target directory for granular JSON files exists
    if not os.path.isdir(JSON_DIR_GRANULAR):
        print(f"Error: Directory not found at '{JSON_DIR_GRANULAR}'")
        return

    # Loop through each file in the granular JSON directory to process it individually
    for filename in os.listdir(JSON_DIR_GRANULAR):
        if filename.endswith('.json'):
            file_path = os.path.join(JSON_DIR_GRANULAR, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Could not read or parse {filename}: {e}")
                continue
            
            file_records = []
            # Iterate through each key (category) in the JSON data
            for key, value in data.items():
                if isinstance(value, list):
                    # For each record in the list, add source file and group info
                    for record in value:
                        if isinstance(record, dict):
                            record_copy = record.copy()
                            record_copy['SourceFile'] = filename
                            record_copy['Group'] = key
                            file_records.append(record_copy)

            # If no records were found in this file, move to the next
            if not file_records:
                continue

            # Convert the list of records for the current file into a Pandas DataFrame
            df = pd.DataFrame(file_records)
            
            # Ensure the essential columns exist to avoid errors
            if not all(col in df.columns for col in ['Component', 'ContainerValue']):
                print(f"Skipping {filename} due to missing 'Component' or 'ContainerValue' columns.")
                continue

            # Group by 'Component' and count the number of unique 'ContainerValue's
            inconsistent_components = df.groupby('Component')['ContainerValue'].nunique()
            
            # Filter to get only the components with more than one unique value
            inconsistent_components = inconsistent_components[inconsistent_components > 1].index

            # Filter the file's DataFrame to get all rows for the inconsistent components
            if len(inconsistent_components) > 0:
                inconsistent_df_for_file = df[df['Component'].isin(inconsistent_components)].copy()
                all_inconsistent_records.append(inconsistent_df_for_file)

    # Check if any inconsistencies were found across all files
    if all_inconsistent_records:
        # Concatenate all DataFrames of inconsistent records into one
        final_inconsistent_df = pd.concat(all_inconsistent_records, ignore_index=True)

        # Sort the results for easier review
        final_inconsistent_df.sort_values(by=['SourceFile', 'Group', 'Component', 'ContainerValue'], inplace=True)

        # Reorder columns for the final report
        report_columns = ['SourceFile', 'Group', 'Component', 'ContainerValue']
        other_columns = [col for col in final_inconsistent_df.columns if col not in report_columns]
        final_inconsistent_df = final_inconsistent_df[report_columns + other_columns]
        
        # Generate a timestamp for the report filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(REPORTS_DIR, f'inconsistent_granular_values_report_{timestamp}.xlsx')
        
        # Save the report to an Excel file
        final_inconsistent_df.to_excel(report_path, index=False)
        total_inconsistent_components = final_inconsistent_df['Component'].nunique()
        print(f"Found {total_inconsistent_components} components with inconsistent values within individual files.")
        print(f"Generated inconsistency report at: {report_path}")
    else:
        print("No inconsistent ContainerValues found for any Component within any single file.")


if __name__ == '__main__':
    print("Starting analysis of granular JSON files for inconsistent values...")
    find_inconsistent_values()
    print("Analysis finished.")
