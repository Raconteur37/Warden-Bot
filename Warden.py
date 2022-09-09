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

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!"}

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


# @client.command()
# @has_permissions(manage_messages = True) 
# async def chatchecker(ctx):
#     print("Starting")
#     global chatChannels
#     for z in chatChannels:
#         global msgStringCache
#         channel = client.get_channel(z) #This is the general channel, when we check other channels I can create a sorting algorithm for multiple ones and substitute
#         c.execute('SELECT * FROM wardenMoniter WHERE general = general')
#         startMsg = c.fetchall()
#         startMsg = startMsg[0]
#         startMsg = str(startMsg)
#         startMsg = cleanDbTable(startMsg)
#         startMsg = datetime.datetime.strptime(startMsg, '%Y-%m-%d %H:%M:%S.%f')
#         messages = await channel.history(after=startMsg).flatten()
#         finalMsg = (messages[len(messages) - 1])
#         finalMsgTime = finalMsg.created_at
#         for a in messages:
#             if (a.author.bot != True):
#                 senderId = a.author.id
#                 senderName = str(a.author)
#                 senderName = senderName.replace(" ","")
#                 senderMsg = a.content
#                 senderTime = a.created_at
#                 senderSeconds = float(senderTime.timestamp())
#                 senderTime = float(senderSeconds)
#                 strMsgData = senderName + ":" + str(senderTime) + ":" + str(senderId) + ":" + "1"
#                 for b in msgStringCache:
#                     if (b != strMsgData or msgStringCache == []):
#                         strMsgData = senderName + ":" + str(senderTime) + ":" + str(senderId) + ":" + "1"
#                         msgStringCache.append(strMsgData)
#                 x = 0
#                 print(msgStringCache)
#                 while x < len(msgStringCache):
#                     scan = msgStringCache[x].split(":")
#                     scanName = scan[0]
#                     if (str(scanName) == str(senderName)):
#                         senderData = msgStringCache[x]
#                         x = len(msgStringCache)
#                     else:
#                         x = x + 1
#                 args = senderData.split(":")
#                 senderTimeDb = float(args[1])
#                 senderIdDb = int(args[2])
#                 senderPointsDb = int(args[3])
#                 if (len(senderMsg) > 1):
#                     if (senderTime - senderTimeDb > 2.5 or senderTimeDb == 0):
#                         senderPointsDb = senderPointsDb + 1
#                     senderTimeDb = senderTime
#                 x = 0
#                 while x < len(msgStringCache):
#                     scan = msgStringCache[x].split(":")
#                     scanName = scan[0]
#                     if (str(scanName) == str(senderName)):
#                         strMsgData = str(senderName) + ":" + str(senderTimeDb) + ":" + str(senderId) + ":" + str(senderPointsDb)
#                         msgStringCache[x] = strMsgData
#                         x = len(msgStringCache)
#                     else:
#                         x = x + 1
#                 for x in msgStringCache:
#                     args = x.split(":")
#                     vicName = args[0]
#                     vicId = args[2]
#                     validMsg = args[3]
#                     vicId = int(vicId)
#                     validMsg = int(validMsg)
#                     rewardGems(vicId, validMsg, vicName)
#     msgStringCache.clear()
#     clearMsgDb()
#     generalLastMsg(finalMsgTime)    
#     print("Finished Algorithm")

# def clearMsgDb():
#     with conn:
#         c.execute('DELETE FROM wardenMessages')
#     print("Cleared wardenMessages db")

# def rewardGems(id, msgs, name):
#         gemsAdd = 0
#         b = 0
#         msgCount = msgs
#         while b < 1:
#             if (msgCount >= 3):
#                 gemsAdd += .2
#                 msgCount = msgCount - 3
#             if (msgCount == 0):
#                 b = 1
#             if (msgCount <= 2):
#                 gemsAdd += .1
#                 msgCount = msgCount - 2
#                 b = 1
#         round(gemsAdd)
#         c.execute('SELECT * FROM warden WHERE id IN (SELECT id FROM warden WHERE id = ?)', (id,))
#         testId = c.fetchall()
#         if (testId == []):
#             c.execute("INSERT INTO warden VALUES (:id, :name, :gems)", {'id': id, 'name': name, 'gems': 0})
#             print("Addition Successful")       
#         with conn:
#             c.execute(
#             'UPDATE warden SET gems = gems + ? WHERE id=?', 
#             (round(gemsAdd), id,))

# def generalLastMsg(time):
#     with conn:
#         c.execute(
#         'UPDATE wardenMoniter SET general = ?',
#         (time,)) 
#         print("Updated general final time.") 

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