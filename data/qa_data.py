import pandas as pd
from data.format_data import formateData
from data.process_data import processData

def cleanReport(file):
    """Load, Clean and create a a new xlsx file"""
    df = pd.read_excel(file) # Load the file
    df = df[df['ContainerValue'] != '[BLANK]'] # Remove blanks
    df.replace('\u00A0', ' ', regex=True, inplace=True) # Remove weird spaces

    cols_to_drop = ['Option', 'Status','SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue' ,'ExtendedDescription','ComponentCompletionDate','ComponentReadiness','SKUReadiness'] # Remove some columns
    df = df.drop(cols_to_drop, axis=1)
    df[['Accuracy', 'Correct Value', 'Additional Information']] = '' # Create new columns for SCS

################################################################ Memory ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('memstdes_01')]
    processData('json/memstdes_01.json', 'memstdes_01', container_df, df)

################################################################ Colour ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('productcolour')]
    processData('json/productcolour.json', 'productcolour', container_df, df)
  
######################################################################## FPR ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('fingerprread')]
    processData('json/fingerprread.json', 'fingerprread', container_df, df)

################################################################ Stylus ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('stylus')]
    processData('json/stylus.json', 'stylus', container_df, df)

################################################################ Battery Type ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('batterytype')]
    processData('json/batterytype.json', 'batterytype', container_df, df)

################################################################ Chipset ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('chipset')]
    processData('json/chipset.json', 'chipset', container_df, df)

################################################################ Processor Name ################################################################

    container_df = df.loc[(df['ContainerName'] == 'processorname') & df['ComponentGroup'].str.contains('Processor')]
    processData('json/processorname.json', 'processorname', container_df, df)

################################################################ Display ################################################################

    container_df = df.loc[df['ContainerName'].str.strip() == 'display']
    processData('json/display.json', 'display', container_df, df)

################################################################ Hard Drive ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('hd_01des') & df['ComponentGroup'].str.contains('Hard Drive')]
    processData('json/hd_01des.json', 'hd_01des', container_df, df)

################################################################ Operating System ################################################################

    container_df = df.loc[df['ContainerName'].str.strip() == 'osinstalled']
    processData('json/osinstalled.json', 'osinstalled', container_df, df)


################################################################ Power Supply Type ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('powersupplytype')]
    processData('json/powersupplytype.json', 'powersupplytype', container_df, df)

################################################################ EPEAT ################################################################

    energyeffcomp_df = df.loc[df['ContainerName'].str.contains('energyeffcomp')]
    maskEPEAT = (energyeffcomp_df['PhwebDescription'].str.contains('FLAG') & \
                        (energyeffcomp_df['ContainerValue'].str.contains('EPEAT® registered', regex=False, case=False)))

    energyeffcomp_df.loc[maskEPEAT, 'Accuracy'] = 'SCS EPEAT OK'
    energyeffcomp_df.loc[~maskEPEAT, 'Accuracy'] = 'ERROR EPEAT'

    df.update(energyeffcomp_df['Accuracy'])

################################################################ ENERGY STAR ################################################################

    energystar_df = df.loc[df['ContainerName'].str.contains('energystar')]
    maskES = (energystar_df['PhwebDescription'].str.contains('FLAG|ESTAR') & \
                        (energystar_df['ContainerValue'].str.contains('ENERGY STAR® certified', regex=False, case=False)))
    
    energystar_df.loc[maskES, 'Accuracy'] = 'SCS ENERGY STAR OK'
    energystar_df.loc[~maskES, 'Accuracy'] = 'ERROR ENERGY STAR'

    df.update(energystar_df['Accuracy'])

