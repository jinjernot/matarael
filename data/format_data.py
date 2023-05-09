import openpyxl
from openpyxl.styles import PatternFill,Font
import pandas as pd

def formateData():

    wb = openpyxl.load_workbook('SCS_QA.xlsx')

    worksheet = wb.active
    header_fill = PatternFill(start_color='0072C6', end_color='0072C6', fill_type='solid') # Add nice fill

    for cell in worksheet[1]:
        cell.fill = header_fill
    
    for column in worksheet.columns:
        max_length = 0
        column_name = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        worksheet.column_dimensions[column_name].width = adjusted_width

    for cell in worksheet['H']:
        if 'ERROR' in str(cell.value):
            font = cell.font
            cell.font = Font(color='FF0000', name=font.name, size=font.size) # Set font color to red
    
    wb.save('SCS_QA.xlsx')