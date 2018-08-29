from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

# google gives data according relative to the highest relevant attraction
# need to recognise this attraction before pulling off data
# locations = ["Big Ben", "London Underground", "Tower of London"]
locations = ["Dagadusheth Halwai Ganapati Temple","Shaniwar Wada","sinhagad"]
kw_list = []

for location in locations:
    suggestions = pytrends.suggestions(location)
    
    for suggestion in suggestions:
        if location.lower() in suggestion['title'].lower():
            print(suggestion)
            kw_list.append(suggestion['mid'])
            break

pytrends.build_payload(kw_list, cat=67, timeframe='2018-08-18 2018-08-25', geo='', gprop='')
print(pytrends.interest_over_time())