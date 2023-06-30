import json
import pandas as pd

def processData(json_path, container_name, container_df, df):
    # Open the JSON file and load the data into a dictionary.
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Convert the list of containers into a DataFrame.
    container_data = pd.DataFrame(data[container_name])

    # Create an empty dictionary to store the accuracy of each container.
    container_accuracy_dict = {}

    # Iterate over each container in the JSON data.
    for container in container_data.itertuples(index=False):
        # Create a mask using exact string matching.
        maskContainer = (container_df['PhwebDescription'] == container.PhwebDescription) & \
                        (container_df['ContainerValue'] == container.ContainerValue)

        # Update the `container_accuracy_dict` dictionary using boolean indexing.
        container_accuracy_dict.update(container_df[maskContainer].index.to_series().map(lambda idx: (idx, f'SCS {container_name} OK')))

    # Update the `container_accuracy_dict` dictionary with error values.
    container_accuracy_dict.update(container_df[~container_df.index.isin(container_accuracy_dict.keys())].index.to_series().map(lambda idx: (idx, f'ERROR: {container_name}')))

    # Update the `Accuracy` column of the `container_df` DataFrame using boolean indexing.
    container_df.loc[container_accuracy_dict.keys(), 'Accuracy'] = [value for _, value in container_accuracy_dict.values()]

    # Update the `Accuracy` column of the `df` DataFrame using boolean indexing.
    df.loc[container_df.index, 'Accuracy'] = container_df['Accuracy']

    return df

