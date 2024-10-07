import pandas as pd
import json

def process_data(json_path, container_name, container_df, df):
    
    # Open the JSON file and load the data into a dictionary.
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    # Convert the list of containers into a DataFrame.
    container_data = pd.DataFrame(json_data[container_name])

    # Create an empty dictionary
    container_accuracy_dict = {}

    # Iterate over each container in the JSON data.
    for container in container_data.itertuples(index=False):
        # Create a mask using exact string matching.
        maskContainer = (container_df['PhwebDescription'] == container.PhwebDescription) & \
                        (container_df['ContainerValue'] == container.ContainerValue)
        # Update the 'container_accuracy_dict' dictionary using boolean indexing.
        container_accuracy_dict.update(container_df[maskContainer].index.to_series().map(lambda idx: (idx, f'SCS {container_name} OK')))
    # Update the 'Accuracy' column of the 'container_df' DataFrame using boolean indexing.
    container_df.loc[container_accuracy_dict.keys(), 'Accuracy'] = [value for _, value in container_accuracy_dict.values()]
    # Update the 'Accuracy' column of the 'df' DataFrame using boolean indexing.
    df.loc[container_df.index, 'Accuracy'] = container_df['Accuracy']

    # Find the unmatched containers and set error messages
    unmatched_containers = container_df[~container_df.index.isin(container_accuracy_dict.keys())]
    unmatched_error_messages = [f'ERROR: {container_name}' for _ in range(len(unmatched_containers))]
    unmatched_containers['Accuracy'] = unmatched_error_messages
    # Update the 'Accuracy' column of the 'df' DataFrame for unmatched containers.
    df.loc[unmatched_containers.index, 'Accuracy'] = unmatched_containers['Accuracy']

    unmatched_container_values = []
    for container in unmatched_containers.itertuples(index=False):
        matching_containers = container_data[container_data['PhwebDescription'] == container.PhwebDescription]
        if len(matching_containers) > 0:
            correct_value = matching_containers.iloc[0]['ContainerValue']
            unmatched_container_values.append(correct_value)
        else:
            unmatched_container_values.append('N/A')
    # Add 'Correct Value' column to the df DataFrame for unmatched containers
    df.loc[unmatched_containers.index, 'Correct Value'] = unmatched_container_values

    return df

def process_data_av(json_path, container_name, container_df, df):
    
    # Open the JSON file and load the data into a dictionary.
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    # Convert the list of containers into a DataFrame.
    container_data = pd.DataFrame(json_data[container_name])

    # Create an empty dictionary
    container_accuracy_dict = {}

    # Iterate over each container in the JSON data.
    for container in container_data.itertuples(index=False):
        # Create a mask using exact string matching.
        maskContainer = (container_df['Component'] == container.Component) & \
                        (container_df['ContainerValue'] == container.ContainerValue)
        # Update the 'container_accuracy_dict' dictionary using boolean indexing.
        container_accuracy_dict.update(container_df[maskContainer].index.to_series().map(lambda idx: (idx, f'SCS {container_name} OK')))
    # Update the 'Accuracy' column of the 'container_df' DataFrame using boolean indexing.
    container_df.loc[container_accuracy_dict.keys(), 'Accuracy'] = [value for _, value in container_accuracy_dict.values()]
    # Update the 'Accuracy' column of the 'df' DataFrame using boolean indexing.
    df.loc[container_df.index, 'Accuracy'] = container_df['Accuracy']

    # Find the unmatched containers and set error messages
    unmatched_containers = container_df[~container_df.index.isin(container_accuracy_dict.keys())]
    unmatched_error_messages = [f'ERROR: {container_name}' for _ in range(len(unmatched_containers))]
    unmatched_containers['Accuracy'] = unmatched_error_messages
    # Update the 'Accuracy' column of the 'df' DataFrame for unmatched containers.
    df.loc[unmatched_containers.index, 'Accuracy'] = unmatched_containers['Accuracy']

    unmatched_container_values = []
    for container in unmatched_containers.itertuples(index=False):
        matching_containers = container_data[container_data['Component'] == container.Component]
        if len(matching_containers) > 0:
            correct_value = matching_containers.iloc[0]['ContainerValue']
            unmatched_container_values.append(correct_value)
        else:
            unmatched_container_values.append('N/A')
    # Add 'Correct Value' column to the df DataFrame for unmatched containers
    df.loc[unmatched_containers.index, 'Correct Value'] = unmatched_container_values

    return df

