import pandas as pd

def av_check(df):
    # Check for duplicate combinations
    duplicate_mask = df.duplicated(subset=['SKU','ComponentGroup', 'ContainerName'], keep=False)
    
    # Update 'Additional Information' column where duplicates are found
    df.loc[duplicate_mask, 'Additional Information'] = 'Duplicated AV'
    return df