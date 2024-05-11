import pandas as pd
import os
import json

def matrix_file():
    try:
        # Read Excel file into DataFrame
        df = pd.read_excel("compo.xlsx", engine='openpyxl')
        
        # Remove the first row
        df = df.iloc[1:]
        
        # Extract unique values from "SCS Component Group"
        #component_groups = df["SCS Component Group"]
        content = df["Characteristic"]
        print(content)
        
        # Load and iterate over JSON files
        json_folder = "json"
        for filename in os.listdir(json_folder):
            if filename.endswith(".json"):
                with open(os.path.join(json_folder, filename)) as json_file:
                    data = json.load(json_file)
                    for group in data.values():
                        for item in group:
                            container_value = item.get("ContainerValue", "")
                            for c in content:
                                if c in container_value:
                                    df.loc[df['Characteristic'] == c, 'test'] = True
                                else:
                                    df.loc[df['Characteristic'] == c, 'test'] = False
        
        # Save DataFrame to Excel
        df.to_excel("output.xlsx", index=False)
        print("Excel file saved successfully.")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Example usage:
    matrix_file()
