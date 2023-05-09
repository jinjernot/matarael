import json
import pandas as pd

def processData(json_path, container_name, container_df, df):
    with open(json_path, 'r') as f:
        data = json.load(f)

        container_accuracy_dict = {}

        for container in data[container_name]:
            maskContainer = (container_df['PhwebDescription'].str.contains(container['PhwebDescription']) & \
                        (container_df['ContainerValue'].str.contains(container['ContainerValue'], case=False))) 
            for idx in container_df[maskContainer].index:
                container_accuracy_dict[idx] = f'SCS {container_name} OK'

        for idx in container_df.index:
            if idx not in container_accuracy_dict:
                container_accuracy_dict[idx] = f'ERROR: {container_name}'
        container_df['Accuracy'] = container_df.index.map(container_accuracy_dict)

        df.update(container_df['Accuracy'])