#!/usr/bin/env python3

#
# Snooze the message until a future date
# Move the message to the /Later folder
# Mark the message as Seen and Not Junk
# https://www.mail-archive.com/mailmate@lists.freron.com/msg05451.html
#
import sys
import datetime

MORNING_HOUR=6
EVENING_HOUR=18

def monday(d):
  if d.weekday() == 0:
    return d
  return d + datetime.timedelta(days=7-d.weekday())

def saturday(d):
  if d.weekday() == 5:
    return d
  if d.weekday() == 6:
    return d + datetime.timedelta(days=6)
  return d + datetime.timedelta(days=5-d.weekday())

dt = datetime.datetime.today()
dt = dt.replace(hour=MORNING_HOUR, minute=0, second=0, microsecond=0)

when = sys.argv[1]

if when == "evening":
  dt = dt.replace(hour=EVENING_HOUR)
elif when == "tomorrow":
  dt = dt + datetime.timedelta(days=1)
elif when == "tomorrowevening":
  dt = dt.replace(hour=EVENING_HOUR)
  dt = dt + datetime.timedelta(days=1)
elif when == "weekend":
  dt = dt + datetime.timedelta(days=1)
  dt = saturday(dt)
elif when == "nextweek":
  dt = dt + datetime.timedelta(days=1)
  dt = monday(dt)
elif when == "month":
  dt = dt + datetime.timedelta(weeks=4)
  dt = monday(dt)
elif when == "pick":
  dt = datetime.datetime.strptime(sys.argv[2], "%m/%d/%y")
  dt = dt.replace(hour=MORNING_HOUR, minute=0, second=0, microsecond=0)
elif when == "test":
  dt = datetime.datetime.today()
  dt = dt.replace(second=0, microsecond=0)
  dt = dt + datetime.timedelta(minutes=5)
else:
  raise ValueError("Invalid script argument")

until = dt.strftime("%a %b %-d %-I %p")
dt = dt.astimezone(datetime.timezone.utc)
dts = dt.strftime("%Y-%m-%d %H:%M:%S")

out = '''
{ actions = (
	{
		type = "changeHeaders";
		headers = { 
		  "x-snooze" = "%s"; 
		};
	},
  {
    type = "notify";
    formatString = "Snoozed until %s";
  },
  {
    type = "moveMessage";
    mailbox = "/Later";
  },
  {
    type    = "changeFlags";
    enable  = ( "\\Seen", "\\$NotJunk" );
    disable = ( "\\$Junk", "\\Junk" );
  },
); }
''' % (dts, until)
print (out)

