from openpyxl.styles import PatternFill,Font

from app.config.paths import SCS_QA_FILE_PATH

import openpyxl

def format_data():
    """This function is used to to formate the data in the excel file, bold headers, adjust the column width and highlight the errors"""

    # Load Workbook and get the active sheet
    wb = openpyxl.load_workbook(SCS_QA_FILE_PATH) # Server
    #wb = openpyxl.load_workbook('SCS_QA.xlsx') # Local
    worksheet = wb.active

    # Bold and color the headers
    header_fill = PatternFill(start_color='0072C6', end_color='0072C6', fill_type='solid') 
    for cell in worksheet[1]:
        cell.fill = header_fill
    
    # Loop over all the cells in column `I`.
    for cell in worksheet['J']:
        if 'ERROR' in str(cell.value):
            font = cell.font
            cell.font = Font(color='FF0000', name=font.name, size=font.size)
    # Save the workbook to a file called `SCS_QA.xlsx`.
    wb.save(SCS_QA_FILE_PATH) # Server
    #wb.save('SCS_QA.xlsx') # Local