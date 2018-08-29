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

locations = []

for attraction in attraction_list_items:
    name = label_regex.search(str(attraction))
    locations.append(name.group(1)[:-18])

pytrends = TrendReq(hl='en-US', tz=360)

# google gives data according relative to the highest relevant attraction
# need to recognise this attraction before pulling off data
# locations = ["Big Ben", "London Underground", "Tower of London"]

kw_list = []

for location in locations[:10]:
    suggestions = pytrends.suggestions(location+" London")
    
    for suggestion in suggestions:
        if location.lower() in suggestion['title'].lower():
            print(suggestion)
            kw_list.append(suggestion['mid'])
            break

pytrends.build_payload(kw_list[:3], cat=67, timeframe='2018-08-18 2018-08-25', geo='', gprop='')
print(pytrends.interest_over_time())