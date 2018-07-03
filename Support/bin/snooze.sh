#!/bin/bash

#
# Snooze the message until a future date
# Move the message to the /Later folder
# Mark the message as Seen and Not Junk
# https://www.mail-archive.com/mailmate@lists.freron.com/msg05451.html
#

TM="-v0M -v0S"
if [ -z "$PICK" ]
then
  DTS=`date -R $* $TM`
  UNTIL=`date $* $TM "+%a %b %-d %-I%p"`
else
  DTS=`date $TM -jf "%m/%d/%y" ${PICK}`
  UNTIL=`date $TM -jf "%m/%d/%y" ${PICK} "+%a %b %-d %-I%p"`
fi

cat << ENDACTIONS
{ actions = (
	{
		type = "changeHeaders";
		headers = { 
		  "x-snooze" = "$DTS"; 
		};
	},
  {
    type = "notify";
    formatString = "Snoozed until $UNTIL";
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
