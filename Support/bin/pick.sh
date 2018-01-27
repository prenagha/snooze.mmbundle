#!/bin/bash

DEF=`date -v+1d "+%m/%d/%Y"`
osascript <<END
tell application "System Events"
	activate
	set theDate to the text returned of (display dialog "Snooze until mm/dd/yy?" default answer "${DEF}" with title "Snooze Message -- Pick Date" buttons {"Snooze"} default button 1)
	return theDate
end tell
END