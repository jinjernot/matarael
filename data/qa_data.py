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

########################################################################################################################################
################################################################ TechSpecs #############################################################
########################################################################################################################################

################################################################ Memory ################################################################

    memstdes_01_df = df.loc[(df['ContainerName'].str.contains('memstdes_01')) & \
                        (df['ComponentGroup'].str.contains('Memory'))]

    maskMemory = (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 2400 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2400 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM HX 16GB (2x8GB) DDR4 3200 XMP RGBHS', regex=False, case=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('HyperX 16 GB DDR4-3200 MHz XMP RGB Heatsink RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM HX 16GB (2x8GB) DDR4 3467 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('HyperX 16 GB DDR4-3467 MHz XMP RGB Heatsink RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM HX 16GB (2x8GB) DDR4 3733 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('HyperX 16 GB DDR4-3733 MHz XMP RGB Heatsink RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB)  DDR4 3200', regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 4800', regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR5-4800 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('SSD 2TB 2280 PCIe-4x4 NVMe TLC', regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('2 TB PCIe® Gen4 NVMe™ TLC M.2 SSD' ,regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('SSD 2TB PCIe NVMe TLC', regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('2 TB PCIe® NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR4 3200 NECC', regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR4-3200 MHz RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1230U 16GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-1250U 16GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1230U 8GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (2 x 4 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR5 4800',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR5-4800 MHz RAM (2 x 16 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB)  DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR4-3200 MHz RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-1250U 8GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R3 7320U 8GB 17',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB (1x4GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-3200 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ryzen5 5625U 16GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB (1x4GB) DDR4 2400',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-2400 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R3 7320U 8GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7520U 8GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 12GB (1x8GB+1x4GB)DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('12 GB DDR4-3200 MHz RAM (1 x 4 GB, 1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB (1x4GB) DDR4 3200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-3200 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 2400',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2400 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR5 5200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR5-5200 MHz RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 2666',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-2666 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7520U 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 12GB (1x8GB+1x4GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('12 GB DDR4-3200 MHz RAM (1 x 4 GB, 1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R3 7320U 4GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS OPP 24-cr0 23.8 8GB R5-7520U',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB LPDDR5-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7530U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 5200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR5-5200 MHz RAM (2 x 8 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1335U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-6400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R3 7320U 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ath7220U 8GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 12GB (1x8GB+1x4GB)  DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('12 GB DDR4-3200 MHz RAM (1 x 4 GB, 1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-1355U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR5 5600',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR5-5600 MHz RAM (2 x 16 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM KFURY 16GB(2x8GB)DDR5 4400 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('Kingston FURY 16 GB DDR5-5200 MHz XMP RGB Heatsink RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 5600',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR5-5600 MHz RAM (2 x 8 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ath7120U 4GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB(1x8GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R7 7730U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 5200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR5-5200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM KFURY 32GB(2x16GB)DDR54400 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('Kingston FURY 32 GB DDR5-5200 MHz XMP RGB Heatsink RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1340P 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ath7120U 8GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 2666',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2666 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 3200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 12GB (1x8GB+1x4GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('12 GB DDR4-3200 MHz RAM (1 x 8 GB, 1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 3200 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX30504GB i7-1355U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1335U 8GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi5xxxx 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-1355U 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (8x2GB) DDR4 3200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB(1x8GB) DDR4 2933 UDIMM NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2933 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 3200 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7520U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-12700H 16GB fOLED 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 12GB (1x8GB+1x4GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('12 GB DDR4-3200 MHz RAM (1 x 8 GB, 1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 2666',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2666 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS DSC 2GB PH i5-xxxx 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi5xxxxU 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX30504GB i5-1335U 16GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB)DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 5200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR5-5200 MHz RAM (2 x 8 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB(1x16GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (1 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (1x16GB) DDR4 3200 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (1 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA CelN4500 4GB 128GeMMC 14a-ca1',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB LPDDR4x-2933 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7535U 16GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB (1x4GB) DDR4 2666',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-2666 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB (1x4GB) DDR4 2933',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-2933 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ath7120U 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS DSCArc4GB PHi7RM 16GB fOLED 16',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R7 7735U 16GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi7xxxxU 32GB fOLED 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7535U 8GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-6400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM HX 16GB (2x8GB) DDR4 3200 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('HyperX 16 GB DDR4-3200 MHz XMP RGB Heatsink RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PH i7-xxxx 32GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 3200 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA CelN4500 8GB 128GeMMC 15a-na0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4x-2933 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS OPP 27-cr0 27 16GB R5-7520U',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 3200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains(' 32GB (2x16GB)  DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR4-3200 MHz RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PH i7-xxxx 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi7xxxxU 16GB fOLED 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi712xxx 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi7xxxxU 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM KFURY 16GB (2x8GB)DDR5 4400 XMP HSnk',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('Kingston FURY 16 GB DDR5-5200 MHz XMP Heatsink RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-13700H 16GB fOLED 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7520U 8GB 17',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi7xxxxU 32GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS DSCRTX20504GB i7-1355U16GBfOLED14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM KFURY 32GB(2x16GB)DDR55200 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('Kingston FURY 32 GB DDR5-5200 MHz XMP RGB Heatsink RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (1 x 8 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi312xxx 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ryzen7 5825U 16GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR5 4800',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR5-4800 MHz RAM (1 x 8 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS DSCMX5502GB i5-1335U 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA CelN41204GB64GeMMCnSDC14a-ca0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB LPDDR4-2400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1235U 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-13500H 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i7-1255U 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 2933',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2933 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM KFURY 64GB(4x16GB)DDR54400 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('Kingston FURY 64 GB DDR5-5200 MHz XMP RGB Heatsink RAM (4 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi512xxx 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7520U 16GB 17',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (1x16GB) DDR4 3200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (1 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7530U 8GB 15',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 2933',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2933 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 2933',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-2933 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA R5 7520U 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB LPDDR5-5500 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA Ryzen5 5625U 8GB 13',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM KFURY 64GB(4x16GB)DDR55200 XMP RGBHS',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('Kingston FURY 64 GB DDR5-5200 MHz XMP RGB Heatsink RAM (4 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA PHi512xxx 16GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (1x16GB) DDR4 3200 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 SDRAM (1 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 12GB (1x8GB+1x4GB) DDR4 2933',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('12 GB DDR4-2933 MHz RAM (1 x 4 GB, 1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR5 4800',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR5-4800 MHz RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR5 4000',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR5-4000 MHz RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR5 4000',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR5-4000 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMACelN41208GB128GeMMCnSDC14a-na0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4-2400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMAPentSilN60008GB128GeMMC15a-na0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4x-2933 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR5 5200',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR5-5200 MHz RAM (2 x 16 GB);', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM HX 32GB (2x16GB) DDR4 3200 XMP HSnk',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('HyperX 32 GB DDR4-3200 MHz XMP Heatsink RAM (2 x 16 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 16GB (2x8GB) DDR4 3200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDSUPentSN50308GB64GeMMCfBLnSDC14aca0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4-2400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDSUMAPSilN50308GB128GeMMCnSDC14a-na0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4-2400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA CelN41204GB64GeMMCnSDC14a-na0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB LPDDR4-2400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (2x4GB) DDR4 2400 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2400 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-13500H 16GB fOLED 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA MT8195GV 8GB 13b-ca0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR4x-4266 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 3200 CR',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (2 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i5-1235U 8GB 14',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-3200 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i3-N305 8GB 256GUFS 15a-nb0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-6400 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB (1x4GB) DDR4 2666 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-2666 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('BU IDS UMA i3-N305 8GB 128GUFS 15a-nb0',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB LPDDR5-4800 MHz RAM (onboard)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains(' 16GB (2x8GB)  DDR4 3200 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('16 GB DDR4-3200 MHz RAM (2 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 4GB(1x4GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('4 GB DDR4-3200 MHz RAM (1 x 4 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 8GB (1x8GB) DDR4 2666 NECC',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('8 GB DDR4-2666 MHz RAM (1 x 8 GB)', regex=False, case=False))) | \
                    (memstdes_01_df['PhwebDescription'].str.contains('RAM 32GB (2x16GB) DDR4 3200 SODIMM',regex=False) & \
                        (memstdes_01_df['ContainerValue'].str.contains('32 GB DDR4-3200 MHz RAM (2 x 16 GB)', regex=False, case=False)))

    memstdes_01_df.loc[maskMemory, 'Accuracy'] = 'SCS Memory OK'
    memstdes_01_df.loc[~maskMemory, 'Accuracy'] = 'ERROR Memory'

    df.update(memstdes_01_df['Accuracy'])

################################################################ Colors ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('productcolour')]
    processData('json/productcolour.json', 'productcolour', container_df, df)

  
######################################################################## FPR ################################################################

    fingerprread_df = df.loc[df['ContainerName'].str.contains('fingerprread')]
    maskFPR = (fingerprread_df['PhwebDescription'].str.contains('FPR') & \
                    (fingerprread_df['ContainerValue'].str.contains('Fingerprint reader', case=False)))

    fingerprread_df.loc[maskFPR, 'Accuracy'] = 'SCS FPR OK'
    fingerprread_df.loc[~maskFPR, 'Accuracy'] = 'ERROR FPR'

    df.update(fingerprread_df['Accuracy'])

################################################################ Stylus ################################################################

    stylus_df = df.loc[df['ContainerName'].str.contains('stylus')]
    maskStylus = (stylus_df['PhwebDescription'].str.contains('Pen') & \
                    (stylus_df['ContainerValue'].str.contains('HP Rechargeable MPP2.0 Tilt Pen', case=False)))
                    
    stylus_df.loc[maskStylus, 'Accuracy'] = 'SCS Stylus OK'
    stylus_df.loc[~maskStylus, 'Accuracy'] = 'ERROR Stylus'

    df.update(stylus_df['Accuracy'])

################################################################ Battery Type ################################################################

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
                        (batterytype_df['ContainerValue'].str.contains('4-cell, 66 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 3 cell C Long Life 43Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 43 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 4 cell C Long Life 70Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('4-cell, 70 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 4 cell C Long Life 55Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('4-cell, 55 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 4C 66 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('4-cell, 66 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 3 cell C Long Life 41Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 41 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 2C 47 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('2-cell, 47 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 4C 55 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('4-cell, 55 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 6 cell C Long Life 83Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('6-cell, 83 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 6 cell C Long Life 97Whr FstCrg') & \
                        (batterytype_df['ContainerValue'].str.contains('6-cell, 97 Wh Li-ion polymer', case=False))) | \
                    (batterytype_df['PhwebDescription'].str.contains('BATT 3C 58 WHr Long Life') & \
                        (batterytype_df['ContainerValue'].str.contains('3-cell, 58 Wh Li-ion polymer', case=False)))
                                   
    batterytype_df.loc[maskBatterytype, 'Accuracy'] = 'SCS Battery Type OK'
    batterytype_df.loc[~maskBatterytype, 'Accuracy'] = 'ERROR Battery Type'

    df.update(batterytype_df['Accuracy'])

################################################################ Chipset ################################################################

    chipset_df = df.loc[df['ContainerName'].str.contains('chipset')]
    maskChipset = (chipset_df['PhwebDescription'].str.contains('H470') & \
                        (chipset_df['ContainerValue'].str.contains('Intel® H470', case=False))) 

    chipset_df.loc[maskChipset, 'Accuracy'] = 'SCS Chipset OK'
    chipset_df.loc[~maskChipset, 'Accuracy'] = 'ERROR Chipset'

    df.update(chipset_df['Accuracy'])

################################################################ Processor Name ################################################################

    processorname_df = df.loc[(df['ContainerName'] == 'processorname') & df['ComponentGroup'].str.contains('Processor')]
    maskProcessorName = (processorname_df['PhwebDescription'].str.contains('3020e') & \
                            (processorname_df['ContainerValue'].str.contains('AMD 3020e (1.2 GHz base clock, up to 2.6 GHz max boost clock, 4 MB L3 cache, 2 cores, 2 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('3050U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ 3050U (2.3 GHz base clock, up to 3.2 GHz max boost clock, 4 MB L3 cache, 2 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('3150U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ Gold 3150U (2.4 GHz base clock, up to 3.3 GHz max boost clock, 4 MB L3 cache, 2 cores, 4 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('3250U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 3250U (2.6 GHz base clock, up to 3.5 GHz max boost clock, 4 MB L3 cache, 2 cores, 4 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('4300G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 4300G (3.8 GHz base clock, up to 4.0 GHz max boost clock, 4 MB L3 cache, 4 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5300U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 5300U (up to 3.8 GHz max boost clock, 4 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5425U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 5425U (2.7 GHz base clock, up to 4.1 GHz max boost clock, 8 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('4600G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 4600G (3.7 GHz base clock, up to 4.2 GHz max boost clock, 8 MB L3 cache, 6 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5500U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5500U (up to 4.0 GHz max boost clock, 8 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5600G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5600G (up to 4.4 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5625U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5625U (up to 4.3 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5700G') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5700G (up to 4.6 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5700U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5700U (up to 4.3 GHz max boost clock, 8 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5800H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5800H (up to 4.4 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5800U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5800U (up to 4.4 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5800X') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5800X (up to 4.7 GHz max boost clock, 32 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5825U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5825U (up to 4.5 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('6800H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 6800H (up to 4.7 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-11300H') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-11300H (up to 4.4 GHz with Intel® Turbo Boost Technology, 8 MB L3 cache, 4 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i9-12900K') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i9-12900K (up to 5.2 GHz with Intel® Turbo Boost Technology, 30 MB L3 cache, 16 cores, 24 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('Ath3050U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ Silver 3050U (2.3 GHz base clock, up to 3.2 GHz max boost clock, 4 MB L3 cache, 2 cores, 2 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5600H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5600H (up to 4.2 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5600U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5600U (up to 4.2 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('6600H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 6600H (up to 4.5 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('96900HX') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 9 6900HX (up to 4.9 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5900H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 9 5900HX (up to 4.6 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('J4025') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Celeron® J4025 (2.0 GHz base frequency, up to 2.9 GHz, 2 MB L2 cache, 2 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('CelN4120') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Celeron® N4120 (up to 2.6 GHz burst frequency, 4 MB L2 cache, 4 cores, 4 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('CelN4500') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Celeron® N4500 (up to 2.8 GHz burst frequency, 4 MB L3 cache, 2 cores, 2 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-1115G4') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1115G4 (up to 4.1 GHz with Intel® Turbo Boost Technology, 6 MB L3 cache, 2 cores, 4 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-1125G4') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1125G4 (up to 3.7 GHz with Intel® Turbo Boost Technology, 8 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-1215U') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1215U (up to 4.4 GHz with Intel® Turbo Boost Technology, 10 MB L3 cache, 6 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-12xxx') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1215U (up to 4.4 GHz with Intel® Turbo Boost Technology, 10 MB L3 cache, 6 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-1155G7') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-1155G7 (up to 4.5 GHz with Intel® Turbo Boost Technology, 8 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-1135G7') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-1135G7 (up to 4.2 GHz with Intel® Turbo Boost Technology, 8 MB L3 cache, 4 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-11400H') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-11400H (up to 4.5 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-1235U') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-1235U (up to 4.4 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-1230U') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-1230U (up to 4.4 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-12400') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-12400 (up to 4.4 GHz with Intel® Turbo Boost Technology, 18 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-1240P') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-1240P (up to 4.4 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 12 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-12400T') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-12400T (up to 4.2 GHz with Intel® Turbo Boost Technology, 18 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-12400F') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-12400F (up to 4.4 GHz with Intel® Turbo Boost Technology, 18 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-12500H') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-12500H (up to 4.5 GHz with Intel® Turbo Boost Technology, 18 MB L3 cache, 12 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-11370H') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-11370H (up to 4.8 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 4 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-1165G7') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-1165G7 (up to 4.7 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-11700') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-11700 (2.5 GHz base frequency, up to 4.9 GHz with Intel® Turbo Boost Technology, 16 MB L3 cache, 8 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-1255U') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-1255U (up to 4.7 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('Ath7220U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ Gold 7220U (up to 3.7 GHz max boost clock, 4 MB L3 cache, 2 cores, 4 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('Athlon-3050U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ Silver 3050U (2.3 GHz base clock, up to 3.2 GHz max boost clock, 4 MB L3 cache, 2 cores, 2 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('Ath7120U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Athlon™ Silver 7120U (up to 3.5 GHz max boost clock, 2 MB L3 cache, 2 cores, 2 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('Ryzen3-3250U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 3250U (2.6 GHz base clock, up to 3.5 GHz max boost clock, 4 MB L3 cache, 2 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7320U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 3 7320U (up to 4.1 GHz max boost clock, 4 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7520U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 7520U (up to 4.3 GHz max boost clock, 4 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7530U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 7530U (up to 4.5 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7535U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 7535U (up to 4.55 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7640HS') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 7640HS (up to 5.0 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7730U') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 7730U (up to 4.5 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7840HS') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 7840HS (up to 5.1 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7840H') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 7840H (up to 5.1 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('7940HS') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 9 7940HS (up to 5.2 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('J4025') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Celeron® J4025 (2.0 GHz base frequency, up to 2.9 GHz, 4 MB L2 cache, 2 cores, 2 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-1125G4') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™  i3-1125G4 (up to 3.7 GHz with Intel® Turbo Boost Technology, 8 MB cache, 4 cores)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-12100') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-12100 (up to 4.3 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-13100T') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-13100T (up to 4.2 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-11xx') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1215U (up to 4.4 GHz with Intel® Turbo Boost Technology, 10 MB L3 cache, 6 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i3-1315U') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1315U (up to 4.5 GHz with Intel® Turbo Boost Technology, 10 MB L3 cache, 6 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-11xx') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-1235U (up to 4.4 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-1195G7') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-1195G7 (up to 5.0 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 4 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-12700K') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-12700K (up to 5.0 GHz with Intel® Turbo Boost Technology, 25 MB L3 cache, 12 cores, 20 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-12700H') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-12700H (up to 4.7 GHz with Intel® Turbo Boost Technology, 24 MB L3 cache, 14 cores, 20 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i5-12450H') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-12450H (up to 4.4 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 8 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-11xx') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-1255U (up to 4.7 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-xxxx') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-1255U (up to 4.7 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('i7-12xxx') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-1255U (up to 4.7 GHz with Intel® Turbo Boost Technology, 12 MB L3 cache, 10 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('BU IDS UMA PH R5') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 5 5625U (up to 4.3 GHz max boost clock, 16 MB L3 cache, 6 cores, 12 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('BU IDS DSC GTX 1650 4GB PH i5-RM 15') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i5-12500H (up to 4.5 GHz with Intel® Turbo Boost Technology, 18 MB L3 cache, 12 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('5900X') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 9 5900X (up to 4.8 GHz max boost clock, 64 MB L3 cache, 12 cores, 24 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('BU IDS UMA PH R7 8C ') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 5825U (up to 4.5 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('BU IDS DSC RTX 3050Ti 4GB PH R7 8C 16') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 7 6800H (up to 4.7 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('Ryzen9 6900X ') & \
                            (processorname_df['ContainerValue'].str.contains('AMD Ryzen™ 9 6900HX (up to 4.9 GHz max boost clock, 16 MB L3 cache, 8 cores, 16 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('BU IDS UMA PH i3-xxxx nSDC 15') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i3-1215U (up to 4.4 GHz with Intel® Turbo Boost Technology, 10 MB L3 cache, 6 cores, 8 threads)',regex=False, case=False))) | \
                        (processorname_df['PhwebDescription'].str.contains('CPU INTL i7-12700F 12C 2.10 65W') & \
                            (processorname_df['ContainerValue'].str.contains('Intel® Core™ i7-12700F (up to 4.9 GHz with Intel® Turbo Boost Technology, 25 MB L3 cache, 12 cores, 20 threads)',regex=False, case=False)))
                                    
    processorname_df.loc[maskProcessorName, 'Accuracy'] = 'SCS Processor Name OK'
    processorname_df.loc[~maskProcessorName, 'Accuracy'] = 'ERROR Processor Name'

    df.update(processorname_df['Accuracy'])

################################################################ Display ################################################################

    container_df = df.loc[df['ContainerName'].str.strip() == 'display']
    processData('json/display.json', 'display', container_df, df)

################################################################ Hard Drive ################################################################

    hd_01des_df = df.loc[df['ContainerName'].str.contains('hd_01des') & df['ComponentGroup'].str.contains('Hard Drive')]
    maskHardDrive = (hd_01des_df['PhwebDescription'].str.contains('SSD 512GB PCIe NVMe') & \
                        (hd_01des_df['ContainerValue'].str.contains('512 GB PCIe® Gen4 NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 512G 2280 PCIe NVMe Value') & \
                        (hd_01des_df['ContainerValue'].str.contains('512 GB PCIe® NVMe™ M.2 SSD', case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 512GB PCIe-4x4 NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('512 GB PCIe® NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 256GB PCIe NVMe Value') & \
                        (hd_01des_df['ContainerValue'].str.contains('256 GB PCIe® NVMe™ M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 256GB PCIe NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('256 GB PCIe® NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 1TB PCIe NVMe Value') & \
                        (hd_01des_df['ContainerValue'].str.contains('1 TB PCIe® NVMe™ M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 1TB PCIe NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('1 TB PCIe® Gen4 NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 2TB 2280 PCIe-4x4 NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('2 TB PCIe® Gen4 NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 2TB PCIe NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('2 TB PCIe® NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 512GB PCIe-4x4 NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('512 GB PCIe® Gen4 NVMe™ TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('HDD 1TB 5400RPM SATA') & \
                        (hd_01des_df['ContainerValue'].str.contains('1 TB 5400 rpm SATA HDD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD WD Black 1T 2280 PCIe-4x4 NVMe TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('1 TB WD Black PCIe® Gen4 NVMe™ TLC M.2  SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD WD Black 2TB 2280 PCIe-4x4 TLC') & \
                        (hd_01des_df['ContainerValue'].str.contains('2 TB WD Black PCIe® Gen4 TLC M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD WD 512G 2280 PCIe NVMe Value') & \
                     hd_01des_df['ContainerValue'].str.contains('512 GB WD Black PCIe® NVMe™ TLC M.2  SSD', regex=False, case=False) | \
                    (hd_01des_df['ContainerValue'].str.contains('512 GB PCIe® NVMe™ M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD 1T 2280 PCIe NVMe Value') & \
                        (hd_01des_df['ContainerValue'].str.contains('1 TB PCIe® NVMe™ M.2 SSD', regex=False, case=False))) | \
                    (hd_01des_df['PhwebDescription'].str.contains('SSD WD 1T 2280 PCIe NVMe Value') & \
                        (hd_01des_df['ContainerValue'].str.contains('1 TB PCIe® NVMe™ M.2 SSD', regex=False, case=False)))

    hd_01des_df.loc[maskHardDrive, 'Accuracy'] = 'SCS Hard Drive OK'
    hd_01des_df.loc[~maskHardDrive, 'Accuracy'] = 'ERROR Hard Drive'

    df.update(hd_01des_df['Accuracy'])

################################################################ Operating System ################################################################

    osinstalled_df = df.loc[df['ContainerName'].str.strip() == 'osinstalled']
    maskOperatingSystem = (osinstalled_df['PhwebDescription'].str.contains('Chrome64') & \
                        (osinstalled_df['ContainerValue'].str.contains('ChromeOS', case=False))) | \
                    (osinstalled_df['PhwebDescription'].str.contains('FreeDOS') & \
                        (osinstalled_df['ContainerValue'].str.contains('FreeDOS', case=False))) | \
                    (osinstalled_df['PhwebDescription'].str.contains('NWZH6') & \
                        (osinstalled_df['ContainerValue'].str.contains('Windows 11 Home', case=False))) | \
                    (osinstalled_df['PhwebDescription'].str.contains('NWZHS6') & \
                        (osinstalled_df['ContainerValue'].str.contains('Windows 11 Home in S mode', case=False))) | \
                    (osinstalled_df['PhwebDescription'].str.contains('NWZP6') & \
                        (osinstalled_df['ContainerValue'].str.contains('Windows 11 Pro', case=False))) 

    osinstalled_df.loc[maskOperatingSystem, 'Accuracy'] = 'SCS Operating System OK'
    osinstalled_df.loc[~maskOperatingSystem, 'Accuracy'] = 'ERROR Operating System'

    df.update(osinstalled_df['Accuracy'])

################################################################ Power Supply Type ################################################################

    powersupplytype_df = df.loc[df['ContainerName'].str.contains('powersupplytype')]
    maskPowerSupply = (powersupplytype_df['PhwebDescription'].str.contains('120 Watt') & \
                        (powersupplytype_df['ContainerValue'].str.contains('120 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('135 Watt') & \
                        (powersupplytype_df['ContainerValue'].str.contains('135 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('150 Watt') & \
                        (powersupplytype_df['ContainerValue'].str.contains('150 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('180W ENT20') & \
                        (powersupplytype_df['ContainerValue'].str.contains('180 W 80 Plus Gold certified power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('180W SFF ENTS20') & \
                        (powersupplytype_df['ContainerValue'].str.contains('180 W Gold efficiency power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('180W Smart PFC') & \
                        (powersupplytype_df['ContainerValue'].str.contains('180 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('200 Watt') & \
                        (powersupplytype_df['ContainerValue'].str.contains('200 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('210W') & \
                        (powersupplytype_df['ContainerValue'].str.contains('210 W 80 Plus Platinum certified power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('230W SLM') & \
                        (powersupplytype_df['ContainerValue'].str.contains('230 W AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('280W') & \
                        (powersupplytype_df['ContainerValue'].str.contains('280 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('310W') & \
                        (powersupplytype_df['ContainerValue'].str.contains('310 W 80 Plus Gold certified power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('330W NSLM') & \
                        (powersupplytype_df['ContainerValue'].str.contains('330 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('350W') & \
                        (powersupplytype_df['ContainerValue'].str.contains('350 W 80 Plus Gold certified power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('400W') & \
                        (powersupplytype_df['ContainerValue'].str.contains('400 W 80 Plus Gold certified power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('P/S 500W MT WS20') & \
                        (powersupplytype_df['ContainerValue'].str.contains('500 W 80 Plus Bronze certified power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('1200W ATX') & \
                        (powersupplytype_df['ContainerValue'].str.contains('1200 W 80 Plus Gold certified ATX power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 200WSLM4.5mmPFCRtAngSmrt') & \
                        (powersupplytype_df['ContainerValue'].str.contains('200 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 45 Watt Smart nPFC RA') & \
                        (powersupplytype_df['ContainerValue'].str.contains('45 W Smart AC power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 45 Watt nPFC USB-C') & \
                        (powersupplytype_df['ContainerValue'].str.contains('45 W USB Type-C® power adapter', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('P/S 500W ATX Persan3') & \
                        (powersupplytype_df['ContainerValue'].str.contains('500 W 80 Plus Bronze certified ATX power supply', case=False))) | \
                     (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 65 Watt Smart nPFC') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 200W SLM 4.5mm PFC Rt Ang Smart') & \
                        (powersupplytype_df['ContainerValue'].str.contains('200 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 200WSLM4.5mmPFCRtAngSmtL') & \
                        (powersupplytype_df['ContainerValue'].str.contains('200 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 65 Watt nPFC Slim BLK') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 45 Watt Smart nPFC RA') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 65 Watt nPFC Slim USB-C') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W USB Type-C® power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 65 Watt Smart nPFC') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 65 Watt Smart nPFC RA') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 65W SLM USB-C Str') & \
                        (powersupplytype_df['ContainerValue'].str.contains('65 W USB Type-C® power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 90 Watt PFC USB-C') & \
                        (powersupplytype_df['ContainerValue'].str.contains('90 W USB Type-C® power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 90 Watt Smart PFC') & \
                        (powersupplytype_df['ContainerValue'].str.contains('90 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('ACADPT 90 Watt Smart PFC RA') & \
                        (powersupplytype_df['ContainerValue'].str.contains('90 W Smart AC power adapter', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('P/S 330W AiO') & \
                        (powersupplytype_df['ContainerValue'].str.contains('330 W 80 Plus Platinum certified power supply', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('P/S 800W ATX Gold') & \
                        (powersupplytype_df['ContainerValue'].str.contains('800 W 80 Plus Gold certified ATX power supply', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('P/S 600W ATX Gold') & \
                        (powersupplytype_df['ContainerValue'].str.contains('600 W 80 Plus Gold efficiency certified ATX power supply', case=False))) | \
                      (powersupplytype_df['PhwebDescription'].str.contains('P/S 500W MT WS20') & \
                        (powersupplytype_df['ContainerValue'].str.contains('500 W Bronze efficiency power supply', case=False))) | \
                    (powersupplytype_df['PhwebDescription'].str.contains('P/S 600W ATX Gold') & \
                        (powersupplytype_df['ContainerValue'].str.contains('600 W 80 Plus Gold certified ATX power supply', case=False)))

    powersupplytype_df.loc[maskPowerSupply, 'Accuracy'] = 'SCS Power Supply Type OK'
    powersupplytype_df.loc[~maskPowerSupply, 'Accuracy'] = 'ERROR Power Supply Type'

    df.update(powersupplytype_df['Accuracy'])

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
    