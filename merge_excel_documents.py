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
    for row in sheet:
        list_of_cells_in_row = []
        for cell in row:
            list_of_cells_in_row.append(cell.value)
        list_of_sheets_rows.append(list_of_cells_in_row)

# Open a new workbook to save results into.
new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

# Before saving the data, remove repeated headers.
headers = list_of_sheets_rows[0]
list_of_sheets_rows = [row for row in list_of_sheets_rows if row != headers]
list_of_sheets_rows.insert(0, headers)

for row_of_data in list_of_sheets_rows:
    new_sheet.append(row_of_data)

# Save the data to a new workbook.
new_wb.save(os.path.join(excels_dir, target_name))
