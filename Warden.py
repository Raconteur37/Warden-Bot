import asyncio
import os
import json
import discord
# python3 -m pip install (package).py fixes many problems
import time
import datetime
from discord import message
from discord import user
from discord import channel
from discord.client import Client
from discord.enums import SpeakingState  
from discord.ext import commands
import sqlite3
import random
from time import sleep
from discord.ext import tasks, commands
from discord.utils import get

from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import bot
from discord.webhook import AsyncWebhookAdapter

import Commands as commands

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": ">"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]

client = commands.Bot(prefix)

conn = sqlite3.connect('warden.db')
c = conn.cursor()

#.execute(""" CREATE TABLE IF NOT EXISTS wardenMessages (
#    id integer,
#    name text,
#    msg text,
#    time integer)""")

#c.execute(""" CREATE TABLE IF NOT EXISTS warden (
#        id integer,
#        name text,
#        gems integer)""")

#c.execute(""" CREATE TABLE IF NOT EXISTS wardenMoniter ( edtrhg

commands.

@client.event
async def on_ready():
    activity = discord.Activity(name=" channels...", type=3)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    # await guessWordGame.start()
    print('Bot is now online')

    #
    # Commands
    #

# TODO make it so all command add you to the data base and still have propper function if said person isnt in it already

# Adds one gem and adds player to db if they are not there


@client.command(name='online')
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


@client.command()
@has_permissions(manage_messages=True)
async def shop(ctx):
    # String will be pulled from db and determine the items that rotate 
    await ctx.send("""
                        ```   𝐈𝐭𝐞𝐦:              𝐂𝐨𝐬𝐭: 
""" + "- Kitpvp Cash" + "      "  + "20 Gems per $" 
    +  '\n' + " - VIP Role" + "      "  + "50,000 Gems"
    +  '\n' + " - Warden Tag" + "      "  + "25,000 Gems"  +  """```""")



@client.event
async def on_command_error(msg, error):
    await msg.channel.send(str(error))

# chatchecker()
client.run(token)