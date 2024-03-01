import pandas as pd
from app.format_data import formateData  
from app.process_data import processData  
from app.product_line import plCheck  
from app.av_check import avCheck
import os
import json

def clean_report(file):
    try:
        # Reading Excel file
        # df = pd.read_excel(file, engine='openpyxl')
        df = pd.read_excel(file.stream, engine='openpyxl')  # Reading Excel file from a stream

        # Columns to drop from DataFrame
        cols_to_drop = ['Option', 'Status', 'SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue', 'ExtendedDescription', 'ComponentCompletionDate', 'ComponentReadiness', 'SKUReadiness']
        df = df.drop(cols_to_drop, axis=1)

        # Adding new columns to DataFrame
        df[['Accuracy', 'Correct Value', 'Additional Information']] = ''
        
        # Checking product line
        plCheck(df)

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

        # Loading JSON data
        with open('/home/garciagi/SCS_Tool/app/data.json', 'r') as json_file:
        #with open('app/data.json', 'r') as json_file:
            json_data = json.load(json_file)
        groups = json_data['Groups']
        
        # Filtering rows based on criteria from JSON data
        filtered_rows = df[df.apply(lambda row: any(row['ComponentGroup'] == group['ComponentGroup'] and row['ContainerName'] in group['ContainerName'] for group in groups), axis=1)]
        rows_to_delete = df.index.difference(filtered_rows.index)
        df = df.drop(rows_to_delete)

        # Processing JSON files in a directory
        for x in os.listdir('/home/garciagi/SCS_Tool/json'):
        #for x in os.listdir('json'):
            if x.endswith('.json'):
                container_name = x.split('.')[0]
                container_df = df[df['ContainerName'] == container_name]
                processData(os.path.join('/home/garciagi/SCS_Tool/json', x), container_name, container_df, df)
                #processData(os.path.join('json', x), container_name, container_df, df)
        

        # Validate AV's
        avCheck(df)
        
        # Writing DataFrame to Excel file
        df.to_excel('/home/garciagi/SCS_Tool/SCS_QA.xlsx', index=False)
        #df.to_excel('SCS_QA.xlsx', index=False)
        
        # Formatting data
        formateData()
    
    except Exception as e:
        print(e)
    
    return
