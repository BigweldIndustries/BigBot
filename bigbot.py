#Logo
print("██████╗ ██╗ ██████╗ ██████╗  ██████╗ ████████╗")
print("██╔══██╗██║██╔════╝ ██╔══██╗██╔═══██╗╚══██╔══╝")
print("██████╔╝██║██║  ███╗██████╔╝██║   ██║   ██║   ")
print("██╔══██╗██║██║   ██║██╔══██╗██║   ██║   ██║   ")
print("██████╔╝██║╚██████╔╝██████╔╝╚██████╔╝   ██║   ")
print("╚═════╝ ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ")

#Import
print("Importing discord.py and stuff...")
print("________________________________________________")
import os
print("Imported os")
import time
print("Imported time")
import random
print("Imported random")
import string
print("Imported string")
import discord
print("Imported discord")
from discord.ext import commands
from discord.ext.commands import Bot
print("Imported discord.ext stuff")
print("________________________________________________")

#Set important variables
TOKEN = input("Please input your user token: ")
crazytext = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
donotdisturb = False
reply = ""
status = "Finished"

print("Logging in...")
bot = commands.Bot(command_prefix='>', help_command=None, self_bot=True)

#Print when bot is  logged in
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

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
    elif arg1 == "status" or arg1 == "Status":
        await ctx.message.delete()
        statusmsg = await ctx.send(str(donotdisturb))
        time.sleep(2)
        await statusmsg.delete()


#Help command
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    print("Bigbot commands:")
    print('>help')
    print('>embed "title" "desc" "footer"')
    print('>hide "visible text" "hidden ping/invite"')
    print('>dnd status')
    print('>dnd on "default reply to all dms"')
    print('>dnd off')
    print('>wipe')
    print('>nitro')
    print('>nitrogen "amount"')
    print('>nitrogenstatus')


#Wipe command
@bot.command()
async def wipe(ctx):
    await ctx.message.delete()
    wipeinput = input("Are you sure you want to destroy every channel in this server? (WARNING: This happens really fast so it will probably flag your account)(y or n): ")
    if wipeinput == "y" or wipeinput == "Y":
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        print("Wiped")

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
    working = False
    while working == False:
        try:
            os.remove("codes.txt")
            working = True
            print("Deleted")
        except:
            print("Trying to delete...")

#Nitrogen status command
@bot.command()
async def nitrogenstatus(ctx):
    global status
    await ctx.send(status)

#On message
@bot.event
async def on_message(message):
    global donotdisturb
    if donotdisturb == True:
        global reply
        if message.author != bot.user:
            if not message.guild:
                await message.channel.send(reply)
    await bot.process_commands(message)

#Run bot
bot.run(TOKEN, bot=False)
