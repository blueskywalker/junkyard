
import pytz

from datetime import datetime

utc = pytz.timezone('UTC')
now = utc.localize(datetime.utcnow())

la = pytz.timezone('America/Los_Angeles')
local_time = now.astimezone(la)
print local_time

