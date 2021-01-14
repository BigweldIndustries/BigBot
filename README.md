# BigBot
BigBot is a discord selfbot made using python. It can send invisible pings, autoclaim nitro, send yt videos just from titles and more. Can be set up with no experience nearly instantly 

[1.3 Demo](https://www.youtube.com/watch?v=1XmJ9mzRdSQ)  
[Invisible ping showcase](https://www.youtube.com/watch?v=Jvpc7f-cE_k)  
[Raiding showcase](https://www.youtube.com/watch?v=7LZnb59OzjI)  

# How to download/setup
Go to [releases](https://github.com/BigweldIndustries/BigBot/releases) and click on the latest one.
Typically though, the exe build may be just a bit behind the python file, so scroll down if you are
experienced enough to mess with that. To get your user token, look at the catagory below.

# How do I get my token?
<img src="assets/howtogettoken.gif" width="1000">

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
not using this in public servers. If you are wary about the software however,
simply instead of downloading the release do this:

# Build from scratch:
You need to have python and some modules installed to use this

Get:
Python 3.7 - 3.7.9

Discord.py

httpx

colorama

To install python ->>>>> https://www.python.org/downloads/release/python-379/

To install discord.py, get python, install it, and then type in the command prompt "pip install discord.py"

To install httpx, get python, install it, and then type in the command prompt "pip install httpx"

To install colorama, get python, install it, and then type in the command prompt "pip install colorama"

there are also like 2 more, but if you're going to bother doing this, you can figure it out


# Commands:

The prefix is ">"

>help - Prints commands to the console

>add "command name" "command message" - Add your own command that sends a custom message when you call it! (This will store in a csv file which can be used next time you launch)

>embed color "title" "desc" "footer" - Sends an embed message with those arguments (must be in quotes), Colors are red, orange, yellow, green, blue, purple, black, none

>hide "visible text" "hidden ping/invite" - The visible is what the message looks like, the hidden is a ping or invite that will show despite not being an invite link or ping visible to the reader. (Include quotes)

>dnd on "default reply to all dms" - Replies to all dm messages with what you tell it to (Include quotes)

>dnd off - Turns off do not disturb

>status dnd - Checks if do not disturb is on

>yt "video name" - Sends the first result for those youtube search terms in chat

>poll color "poll contents" - Sends a poll with reactions set up, in a fancy embed format. Colors are red, orange, yellow, green, blue, purple, black, none

>spam 5 "message" - Spams a message a certain number of times

>massdm "message" - DM's everyone in the server (You must own the server)

>nitro - Sends a random nitro code

>nitrogen "amount" - Generates an amount of random codes to a file and sends it

>status nitrogen - Checks if nitrogen is generating

>nitrosnipe on - Turns on a nitrosniper that automatically claims codes sent in servers

>nitrosnipe off - Turns off nitrosnipe

>status nitrosnipe - Checks if nitrosnipe is on

>coolorcringe - Randomly picks from either "cool" or "cringe"

(Note: For a better more in depth nitro generator, see my other project: https://github.com/BigweldIndustries/Nitrogen)

# Why is this actually so terrible
This is an alpha version, of course it is terrible. Heres a tip:
If you hate entering the token each time, download the "one-time-token" branch, and you only enter it once. This is not the main branch for security reasons. (Note: It is like 5 updates behind and really bad)

# I need help...
Just create an issue on this repository

# TODO
- update releases when big update comes out
