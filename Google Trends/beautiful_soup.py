from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup
import re

# Collect and parse first page
page = requests.get('https://www.triphobo.com/places/london-united-kingdom/things-to-do')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
attraction_list_names = soup.find(class_='js_attraction_list')

# Pull text from all instances of <a> tag within BodyText div
attraction_list_items = attraction_list_names.find_all('label')
label_regex = re.compile('<label>(.*)</label>')

kw_list = []

for attraction in attraction_list_items:
    name = label_regex.search(str(attraction))
    kw_list.append(name.group(1)[:-18])

print(kw_list)