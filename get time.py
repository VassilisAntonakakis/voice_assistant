import datetime
import json
from urllib.request import urlopen
def get_time():

  time = datetime.datetime.now()
  print (time.strftime("Time is: %H:%M"))

def Time_In_the_World():
##get the users default timezone
  
  url = "http://ipinfo.io/json"
  response = urlopen(url)
  data = json.load(response)
##time_zone is acssesing the time zone throught the data dictionary
  time_zone=data["timezone"]
  time_there = datetime.datetime.now(time_zone)
  print (time_there.strftime("Time in {} is: %H:%M".format(time_zone)))
  
get_time()

Time_In_the_World()
