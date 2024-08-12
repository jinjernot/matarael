import pandas as pd

df = pd.read_excel("Graphic facet.xlsx")

processor_values = ["NVIDIA", "Intel", "AMD"]
graphic_values = [0, 2, 4, 8, 16]

processor = df[df['PDCHVUNM'].str.contains('|'.join(processor_values), case=False, na=False)]

graphics = df[df['PDCHVUNM'].isin(graphic_values)]

cagada = df[~df['PDCHVUNM'].str.contains('|'.join(processor_values), case=False, na=False) & ~df['PDCHVUNM'].isin(graphic_values)]

with pd.ExcelWriter('data.xlsx') as writer:
    processor.to_excel(writer, sheet_name='processor', index=False)
    graphics.to_excel(writer, sheet_name='graphics', index=False)
    cagada.to_excel(writer, sheet_name='cagada', index=False)