################################################################ Graphic Card ################################################################

    graphicseg_02card_01_df = df.loc[df['ContainerName'].str.contains('graphicseg_02card_01') & df['ComponentGroup'].str.contains('Graphic card')]
    maskGraphicCard = (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX AMD Rdn RX 6400 4GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('AMD Radeon™ RX 6400 Graphics (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RX 6500M 4GB Ryzen5 5600H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('AMD Radeon™ RX 6500M Graphics (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX AMD Rdn RX 6600XT 8GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('AMD Radeon™ RX 6600 XT Graphics (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RX xxx 8GB Ryzen7 5800H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('AMD Radeon™ RX 6600M Graphics (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('RX 6650M 8GB') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('AMD Radeon™ RX 6650M Graphics (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX AMD Rdn RX 6700XT 12GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('AMD Radeon™ RX 6700 XT Graphics (12 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('Arc A370M 4G') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('Intel® Arc™ A370M Graphics (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX20504GB i7-1255U') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 2050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC 4GB i7-11370H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC 4GB PH i5-xxxxH 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC 4GB PH i7-xxxx 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC GTX 1650 4GB i5-11300H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® GTX 1650 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC GTX 1650 4GB i5-12500H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® GTX 1650 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC GTX 1650 4GB i7-12700H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® GTX 1650 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC GTX 1650 4GB Ryzen5 5600H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® GTX 1650 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC GTX 1650 4GB Ryzen7 5800H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® GTX 1650 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC MX450 2GB i7-1165G7 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX450 (2 GB GDDR5 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC MX550 2GB i5-1235U 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX550 (2 GB GDDR6 dedicated);', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC MXxxx 2GB PH i7-12xxx U15 17') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX550 (2 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC MX550 2GB i7-1255U nSDC 14') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX550 (2 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC MX550 2GB i7-1255U 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX550 (2 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050 4GB i7-12700H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050 4GB i5-12500H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050 4GB Ryzen5 5600H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050 4GB R7 6800H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050Ti 4GB i5-12500H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Ti Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050 4GB Ryzen7 5800H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050Ti 4GB i7-12700H 15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Ti Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050Ti 4GB i5-12500H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Ti Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050Ti 4GB Ryzen7 5800H15') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Ti Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050Ti 4GB R5 6600H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Ti Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3060 6GB i7-12700H 17') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Laptop GPU (6 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3060 6GB i5-12500H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Laptop GPU (6 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3060 6GB i5-11400H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Laptop GPU (6 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3060 6GB R7 6800H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Laptop GPU (6 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3060 6GB i9-12900HfOLED16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Laptop GPU (6 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3070 MQ 8GB Ryzen75800H16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 Laptop GPU (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3070Ti 8GB i7-12700H 17') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 Ti Laptop GPU (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3070Ti MQ 8GB R7 6800H 16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 Ti Laptop GPU (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3070TiMQ8GBRyzen96900HX16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 Ti Laptop GPU (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX3070TiMQ8GBfGSynci7-12700H1') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 Ti Laptop GPU (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX20504GB i5-1235U 17') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 2050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDSDSCMXxxx2GBPHi5-12xxxU15nSDC15-eg2') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX550 (2 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX3080Ti16GBfGSynci7-12700H17') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3080 Ti Laptop GPU (16 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDSDSCRTX3050MQ4GBPHi7xxxx32GBfOLED16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 Laptop GPU (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('BU IDSDSCRTX3070TiMQ8GBfGSynci9-12900H16') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 Ti Laptop GPU (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF MX450 2GB ADL-P') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® MX450 (2 GB DDR5 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF GTX 1650 Super 4GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce® GTX 1650 SUPER™ (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3060 12GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 (12 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3050 8GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3050 MQ 4GB GDDR6 G4') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3050 (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3070 8GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3070 (8 GB GDDR6 dedicated) with LHR', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3060 Ti 8GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Ti (8 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3080 10GB GDDR6X') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3080 (10 GB GDDR6X dedicated) with LHR', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3080Ti 12GB GDDR6X') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3080 Ti (12 GB GDDR6X dedicated)', regex=False, case=False))) | \
                    (graphicseg_02card_01_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3060 Ti 8GB GDDR6') & \
                        (graphicseg_02card_01_df['ContainerValue'].str.contains('NVIDIA® GeForce RTX™ 3060 Ti (8 GB GDDR6 dedicated) with LHR', regex=False, case=False)))

    graphicseg_02card_01_df.loc[maskGraphicCard, 'Accuracy'] = 'SCS Graphic Card OK'
    graphicseg_02card_01_df.loc[~maskGraphicCard, 'Accuracy'] = 'ERROR Graphic Card'

    df.update(graphicseg_02card_01_df['Accuracy'])

################################################################ Optical Drive ################################################################

    cdromdvd_df = df.loc[df['ContainerName'].str.contains('cdromdvd') & df['ComponentGroup'].str.contains('Optical Drive')]
    maskCD = (cdromdvd_df['PhwebDescription'].str.contains('DVDWR') & \
                        (cdromdvd_df['ContainerValue'].str.contains('DVD-Writer', case=False))) | \
                    (cdromdvd_df['PhwebDescription'].str.contains('NO ODD') & \
                        (cdromdvd_df['ContainerValue'].str.contains('##BLANK##', case=False))) | \
                    (cdromdvd_df['PhwebDescription'].str.contains('MISC No ODD non-Win') & \
                        (cdromdvd_df['ContainerValue'].str.contains('##BLANK##', case=False))) | \
                        cdromdvd_df['ContainerValue'].str.contains('##BLANK##', case=False)
    


    cdromdvd_df.loc[maskCD, 'Accuracy'] = 'SCS Optical Drive OK'
    cdromdvd_df.loc[~maskCD, 'Accuracy'] = 'ERROR Optical Drive'

    df.update(cdromdvd_df['Accuracy'])

################################################################ Wireless Tech ################################################################

    wirelesstech_df = df.loc[df['ContainerName'].str.strip() == 'wirelesstech']
    maskWirelessTech = (wirelesstech_df['PhwebDescription'].str.contains('WLAN IWiFi6AX201ax2x2MUMIMOnvP160MHz+BT5', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wi-Fi 6 AX201 (2x2) and Bluetooth® 5.2 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT ac 1x1 +BT 4.2LE WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN I AX210 Wi-Fi6e nvP 160MHz +BT5.2WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wi-Fi 6E AX210 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN I AX211 Wi-Fi6e 160MHz +BT 5.2 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wi-Fi 6E AX211 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN I AX411 Wi-Fi6e 160MHz +BT 5.2 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wi-Fi 6E AX411 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN I 9461 ac 1x1 MU-MIMO nvP+BT5WW1Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wireless-AC 9461 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 5.1 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ac 2x2 +BT 5 WW 2Ant', regex=False) & \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False) | \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wi-Fi 6E AX211 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN Wi-Fi6 +BT 5.2', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('MediaTek Wi-Fi 6 MT7921 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('Arc A370M 4G', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Arc™ A370M Graphics (4 GB GDDR6 dedicated)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT ac 2x2 +BT 5 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False) | \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT 8852AE Wi-Fi6 +BT 5.2 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek Wi-Fi 6 (2x2) and Bluetooth® 5.2 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ac 1x1 +BT 4.2 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False) | \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE-M 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ac 1x1 +BT 4.2 WW 1Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE-M 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False) | \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ac2x2 +BT 5.0 WW 2Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT 8821CE ac1x1 +BT 4.2', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ax1x2 +BT 5.2 WW 2Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek Wi-Fi 6 (1x2) and Bluetooth® 5.2 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT ac2x2 +BT 5.0 2Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT RTL8821CE ac 1x1 +BT 4.2 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT RTL8822CE ac 2x2 +BT 5 WW', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT ac 2x2 +BT 5 WW 2Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® and Bluetooth® 5 wireless card', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN Wi-Fi6e +BT 5.2', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('MediaTek Wi-Fi 6E MT7922 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN IWiFi6AX201ax2x2MUMIMOnvP160MHz+BT5', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('Intel® Wi-Fi 6 AX201 (2x2) and Bluetooth® 5.2 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ax2x2 +BT 5.2 2Ant', regex=False) & \
                        (wirelesstech_df['ContainerValue'].str.contains('MediaTek Wi-Fi 6 MT7921 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False) | \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek Wi-Fi 6 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False) | \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek Wi-Fi 6 (2x2) and Bluetooth® 5.2 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN ax2x2 +BT 5.2 WW 2Ant', regex=False) & \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek Wi-Fi 6 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False) | \
                        (wirelesstech_df['ContainerValue'].str.contains('MediaTek Wi-Fi 6 MT7921 (2x2) and Bluetooth® 5.3 wireless card (supporting gigabit data rate)', regex=False, case=False))) | \
                    (wirelesstech_df['PhwebDescription'].str.contains('WLAN RT RTL8821CE ac 1x1 +BT 4.2LE WW', regex=False) & \
                        wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE-M 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False) | \
                        (wirelesstech_df['ContainerValue'].str.contains('Realtek RTL8821CE 802.11a/b/g/n/ac (1x1) Wi-Fi® and Bluetooth® 4.2 wireless card', regex=False, case=False)))

    wirelesstech_df.loc[maskWirelessTech, 'Accuracy'] = 'SCS Wireless Tech OK'
    wirelesstech_df.loc[~maskWirelessTech, 'Accuracy'] = 'ERROR Wireless Tech'

    df.update(wirelesstech_df['Accuracy'])

################################################################ Keyboard ################################################################

    keybrd_df = df.loc[df['ContainerName'].str.contains('keybrd')]
    maskKeyboard = (keybrd_df['PhwebDescription'].str.contains('HP 225 Black Wired KB/Mse Combo') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 225 Black Wired Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 225 White Wired KB/Mse Combo') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 225 White Wired Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 230 WL Mouse+KB Combo BLK', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('HP 230 Black Wireless Keyboard and Mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 230 WL Mouse+KB Combo WHT', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('HP 230 White Wireless Keyboard and Mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 310 Blk Wired KB/Mse') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 310 Black Wired Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 310 White Wired KB/Mse') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 310 White Wired Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 510SP WHT WRLS KB/Mse') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 510SP White Wireless Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 510SP BLK WRLS KB/Mse') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 510SP Black Wireless Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 710 White WLS KB/Mse') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 710 White Wireless Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 710 Blk WLS KB/Mse') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 710 Black Wireless Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD BLR CP BL-RGB 4Zone') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 4-zone RGB backlit, shadow black keyboard and 26-Key Rollover Anti-Ghosting Key technology', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CBL CP BL num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, cloud blue keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD BLR CP BL-WHT 1Zone') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 1-zone white backlit, shadow black keyboard and 26-Key Rollover Anti-Ghosting Key technology', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CCW CP+IS BL num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, ceramic white keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CBL CP num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, cloud blue keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CBL ISK CP+IS BL', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, cloud blue keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CCW ISK CP BL') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, ceramic white keyboard;', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CCW ISK PT CP+IS BL numkypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, ceramic white keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CCW CP+IS BL-RGB 4Zone', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 4-zone RGB backlit, ceramic white keyboard and 26-Key Rollover Anti-Ghosting Key technology', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD ENB FS STD CP+IS num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, evening blue keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD CCWISKPTCP+ISBL-RGB1Zonenum', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 1-zone RGB backlit, ceramic white keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD ENB FS STD CP+IS num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, evening blue keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD JTB ISK STD TP num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, jet black keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD JTB ISK STD CP num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, jet black keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD LMG CP BL num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, luminous gold keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD JTB STD CP') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, jet black keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('MISC No Included Keyboard') & \
                        (keybrd_df['ContainerValue'].str.contains('##BLANK##', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD WTLISKWNBPwrBtnPTCP+ISBL1Z', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 1-zone white backlit, mica silver keyboard and 26-Key Rollover Anti-Ghosting Key technology', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD MCS CP BL-RGB 4Zone') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 4-zone RGB backlit, mica silver keyboard and 26-Key Rollover Anti-Ghosting Key technology', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV CP') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, natural silver keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD POB ISK CP BL') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, poseidon blue keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD PLG ISK CP BL') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, pale gold keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('HP 510 WHT WRLS KB/MSE') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 510 White Wireless Keyboard and mouse combo', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV ISK PT CP BL num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, natural silver keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD MCS CP+IS BL num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, mica silver keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD HP 125 BLK WD') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 125 USB Black Wired Keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD HP 125 WHT WD') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 125 USB White Wired Keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD LMG CP') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, luminous gold keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD HP 125 WHT WD') & \
                        (keybrd_df['ContainerValue'].str.contains('HP 125 USB White Wired Keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD JTB ISK PT CP BL') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, jet black keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD JTB ISK STD CP') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, jet black keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD SNW ISK STD CP') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, snow white keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD SNW ISK STD CP num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, snow white keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV ISK PT CP BL num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, natural silver keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV ISK PT CP num kypd') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, natural silver keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV ISK CP BL') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, natural silver keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD SBL ISK PT CP+IS BL', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, space blue keyboard', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD PFB CP+IS BL num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, performance blue keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD ENB FS STD CP+IS num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, evening blue keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV CP BL num kypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, natural silver keyboard with numeric keypad', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD SDB CP BL-RGB 4Zone numkypd', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, 4-zone RGB backlit, shadow black keyboard with numeric keypad and 26-Key Rollover Anti-Ghosting Key technology', case=False))) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NSV ISK PT CP+IS BL', regex=False) & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, natural silver keyboard', case=False))) | \
                        keybrd_df['ContainerValue'].str.contains('##BLANK##', case=False) | \
                    (keybrd_df['PhwebDescription'].str.contains('KBD NFB ISK CP BL') & \
                        (keybrd_df['ContainerValue'].str.contains('Full-size, backlit, nightfall black keyboard', case=False)))

    keybrd_df.loc[maskKeyboard, 'Accuracy'] = 'SCS Keyboard OK'
    keybrd_df.loc[~maskKeyboard, 'Accuracy'] = 'ERROR Keyboard'

    df.update(keybrd_df['Accuracy'])


################################################################ Video Connectors ################################################################

    videoconnectors_df = df.loc[df['ContainerName'].str.contains('videoconnectors')]
    maskVideoDonnectors = (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF 12GB GDDR6X') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI; 3 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF 6GB GDDR6 RKL-S') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI; 3 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF 8GB GDDR6 RKL-S') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI; 3 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3060 12GB GDDR6') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI 2.1; 1 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3060 Ti 8GB GDDR6') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI 2.1; 1 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 3070 8GB GDDR6') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI 2.1; 3 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 4080 12GB GDDR6X') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI 2.1; 3 DisplayPort™', regex=False, case=False))) | \
                    (videoconnectors_df['PhwebDescription'].str.contains('GFX NVIDIA GeF RTX 4080 16GB GDDR6X') & \
                        (videoconnectors_df['ContainerValue'].str.contains('1 HDMI; 3 DisplayPort™', regex=False, case=False)))

    videoconnectors_df.loc[maskVideoDonnectors, 'Accuracy'] = 'SCS Video Connectors OK'
    videoconnectors_df.loc[~maskVideoDonnectors, 'Accuracy'] = 'ERROR Video Connectors'

    df.update(videoconnectors_df['Accuracy'])

