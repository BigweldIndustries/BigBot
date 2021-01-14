import msvcrt
import ctypes
import os
if os.name == 'nt':

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
hide_cursor()
#Logo
print("██████╗ ██╗ ██████╗ ██████╗  ██████╗ ████████╗")
print("██╔══██╗██║██╔════╝ ██╔══██╗██╔═══██╗╚══██╔══╝")
print("██████╔╝██║██║  ███╗██████╔╝██║   ██║   ██║   ")
print("██╔══██╗██║██║   ██║██╔══██╗██║   ██║   ██║   ")
print("██████╔╝██║╚██████╔╝██████╔╝╚██████╔╝   ██║   ")
print("╚═════╝ ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ")
import colorama
from colorama import init
from colorama import Fore, Back, Style
colorama.init()
print(Fore.GREEN+"V. 1.5.0\nCreated by Bigweld Industries | Bigweld.xyz"+Style.RESET_ALL)
#Import
print("Importing discord.py and stuff...")
print("________________________________________________")
import sys
print(Fore.RED+"[>] Imported sys")
import time
print(Fore.RED+"[>] Imported time")
import random
print(Fore.RED+"[>] Imported random")
import pyfiglet
print(Fore.RED+"[>] Imported pyfiglet")
import string
print(Fore.YELLOW+"[>] Imported string")
import re
print(Fore.YELLOW+"[>] Imported re")
import httpx
print(Fore.YELLOW+"[>] Imported httpx")
import asyncio
print(Fore.YELLOW+"[>] Imported asyncio")
import json
print(Fore.GREEN+"[>] Imported json")
import csv
print(Fore.GREEN+"[>] Imported csv")
from youtubesearchpython import SearchVideos
print(Fore.GREEN+"[>] Imported YT Search")
import discord
from discord import Color
print(Fore.GREEN+"[>] Imported discord")
from discord.ext import commands
from discord.ext.commands import Bot
print(Fore.GREEN+"[>] Imported discord.ext stuff")
print(Style.RESET_ALL+"________________________________________________")

#Set important variables

#Initializes custom commands
commanddict = {}
csvpath = os.path.expandvars(r'%LOCALAPPDATA%\BigBot\commands.csv')
try:
    csvthing = open(csvpath, 'w+')
    reader = csv.reader(csvthing)
    for row in reader: 
	    if row != "": 
		    k, v = row 
		    commanddict[k] = v
except:
    os.mkdir(csvpath.rstrip('commands.csv'))
    open(csvpath, 'x')
    commanddict["example command"] = "hey! this is a message!"
    with open(csvpath, 'w') as f:
        for key in commanddict.keys():
            f.write("%s,%s\n"%(key,commanddict[key]))
print(Fore.GREEN+"[>] Custom commands loaded!"+Style.RESET_ALL)

#Login token
show_cursor()
TOKEN = input("Please input your user token: ")
hide_cursor()


#Used in hide command
crazytext = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

#If dnd is on
donotdisturb = False

#The dnd message
reply = ""

#Used in nitrogen
status = "Finished"

#Nitrosnipe
nitrosnipestatus = False
codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")

print(Fore.YELLOW+"[>] Logging in...", end="\r")
intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix='>', help_command=None, self_bot=True, intents=intents)

#Print when bot is  logged in
@bot.event
async def on_ready():
    print(Fore.GREEN+f'[>] Logged in as {bot.user}!')
    print(Style.RESET_ALL)
    show_cursor()
    clear = input("Now that you are logged in, should we clear the console so you don't accidentally show your token? (y or n): ")
    hide_cursor()
    if clear == "y":
        clear = lambda: os.system('cls')
        clear()
        print(Fore.GREEN+f"Console cleared, logged in as {bot.user}")
    else:
        print(Fore.YELLOW+"Console not cleared")
    print(Fore.GREEN + "Type >help in discord for commands!")
    print(Fore.RESET)

#Add command
@bot.command()
async def add(ctx, arg1, arg2):
    global commanddict
    name = arg1
    returns = arg2
    await ctx.message.delete()
    commanddict[arg1] = arg2
    print(Fore.GREEN + f'[>] Command "{name}" added!' + Style.RESET_ALL)
    with open(csvpath, 'w') as f:
        for key in commanddict.keys():
            f.write("%s,%s\n"%(key,commanddict[key]))

