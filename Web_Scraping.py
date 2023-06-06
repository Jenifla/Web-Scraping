#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://proxyway.com/reviews"

# Menyiapkan file CSV
csv_file = open('scraping_judul_Jenifla.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Page Number', 'Title Number', 'Title'])

for page in range(1, 4):  
    page_url = URL + '/page/' + str(page)
    req = requests.get(page_url)
    soup = bs(req.text, 'html.parser')
    titles = soup.find_all('h3', attrs={'class': 'archive-list__title'})

    for i, title in enumerate(titles):
        title_text = title.get_text(strip=True)
        csv_writer.writerow([f'Page {page}', f'Title {i+1}', title_text])

# Menutup file CSV
csv_file.close()

print("Data telah disimpan ke dalam file scraping_judul_Jenifla.csv")


# In[ ]:




