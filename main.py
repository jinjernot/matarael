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

    ################################################################ Colors

    productcolor_df = df.loc[df['ContainerName'].str.contains('colour')]

    maskColor = (productcolor_df['PhwebDescription'].str.contains('NSV') & \
                    (productcolor_df['ContainerValue'].str.contains('Natural silver', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('MCS') & \
                    (productcolor_df['ContainerValue'].str.contains('Mica silver', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('CCW') & \
                    (productcolor_df['ContainerValue'].str.contains('Ceramic white', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SNW') & \
                    (productcolor_df['ContainerValue'].str.contains('Snow white', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SWH') & \
                    (productcolor_df['ContainerValue'].str.contains('Starry white', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('NFB') & \
                    (productcolor_df['ContainerValue'].str.contains('Nightfall black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('JTB') & \
                    (productcolor_df['ContainerValue'].str.contains('Jet black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SKB') & \
                    (productcolor_df['ContainerValue'].str.contains('Sparkling black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('PLG') & \
                    (productcolor_df['ContainerValue'].str.contains('Starry white', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('JKB') & \
                    (productcolor_df['ContainerValue'].str.contains('Dark black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('CBG') & \
                    (productcolor_df['ContainerValue'].str.contains('Chalkboard gray', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('STB') & \
                    (productcolor_df['ContainerValue'].str.contains('Jet black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('WHT') & \
                    (productcolor_df['ContainerValue'].str.contains('Snow white', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SDB') & \
                    (productcolor_df['ContainerValue'].str.contains('Shadow black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('POB') & \
                    (productcolor_df['ContainerValue'].str.contains('Poseidon blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('IOB') & \
                    (productcolor_df['ContainerValue'].str.contains('Indigo blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('PFB') & \
                    (productcolor_df['ContainerValue'].str.contains('Performance blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('BLK') & \
                    (productcolor_df['ContainerValue'].str.contains('Black', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SPB') & \
                    (productcolor_df['ContainerValue'].str.contains('Spruce blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('ENB') & \
                    (productcolor_df['ContainerValue'].str.contains('Evening Blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('PLG') & \
                    (productcolor_df['ContainerValue'].str.contains('Pale gold', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SBL') & \
                    (productcolor_df['ContainerValue'].str.contains('Space blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('WGD') & \
                    (productcolor_df['ContainerValue'].str.contains('Warm gold', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('SFW') & \
                    (productcolor_df['ContainerValue'].str.contains('Snowflake white', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('MNS') & \
                    (productcolor_df['ContainerValue'].str.contains('Mineral silver', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('FTL') & \
                    (productcolor_df['ContainerValue'].str.contains('Forest teal', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('TBS') & \
                    (productcolor_df['ContainerValue'].str.contains('Turbo silver', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('FGB') & \
                    (productcolor_df['ContainerValue'].str.contains('Fog blue', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('STF') & \
                    (productcolor_df['ContainerValue'].str.contains('Starry forest', case=False))) | \
                (productcolor_df['PhwebDescription'].str.contains('NTB') & \
                    (productcolor_df['ContainerValue'].str.contains('Nocturne blue', case=False)))

    productcolor_df.loc[maskColor, 'Accuracy'] = 'SCS Color OK'
    productcolor_df.loc[~maskColor, 'Accuracy'] = 'ERROR'

    df.update(productcolor_df['Accuracy'])

######################################################################## FPR

    fingerprread_df = df.loc[df['ContainerName'].str.contains('fingerprread')]
    maskFPR = (fingerprread_df['PhwebDescription'].str.contains('FPR') & \
                    (fingerprread_df['ContainerValue'].str.contains('Fingerprint reader', case=False)))

    fingerprread_df.loc[maskFPR, 'Accuracy'] = 'SCS FPR OK'
    fingerprread_df.loc[~maskFPR, 'Accuracy'] = 'ERROR'

    df.update(fingerprread_df['Accuracy'])

######################################################################## Webcam


    webcam_df = df.loc[df['ContainerName'].str.contains('webcam')]
    maskWebcam = (webcam_df['PhwebDescription'].str.contains('wHDC') & \
                    (webcam_df['ContainerValue'].str.contains('HP True Vision 720p HD camera with integrated dual array digital microphones', case=False))) | \
                (webcam_df['PhwebDescription'].str.contains('wHDC TNR') & \
                    (webcam_df['ContainerValue'].str.contains('HP True Vision 720p HD camera with temporal noise reduction and integrated dual array digital microphones', case=False))) | \
                (webcam_df['PhwebDescription'].str.contains('w5MPC') & \
                    (webcam_df['ContainerValue'].str.contains('HP True Vision 5MP camera with camera shutter, temporal noise reduction and integrated dual array digital microphones', case=False))) | \
                (webcam_df['PhwebDescription'].str.contains('wFHDC IR') & \
                    (webcam_df['ContainerValue'].str.contains('HP Wide Vision 1080p FHD IR privacy camera with integrated dual array digital microphones', case=False)))

    webcam_df.loc[maskWebcam, 'Accuracy'] = 'SCS Webcam OK'
    webcam_df.loc[~maskWebcam, 'Accuracy'] = 'ERROR'

    df.update(webcam_df['Accuracy'])


################################################################ Stylus


    webcam_df = df.loc[df['ContainerName'].str.contains('webcam')]
    maskWebcam = (webcam_df['PhwebDescription'].str.contains('wHDC') & \
                    (webcam_df['ContainerValue'].str.contains('HP True Vision 720p HD camera with integrated dual array digital microphones', case=False))) | \

    webcam_df.loc[maskWebcam, 'Accuracy'] = 'SCS Webcam OK'
    webcam_df.loc[~maskWebcam, 'Accuracy'] = 'ERROR'

    df.update(webcam_df['Accuracy'])


    df.to_excel('chido.xlsx', index=False)
    workbook = openpyxl.load_workbook('chido.xlsx')
    worksheet = workbook.active
    header_fill = PatternFill(start_color='0072C6', end_color='0072C6', fill_type='solid')
    for cell in worksheet[1]:
        cell.fill = header_fill
    workbook.save('chido.xlsx')

def main():
    loadReport()


if __name__ == "__main__":
    main()