#Poll command
@bot.command()
async def poll(ctx, col, arg2):
    try:
        if col == "red":
            embedcolor = Color.red()
        if col == "orange":
            embedcolor = Color.orange()
        if col == "yellow":
            embedcolor = Color.yellow()
        if col == "green":
            embedcolor = Color.green()
        if col == "blue":
            embedcolor = Color.blue()
        if col == "purple":
            embedcolor = Color.purple()
        if col == "black":
            embedcolor = Color.black()
        if col == "none":
            embedcolor = Color.default()
        embed=discord.Embed(title="POLL:", description=arg2, color=embedcolor)
        embed.set_footer(text="Vote by reacting")
        embedmsg = await ctx.send(embed=embed)
        await ctx.message.delete()
        await embedmsg.add_reaction("👍")
        await embedmsg.add_reaction("👎")
        print(Fore.GREEN+f'[>] Poll "{arg2}" sent!')
    except:
        print(Fore.RED+"[>] Poll failed")
    print(Fore.RESET)

#Spam command
@bot.command()
async def spam(ctx, arg1, arg2):
    try:
        amount = arg1
        msg = arg2
        await ctx.message.delete()
        for _ in range(int(amount)):
            await ctx.send(msg)
        print(Fore.GREEN+f'[>] Successfully spammed "{msg}" {amount} times')
    except:
        print(Fore.RED+"[>] Spamming failed")
    print(Fore.RESET)

#Ascii command
@bot.command()
async def ascii(ctx, arg):
    await ctx.message.delete()
    try:
        text = pyfiglet.figlet_format(arg)
        await ctx.send(f"```{text}```")
        print(Fore.GREEN+f'[>] Successfully sent ascii "{arg}"')
    except:
        print(Fore.RED+"[>] Ascii failed")

#Embed command
@bot.command()
async def embed(ctx, col, arg1, arg2, arg3):
    try:
        if col == "red":
            embedcolor = Color.red()
        if col == "orange":
            embedcolor = Color.orange()
        if col == "yellow":
            embedcolor = Color.yellow()
        if col == "green":
            embedcolor = Color.green()
        if col == "blue":
            embedcolor = Color.blue()
        if col == "purple":
            embedcolor = Color.purple()
        if col == "black":
            embedcolor = Color.black()
        if col == "none":
            embedcolor = "none"
        if embedcolor == "none":
            embed=discord.Embed(title=arg1, description=arg2)
            embed.set_footer(text=arg3)
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if embedcolor != "none":
            embed=discord.Embed(title=arg1, description=arg2, color=embedcolor)
            embed.set_footer(text=arg3)
            await ctx.send(embed=embed)
            await ctx.message.delete()
    except:
        print(Fore.RED+"[>] Failed to send embed")

#Hide command
@bot.command()
async def hide(ctx, arg1, arg2):
    await ctx.send(arg1+crazytext+arg2)
    await ctx.message.delete()

#YT Search command
@bot.command()
async def yt(ctx, arg1):
    vid = arg1
    await ctx.message.delete()
    search = SearchVideos(vid, offset = 1, mode = "dict", max_results = 1)
    end = search.result()
    await ctx.send(end["search_result"][0]["link"])

#Do not disturb
@bot.command()
async def dnd(ctx, arg1,arg2=""):
    global donotdisturb
    global reply
    if arg1 == "on" or arg1 == "On":
        reply = arg2
        donotdisturb = True
        await ctx.message.delete()
    elif arg1 == "off" or arg1 == "Off":
        donotdisturb = False
        reply = ""
        await ctx.message.delete()

#secret command
@bot.command()
async def beatthesoapinhishand(ctx):
    await ctx.message.delete()
    await ctx.send("https://www.youtube.com/watch?v=bJMXliokGrY")

#Multipurpose status
@bot.command()
async def status(ctx, arg):
    global donotdisturb
    global status
    global nitrosnipestatus
    thing = arg
    await ctx.message.delete()
    if thing == "dnd":
        statusmsg = await ctx.send(str(donotdisturb))
        time.sleep(2)
        await statusmsg.delete()
    if thing == "nitrogen":
        statusmsg = await ctx.send(status)
        time.sleep(2)
        await statusmsg.delete()
    if thing == "nitrosnipe":
        statusmsg = await ctx.send(str(nitrosnipestatus))
        time.sleep(2)
        await statusmsg.delete()

