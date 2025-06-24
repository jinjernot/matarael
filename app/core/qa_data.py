from app.core.process_data import process_data, process_data_av, process_data_granular
from app.core.format_data import format_data, format_data_granular
from app.core.product_line import pl_check
from app.core.qa_av import av_check
from app.config.variables import *
from app.config.paths import *
from app.core.check_missing_fields import check_missing_fields

import pandas as pd
import json
import os
import asyncio


async def process_granular_file_async(json_file, container_name, container_df, df):
    """
    Asynchronous wrapper for the process_data_granular function.
    """
    try:
        process_data_granular(json_file, container_name, container_df, df)
        #print(f"Processed Granular file: {json_file}")
    except Exception as e:
        print(f"Error processing Granular file {json_file}: {e}")

async def process_all_granular_files_async(df):
    """
    Gathers all tasks for processing granular JSON files and runs them concurrently.
    """
    tasks = []
    for x in os.listdir(JSON_GRANULAR_PATH):
        if x.endswith('.json') and 'component_groups_granular' not in x:
            container_name = x.split('.')[0]
            container_df = df[df['Granular Container Tag'] == container_name]
            json_file = os.path.join(JSON_GRANULAR_PATH, x)
            tasks.append(process_granular_file_async(json_file, container_name, container_df, df))
    await asyncio.gather(*tasks)

def run_asyncio_task(task):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    loop.run_until_complete(task)


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
        else:
            df.to_excel(SCS_QA_FILE_PATH, index=False)  # Server
    
        # Formatting data
        format_data()
    
    except Exception as e:
        print(e)

    return

def clean_report_av(file):
    try:
        # Read excel file
        #df = pd.read_excel(file.stream, engine='openpyxl', sheet_name='SKU Accuracy')  # Server
        df = pd.read_excel(file, engine='openpyxl')  # Local

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
        for x in os.listdir(JSON_PATH_AV): # Server
        #for x in os.listdir('json'): # Local
            if x.endswith('.json'):
                container_name = x.split('.')[0]
                container_df = df[df['ContainerName'] == container_name]
                process_data_av(os.path.join(JSON_PATH_AV, x), container_name, container_df, df) # Server 
                #process_data(os.path.join('json', x), container_name, container_df, df) # Local
                
        #excel_file = pd.ExcelFile(file.stream, engine='openpyxl')
        excel_file = pd.ExcelFile(file, engine='openpyxl')
        
        # Check if "ms4" sheet exists
        if "ms4" in excel_file.sheet_names:
            df_final = av_check(file)
            print("¡salio de av_check!")
            with pd.ExcelWriter(SCS_QA_FILE_PATH) as writer:
                df.to_excel(writer, sheet_name='qa', index=False)  # Server
                df_final.to_excel(writer, sheet_name='duplicated', index=False)  # Server
                print("grabo?")
        else:
            df.to_excel(SCS_QA_FILE_PATH, index=False)  # Server
    
        # Formatting data
        format_data()
    
    except Exception as e:
        print(e)

    return

def clean_report_granular(file):
    try:
        # Read excel file
        df = pd.read_excel(file.stream, engine='openpyxl', sheet_name='GranularContentReport')  # Server
        #df = pd.read_excel(file, engine='openpyxl')  # Local

        # Drop a list of columns
        cols_to_drop = COLS_TO_DROP_GRANULAR
        df = df.drop(cols_to_drop, axis=1)

        # Add a list of columns
        df[COLS_TO_ADD] = ''
        
        # Call the pl_check
        #pl_check(df)

        # This section is commented out to treat '[BLANK]' as a valid value
        # df = df[df['Granular Container Value'] != '[BLANK]']
        # df = df[df['Granular Container Tag'] != '[BLANK]']
        
        # Drop rows with NaN values
        df = df.dropna(subset=['Granular Container Value', 'Granular Container Tag'])

        # Replace unicode character '\u00A0' with space
        df.replace('\u00A0', ' ', regex=True, inplace=True)
        
        # Removing ';' from end of ContainerValue
        df.loc[df['Granular Container Value'].str.endswith(';'), 'Granular Container Value'] = df['Granular Container Value'].str.slice(stop=-1)
        
        # Converting ContainerValue column to string type
        df['Granular Container Value'] = df['Granular Container Value'].astype(str)

        run_asyncio_task(process_all_granular_files_async(df))
    
        # NEW EXTRA CHECK: This block is added to run the new check for missing fields.
        granular_rules_path = COMPONENT_GROUPS_GRANULAR_PATH
        df = check_missing_fields(df, granular_rules_path)

        # Check if "ms4" sheet exists
        excel_file = pd.ExcelFile(file.stream, engine='openpyxl')
        if "ms4" in excel_file.sheet_names:
            df_final = av_check(file.stream)
            with pd.ExcelWriter(SCS_GRANULAR_FILE_PATH) as writer:
                df.to_excel(writer, sheet_name='qa', index=False)
                df_final.to_excel(writer, sheet_name='duplicated', index=False)
        else:
            df.to_excel(SCS_GRANULAR_FILE_PATH, index=False)

        # Formatting data
        format_data_granular()
    
    except Exception as e:
        print(e)

    return