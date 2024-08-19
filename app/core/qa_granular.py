import pandas as pd
import json
import os
from app.core.process_data_granular import process_data_granular

from app.config.paths import *
from app.config.variables import *

def clean_granular(file):
    try:
        # Read excel file
        df = pd.read_excel(file, engine='openpyxl') 

        # Drop a list of columns
        cols_to_drop = COLS_TO_DROP_GRANULAR
        df = df.drop(cols_to_drop, axis=1)
        
        # Add a list of columns
        df[COLS_TO_ADD] = ''
        
        # Filter out the rows where any column in COLS_TO_CHECK has '[BLANK]'
        mask = df[COLS_TO_CHECK].apply(lambda x: x.isin(['[BLANK]']).any(), axis=1)
        df = df[~mask]

        df = df.dropna(subset=COLS_TO_CHECK)
        
        # Walk through all subdirectories and process JSON files
        for root, dirs, files in os.walk(JSON_GRANULAR_PATH): # Server
            for x in files:
                if x.endswith('.json'):
                    container_name = x.split('.')[0]
                    container_df = df[df['Granular Container Tag'] == container_name]
                    process_data_granular(os.path.join(root, x), container_name, container_df, df) # Server 
        
        # Export DataFrame to Excel with the updated 'Comments' column
        df.to_excel('Granular_QA.xlsx', index=False)

    except Exception as e:
        print(e)
