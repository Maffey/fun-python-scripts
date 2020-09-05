import openpyxl
import os

excels_dir = "temp"
target_name = "combined_file.xlsx"
excels_list = os.listdir(excels_dir)
print(excels_list)

# Combine all the data from xlsx files into one data structure.
list_of_sheets_rows = []
for file in excels_list:
    # If combined file already exists, don't try to combine it together.
    if file == target_name:
        continue
    wb = openpyxl.load_workbook(os.path.join(excels_dir, file))
    sheet = wb.active
    # TODO: Remove redundant headers.
    for row in sheet:
        list_of_cells_in_row = []
        for cell in row:
            list_of_cells_in_row.append(cell.value)
        list_of_sheets_rows.append(list_of_cells_in_row)

# Save the data to a new workbook.
new_wb = openpyxl.Workbook()
for row_of_data in list_of_sheets_rows:
    new_wb.active.append(row_of_data)
new_wb.save(os.path.join(excels_dir, target_name))
