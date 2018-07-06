# snooze.mmbundle
MailMate Bundle to implement message snooze. Similar to the feature used in many mail clients today. I like the [Spark](https://sparkmailapp.com) implementation and used it as a guide for this bundle.

Snoozing a message does the following:
* Add a `x-snooze` header to the message with the wake-up date
* Move the message to the `Later` folder
* Mark the message as Seen and Not Junk

Make sure you have a `Later` folder in all your IMAP accounts.

Make sure you have `python3` installed, [http://docs.python-guide.org/en/latest/starting/install3/osx/](http://docs.python-guide.org/en/latest/starting/install3/osx/)

You need the latest BETA of MailMate, which has special `x-snooze` header support built-in.

Message wake-up by appearing in a Smart Mailbox when they awake.
To achieve this create a Smart Mailbox, Snooze:
* Source the `Later` folder in each IMAP account
* Set the mailbox condition to `Any` of
    * `x-snooze is not within last 0 days`
    * `x-snooze does not exist`
    * `date is not within last 32 days`
* Set the Displayed Count on the mailbox to `All`

I use the display count on the Snooze mailbox as the indication something has woken-up. You could also set a rule on the Snooze mailbox and move messages to the Inbox when they wake-up.