#Nitrosnipe command
@bot.command()
async def nitrosnipe(ctx, arg):
    global nitrosnipestatus
    thing = arg
    await ctx.message.delete()
    if thing == "on":
        nitrosnipestatus = True
    if thing == "off":
        nitrosnipestatus = False

#Help command
@bot.command()
async def help(ctx):
    global commanddict
    await ctx.message.delete()
    print("")
    print(Fore.GREEN+"Bigbot commands:"+Style.RESET_ALL)
    print('>help')
    print('>add "command name" "command message"')
    print('>embed color "title" "desc" "footer"    (Colors are red, orange, yellow, green, blue, purple, black, none)')
    print('>hide "visible text" "hidden ping/invite"')
    print('>dnd on "default reply to all dms"')
    print('>dnd off')
    print('>status dnd')
    print('>yt "video name"')
    print('>poll color "poll contents"')
    print('>spam 5 "message"')
    print('>nitro')
    print('>nitrogen "amount"')
    print('>status nitrogen')
    print('>nitrosnipe')
    print('>status nitrosnipe')
    print('>coolorcringe')
    print("")
    print(Fore.GREEN+"Custom commands:"+Style.RESET_ALL)
    for key in commanddict:
        print(key + " - " + commanddict[key])
#Cool or Cringe command
@bot.command()
async def coolorcringe(ctx):
    await ctx.message.delete()
    coolorcringelist = ["cool", "cringe"]
    result = random.choice(coolorcringelist)
    await ctx.send(result)

#Nitro command
@bot.command()
async def nitro(ctx):
    await ctx.message.delete()
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    nitrocode = "https://discord.gift/" + code
    await ctx.send("**Random nitro code:**" + "\n" + nitrocode)

#Nitrogen command
@bot.command()
async def nitrogen(ctx, arg):
    global status
    amount = int(arg)
    await ctx.message.delete()
    nitrocodes = ""
    print(Fore.YELLOW + f"[>] Generating {arg} nitro codes...")
    for i in range(0,amount):
        code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        nitrocode = "https://discord.gift/" + code + "\n"
        nitrocodes += nitrocode
        status = "Generating..."
    print(Fore.GREEN + f"[>] Generated")
    myfile = open("codes.txt","w+")
    myfile.write("CODES: " + "\n")
    myfile.close()
    myfile2=open("codes.txt", "a+")
    myfile2.write(nitrocodes)
    myfile2.close
    endfile=discord.File("codes.txt")
    await ctx.send(file=endfile)
    print(Fore.GREEN + f"[>] Sent")
    status = "Finished"
    endfile.close()
    f = open('codes.txt', 'r+')
    f.truncate(0)
    f.close()

#On message
@bot.event
async def on_message(message):
    global donotdisturb
    global nitrosnipestatus
    global commanddict
    if nitrosnipestatus == True:
        if codeRegex.search(message.content):
            code = codeRegex.search(message.content).group(2)
            start_time = time.time()
            async with httpx.AsyncClient() as client:
                result = await client.post(
                'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                json={'channel_id': str(message.channel.id)},
                headers={'authorization': TOKEN, 'user-agent': 'Mozilla/5.0'})
                delay = (time.time() - start_time)
                if 'This gift has been redeemed already' in str(result.content):
                    print(Fore.YELLOW+f"[>] We found a code but it was redeemed already ({code}, delay of {delay})")
                elif 'nitro' in str(result.content):
                    print(Fore.GREEN+f"[>] We found a code and claimed it! ({code}, delay of {delay})")
                elif 'Unknown Gift Code' in str(result.content):
                    print(Fore.RED+f"[>] We found a code but it was invalid ({code}, delay of {delay})")
    for key in commanddict:
        if message.content == key:
            await message.delete()
            await message.channel.send(commanddict[key])
    if donotdisturb == True:
        global reply
        if message.author != bot.user:
            if not message.guild:
                await message.channel.send(reply)
    await bot.process_commands(message)

#Run bot
try:
    bot.run(TOKEN, bot=False)
except:
    print(Style.RESET_ALL)
    print("It appears we could not login...")
    print("Make sure your token does not have quotes around it, and you are connected to the internet")
    finalpass = input("Press enter to close...")
    sys.exit()
