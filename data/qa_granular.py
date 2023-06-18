import pandas as pd
from data.format_data import formateData
from data.process_data import processData
import os

def clean_granular(file):

    try:
        df = pd.read_excel(file)
        df.rename(columns={'PH Web Description': 'PhwebDescription'}, inplace=True)
        df.rename(columns={'Granular Container Value': 'ContainerValue'}, inplace=True)
        df = df[df['ContainerValue'] != '[BLANK]']
        df.replace('\u00A0', ' ', regex=True, inplace=True)
        cols_to_drop = ['PL','ExtendedDescription', 'PH Web Value', 'Createddate']
        df = df.drop(cols_to_drop, axis=1)
        df[['Accuracy']] = ''

        for x in os.listdir('json'):
            if x.endswith('.json'):
                container_name = x.split('.')[0]
                container_df = df.loc[df['Granular Container Tag'].str.contains(container_name)]
                processData(os.path.join('json', x), container_name, container_df, df)

        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)
        df.to_excel('SCS_QA.csv', index=False)
        formateData()

    except Exception as e:
        print(e)
    return
    