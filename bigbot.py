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
#Import
print("Importing discord.py and stuff...")
print("________________________________________________")
import os
print(Fore.RED+"Imported os")
import time
print(Fore.RED+"Imported time")
import random
print(Fore.RED+"Imported random")
import string
print(Fore.YELLOW+"Imported string")
import re
print(Fore.YELLOW+"Imported re")
import httpx
print(Fore.YELLOW+"Imported httpx")
import asyncio
print(Fore.GREEN+"Imported asyncio")
import json
print(Fore.GREEN+"Imported json")
import discord
print(Fore.GREEN+"Imported discord")
from discord.ext import commands
from discord.ext.commands import Bot
print(Fore.GREEN+"Imported discord.ext stuff")
print(Style.RESET_ALL+"________________________________________________")

#Set important variables

#Login token
TOKEN = input("Please input your user token: ")
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

print(Fore.YELLOW+"Logging in...")
bot = commands.Bot(command_prefix='>', help_command=None, self_bot=True)

#Print when bot is  logged in
@bot.event
async def on_ready():
    print(Fore.GREEN+f'Logged in as {bot.user}!')
    print(Style.RESET_ALL)
    clear = input("Now that you are logged in, should we clear the console so you don't accidentally show your token? (y or n): ")
    if clear == "y":
        clear = lambda: os.system('cls')
        clear()
        print(Fore.GREEN+f"Console cleared, logged in as {bot.user}")
    else:
        print(Fore.YELLOW+"Console not cleared")


#Embed command
@bot.command()
async def embed(ctx, arg1, arg2, arg3):
    embed=discord.Embed(title=arg1, description=arg2, color=0x002dff)
    embed.set_footer(text=arg3)
    await ctx.send(embed=embed)
    await ctx.message.delete()

#Hide command
@bot.command()
async def hide(ctx, arg1, arg2):
    await ctx.send(arg1+crazytext+arg2)
    await ctx.message.delete()

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
    await ctx.message.delete()
    print(Fore.GREEN+"Bigbot commands:")
    print(Style.RESET_ALL)
    print('>help')
    print('>embed "title" "desc" "footer"')
    print('>hide "visible text" "hidden ping/invite"')
    print('>dnd on "default reply to all dms"')
    print('>dnd off')
    print('>status dnd')
    print('>wipe')
    print('>nitro')
    print('>nitrogen "amount"')
    print('>status nitrogen')
    print('>nitrosnipe')
    print('>status nitrosnipe')


#Wipe command
@bot.command()
async def wipe(ctx):
    await ctx.message.delete()
    wipeinput = input(Fore.RED+"Are you sure you want to destroy every channel in this server? (WARNING: This happens really fast so it will probably flag your account)(y or n): ")
    if wipeinput == "y" or wipeinput == "Y":
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        print(Fore.GREEN+"Wiped")

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
    for i in range(0,amount):
        code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        nitrocode = "https://discord.gift/" + code + "\n"
        nitrocodes += nitrocode
        status = "Generating..."
    myfile = open("codes.txt","w+")
    myfile.write("CODES: " + "\n")
    myfile.close()
    myfile2=open("codes.txt", "a+")
    myfile2.write(nitrocodes)
    myfile2.close
    endfile=discord.File("codes.txt")
    await ctx.send(file=endfile)
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
                    print(Fore.YELLOW+f"We found a code but it was redeemed already ({code})")
                elif 'nitro' in str(result.content):
                    print(Fore.GREEN+f"We found a code and claimed it! ({code})")
                elif 'Unknown Gift Code' in str(result.content):
                    print(Fore.RED+f"We found a code but it was invalid ({code})")
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
    print("It appears we could not login, make sure your token does not have quotes around it, and you are connected to the internet")
    finalpass = input("Press enter to close...")
    if finalpass=="":
        sys.exit()
