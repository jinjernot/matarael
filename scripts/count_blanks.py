import os
import json
import pandas as pd

def count_blank_values(folder_path, output_excel_path):
    blank_data = []

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            # Load JSON data from the file with explicit encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

            # Count '[BLANK]' occurrences in each file
            blank_count = 0
            filename_without_extension = os.path.splitext(filename)[0]
            if filename_without_extension in json_data:
                for pair in json_data[filename_without_extension]:
                    if pair['ContainerValue'] == '[BLANK]':
                        blank_count += 1

            # Only store files with at least one '[BLANK]' value
            if blank_count > 0:
                blank_data.append({'Filename': filename, 'Blank Count': blank_count})

    # Convert blank data to a pandas DataFrame
    df = pd.DataFrame(blank_data)

    # Export to Excel
    df.to_excel(output_excel_path, index=False)
    
    print(f'Excel file saved to: {output_excel_path}')
    return len(blank_data)

# Specify the folder path and output Excel file path
folder_path = './app/data/json_granular'
output_excel_path = './blank_values_summary.xlsx'

# Count blank values and export to Excel
count_blank_values(folder_path, output_excel_path)