################################################################ Special Features ################################################################

    perftechn_df = df.loc[df['ContainerName'].str.contains('perftechn')]
    maskSpecialFeatures = (perftechn_df['PhwebDescription'].str.contains('Intel Evo') & \
                        (perftechn_df['ContainerValue'].str.contains('Intel® Evo™ laptop', case=False)))

    perftechn_df.loc[maskSpecialFeatures, 'Accuracy'] = 'SCS Special Features OK'
    perftechn_df.loc[~maskSpecialFeatures, 'Accuracy'] = 'ERROR Special Features'

    df.update(perftechn_df['Accuracy'])
    
########################################################################################################################################
################################################################ Facets ################################################################
########################################################################################################################################


################################################################ facet_environ ################################################################

    facet_environ_df = df.loc[df['ContainerName'].str.contains('facet_environ')]
    maskfacet_environ = (facet_environ_df['PhwebDescription'].str.contains('FLAG') & \
                        (facet_environ_df['ContainerValue'].str.contains('ENERGY STAR® certified; EPEAT® registered', regex=False, case=False)))

    facet_environ_df.loc[maskfacet_environ, 'Accuracy'] = 'SCS ENERGY STAR OK'
    facet_environ_df.loc[~maskfacet_environ, 'Accuracy'] = 'ERROR ENERGY STAR'

    df.update( facet_environ_df['Accuracy'])

