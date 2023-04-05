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
    df = df[df['ContainerValue'] != '[BLANK]']

    cols_to_drop = ['Option', 'Status','SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue' ,'ExtendedDescription','ComponentCompletionDate','ComponentReadiness','SKUReadiness']
    df = df.drop(cols_to_drop, axis=1)
    df[['Accuracy', 'Correct Value', 'Additional Information']] = ''


    ################################################################ Memory

    memstdes_01 = df.loc[df['ContainerName'].str.contains('memstdes_01')]

    maskMemory = (memstdes_01['PhwebDescription'].str.contains(' RAM HX 16GB (2x8GB) DDR4 3733 XMP HSnk') & \
                        (memstdes_01['ContainerValue'].str.contains('HyperX 16 GB DDR4-3200 MHz XMP Heatsink RAM (2 x 8 GB)', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains(' RAM HX 16GB (2x8GB) DDR4 3200 XMP RGBHS') & \
                        (memstdes_01['ContainerValue'].str.contains('HyperX 16 GB DDR4-3200 MHz XMP RGB Heatsink RAM (2 x 8 GB)', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains('RAM HX 16GB (2x8GB) DDR4 3467 XMP RGBHS') & \
                        (memstdes_01['ContainerValue'].str.contains('HyperX 16 GB DDR4-3467 MHz XMP RGB Heatsink RAM (2 x 8 GB)', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains('RAM HX 16GB (2x8GB) DDR4 3733 XMP RGBHS') & \
                        (memstdes_01['ContainerValue'].str.contains('HyperX 16 GB DDR4-3733 MHz XMP RGB Heatsink RAM (2 x 8 GB)', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains('RAM 16GB (2x8GB)  DDR4 3200') & \
                        (memstdes_01['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 4800') & \
                        (memstdes_01['ContainerValue'].str.contains('16 GB DDR5-4800 MHz RAM (2 x 8 GB)', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains('SSD 2TB 2280 PCIe-4x4 NVMe TLC') & \
                        (memstdes_01['ContainerValue'].str.contains('2 TB PCIe® Gen4 NVMe™ TLC M.2 SSD', case=False))) | \
                    (memstdes_01['PhwebDescription'].str.contains('SSD 2TB PCIe NVMe TLC') & \
                        (memstdes_01['ContainerValue'].str.contains('2 TB PCIe® NVMe™ TLC M.2 SSD', case=False)))

    memstdes_01.loc[maskMemory, 'Accuracy'] = 'SCS Memory OK'
    memstdes_01.loc[~maskMemory, 'Accuracy'] = 'ERROR memory'

    df.update(memstdes_01['Accuracy'])


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


    stylus_df = df.loc[df['ContainerName'].str.contains('stylus')]
    maskStylus = (stylus_df['PhwebDescription'].str.contains('Pen') & \
                    (stylus_df['ContainerValue'].str.contains('HP Rechargeable MPP2.0 Tilt Pen', case=False)))
                    
    stylus_df.loc[maskStylus, 'Accuracy'] = 'SCS Stylus OK'
    stylus_df.loc[~maskStylus, 'Accuracy'] = 'ERROR'

    df.update(stylus_df['Accuracy'])

    ################################################################ Battery Type

    batterytype_df = df.loc[df['ContainerName'].str.contains('batterytype')]
    maskBatterytype = (batterytype_df['PhwebDescription'].str.contains('BATT 3C 41 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 41 Wh Li-ion', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 3C 43 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 43 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 3C 51 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 51 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 3C 52.5 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 52.5 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 4 cell C XL 66Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('4-cell, 66 Wh Li-ion polymer', case=False)))
                                                
    batterytype_df.loc[maskBatterytype, 'Accuracy'] = 'SCS Battery Type OK'
    batterytype_df.loc[~maskBatterytype, 'Accuracy'] = 'ERROR'

    df.update(batterytype_df['Accuracy'])

    ################################################################ Chipset

    chipset_df = df.loc[df['ContainerName'].str.contains('chipset')]
    maskChipset = (chipset_df['PhwebDescription'].str.contains('H470') & \
                        (chipset_df['ContainerValue'].str.contains('Intel® H470', case=False))) 

    chipset_df.loc[maskChipset, 'Accuracy'] = 'SCS Chipset OK'
    chipset_df.loc[~maskChipset, 'Accuracy'] = 'ERROR'

    df.update(chipset_df['Accuracy'])

    ################################################################ Processor Name

    processorname_df = df.loc[df['ContainerName'].str.contains('processorname')]
    maskProcessorName = (processorname_df['PhwebDescription'].str.contains('3020e') & \
                            (processorname_df['ContainerValue'].str.contains('AMD 3020e (1.2 GHz base clock, up to 2.6 GHz max boost clock, 4 MB L3 cache, 2 cores, 2 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('3050U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ 3050U (2.3 GHz base clock, up to 3.2 GHz max boost clock, 4 MB L3 cache, 2 cores)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('3150U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ Gold 3150U (2.4 GHz base clock, up to 3.3 GHz max boost clock, 4 MB L3 cache, 2 cores, 4 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('3250U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 3250U (2.6 GHz base clock, up to 3.5 GHz max boost clock, 4 MB L3 cache, 2 cores, 4 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('4300G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 4300G (3.8 GHz base clock, up to 4.0 GHz max boost clock, 4 MB L3 cache, 4 cores)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5300U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 5300U (up to 3.8 GHz max boost clock, 4 MB L3 cache, 4 cores, 8 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5425U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 5425U (2.7 GHz base clock, up to 4.1 GHz max boost clock, 8 MB L3 cache, 4 cores, 8 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('4600G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 4600G (3.7 GHz base clock, up to 4.2 GHz max boost clock, 8 MB L3 cache, 6 cores)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5500U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5500U (up to 4.0 GHz max boost clock, 8 MB L3 cache, 6 cores, 12 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5600G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5600G (up to 4.4 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5625U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5625U (up to 4.3 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5700G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5700G (up to 4.6 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5700U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5700U (up to 4.3 GHz max boost clock, 8 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5800H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5800H (up to 4.4 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5800U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5800U (up to 4.4 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5800X') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5800X (up to 4.7 GHz max boost clock, 32 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5825U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5825U (up to 4.5 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('6800H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 6800H (up to 4.7 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)', case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5900X') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 9 5900X (up to 4.8 GHz max boost clock, 64 MB L3 cache, 12 cores, 24 threads)', case=False)))
                                    
    processorname_df.loc[maskProcessorName, 'Accuracy'] = 'SCS Processor Name OK'
    processorname_df.loc[~maskProcessorName, 'Accuracy'] = 'ERROR'

    df.update(processorname_df['Accuracy'])


    ################################################################ Display

    display_df = df.loc[df['ContainerName'].str.contains('display')]
    maskDisplay =   (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED UWVA250144HzNWBZflat') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), 144 Hz, 9 ms response time, IPS, micro-edge, anti-glare, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LEDUWVA300uslim144HzNWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), 144 Hz, 7 ms response time, IPS, micro-edge, anti-glare, 300 nits, 72% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 QHDAGLwBluLt300UWVA120HzNWBZbnt') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, QHD (2560 x 1440), multitouch-enabled, 120 Hz, IPS, edge-to-edge glass, micro-edge, Low Blue Light, 300 nits, 100% sRGB', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 HDV LED SVA 220 slim NWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, HD (1366 x 768), micro-edge, BrightView, 220 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED UWVA 250') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), IPS, micro-edge, anti-glare, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED UWVA 250ent NWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), multitouch-enabled, IPS, edge-to-edge glass, micro-edge, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED UWVA 250ent TSNWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), multitouch-enabled, IPS, edge-to-edge glass, micro-edge, Corning® Gorilla® Glass NBT™, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LwBluLt 300 UWVA NWBZflt') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), IPS, micro-edge, anti-glare, Low Blue Light, 300 nits, 100% sRGB', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHDV LED UWVA 250 slim NWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), IPS, micro-edge, BrightView, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED SVA 220 slim NWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), micro-edge, anti-glare, 220 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED SVA 250 NWBZ uslim') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), micro-edge, anti-glare, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHD AG LED UWVA 400ent LPNWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), multitouch-enabled, IPS, edge-to-edge glass, micro-edge, 400 nits, 100% sRGB', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('OLED 15.6 FHDV OLED+LBL 400UWVANWBZbnt') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), OLED, multitouch-enabled, UWVA, edge-to-edge glass, micro-edge, Low Blue Light, SDR 400 nits, HDR 500 nits, 100% DCI-P3', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 FHDV LED UWVA 250 slimTOPNWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, FHD (1920 x 1080), touch, IPS, micro-edge, BrightView, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 HD AG LED SVA 220 slim NWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, HD (1366 x 768), micro-edge, anti-glare, 220 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 HD AG LED SVA 250 NWBZ uslim') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, HD (1366 x 768), micro-edge, anti-glare, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 HDV LED SVA 220 slim TOP NWBZ') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, HD (1366 x 768), touch, micro-edge, BrightView, 220 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 HDV LED SVA 250 NWBZ uslim') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, HD (1366 x 768), micro-edge, BrightView, 250 nits, 45% NTSC', case=False))) | \
                    (display_df['PhwebDescription'].str.contains('LCD 15.6 HDV LED SVA 250 TOP NWBZ flat') & \
                        (display_df['ContainerValue'].str.contains('15.6" diagonal, HD (1366 x 768), touch, micro-edge, BrightView, 250 nits, 45% NTSC', case=False)))

    display_df.loc[maskDisplay, 'Accuracy'] = 'SCS Display OK'
    display_df.loc[~maskDisplay, 'Accuracy'] = 'ERROR'

    df.update(display_df['Accuracy'])

    ################################################################ Hard Drive

    hd_01des = df.loc[df['ContainerName'].str.contains('hd_01des')]
    maskHardDrive = (hd_01des['PhwebDescription'].str.contains('SSD 512GB PCIe NVMe') & \
                        (hd_01des['ContainerValue'].str.contains('512 GB PCIe® Gen4 NVMe™ TLC M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 512G 2280 PCIe NVMe Value') & \
                        (hd_01des['ContainerValue'].str.contains('512 GB PCIe® NVMe™ M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 512GB PCIe-4x4 NVMe TLC') & \
                        (hd_01des['ContainerValue'].str.contains('512 GB PCIe® NVMe™ TLC M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 256GB PCIe NVMe Value') & \
                        (hd_01des['ContainerValue'].str.contains('256 GB PCIe® NVMe™ M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 256GB PCIe NVMe TLC') & \
                        (hd_01des['ContainerValue'].str.contains('256 GB PCIe® NVMe™ TLC M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 1TB PCIe NVMe Value') & \
                        (hd_01des['ContainerValue'].str.contains('1 TB PCIe® NVMe™ M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 1TB PCIe NVMe TLC') & \
                        (hd_01des['ContainerValue'].str.contains('1 TB PCIe® Gen4 NVMe™ TLC M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 2TB 2280 PCIe-4x4 NVMe TLC') & \
                        (hd_01des['ContainerValue'].str.contains('2 TB PCIe® Gen4 NVMe™ TLC M.2 SSD', case=False))) | \
                    (hd_01des['PhwebDescription'].str.contains('SSD 2TB PCIe NVMe TLC') & \
                        (hd_01des['ContainerValue'].str.contains('2 TB PCIe® NVMe™ TLC M.2 SSD', case=False)))

    hd_01des.loc[maskHardDrive, 'Accuracy'] = 'SCS Hard Drive OK'
    hd_01des.loc[~maskHardDrive, 'Accuracy'] = 'ERROR'

    df.update(display_df['Accuracy'])

    ################################################################ save the excel

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
