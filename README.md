# snooze.mmbundle
MailMate Bundle to implement message snooze. Similar to the feature used in many mail clients today. I like the [Spark](https://sparkmailapp.com) implementation and have used is as a guide for this bundle.

Snoozing a message does the following:
* Add a `X-Snooze` header to the message with the wake-up date
* Move the message to the `Later` folder
* Mark the message as Seen and Not Junk

Make sure you have a `Later` folder in all your IMAP accounts.

Message wake-up by appearing in a Smart Mailbox when they awake.
To achieve this create a Smart Mailbox:
* Source the `Later` folder in each IMAP account
* Set the mailbox condition to `X-Snooze is not within last 0 days`
* Set the Displayed Count on the mailbox to `All`

Date calculations use the Mac's [command line date function](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/date.1.html)
