import pandas as pd

def avCheck(df):

    # Check for duplicate combinations of 'SKU', 'Component', and 'ContainerName'
    duplicate_mask = df.duplicated(subset=['SKU','ComponentGroup', 'ContainerName'], keep=False)
    
    # Update 'Accuracy' column where duplicates are found
    df.loc[duplicate_mask, 'Additional Information'] = 'Duplicated AV'
    return df