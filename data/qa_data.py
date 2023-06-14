import pandas as pd
from data.format_data import formateData
from data.process_data import processData
import os

def cleanReport(file):
    print(file)

    try:
        # Remove rows where the ContainerValue column is equal to "[BLANK]".
        df = pd.read_excel(file.stream, engine='openpyxl')
        print(df)
        df = df[df['ContainerValue'] != '[BLANK]']

        # Replace all occurrences of the character `\u00A0` with a space.
        df.replace('\u00A0', ' ', regex=True, inplace=True)

        # Create a list of columns to drop.
        cols_to_drop = ['Option', 'Status', 'SKU_FirstAppearanceDate', 'SKU_CompletionDate', 'SKU_Aging', 'PhwebValue', 'ExtendedDescription', 'ComponentCompletionDate', 'ComponentReadiness', 'SKUReadiness']

        # Drop the columns from the DataFrame.
        df = df.drop(cols_to_drop, axis=1)

        # Create three new columns in the DataFrame.
        df[['Accuracy', 'Correct Value', 'Additional Information']] = ''

        # Loop over all the files in the `json` directory.
        for x in os.listdir('/home/garciagi/SCS_Tool/json'):

            # Check if the file name ends with `.json`.
            if x.endswith('.json'):

                # Split the file name on the period character and get the first part of the file name.
                container_name = x.split('.')[0]

                # Get the DataFrame rows where the ContainerName column contains the container name.
                container_df = df.loc[df['ContainerName'].str.contains(container_name)]

                # Pass the rows to the processData() function.
                processData(os.path.join('/home/garciagi/SCS_Tool/json', x), container_name, container_df, df)

        # Remove all trailing semicolons from the ContainerValue column.
        df.loc[df['ContainerValue'].str.endswith(';'), 'ContainerValue'] = df['ContainerValue'].str.slice(stop=-1)

        # Save the DataFrame to a file called `SCS_QA.xlsx`.
        df.to_csv('/home/garciagi/SCS_Tool/SCS_QA.csv', index=False)
        #formateData()

    except Exception as e:
        print(e)
    return
    