################################################################ facet_memstd ################################################################

    facet_memstd_df = df.loc[df['ContainerName'].str.contains('facet_memstd') & df['ComponentGroup'].str.contains('Memory')]

    maskfacet_memstd = (facet_memstd_df['PhwebDescription'].str.contains('12GB') & \
                            (facet_memstd_df['ContainerValue'].str.contains('112', regex=False, case=False))) | \
                        (facet_memstd_df['PhwebDescription'].str.contains('128GB') & \
                            (facet_memstd_df['ContainerValue'].str.contains('128', regex=False, case=False))) | \
                        (facet_memstd_df['PhwebDescription'].str.contains('16') & \
                            (facet_memstd_df['ContainerValue'].str.contains('16', regex=False, case=False))) | \
                        (facet_memstd_df['PhwebDescription'].str.contains('32GB') & \
                            (facet_memstd_df['ContainerValue'].str.contains('32', regex=False, case=False))) | \
                        (facet_memstd_df['PhwebDescription'].str.contains('64GB') & \
                            (facet_memstd_df['ContainerValue'].str.contains('64', regex=False, case=False))) | \
                        (facet_memstd_df['PhwebDescription'].str.contains('8GB') & \
                            (facet_memstd_df['ContainerValue'].str.contains('8', regex=False, case=False))) | \
                        (facet_memstd_df['PhwebDescription'].str.contains('4GB') & \
                            (facet_memstd_df['ContainerValue'].str.contains('4', regex=False, case=False)))                            

    facet_memstd_df.loc[maskfacet_memstd, 'Accuracy'] = 'SCS Facet Memory OK'
    facet_memstd_df.loc[~maskfacet_memstd, 'Accuracy'] = 'ERROR Facet Memory'

    df.update(facet_memstd_df['Accuracy'])

