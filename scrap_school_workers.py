# .mtr-table
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Since Kali uses different default Firefox version, we need to link it's binary file.
binary = FirefoxBinary("/usr/bin/firefox-esr")
browser = webdriver.Firefox(firefox_binary=binary)

browser.get("https://horyzont.eu/uczelnia/pracownicy-administracyjni/")
table_element = browser.find_element_by_class_name("mtr-table")
table_rows = table_element.find_elements_by_tag_name("tr")

list_of_workers = []
for row in table_rows:
    worker_data = []
    row_cells = row.find_elements_by_tag_name("td")
    for cell in row_cells:
        cell_content = cell.find_element_by_class_name("mtr-cell-content").text
        worker_data.append(cell_content)
    list_of_workers.append(worker_data)

browser.close()

workers_dataframe = pd.DataFrame(list_of_workers[1:], columns=list_of_workers[0])
workers_dataframe_csv = workers_dataframe.to_csv(path_or_buf="school_workers.csv")
