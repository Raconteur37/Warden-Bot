import asyncio
import os
import json
import discord
# python3 -m pip install (package).py fixes many problems
import sqlite3
from discord.ext import commands


if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]

intents = discord.Intents.all()
intents.all()

activity = discord.Activity(name=" channels...", type=3)
bot = commands.Bot(command_prefix='>',activity=activity,intents=intents)


conn = sqlite3.connect('warden.db')
c = conn.cursor()


@bot.event
async def on_ready():
    print(f'Warden is now online')


    #
    # Commands 
    #
    
    #TODO Check if any command is typed or just the prefix then access the commands class to 
    
@bot.command(name='ping') 
async def ping(ctx):
    await ctx.send("pong")
    
 



# TODO make it so all command add you to the data base and still have propper function if said person isnt in it already

# Adds one gem and adds player to db if they are not there


@bot.command(name='online')
async def ping_server_command(msg):

    hostname = "mtl.renatusnetwork.com"
    response = os.system("ping " + hostname)

    if (response == 0):
        embed = discord.Embed(color=0x31EF31)
        embed.title="Renatus Network"
        embed.description="Server is Online!"
        await msg.channel.send(embed=embed)
    else:
        embed = discord.Embed(color=0xE51A1A)
        embed.title="Renatus Network"
        embed.description="Server is Offline!"
        await msg.channel.send(embed=embed)


# CTRL + K then CTRL + C to mass comment


@bot.command()
async def shop(ctx):
    # String will be pulled from db and determine the items that rotate 
    await ctx.send("""
                        ```   𝐈𝐭𝐞𝐦:              𝐂𝐨𝐬𝐭: 
""" + "- Kitpvp Cash" + "      "  + "20 Gems per $" 
    +  '\n' + " - VIP Role" + "      "  + "50,000 Gems"
    +  '\n' + " - Warden Tag" + "      "  + "25,000 Gems"  +  """```""")



@bot.event
async def on_command_error(msg, error):
    await msg.channel.send(str(error))

# chatchecker()
bot.run(token)
