from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Collect and parse first page
page = requests.get('https://www.triphobo.com/places/london-united-kingdom/things-to-do')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
attraction_list_names = soup.find(class_='js_attraction_list')

# Pull text from all instances of <a> tag within BodyText div
attraction_list_items = attraction_list_names.find_all('label')
label_regex = re.compile('<label>(.*)</label>')

locations = []

for attraction in attraction_list_items:
    name = label_regex.search(str(attraction))
    locations.append(name.group(1)[:-18])

pytrends = TrendReq(hl='en-US', tz=360)

# google gives data according relative to the highest relevant attraction
# need to recognise this attraction before pulling off data
# locations = ["Big Ben", "London Underground", "Tower of London"]

kw_list, kw_list_mapping = [], {}

for location in locations[:20]:
    suggestions = pytrends.suggestions(location+" London")
    
    for suggestion in suggestions:
        if location.lower() in suggestion['title'].lower():
            kw_list.append(suggestion['mid'])
            kw_list_mapping[suggestion['mid']] = location
            break

print(kw_list_mapping)
time = pd.Timestamp(2018, 8, 25)

final_mapping = {}

for n in range(0, len(kw_list)):
    mid = kw_list[n]
    pytrends.build_payload([mid], cat=67, timeframe='2018-08-18 2018-08-25', geo='', gprop='')
    result = pytrends.interest_over_time().to_dict()
    if result:
        final_mapping[kw_list_mapping[mid]] = result[mid][time]

print(final_mapping)
print(sorted(final_mapping, key=lambda x:x[1]))