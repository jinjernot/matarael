import pandas as pd
import os
import json

def search_json_files(value, container_names):
    json_folder = "json"
    for filename in os.listdir(json_folder):
        if filename.endswith(".json") and filename.split(".")[0] in container_names:
            with open(os.path.join(json_folder, filename), encoding="utf-8") as json_file:
                data = json.load(json_file)
                for item in data:
                    for entry in data[item]:
                        container_value = entry.get("ContainerValue", "")
                        if isinstance(container_value, str):
                            container_words = container_value.lower().split()  
                            value_words = value.lower().split()
                            if any(word in container_words for word in value_words):
                                return filename.split(".")[0], container_value
    return None, None  #

def load_component_groups():
    with open('app/data/component_groups.json', 'r', encoding='utf-8') as json_file:
        component_groups = json.load(json_file)
    return {group['ComponentGroup']: group['ContainerName'] for group in component_groups['Groups']}

def matrix_file():
    try:
        component_groups = load_component_groups()

        df = pd.read_excel("compo.xlsx", engine='openpyxl', skiprows=1)

        df = df.dropna(subset=["Characteristic"])

        df["Characteristic"] = df["Characteristic"].str.strip()

        found_data = []

        # Search for data in JSON files and add new columns
        for index, row in df.iterrows():
            scs_group = row["SCS Component Group"]
            if scs_group in component_groups:
                container_names = component_groups[scs_group]
                json_name, container_value = search_json_files(row["Characteristic"], container_names)
                if json_name is not None and container_value is not None:
                    found_row = {
                        "Component": row["Component"],
                        "SCSGroup": scs_group,
                        "ContainerType": "Prism",
                        json_name: container_value
                    }
                    found_data.append(found_row)

        # Convert the list of dictionaries to a DataFrame
        if found_data:
            matrix_df = pd.DataFrame(found_data)
        else:
            matrix_df = pd.DataFrame(columns=["Component", "SCSGroup", "ContainerType"])

        # Save matrix_df to Excel
        matrix_df.to_excel("matrix_output.xlsx", index=False)
        print("Matrix Excel completed.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    matrix_file()
