import datetime
import astral
from astral.sun import sun
from astral import LocationInfo
import pytz #to deal with timezone changes
yellowstone= LocationInfo("Yellowstone","US", "US/Mountain", 44.428, -110.589) #set the location to calculate sun times
today = datetime.datetime.now() #get the current date, in the local (computer) timezone
mountain = pytz.timezone('US/Mountain') #set mountain timezone

s = sun(yellowstone.observer, date=today) #s in the object that stores the sunrise and sunset values, in UTC

#print((
#    f'Dawn:    {s["dawn"]}\n'
#    f'Sunrise: {s["sunrise"]}\n'
#    f'Noon:    {s["noon"]}\n'
#    f'Sunset:  {s["sunset"]}\n'
#    f'Dusk:    {s["dusk"]}\n'
#))
sunrise_mountain_time = s['sunrise'].astimezone(mountain) #generate time object for sunrise in mountain time
sunset_mountain_time = s['sunset'].astimezone(mountain) #generate time object for sunset in mountain time

sunrise = open('sunrise.txt', 'w')
sunrise.write(str(sunrise_mountain_time.hour))
sunrise.close()
sunset = open('sunset.txt', 'w')
sunset.write(str(sunset_mountain_time.hour))
sunset.close()

