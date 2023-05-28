import pandas as pd
from data.format_data import formateData
from data.process_data import processData
import os

def cleanGranular(file):

    try:
        df = pd.read_excel(file)
        df = df[df['ContainerValue'] != '[BLANK]']
        df.replace('\u00A0', ' ', regex=True, inplace=True)

        cols_to_drop = ['Option', 'Status', 'SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue', 'ExtendedDescription', 'ComponentCompletionDate', 'ComponentReadiness', 'SKUReadiness']
        df = df.drop(cols_to_drop, axis=1)
        df[['Accuracy', 'Correct Value', 'Additional Information']] = ''

        for file in os.listdir('json'):
            if file.endswith('.json'):
                container_name = file.split('.')[0]
                container_df = df.loc[df['ContainerName'].str.contains(container_name)]
                processData(os.path.join('json', file), container_name, container_df, df)

        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)
        df.to_excel('SCS_QA.xlsx', index=False)
        formateData()

    except Exception as e:
        print(e)
    return
    