################################################################ facet_cap ################################################################

    facet_cap_df = df.loc[df['ContainerName'].str.contains('facet_cap')]
    maskfacet_cap = (facet_cap_df['PhwebDescription'].str.contains('1T') & \
                        (facet_cap_df['ContainerValue'].str.contains('1000', regex=False, case=False))) | \
                    (facet_cap_df['PhwebDescription'].str.contains('512') & \
                        (facet_cap_df['ContainerValue'].str.contains('512', regex=False, case=False)))
    
    facet_cap_df.loc[maskfacet_cap, 'Accuracy'] = 'SCS Facet Hard Drive OK'
    facet_cap_df.loc[~maskfacet_cap, 'Accuracy'] = 'ERROR Facet Hard Drive'

    df.update(facet_cap_df['Accuracy'])

################################################################ facet_os ################################################################

    facet_os_df = df.loc[df['ContainerName'].str.contains('facet_os')]
    maskfacet_os = (facet_os_df['PhwebDescription'].str.contains('FreeDOS') & \
                        (facet_os_df['ContainerValue'].str.contains('FreeDOS', regex=False, case=False))) | \
                    (facet_os_df['PhwebDescription'].str.contains('Chrome') & \
                        (facet_os_df['ContainerValue'].str.contains('ChromeOS', regex=False, case=False))) | \
                    (facet_os_df['PhwebDescription'].str.contains('NWZH6') & \
                        (facet_os_df['ContainerValue'].str.contains('Windows 11 Home', regex=False, case=False)))    
    
    facet_os_df.loc[maskfacet_os, 'Accuracy'] = 'SCS Facet Operating System OK'
    facet_os_df.loc[~maskfacet_os, 'Accuracy'] = 'ERROR Facet Operating System'

    df.update(facet_os_df['Accuracy'])

