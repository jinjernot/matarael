import pandas as pd

def cleanS(file):
    df = pd.read_excel(file) #load the file
    df.drop(index=range(5), inplace=True) #remove the first 5 rows
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])

    split_string = lambda x: '/'.join(x.split('/')[2:]) if x and isinstance(x, str) and len(x.split('/')) >= 2 else x #clean up the string
    df['ContainerName'] = df['ContainerName'].apply(split_string)#split the string

    df['Tag'] = df['ContainerName'].str.extract('\[(.*?)\]', expand=False) #create new column with the tag
    df['ContainerName'] = df['ContainerName'].str.replace('\[.*?\]', '', regex=True) #clean the tag

    idx_chunk = (df.iloc[0] == 'ChunkValue').values #search for the columns chunk and M to swap
    idx_m = (df.iloc[0] == 'M').values
    df.loc[:, idx_chunk], df.loc[:, idx_m] = df.loc[:, idx_m].values, df.loc[:, idx_chunk].values

    nan_columns = df.columns[pd.isna(df.columns)].tolist() #look for NaN headers
    df = df.drop(columns=nan_columns)#remove columns with NaN header

    first_col = df.iloc[:, 0] #move last column to the second position
    last_col = df.iloc[:, -1]
    middle_cols = df.iloc[:, 1:-1]
    new_df = pd.concat([first_col, last_col, middle_cols], axis=1)
    writer = pd.ExcelWriter(file, engine='xlsxwriter') #create a writer object
    
    new_df.to_excel("Summary.xlsx", sheet_name="oli", index=False) #create the excel
  
    return

