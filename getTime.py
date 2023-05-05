import datetime
import json
from urllib.request import urlopen



def Time_In_the_World():
##get the users default timezone
  
  url = "http://ipinfo.io/json"
  response = urlopen(url)
  data = json.load(response)
##time_zone is acssesing the time zone throught the data dictionary
  time_zone=data["timezone"]
  time = datetime.datetime.now()
  print (time.strftime("Time in {} is: %H:%M").format(time_zone))

  


#
