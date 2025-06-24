import pandas as pd
import json
import os
from collections import defaultdict

# IMPORTANT: To run this script, you need to install the 'openpyxl' library.
# Open your command prompt or terminal and type: pip install openpyxl

def find_file(filename, search_path):
    """
    Recursively searches for a file within a given directory and its subdirectories.

    Args:
        filename (str): The name of the file to find (e.g., "batteryrechrg.json").
        search_path (str): The root directory to start the search from.

    Returns:
        str: The full path to the file if found, otherwise None.
    """
    for root, dirnames, filenames in os.walk(search_path):
        if filename in filenames:
            return os.path.join(root, filename)
    return None

def update_json_files(excel_path, dictionaries_root_path, report_path):
    """
    Reads an Excel file to update JSONs, removes exact duplicates, and reports components
    with multiple different values.

    Args:
        excel_path (str): Path to the input .xlsx Excel file.
        dictionaries_root_path (str): Root directory containing the JSON files.
        report_path (str): Path to save the duplicate components report.
    """
    try:
        updates_df = pd.read_excel(excel_path, engine='openpyxl')
        print("✅ Excel file read successfully.")
        print(f"ℹ️ Columns found in Excel file: {updates_df.columns.tolist()}")
    except FileNotFoundError:
        print(f"🚨 Error: The Excel file was not found at the specified path: {excel_path}")
        return
    except Exception as e:
        print(f"🚨 An error occurred while reading the Excel file: {e}")
        return

    # List to hold data for the duplicate component report
    duplicate_report_data = []

    # Process each file group from the Excel sheet
    for container_name, group in updates_df.groupby('ContainerName'):
        if not container_name:
            continue
        json_filename = f"{container_name}.json"
        json_path = find_file(json_filename, dictionaries_root_path)

        if not json_path:
            print(f"⚠️ Warning: Could not find '{json_filename}'. Skipping.")
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"🚨 Error reading or parsing {json_path}: {e}. Skipping.")
            continue

        print(f"\n🔄 Processing file: {json_path}")

        if not data or not isinstance(data, dict) or not list(data.keys()):
            print(f"🚨 Error: JSON file {json_path} is empty or has an unexpected format. Skipping.")
            continue
            
        json_key = list(data.keys())[0]
        items_list = data[json_key]
        
        # This dictionary is used for quick lookups to update existing components
        items_dict = {str(item.get('Component')): item for item in items_list if 'Component' in item}
        
        updated = False

        # --- Step 1: Add or Update items from the Excel file ---
        for _, row in group.iterrows():
            component = str(row.get('Component', '')).strip()
            correct_value_for_update = row.get('Correct Value', '')
            container_value_for_new = row.get('ContainerValue', '')

            if pd.isna(correct_value_for_update): correct_value_for_update = ''
            if pd.isna(container_value_for_new): container_value_for_new = ''
            
            if not component:
                continue

            if component in items_dict:
                if items_dict[component].get('ContainerValue') != correct_value_for_update:
                    print(f"  -> Updating component '{component}'...")
                    items_dict[component]['ContainerValue'] = correct_value_for_update
                    updated = True
                else:
                    print(f"  -> No change needed for component '{component}'.")
            else:
                print(f"  -> Adding new component '{component}'...")
                new_item = {"Component": component, "ContainerValue": container_value_for_new}
                items_list.append(new_item)
                updated = True

        # --- Step 2: Find components with multiple different values for reporting ---
        component_values = defaultdict(list)
        for item in items_list:
            comp_id = item.get('Component')
            if comp_id:
                component_values[comp_id].append(item.get('ContainerValue'))
        
        for comp_id, values in component_values.items():
            # Using set to find unique values
            if len(set(values)) > 1:
                print(f"  -> Found conflicting values for component '{comp_id}'. Adding to report.")
                for value in set(values): # Use set to avoid reporting same conflict multiple times
                    duplicate_report_data.append({
                        'File': os.path.basename(json_path),
                        'Component': comp_id,
                        'ConflictingContainerValue': value
                    })

        # --- Step 3: Remove identical duplicates (same Component AND same ContainerValue) ---
        unique_items = []
        seen_pairs = set()
        for item in items_list:
            # Create a tuple of the component and value to check for duplicates
            pair = (item.get('Component'), item.get('ContainerValue'))
            if pair not in seen_pairs:
                unique_items.append(item)
                seen_pairs.add(pair)
        
        if len(items_list) != len(unique_items):
            print(f"  -> Removed {len(items_list) - len(unique_items)} identical duplicate(s).")
            data[json_key] = unique_items
            updated = True
        
        # --- Step 4: Save the cleaned and updated JSON file ---
        if updated:
            try:
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print(f"✅ Successfully saved updates to {json_path}")
            except Exception as e:
                print(f"🚨 Error writing updates to {json_path}: {e}")

    # --- Step 5: Generate the final report for conflicting duplicates ---
    if duplicate_report_data:
        print(f"\n📝 Generating duplicate components report...")
        report_df = pd.DataFrame(duplicate_report_data)
        try:
            # Use 'utf-8-sig' encoding to ensure Excel reads special characters correctly
            report_df.to_csv(report_path, index=False, encoding='utf-8-sig')
            print(f"✅ Report successfully saved to: {os.path.abspath(report_path)}")
        except Exception as e:
            print(f"🚨 Could not save the report. Reason: {e}")
    else:
        print("\n✅ No conflicting duplicate components found to report.")


# --- Configuration ---
# 1. The full path to your ORIGINAL .xlsx Excel file.
csv_file_path = 'update dictionaries june week 1.xlsx'

# 2. The full path to the root 'dictionaries' folder.
dictionaries_folder_path = 'app\\data\\new_json_backup' # Using a relative path

# 3. The name for the duplicate component report file.
duplicate_report_filename = 'duplicate_components_report.csv'

# --- Main execution block ---
if __name__ == "__main__":
    if not os.path.exists(csv_file_path):
        print(f"🚨 FATAL ERROR: The Excel file does not exist at: {os.path.abspath(csv_file_path)}")
        print("Please update the 'csv_file_path' variable in the script.")
    elif not os.path.exists(dictionaries_folder_path):
        print(f"🚨 FATAL ERROR: The dictionaries folder does not exist at: {os.path.abspath(dictionaries_folder_path)}")
        print("Please update the 'dictionaries_folder_path' variable in the script.")
    else:
        print("🚀 Starting JSON update process...")
        update_json_files(csv_file_path, dictionaries_folder_path, duplicate_report_filename)
        print("\n🎉 All updates are complete!")
