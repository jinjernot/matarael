import json
import pandas as pd

def processData(json_path, container_name, container_df, df):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    container_data = pd.json_normalize(data[container_name])

    maskContainer = container_df[['PhwebDescription', 'ContainerValue']].isin(container_data[['PhwebDescription', 'ContainerValue']].values).all(axis=1)
    container_df.loc[maskContainer, 'Accuracy'] = f'SCS {container_name} OK'
    container_accuracy_dict = dict(container_df[maskContainer].index)
    
    df['Accuracy'] = container_df['Accuracy']

    unmatched_containers = container_df.merge(container_accuracy_dict, how='left', left_index=True, right_index=True, indicator=True)
    unmatched_containers.loc[unmatched_containers['_merge'] == 'left_only', 'Accuracy'] = f'ERROR: {container_name}'
    unmatched_containers.drop('_merge', axis=1, inplace=True)

    unmatched_containers['Correct Value'] = unmatched_containers['PhwebDescription'].map(container_data.set_index('PhwebDescription')['ContainerValue']).fillna('N/A')
    df.loc[unmatched_containers.index, 'Accuracy'] = unmatched_containers['Accuracy']
    df.loc[unmatched_containers.index, 'Correct Value'] = unmatched_containers['Correct Value']

    return df