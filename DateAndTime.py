from datetime import datetime

import pytz


tz_OR = pytz.timezone('America/Oregon')
datetime_OR = datetime.now(tz-OR)
print("Portland HQ Time: ", datetime_OR.strftime("%H:%M:%S"))

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NYC HQ Time: :", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London HQ time: ", datetime_London.strftime("%H:%M:%S"))
