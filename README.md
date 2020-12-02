# BigBot
BigBot is a discord selfbot made using python

# Notes:
You need to have python and discord.py installed to use this
Get:
Python 3.7 - 3.7.9
Discord.py
To install discord.py, get python, install it, and then type in the command prompt "pip install discord.py"

# What is this?
Discord selfbots are kind of like normal discord bots, that
perform actions when given commands, but this does it on
a user account. This can help you do cool stuff like
send embed messages, send messages that ping people without
a ping, and other cool stuff.

# Is this safe?
The software itself is safe, I have all the code on here after all
for anyone to review. However, selfbots are against discord TOS so
use this carefully. I reccomend only showing friends you trust and 
not using this in public servers.


# Commands:

The prefix is ">"

>help - Prints commands to the console

>embed "title" "desc" "footer" - Sends an embed message with those arguments (must be in quotes)

>hide "visible text" "hidden ping/invite" - The visible is what the message looks like, the hidden is a ping or invite that will show despite not being an invite link or ping visible to the reader

>dnd on "default reply to all dms" - Replies to all dm messages with what you tell it to

>dnd off - Turns off do not disturb

>status dnd - Checks if do not disturb is on

>wipe - Deletes all channels (Requires confirmation in the console)

>nitro - Sends a random nitro code

>nitrogen "amount" - Generates an amount of random codes to a file and sends it

>status nitrogen - Checks if nitrogen is generating

(Note: For a better more in depth nitro generator, see my other project: https://github.com/BigweldIndustries/Nitrogen)

# Why is this actually so terrible
This is an alpha version, of course it is terrible. Heres a tip:
If you hate entering the token each time, just open the file and change 
TOKEN = input("something something")
to
TOKEN = "PUT YOUR TOKEN IN HERE"

# I need help...
Just create an issue on this repository

# TODO
- Fix that bug where you need a second argument in >dnd off
