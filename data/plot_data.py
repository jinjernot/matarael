import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def createPlot():
    df = pd.read_excel('SCS_QA.xlsx')
    df = df.dropna(subset=['Accuracy'])
    
    error_df = df[df['Accuracy'].str.contains('ERROR')]
    container_count = error_df.groupby('ContainerName').size().reset_index(name='Count')
    top_containers = container_count.sort_values('Count', ascending=False).head(10)

    barcolor = '#0096d6'
    plt.figure(figsize=(12, 8))
    plt.bar(top_containers['ContainerName'], top_containers['Count'], color=barcolor)
    plt.title('Top Offenders')
    plt.xlabel('Container Name')
    plt.ylabel('')
    plt.xticks(rotation=25, ha='right')
    plt.savefig('./static/images/chart.png')

    wb = load_workbook('SCS_QA.xlsx')
    ws = wb.active
    ws.title = 'SCS QA Report'
    ws = wb.create_sheet(title='Bar Plot')
    ws = wb.active
    ws = wb['Bar Plot']
    img = Image('./static/images/chart.png')
    ws.add_image(img, 'A1')
    wb.save('SCS_QA.xlsx')
