#!/bin/bash

#
# Test snoozing, forcing to a date
#

cat << ENDACTIONS
{ actions = (
	{
		type = "changeHeaders";
		headers = { 
		  "x-snooze" = "Sun, 01 Jul 2018 09:00:00 +0000"; 
		};
	},
  {
    type = "notify";
    formatString = "Test snoozed to Jul 1";
  },
  {
    type = "moveMessage";
    mailbox = "/Later";
  },
  {
    type    = "changeFlags";
    enable  = ( "\\Seen", "\\\$NotJunk" );
    disable = ( "\\\$Junk", "\\Junk" );
  },
); }
ENDACTIONS
