
import pytz

from datetime import datetime

#utc = pytz.timezone('UTC')
# now = utc.localize(datetime.utcnow())

la = pytz.timezone('America/Los_Angeles')
now = datetime.now(la)
print now.astimezone(pytz.utc)

