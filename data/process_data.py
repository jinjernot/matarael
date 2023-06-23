import json

def processData(json_path, container_name, container_df, df):

    # Open the JSON file and load the data into a dictionary.
    with open(json_path, 'r', encoding='utf-8') as f:

        data = json.load(f)
        # Create an empty dictionary to store the accuracy of each container.
        container_accuracy_dict = {}

        # For each container in the JSON file, create a mask that filters the `container_df` DataFrame to only include rows where the `PhwebDescription` column contains the container's `PhwebDescription` value and the `ContainerValue` column contains the container's `ContainerValue` value.
        for container in data[container_name]:
            maskContainer = (container_df['PhwebDescription'].str.contains(container['PhwebDescription']) & \
                        (container_df['ContainerValue'].str.contains(container['ContainerValue'], case=False, regex=False))) 
            for idx in container_df[maskContainer].index:
                container_accuracy_dict[idx] = f'SCS {container_name} OK'
        
        # For each index in the `container_df` DataFrame, if the index is not in the `container_accuracy_dict` dictionary, add the index to the dictionary with the value `ERROR: ` + `container_name`.
        for idx in container_df.index:
            if idx not in container_accuracy_dict:
                container_accuracy_dict[idx] = f'ERROR: {container_name}'

        # Update the `Accuracy` column of the `container_df` DataFrame with the values from the `container_accuracy_dict` dictionary.
        container_df['Accuracy'] = container_df.index.map(container_accuracy_dict)

    # Update the `Accuracy` column of the `df` DataFrame with the values from the `container_df` DataFrame.
    df.update(container_df['Accuracy'])
    return df