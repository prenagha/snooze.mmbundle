#!/bin/bash

cat << ENDACTIONS
{ actions = (
	{
		type = changeHeaders;
		headers = { 
		  "Date"     = "Mon, 1 Jan 2018 10:00:00 -0500"; 
		  "X-Snooze" = "Mon, 1 Jan 2018 10:00:00 -0500"; 
		};
	}
); }
ENDACTIONS