def process_data_granular(json_path, container_name, container_df, df):
    # Load the JSON data and convert the relevant part into a DataFrame.
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    container_data = pd.DataFrame(json_data[container_name])

    # Ensure column names are consistent between DataFrames
    if 'ContainerValue' not in container_data.columns:
        raise KeyError(f"Expected 'ContainerValue' in {container_name} data")

    # Keep track of original indices in container_df for safe updates later
    container_df = container_df.reset_index(drop=False)

    # Merge container_df with container_data on Component and ContainerValue for exact matching.
    merged_df = pd.merge(container_df, container_data, how='left', 
                         left_on=['Component', 'ContainerValue'], 
                         right_on=['Component', 'ContainerValue'], 
                         indicator=True)

    # Update 'Accuracy' where the match is found ('_merge' == 'both')
    matched_mask = merged_df['_merge'] == 'both'
    container_df.loc[matched_mask.index[matched_mask], 'Accuracy'] = f'SCS {container_name} OK'

    # Set unmatched containers where '_merge' != 'both'
    unmatched_mask = merged_df['_merge'] != 'both'
    unmatched_containers = container_df[unmatched_mask]

    # Only proceed if there are unmatched containers
    if not unmatched_containers.empty:
        # Update 'Accuracy' for unmatched containers with an error message
        container_df.loc[unmatched_mask, 'Accuracy'] = f'ERROR: {container_name}'

        # Get correct values for unmatched containers from container_data
        def get_correct_value(row):
            matching_containers = container_data[container_data['Component'] == row['Component']]
            if not matching_containers.empty:
                return matching_containers.iloc[0]['ContainerValue']
            else:
                return 'N/A'

        # Apply function to get correct values for unmatched containers
        correct_values = unmatched_containers.apply(get_correct_value, axis=1)

        # Update the 'Correct Value' column in the original df for unmatched containers
        df.loc[unmatched_containers['index'], 'Correct Value'] = correct_values.values

    # Update the main df's 'Accuracy' column with the modified container_df's 'Accuracy'
    df.loc[container_df['index'], 'Accuracy'] = container_df['Accuracy']

    return df



def process_data_granular(json_path, container_name, container_df, df):
    # Load the JSON data and convert the relevant part into a DataFrame.
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    container_data = pd.DataFrame(json_data[container_name])

    # Ensure column names are consistent between DataFrames
    if 'ContainerValue' not in container_data.columns:
        raise KeyError(f"Expected 'ContainerValue' in {container_name} data")

    # Keep track of original indices in container_df for safe updates later
    container_df = container_df.reset_index(drop=False)

    # Merge container_df with container_data on Component and ContainerValue for exact matching.
    merged_df = pd.merge(container_df, container_data, how='left', 
                         left_on=['Component', 'Granular Container Value'], 
                         right_on=['Component', 'ContainerValue'], 
                         indicator=True)

    # Update 'Accuracy' where the match is found ('_merge' == 'both')
    matched_mask = merged_df['_merge'] == 'both'
    container_df.loc[matched_mask.index[matched_mask], 'Accuracy'] = f'SCS {container_name} OK'

    # Set unmatched containers where '_merge' != 'both'
    unmatched_mask = merged_df['_merge'] != 'both'
    unmatched_containers = container_df[unmatched_mask]

    # Only proceed if there are unmatched containers
    if not unmatched_containers.empty:
        # Update 'Accuracy' for unmatched containers with an error message
        container_df.loc[unmatched_mask, 'Accuracy'] = f'ERROR: {container_name}'

        # Get correct values for unmatched containers from container_data
        def get_correct_value(row):
            matching_containers = container_data[container_data['Component'] == row['Component']]
            if not matching_containers.empty:
                return matching_containers.iloc[0]['ContainerValue']
            else:
                return 'N/A'

        # Apply function to get correct values for unmatched containers
        correct_values = unmatched_containers.apply(get_correct_value, axis=1)

        # Update the 'Correct Value' column in the original df for unmatched containers
        df.loc[unmatched_containers['index'], 'Correct Value'] = correct_values.values

    # Update the main df's 'Accuracy' column with the modified container_df's 'Accuracy'
    df.loc[container_df['index'], 'Accuracy'] = container_df['Accuracy']

    return df