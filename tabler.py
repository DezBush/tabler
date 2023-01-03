import requests
from bs4 import BeautifulSoup
import pandas as pd
import shutil
import os

while True:
    # Send an HTTP request to the website and retrieve the HTML content
    url = input("Enter the URL of the website: ")
    try:
        response = requests.get(url)
        break
    except requests.exceptions.RequestException:
        print("Invalid URL. Please Try Again.")
html = response.text

# Use BeautifulSoup to parse the HTML and extract the table elements
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')

# Convert the tables to a list and print the number of tables found
table_list = list(tables)
print(f'Number of tables found: {len(table_list)}')

# Iterate over the list of tables and convert each table to a CSV file
for i, table in enumerate(table_list):
  df = pd.read_html(str(table))[0]
  csv_file = f'table_{i}.csv'
  df.to_csv(csv_file, index=False)

# Get the user's Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Iterate over the CSV files and move them to the Downloads folder
for csv_file in os.listdir():
  if csv_file.endswith('.csv'):
    shutil.move(csv_file, downloads_folder)