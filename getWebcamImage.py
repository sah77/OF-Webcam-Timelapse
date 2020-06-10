import datetime
import pytz #to deal with timezone changes

YellowstoneTime = datetime.datetime.now(tz=pytz.timezone('US/Mountain')) #get the current time, in mountain timezone

sunup = open('sunrise.txt', 'r')  
sunriseTime = int(sunup.read())
sunup.close()

sundown = open('sunset.txt', 'r')
sunsetTime = int(sundown.read())
sundown.close()

import requests #module to get data from a URL

filename = 'images/' + YellowstoneTime.strftime('%Y') + "_" + YellowstoneTime.strftime('%j') + "_" + YellowstoneTime.strftime('%H') + '.jpg'
url = 'https://www.nps.gov/webcams-yell/oldfaithful.jpg'

if YellowstoneTime.hour >= sunriseTime and YellowstoneTime.hour <= sunsetTime:
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
