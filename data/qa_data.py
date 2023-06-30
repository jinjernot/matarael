import pandas as pd
from data.format_data import formateData
from data.process_data import processData
import os
import json

import pandas as pd
import os
import json

def clean_report(file):
    try:

        #df = pd.read_excel(file, engine='openpyxl')
        df = pd.read_excel(file.stream, engine='openpyxl')

        df = df[df['ContainerValue'] != '[BLANK]']
        df.replace('\u00A0', ' ', regex=True, inplace=True)
        df['PhwebDescription'] = df['PhwebDescription'].str.lstrip()
        df['ContainerValue'] = df['ContainerValue'].astype(str)

        cols_to_drop = ['Option', 'Status', 'SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue', 'ExtendedDescription', 'ComponentCompletionDate', 'ComponentReadiness', 'SKUReadiness']
        df = df.drop(cols_to_drop, axis=1)

        with open('/home/garciagi/SCS_Tool/data/data.json', 'r') as json_file:
        #with open('data/data.json', 'r') as json_file:
            json_data = json.load(json_file)

        groups = json_data['Groups']
        filtered_rows = df[df.apply(lambda row: any(row['ComponentGroup'] == group['ComponentGroup'] and row['ContainerName'] in group['ContainerName'] for group in groups), axis=1)]

        rows_to_delete = df.index.difference(filtered_rows.index)
        df = df.drop(rows_to_delete)

        df[['Accuracy', 'Correct Value', 'Additional Information']] = ''

        for x in os.listdir('/home/garciagi/SCS_Tool/json'):
        #for x in os.listdir('json'):
            if x.endswith('.json'):
                container_name = x.split('.')[0]
                container_df = df[df['ContainerName'] == container_name]
                processData(os.path.join('/home/garciagi/SCS_Tool/json', x), container_name, container_df, df)
                #processData(os.path.join('json', x), container_name, container_df, df)

        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)
        df.to_excel('/home/garciagi/SCS_Tool/SCS_QA.xlsx', index=False)
        #df.to_excel('SCS_QA.xlsx', index=False)
        formateData()
    
    except Exception as e:
        print(e)
    
    return
