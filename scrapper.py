import requests
import pandas as pd
from bs4 import BeautifulSoup

result = requests.get("https://www.ebay.com/deals")

ebay_page = result.content
# print(ebay_page)

soup = BeautifulSoup(ebay_page, 'html.parser')

# 1. Get container with all featured items
featured_items_container = soup.find_all('div', 'ebayui-dne-item-featured-card')

# 2. Get all featured items in the container
items = featured_items_container[0].find_all('div', 'dne-itemtile dne-itemtile-medium')

print(items[0].find('div', 'dne-itemtile-price').text)
# 3. Loop through each item
prices = []
for index, item in enumerate(items):
  # 4. Get each item's h3 tag and the title from it
  print('{}. {}\n'.format(index + 1, item.find('h3').get('title')))

  if item.find('div', 'dne-itemtile-price'):
    prices.append(item.find('div', 'dne-itemtile-price').text)
  else:
    prices.append('NA')



titles = [item.find('h3').get('title') for item in items]
print(titles)



print(prices)
print(len(titles))
print(len(prices))

result_final = pd.DataFrame(
  {
    'title': titles,
    'price': prices,
    }
)

result_final.to_csv('ebay_deals.csv')