################################################################ facet_graphics ################################################################

    facet_graphics_df = df.loc[df['ContainerName'].str.contains('facet_graphics') & df['ComponentGroup'].str.contains('Graphic card')]
    maskfacet_graphics = (facet_graphics_df['PhwebDescription'].str.contains('RTX') & \
                            (facet_graphics_df['ContainerValue'].str.contains('NVIDIA GeForce', regex=False, case=False))) | \
                        (facet_graphics_df['PhwebDescription'].str.contains('NVIDIA') & \
                            (facet_graphics_df['ContainerValue'].str.contains('NVIDIA GeForce', regex=False, case=False))) | \
                        (facet_graphics_df['PhwebDescription'].str.contains('GeF') & \
                            (facet_graphics_df['ContainerValue'].str.contains('NVIDIA GeForce', regex=False, case=False))) | \
                        (facet_graphics_df['PhwebDescription'].str.contains('AMD') & \
                            (facet_graphics_df['ContainerValue'].str.contains('AMD Radeon', regex=False, case=False))) | \
                        (facet_graphics_df['PhwebDescription'].str.contains('GTX') & \
                            (facet_graphics_df['ContainerValue'].str.contains('NVIDIA GeForce', regex=False, case=False)))


    facet_graphics_df.loc[maskfacet_graphics, 'Accuracy'] = 'SCS Facet Graphics OK'
    facet_graphics_df.loc[~maskfacet_graphics, 'Accuracy'] = 'ERROR Facet Graphics'

    df.update(facet_graphics_df['Accuracy'])


