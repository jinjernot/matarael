import pandas as pd

data = pd.read_excel('clean.xlsx')

data = data[data['ContainerValue'] != '[BLANK]']

data.to_excel('chido.xlsx', index=False)