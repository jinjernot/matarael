qa_data.py

The cleanReport() function takes a file name as input and cleans a report in that file.

The function first reads the file into a Pandas DataFrame. It then removes rows where the ContainerValue column is equal to [BLANK]. It then replaces all occurrences of the character \u00A0 with a space.

The function then creates a list of columns to drop. These columns are Option, Status, SKU_FirstAppearanceDate, SKU_CompletionDate, SKU_Aging, PhwebValue, ExtendedDescription, ComponentCompletionDate, ComponentReadiness, and SKUReadiness. The function then drops these columns from the DataFrame.

The function then creates three new columns in the DataFrame: Accuracy, Correct Value, and Additional Information. These columns are all initialized to the empty string.

The function then loops over all the files in the json directory. For each file, it checks if the file name ends with .json. If it does, the function splits the file name on the period character and gets the first part of the file name. This is the name of the container. The function then gets the DataFrame rows where the ContainerName column contains the container name. It then passes these rows to the processData() function.

The processData() function takes a DataFrame, a container name, and the original DataFrame as input. It then creates a new DataFrame that contains only the rows where the ContainerName column is equal to the container name. It then calls the formatData() function to format the DataFrame.

The formatData() function takes a DataFrame as input and formats the DataFrame. It does this by removing all trailing semicolons from the ContainerValue column. It then saves the DataFrame to a file called SCS_QA.xlsx.

The cleanReport() function catches all exceptions and prints them to the console.


format_data.py

The formatData() function takes no input and formats a report in a file called SCS_QA.xlsx.

The function first loads the workbook into memory. It then gets the active worksheet. It then creates a pattern fill with the color 0072C6 and the fill type solid. It then applies this fill to all the cells in the first row of the worksheet.

The function then loops over all the columns in the worksheet. For each column, it gets the maximum length of any value in the column. It then calculates the adjusted width of the column, which is the maximum length plus 2 characters, multiplied by 1.2. It then sets the width of the column to the adjusted width.

The function then loops over all the cells in column H. For each cell, it checks if the value of the cell contains the string ERROR. If it does, the function changes the color of the font in the cell to red and add borders.

The function then saves the workbook to a file called SCS_QA.xlsx.

plot_data.py

The createPlot() function creates a bar plot of the top 10 containers with the most errors in the SCS_QA.xlsx file.

The function first reads the Excel file into a Pandas DataFrame. The DataFrame is then filtered to only include rows where the Accuracy column contains the string ERROR. The filtered DataFrame is then grouped by the ContainerName column and the size of each group is calculated. The results are then sorted by the Count column in descending order and the top 10 rows are returned.

The createPlot() function then creates a figure and plots the bar chart. The bar chart is colored blue and the title, x-label, and y-label are all set. The x-ticks are also rotated 25 degrees and aligned to the right. The figure is then saved to the ./static/images/chart.png file.

Next, the createPlot() function opens the SCS_QA.xlsx file and creates a new worksheet named Bar Plot. The Bar Plot worksheet is then activated and an image of the bar chart is added to cell A1. The workbook is then saved.

The createPlot() function handles errors by printing the error message to the console.

process_data.py

The processData() function processes data from a JSON file and updates a Pandas DataFrame.

The function first opens the JSON file and loads the data into a dictionary. The function then creates an empty dictionary to store the accuracy of each container.

For each container in the JSON file, the function creates a mask that filters the container_df DataFrame to only include rows where the PhwebDescription column contains the container's PhwebDescription value and the ContainerValue column contains the container's ContainerValue value. The function then adds the index of each row that matches the mask to the container_accuracy_dict dictionary.

The function then iterates over the index of the container_df DataFrame. If the index is not in the container_accuracy_dict dictionary, the function adds the index to the dictionary with the value ERROR: + container_name.

The function then updates the Accuracy column of the container_df DataFrame with the values from the container_accuracy_dict dictionary. The function then updates the Accuracy column of the df DataFrame with the values from the container_df DataFrame.

The function returns the df DataFrame.