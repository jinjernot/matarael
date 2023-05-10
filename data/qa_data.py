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

    container_df = df.loc[df['ContainerName'].str.contains('energyeffcomp')]
    processData('json/energyeffcomp.json', 'energyeffcomp', container_df, df)

################################################################ ENERGY STAR ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('energystar')]
    processData('json/energystar.json', 'energystar', container_df, df)

################################################################ Graphic Card ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('graphicseg_02card_01') & df['ComponentGroup'].str.contains('Graphic card')]
    processData('json/graphicseg_02card_01.json', 'graphicseg_02card_01', container_df, df)

################################################################ Optical Drive ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('cdromdvd') & df['ComponentGroup'].str.contains('Optical Drive')]
    processData('json/cdromdvd.json', 'cdromdvd', container_df, df)

################################################################ Wireless Tech ################################################################

    container_df = df.loc[df['ContainerName'].str.strip() == 'wirelesstech']
    processData('json/wirelesstech.json', 'wirelesstech', container_df, df)

################################################################ Keyboard ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('keybrd')]
    processData('json/keybrd.json', 'keybrd', container_df, df)

################################################################ Video Connectors ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('videoconnectors')]
    processData('json/videoconnectors.json', 'videoconnectors', container_df, df)


################################################################ Special Features ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('perftechn')]
    processData('json/perftechn.json', 'perftechn', container_df, df)

########################################################################################################################################
################################################################ Facets ################################################################
########################################################################################################################################


################################################################ facet_environ ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('facet_environ')]
    processData('json/perftechn.json', 'perftechn', container_df, df)

################################################################ facet_memstd ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('facet_memstd') & df['ComponentGroup'].str.contains('Memory')]
    processData('json/facet_memstd.json', 'facet_memstd', container_df, df)

################################################################ facet_cap ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('facet_cap')]
    processData('json/facet_cap.json', 'facet_cap', container_df, df)

################################################################ facet_os ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('facet_os')]
    processData('json/facet_os.json', 'facet_os', container_df, df)

################################################################ facet_graphics ################################################################

    container_df  = df.loc[df['ContainerName'].str.contains('facet_graphics') & df['ComponentGroup'].str.contains('Graphic card')]
    processData('json/facet_graphics.json', 'facet_graphics', container_df, df)

################################################################ facet_processortype ################################################################

    container_df = df.loc[df['ContainerName'].str.contains('facet_processortype') & df['ComponentGroup'].str.contains('Processor')]
    processData('json/facet_processortype.json', 'facet_processortype', container_df, df)



################################################################ facet_scrnsizeus ################################################################

    container_df  = df.loc[df['ContainerName'].str.contains('facet_scrnsizeus') & df['ComponentGroup'].str.contains('Display')]
    processData('json/facet_scrnsizeus.json', 'facet_scrnsizeus', container_df, df)


    df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)

    df.to_excel('SCS_QA.xlsx', index=False)

    formateData()

    return 
    