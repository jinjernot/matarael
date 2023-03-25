import pandas as pd
import glob
import openpyxl
from openpyxl.styles import PatternFill

def loadReport():
    """load the prism report from the folder specified, must be a xlsx file"""
    folder_path = "./xlsx/"
    xlsx_files = glob.glob(folder_path + "*.xlsx")

    for xlsx_file in xlsx_files: #loop through all the files
        cleanReport(xlsx_file)

def cleanReport(xlsx_file):
    df = pd.read_excel(xlsx_file) #load the file

    cols_to_drop = ['Option', 'Status','SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue' ,'ExtendedDescription','ComponentCompletionDate','ComponentReadiness','SKUReadiness']
    df = df.drop(cols_to_drop, axis=1)
    df[['Accuracy', 'Correct Value', 'Additional Information']] = ''

    ################################################################ Compare productcolour

    # filter the dataframe based on ContainerName
    productcolor_df = df.loc[df['ContainerName'] == 'productcolour']

    # check the conditions and update the Accuracy column
    mask = (productcolor_df['PhwebDescription'].str.contains('SNW') & \
            (productcolor_df['ContainerValue'] == 'Snow white')) | \
        (productcolor_df['PhwebDescription'].str.contains('RED') & \
            (productcolor_df['ContainerValue'].str.contains('crimson', case=False)))

    productcolor_df.loc[mask, 'Accuracy'] = 'SCS OK'
    productcolor_df.loc[~mask, 'Accuracy'] = 'ERROR'

    # update the original dataframe with the new values
    df.update(productcolor_df['Accuracy'])










    df.to_excel('chido.xlsx', index=False)
    workbook = openpyxl.load_workbook('chido.xlsx')
    worksheet = workbook.active
    header_fill = PatternFill(start_color='0072C6', end_color='0072C6', fill_type='solid')
    for cell in worksheet[1]:
        cell.fill = header_fill
    workbook.save('chido.xlsx')

    print(df)
    
def main():
    loadReport()


if __name__ == "__main__":
    main()
