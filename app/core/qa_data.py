from app.core.process_data import process_data  
from app.core.format_data import formate_data  
from app.core.product_line import pl_check  
from app.core.qa_av import av_check

import pandas as pd
import json
import os

def clean_report(file):
    try:
        # Reading Excel file
        # df = pd.read_excel(file, engine='openpyxl')
        df = pd.read_excel(file.stream, engine='openpyxl')  # Reading Excel file / server side

        # Columns to drop from df
        cols_to_drop = ['Option', 'Status', 'SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue', 'ExtendedDescription', 'ComponentCompletionDate', 'ComponentReadiness', 'SKUReadiness']
        df = df.drop(cols_to_drop, axis=1)

        # Adding new columns to df
        df[['Accuracy', 'Correct Value', 'Additional Information']] = ''
        
        # Checking PL
        pl_check(df)

        # Filtering out rows where ContainerValue and ContainerName are '[BLANK]'
        df = df[df['ContainerValue'] != '[BLANK]']
        df = df[df['ContainerName'] != '[BLANK]']
        
        # Dropping rows with NaN values in specific columns
        df = df.dropna(subset=['ContainerValue', 'ContainerName'])

        # Replacing unicode character '\u00A0' with space
        df.replace('\u00A0', ' ', regex=True, inplace=True)
        
        # Removing ';' from end of ContainerValue
        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)
        
        # Stripping leading whitespaces from PhwebDescription
        df['PhwebDescription'] = df['PhwebDescription'].str.lstrip()
        
        # Converting ContainerValue column to string type
        df['ContainerValue'] = df['ContainerValue'].astype(str)

        # Load JSON data
        with open('/home/garciagi/SCS_Tool/app/core/data/component_groups.json', 'r') as json_file:
        #with open('app/core/data/component_groups.json', 'r') as json_file:
            json_data = json.load(json_file)
        groups = json_data['Groups']
        
        # Filtering rows based on criteria from JSON data
        filtered_rows = df[df.apply(lambda row: any(row['ComponentGroup'] == group['ComponentGroup'] and row['ContainerName'] in group['ContainerName'] for group in groups), axis=1)]
        rows_to_delete = df.index.difference(filtered_rows.index)
        df = df.drop(rows_to_delete)

        # Processing JSON files in a directory
        for x in os.listdir('/home/garciagi/SCS_Tool/json'): # server side
        #for x in os.listdir('json'): # local side
            if x.endswith('.json'):
                container_name = x.split('.')[0]
                container_df = df[df['ContainerName'] == container_name]
                process_data(os.path.join('/home/garciagi/SCS_Tool/json', x), container_name, container_df, df) #server side
                #process_data(os.path.join('json', x), container_name, container_df, df)
        
        # Validate AV's
        av_check(df)
        
        # Writing DataFrame to Excel file
        df.to_excel('/home/garciagi/SCS_Tool/SCS_QA.xlsx', index=False) # server
        #df.to_excel('SCS_QA.xlsx', index=False)
        
        # Formatting data
        formate_data()
    
    except Exception as e:
        print(e)
    
    return
