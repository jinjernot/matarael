from app.core.process_data import process_data  
from app.core.format_data import format_data  
from app.core.product_line import pl_check  
from app.core.qa_av import av_check
from app.config.variables import *
from app.config.paths import *

import pandas as pd
import json
import os

def clean_report(file):
    try:
        # Read excel file
        df = pd.read_excel(file.stream, engine='openpyxl')  # Server
        #df = pd.read_excel(file, engine='openpyxl')  # Local

        # Drop a list of columns
        cols_to_drop = COLS_TO_DROP
        df = df.drop(cols_to_drop, axis=1)

        # Add a list of columns
        df[COLS_TO_ADD] = ''
        
        # Call the pl_check
        pl_check(df)

        # Filter out the rows where ContainerValue and ContainerName are '[BLANK]'
        df = df[df['ContainerValue'] != '[BLANK]']
        df = df[df['ContainerName'] != '[BLANK]']
        
        # Drop rows with NaN values
        df = df.dropna(subset=['ContainerValue', 'ContainerName'])

        # Replace unicode character '\u00A0' with space
        df.replace('\u00A0', ' ', regex=True, inplace=True)
        
        # Removing ';' from end of ContainerValue
        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)
        
        # Stripping leading whitespaces from PhwebDescription
        df['PhwebDescription'] = df['PhwebDescription'].str.lstrip()
        
        # Converting ContainerValue column to string type
        df['ContainerValue'] = df['ContainerValue'].astype(str)

        # Load JSON data
        with open(COMPONENT_GROUPS_PATH, 'r') as json_file: # Server
        #with open('app/data/component_groups.json', 'r') as json_file: # Local
            json_data = json.load(json_file)
        groups = json_data['Groups']
        
        # Filter rows based on criteria from JSON data
        filtered_rows = df[df.apply(lambda row: any(row['ComponentGroup'] == group['ComponentGroup'] and row['ContainerName'] in group['ContainerName'] for group in groups), axis=1)]
        rows_to_delete = df.index.difference(filtered_rows.index)
        df = df.drop(rows_to_delete)

        # Process JSON files
        for x in os.listdir(JSON_PATH): # Server
        #for x in os.listdir('json'): # Local
            if x.endswith('.json'):
                container_name = x.split('.')[0]
                container_df = df[df['ContainerName'] == container_name]
                process_data(os.path.join(JSON_PATH, x), container_name, container_df, df) # Server 
                #process_data(os.path.join('json', x), container_name, container_df, df) # Local
        
        excel_file = pd.ExcelFile(file.stream, engine='openpyxl')
        # Check if "ms4" sheet exists
        if "ms4" in excel_file.sheet_names:
            df_final = av_check(file)
            with pd.ExcelWriter(SCS_QA_FILE_PATH) as writer:
                df.to_excel(writer, sheet_name='qa', index=False)  # Server
                df_final.to_excel(writer, sheet_name='duplicated', index=False)  # Server
            # df.to_excel('SCS_QA.xlsx', index=False)  # Local
        else:
            df.to_excel(SCS_QA_FILE_PATH, index=False)  # Server
            # df.to_excel('SCS_QA.xlsx', index=False)  # Local
    
        # Formatting data
        format_data()
    
    except Exception as e:
        print(e)

    return