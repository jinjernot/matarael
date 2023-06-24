import pandas as pd
from data.format_data import formateData
from data.process_data import processData
import os
import json

def clean_report(file):

    try:
        # Remove rows where the ContainerValue column is equal to "[BLANK]".
        #df = pd.read_excel(file.stream, engine='openpyxl')
        df = pd.read_excel(file, engine='openpyxl')
        df = df[df['ContainerValue'] != '[BLANK]']

        # Replace all occurrences of the character `\u00A0` with a space.
        df.replace('\u00A0', ' ', regex=True, inplace=True)

        # Create a list of columns to drop.
        cols_to_drop = ['Option', 'Status', 'SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue', 'ExtendedDescription', 'ComponentCompletionDate', 'ComponentReadiness', 'SKUReadiness']

        # Drop the columns from the DataFrame.
        df = df.drop(cols_to_drop, axis=1)

        with open('data/data.json', 'r') as json_file:
            json_data = json.load(json_file)
        
        groups = json_data['Groups']
        filtered_rows = pd.DataFrame()

        for group in groups:
            component_group = group['ComponentGroup']
            container_names = group['ContainerName']
            
            group_filtered_rows = df[(df['ComponentGroup'] == component_group) & df['ContainerName'].isin(container_names)]
            filtered_rows = pd.concat([filtered_rows, group_filtered_rows])

        rows_to_delete = df.index.difference(filtered_rows.index)

        # Delete the rows that do not match the filter criteria
        df = df.drop(rows_to_delete)
        
        # Create three new columns in the DataFrame.
        df[['Accuracy', 'Correct Value', 'Additional Information']] = ''

        # Loop over all the files in the `json` directory.
        #for x in os.listdir('/home/garciagi/SCS_Tool/json'):
        for x in os.listdir('json'):
            # Check if the file name ends with `.json`.
            if x.endswith('.json'):

                # Split the file name on the period character and get the first part of the file name.
                container_name = x.split('.')[0]

                # Get the DataFrame rows where the ContainerName column contains the container name.
                #container_df = df.loc[df['ContainerName'].str.contains(container_name)]
                container_df = df.loc[df['ContainerName'] == container_name]

                # Pass the rows to the processData() function.
                #processData(os.path.join('/home/garciagi/SCS_Tool/json', x), container_name, container_df, df)
                processData(os.path.join('json', x), container_name, container_df, df)
        # Remove all trailing semicolons from the ContainerValue column.
        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)

        # Save the DataFrame to a file called `SCS_QA.xlsx`.
        
        # df.to_excel('/home/garciagi/SCS_Tool/SCS_QA.xlsx', index=False)
        df.to_excel('SCS_QA.xlsx', index=False)
        formateData()

    except Exception as e:
        print(e)
    return
    