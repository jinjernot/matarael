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

    productcolor_df = df.loc[df['ContainerName'] == 'productcolour']

    mask = ((productcolor_df['PhwebDescription'] == 'ID SNW PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Snow white')) | \
        ((productcolor_df['PhwebDescription'] == 'ID STB PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Jet black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID CBG MSKT STD wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Chalkboard gray cover and base, black keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID CBG PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Chalkboard gray')) | \
        ((productcolor_df['PhwebDescription'] == 'ID CCW ALU wHDC FPR') & \
            (productcolor_df['ContainerValue'] == 'Ceramic white aluminum cover, natural silver base and natural silver aluminum keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID CCW PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Ceramic white, black chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID CCW PLA wHDC TNR fThin') & \
            (productcolor_df['ContainerValue'] == 'Ceramic white, black chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID DMW IMR wHDC US layout') & \
            (productcolor_df['ContainerValue'] == 'Diamond white cover and base, dove silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID ENB PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Evening Blue cover and base, starry blue keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID FGB ALU wHDC FPR') & \
            (productcolor_df['ContainerValue'] == 'Fog blue aluminum cover, cloud blue base and cloud blue aluminum keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID FTL ALU nSDC wHDC TNR FPR') & \
            (productcolor_df['ContainerValue'] == 'Forest teal aluminum cover, light teal base and light teal aluminum keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID IOB PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Indigo blue')) | \
        ((productcolor_df['PhwebDescription'] == 'ID JTB MSKT STD wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Jet black cover and base, black keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SWH PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Starry white')) | \
        ((productcolor_df['PhwebDescription'] == 'ID JTB PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Jet black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SDB PT GSWP wHDC 21C1') & \
            (productcolor_df['ContainerValue'] == 'Shadow black, chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SWH PLA wFHDC IR') & \
            (productcolor_df['ContainerValue'] == 'Starry white')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SKB PLA w5MPC IR UHD') & \
            (productcolor_df['ContainerValue'] == 'Sparkling black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID WGD ALU nSDC wHDC TNR nFPR') & \
            (productcolor_df['ContainerValue'] == 'Warm gold')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV ALU+PLA w5MPC nFPR nWWAN') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID MCS PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Mica silver, black chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO WHT GLA 600W') & \
            (productcolor_df['ContainerValue'] == 'Snow white, glass side panel, dark chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO MCS SHT MTL 500W') & \
            (productcolor_df['ContainerValue'] == 'Mica silver metal')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA nSDC wHDC TNR FPR FHD TS') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV PLA wHDC FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU wHDC FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum cover and keyboard frame, natural silver base')) | \
        ((productcolor_df['PhwebDescription'] == 'ID MNS +MNS PLA US layout nBEO') & \
            (productcolor_df['ContainerValue'] == 'Mineral silver cover, natural silver base and keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU nSDC wHDC TNR FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum cover and keyboard frame, natural silver base')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV ALU+PLA w5MPC FPR nWWAN') & \
            (productcolor_df['ContainerValue'] == 'Natural silver cover and base, natural silver aluminum keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV ALU+PLA w5MPC nFPR nWWAN') & \
            (productcolor_df['ContainerValue'] == 'Natural silver cover and base, natural silver aluminum keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU nSDC nFPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum cover and keyboard frame, natural silver base')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA wHDC TNR FPR FHD TS') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU nSDC wHDC TNR nFPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU nSDC wHDC TNR FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV PLA+PLA wHDC TNR nFPR nWWAN') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV MTE PT wHDC TNR FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA wHDC FPR FHD TS') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID MCS PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Mica silver, dark chrome logo')) 

    

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
