import requests;
from bs4 import BeautifulSoup
import pandas as pd

page=requests.get('https://forecast.weather.gov/MapClick.php?lat=33.969670000000065&lon=-118.249935#.YJ-huLUzZIA')
soup =BeautifulSoup(page.content,'html.parser')
# print(soup)
week=soup.find(id='seven-day-forecast-body')
# print(week);
items=(week.find_all(class_='tombstone-container'));
# print(items)

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names=[item.find(class_='period-name').get_text() for item in items]
temprature=[item.find(class_='temp').get_text() for item in items]
short_descriptions=[item.find(class_='short-desc').get_text() for item in items]
print(period_names)
print(temprature)
print(short_descriptions)

weatherstuff=pd.DataFrame(
    {
        'period':period_names,
        'short_description':short_descriptions,
        'temprature':temprature,
    }
)
print(weatherstuff)
