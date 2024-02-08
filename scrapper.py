#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

def scrape_flipkart_product_links(search_query):
    base_url = 'https://www.flipkart.com'
    search_query = search_query.replace(' ', '+')
    url = f'{base_url}/search?q={search_query}'
    
    print("Scraping Flipkart URL:", url)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_links = []
    for link in soup.find_all('a', {'class': '_1fQZEK'}):
        product_links.append(base_url + link.get('href'))
    
    return product_links

# Get user input for the product type or specific search query
search_query = input("Enter the product type or specific search query: ")

# Scrape product links from Flipkart
flipkart_links = scrape_flipkart_product_links(search_query)

# Print the scraped product links
print("\nFlipkart Product Links:")
for link in flipkart_links:
    print(link)


# In[ ]:




