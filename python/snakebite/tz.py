
import pytz
from datetime import datetime

la=pytz.timezone('America/Los_Angeles')
now=datetime.now(la)
print now
#print now.replace(2017,8,31,10,50,11)
print datetime(2017,8,31,10,50,11, tzinfo=la)
start="2017-08-31 10:50:11"
rstart = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")

adjust=now.replace(rstart.year, rstart.month, rstart.day, rstart.hour, rstart.minute, rstart.second)

print adjust.astimezone(pytz.utc)