################################################################ facet_processortype ################################################################

    facet_processortype_df = df.loc[df['ContainerName'].str.contains('facet_processortype') & df['ComponentGroup'].str.contains('Processor')]
    maskfacet_processortype = (facet_processortype_df['PhwebDescription'].str.contains('i7') & \
                            (facet_processortype_df['ContainerValue'].str.contains('Intel Core i7', regex=False, case=False))) | \
                        (facet_processortype_df['PhwebDescription'].str.contains('i5') & \
                            (facet_processortype_df['ContainerValue'].str.contains('Intel Core i5', regex=False, case=False))) | \
                        (facet_processortype_df['PhwebDescription'].str.contains('R7') & \
                            (facet_processortype_df['ContainerValue'].str.contains('AMD Ryzen 7', regex=False, case=False))) | \
                        (facet_processortype_df['PhwebDescription'].str.contains('R5') & \
                            (facet_processortype_df['ContainerValue'].str.contains('AMD Ryzen 5', regex=False, case=False))) | \
                        (facet_processortype_df['PhwebDescription'].str.contains('Ryzen5') & \
                            (facet_processortype_df['ContainerValue'].str.contains('AMD Ryzen 5', regex=False, case=False))) | \
                        (facet_processortype_df['PhwebDescription'].str.contains('Ryzen7 ') & \
                            (facet_processortype_df['ContainerValue'].str.contains('AMD Ryzen 7', regex=False, case=False)))

    facet_processortype_df.loc[maskfacet_processortype, 'Accuracy'] = 'SCS Facet Processor OK'
    facet_processortype_df.loc[~maskfacet_processortype, 'Accuracy'] = 'ERROR Facet Processor'

    df.update(facet_processortype_df['Accuracy'])


################################################################ facet_scrnsizeus ################################################################

    facet_scrnsizeus_df = df.loc[df['ContainerName'].str.contains('facet_scrnsizeus') & df['ComponentGroup'].str.contains('Display')]
    maskfacet_scrnsizeus = (facet_scrnsizeus_df['PhwebDescription'].str.contains('15.6') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('15.6', regex=False, case=False))) | \
                        (facet_scrnsizeus_df['PhwebDescription'].str.contains('13.3') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('13.3', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('23.8') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('23.8', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('14') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('14', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('17.3') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('17.3', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('31.5') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('31.5', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('27') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('27', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('11.6') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('11.6', regex=False, case=False))) | \
                       (facet_scrnsizeus_df['PhwebDescription'].str.contains('34.0') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('34', regex=False, case=False))) | \
                        (facet_scrnsizeus_df['PhwebDescription'].str.contains('16.1') & \
                            (facet_scrnsizeus_df['ContainerValue'].str.contains('16.1', regex=False, case=False)))

    facet_scrnsizeus_df.loc[maskfacet_scrnsizeus, 'Accuracy'] = 'SCS Facet Screen Size OK'
    facet_scrnsizeus_df.loc[~maskfacet_scrnsizeus, 'Accuracy'] = 'ERROR Facet Screen Size'

    df.update(facet_scrnsizeus_df['Accuracy'])

    df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)

    df.to_excel('SCS_QA.xlsx', index=False)

    formateData()

    return 
    