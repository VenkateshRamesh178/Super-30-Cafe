import sqlite3
import requests
from bs4 import BeautifulSoup

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('menu.db')
c = conn.cursor()

# Create a table to store the menu data
c.execute('''
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        cost TEXT,
        description TEXT,
        image_url TEXT
    )
''')

# HTML file (load or download)
url = 'http://127.0.0.1:5500/views/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Loop through each menu-content div and extract data
menus = soup.find_all('div', class_='menu-content')

for menu in menus:
    img_url = menu.find_previous('img')['src']
    item_name, cost = menu.find('h2').get_text().split('Rs.')  # Split item and cost by Rs.
    cost = 'Rs.' + cost.strip()  # Add 'Rs.' back to cost
    description = menu.find('p').get_text()

    # Insert data into the database
    c.execute('''
        INSERT INTO menu (item_name, cost, description, image_url) 
        VALUES (?, ?, ?, ?)
    ''', (item_name.strip(), cost, description.strip(), img_url))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully!")
