import pandas as pd

def battery_life(df):
    try:
        # Create a new DataFrame
        barrido_df = df.drop_duplicates(subset='SKU').reset_index(drop=True)
        
        # Define column headers
        headers = ['SKU', 'displaybright', 'displaymet', 'displaycolorgamut',
                   'facet_maxres', 'graphicseg_01header', 'processorname',
                   'filter_storagetype', 'storage_acceleration', 
                   'graphicseg_01card_01', 'facet_graphics']
        
        # Populate the new DataFrame
        for header in headers[1:]:
            barrido_df[header] = df.loc[df['ContainerName'] == header, 'ContainerValue'].values
        
    except Exception as e:
        print(e)
    
    return barrido_df
