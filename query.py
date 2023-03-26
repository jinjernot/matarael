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
            (productcolor_df['ContainerValue'] == 'Mica silver, dark chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO NFB PLA nODD 180W') & \
            (productcolor_df['ContainerValue'] == 'Mica silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO MCS SHT MTL 350W') & \
            (productcolor_df['ContainerValue'] == 'Jet black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID STB PLA wFHDC IR') & \
            (productcolor_df['ContainerValue'] == 'Mica silver, dark chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO SDB GLA 600W') & \
            (productcolor_df['ContainerValue'] == 'Black, glass side panel, dark chrome logo')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO NFB PLA nODD 180W') & \
            (productcolor_df['ContainerValue'] == 'Nightfall black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO JTB PLA 180W 22C1') & \
            (productcolor_df['ContainerValue'] == 'Dark black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO MCS SHT MTL 350W') & \
            (productcolor_df['ContainerValue'] == 'Mica silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID STB PLA wFHDC IR') & \
            (productcolor_df['ContainerValue'] == 'Jet black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID RCTO SWH PLA 180W') & \
            (productcolor_df['ContainerValue'] == 'Dark black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID JTB PLA nSDC wHDC') & \
            (productcolor_df['ContainerValue'] == 'Jet black')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NFB ALU') & \
            (productcolor_df['ContainerValue'] == 'Nightfall black aluminum')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SDB PLA US layout fTDB') & \
            (productcolor_df['ContainerValue'] == 'Shadow black cover and base, shadow black aluminum keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB +NSV PLA wHDC') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID PLG PLA wHDC FPR') & \
            (productcolor_df['ContainerValue'] == 'Pale gold cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA nSDC wHDC nFPR nWWAN FHD TS') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SFW PLA w5MPC IR QHD') & \
            (productcolor_df['ContainerValue'] == 'Snowflake white, natural silver stand')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV PLA wHDC TNR FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB +NSV PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID PLG +NSV PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Pale gold cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV +NSV MTE PT wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV PLA wHDC TNR nFPR FHD TS') & \
            (productcolor_df['ContainerValue'] == 'Natural silver')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU nSDC FPR') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum cover and keyboard frame, natural silver base')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU fRTX wHDC TNR US layout') & \
            (productcolor_df['ContainerValue'] == 'Natural silver aluminum'))
        ((productcolor_df['PhwebDescription'] == 'ID NSV ALU wHDC TNR US layout') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID JTB STD MSKT wHDC') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \
        ((productcolor_df['PhwebDescription'] == 'ID SPB PLA wHDC TNR') & \
            (productcolor_df['ContainerValue'] == 'Spruce blue cover and base, natural silver keyboard frame')) | \