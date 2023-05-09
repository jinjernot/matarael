import pandas as pd

def cleanE(file):
    df = pd.read_excel(file) #load the file
    cols_to_drop = ['Length', 'Definition', 'Example', 'Format', 'Business Rule']
    cols_to_drop.extend([col for col in df.columns if col.startswith('[Model')])
    df = df.drop(cols_to_drop, axis=1)
    df = df.drop([0, 1, 2])

    new_column2 = df['ContainerName'].str.split('/', n=1, expand=True)[1].str.split('/', n=1, expand=True)[0]
    df.insert(loc=0, column='Container Group 2', value=new_column2)

    new_column = df['ContainerName'].str.split('/', n=1, expand=True)[0]
    df.insert(loc=0, column='Container Group 1', value=new_column)

    df['ContainerName'] = df['ContainerName'].str.split('/', n=2, expand=True)[2]

    container_type = df.pop('ContainerType')
    df.insert(loc=0, column='ContainerType', value=container_type)

    df.to_excel("Report.xlsx", index=False)

    return