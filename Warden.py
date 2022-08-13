import asyncio
from asyncio.windows_events import NULL
import os
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

token = 'Njc5ODEyNzg2MjAwNTEwNTgz.Xk2y_g.LjHx-ULuYetXc0hObBe7Pp1Ca64'

client = commands.Bot('>')

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

#c.execute(""" CREATE TABLE IF NOT EXISTS wardenMoniter (
#        general integer)""")

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


@client.command(name='purge', aliases=['clear'])
@commands.has_permissions(manage_messages=True)
async def purge_chat_command(msg: discord.Message, arg):

    amount = await msg.channel.purge(limit=int(arg) + 1)
    date = datetime.datetime.now()
    amountDeleted = format(len(amount) - 1)
    sentMessage = await msg.channel.send("Purged " + str(amountDeleted) + " messages @ " + str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" + str(date.minute))
    messageId = sentMessage.id
    messageToDelete = await msg.channel.fetch_message(messageId)
    time.sleep(5)
    await messageToDelete.delete()

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True) # Change to manage members
async def addVip(ctx, *, user: discord.User):
    member = user
    role = discord.utils.get(member.guild.roles, name="VIP")
    await member.add_roles(role)


@client.command()
@has_permissions(manage_messages=True) # Change to manage members
async def commands(ctx):
    embed=discord.Embed(title="Warden Commands", description="*admins only*", color=0xff0000)
    embed.add_field(name="*>addgems(@, amount)*", value="Adds an amount of @'s gems", inline=True)
    embed.add_field(name=" *>removegems(@, amount)*", value="Removes an amount of @'s gems", inline=True)
    embed.add_field(name="*>setgems(@, amount)*", value="Sets the @'s gem amount", inline=True)
    embed.add_field(name=">gems", value="Says the amount of gems the user has ", inline=True)
    embed.add_field(name="*>clear (amount)*", value="Clears the amount of msgs in chat", inline=True)
    embed.add_field(name="*>addVip (@)*", value="Gives VIP role to the @", inline=True)
    embed.add_field(name="*>roulette*", value="Initate roulette immedietdly", inline=True)
    embed.add_field(name="*>chatchecker*", value="Initiate chat algorithm immedietly ", inline=True)
    embed.add_field(name="*>debug*", value="Senbds debug msg previously editted", inline=True)
    embed.add_field(name=">shop", value="Shows the items in the shop", inline=True)
    embed.add_field(name=">buy (item name)", value="Purchases the item you input", inline=True)
    await ctx.send(embed=embed)


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

# Chat Algorithm
global msgStringCache
msgStringCache = ["warden:1:1:1"] # name:time of msg:id:amount
global chatChannels
chatChannels = [488567034712686602,450120546282242048]#,680997606943621130,602708225263140864] #commands,general,no context quotes,suggestions  


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

def clearMsgDb():
    with conn:
        c.execute('DELETE FROM wardenMessages')
    print("Cleared wardenMessages db")

def rewardGems(id, msgs, name):
        gemsAdd = 0
        b = 0
        msgCount = msgs
        while b < 1:
            if (msgCount >= 3):
                gemsAdd += .2
                msgCount = msgCount - 3
            if (msgCount == 0):
                b = 1
            if (msgCount <= 2):
                gemsAdd += .1
                msgCount = msgCount - 2
                b = 1
        round(gemsAdd)
        c.execute('SELECT * FROM warden WHERE id IN (SELECT id FROM warden WHERE id = ?)', (id,))
        testId = c.fetchall()
        if (testId == []):
            c.execute("INSERT INTO warden VALUES (:id, :name, :gems)", {'id': id, 'name': name, 'gems': 0})
            print("Addition Successful")       
        with conn:
            c.execute(
            'UPDATE warden SET gems = gems + ? WHERE id=?', 
            (round(gemsAdd), id,))

def generalLastMsg(time):
    with conn:
        c.execute(
        'UPDATE wardenMoniter SET general = ?',
        (time,)) 
        print("Updated general final time.") 


    #
    # Games
    #

def hideWord(finalWrd,word):
    x = 0
    while x < 1:
        rand = random.randint(0,len(finalWrd) - 1)
        if finalWrd[rand] == "-":
            finalWrd[rand] = word[rand]
            x == 1
            return finalWrd
        else:
            x == 0


# GAMES
global rouletteBets
rouletteBets = False
global bets
bets = []
global betCheck
betCheck = []

@client.command()
@has_permissions(manage_messages=True)
async def roulette(ctx):
    await client.wait_until_ready()
    channel = client.get_channel(488567034712686602)
    embed=discord.Embed(title="𝐓𝐢𝐦𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐫𝐨𝐮𝐥𝐞𝐭𝐭𝐞, 𝐡𝐞𝐫𝐞 𝐚𝐫𝐞 𝐭𝐡𝐞 𝐧𝐮𝐦𝐛𝐞𝐫𝐬!", description="red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] \n black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35] \n zero = [0]", color=0xff0033)
    embed.set_thumbnail(url="https://www.culturalweekly.com/wp-content/uploads/2020/05/Roulette-wheel-600x350.png")
    embed.set_author(name="Warden Roulette")
    embed.add_field(name="-=𝗟𝗶𝘀𝘁 𝗼𝗳 𝗯𝗲𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀=-", value= " >bet red (amount) \n >bet black (amount) \n >bet even (amount) \n >bet odd (amount) \n >bet zero (amount, 𝔁4 𝓰𝓮𝓶 𝓻𝓮𝔀𝓪𝓻𝓭)", inline=True)
    await ctx.send(embed=embed)
    global rouletteBets
    rouletteBets = True
    await channel.send("Bets close in 30 seconds.")
    await asyncio.sleep(30)
    rouletteBets = False
    winnerString = ""
    loserString = ""
    await channel.send("Bets closed. Starting the roll.") 
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    colorNum = random.randint(0,101)
    color = "white"
    finalNumString = ""
    if (colorNum <= 2): # Color is green and number is 0
        finalNumWord = "zero"
    if (2 < colorNum <= 51): # Color is red
        finalNum = red[random.randint(0,17)]
        color = "red"
    if (51 < colorNum <= 100): # Color is black
        finalNum = black[random.randint(0,17)]
        color = "black"
    if finalNum % 2 == 0:
        finalNumWord = "even"
    else:
        finalNumWord = "odd"
    if finalNum == 0:
        finalNumWord = "zero"
    await channel.send("Brrrrrrr")
    await asyncio.sleep(7)
    await channel.send("Almost there..")
    await asyncio.sleep(6)
    print("Number type is " + finalNumWord)
    print("Color is " + color)
    x = 0
    global bets
    while x < len(bets):
        arg = bets[x]
        args = arg.split(":")
        playerId = args[0]
        player = args[1]
        betType = args[2]
        amount = args[3]
        if betType == color or betType == finalNumWord:
            if betType == "zero":
                amount = int(amount) * 4
                winnerString += "" + str(player) + " " + str(amount) +  "\n "
            else:
                amount = int(amount) * 2
            gemsEdit(playerId, amount, True)
            winnerString += "" + str(player) + " " + str(amount) +  "\n "
        else:
            loserString += "" + str(player) + " " + str(amount) +  "\n "
        x = x + 1
    finalNumString = str(finalNum)
    await channel.send("""```            𝙒𝙖𝙧𝙙𝙚𝙣 𝙍𝙤𝙪𝙡𝙚𝙩𝙩𝙚
    𝐂𝐨𝐥𝐨𝐫 𝐢𝐬 - """  + color + """     𝐍𝐮𝐦𝐛𝐞𝐫 𝐢𝐬 - """ + finalNumString + """```""")
    await channel.send("""
                         ``` 𝗪𝗶𝗻𝗻𝗲𝗿𝘀:        𝗟𝗼𝘀𝗲𝗿𝘀: 
 """ + winnerString + "                "  + loserString +"""```""")
    bets = []
    global betCheck
    betCheck = []
    winnerString = ""
    loserString = ""

@client.command()
async def bet(ctx, *, state):
    if rouletteBets == True:
        for key in betCheck:
            if key == ctx.author.name:
                await ctx.send("You already placed a bet!")
                return
        args = state.split(" ")
        betType = args[0]
        amount = args[1]
        player = ctx.author.name
        vicId = ctx.author.id
        c.execute('SELECT * FROM warden WHERE id IN (SELECT id FROM warden WHERE id = ?)', (vicId,))
        testId = c.fetchall()
        num = getInstanceInTuple(testId, 2)
        num = int(num)
        amount = int(amount)
        if (testId == []):
            await ctx.send("You have no gems!")
            return
        if(num - amount < 0):
            await ctx.send("You dont have enough gems!")
            return
        if betType == "red":
            bets.append(str(vicId)+ ":" + str(player) + ":" + str(betType) + ":" + str(amount))
            gemsEdit(vicId, amount, False)
            await ctx.send(player + " has bet " + str(amount) + " gems on red!")
            betCheck.append(player) 
            return
        if betType == "black":
            bets.append(str(vicId)+ ":" + str(player) + ":" + str(betType) + ":" + str(amount))
            gemsEdit(vicId, amount, False)
            betCheck.append(player)
            await ctx.send(player + " has bet " + str(amount) + " gems on black!")
            return
        if betType == "even":
            bets.append(str(vicId)+ ":" + str(player) + ":" + str(betType) + ":" + str(amount))
            gemsEdit(vicId, amount, False)
            betCheck.append(player)
            await ctx.send(player + " has bet " + str(amount) + " gems on even!")
            return
        if betType == "odd":
            bets.append(str(vicId)+ ":" + str(player) + ":" + str(betType) + ":" + str(amount))
            gemsEdit(vicId, amount, False)
            betCheck.append(player)
            await ctx.send(player + " has bet " + str(amount) + " gems on odd!")
            return
        if betType == "zero":
            bets.append(str(vicId)+ ":" + str(player) + ":" + str(betType) + ":" + str(amount))
            gemsEdit(vicId, amount, False)
            betCheck.append(player)
            await ctx.send(player + " has bet " + str(amount) + " gems on zero!")
            return
        else:
            await ctx.send("That's not a valid bet command!")
            return
    else:
        await ctx.send("No bets are currently being taken!")
        return

global guessGame 
guessGame = False
@tasks.loop(minutes=10)
async def guessWordGame():
    global guessGame
    guessGame = True
    await client.wait_until_ready()
    channel = client.get_channel(488567034712686602)
    await channel.send("Time to guess that word! In 3...")
    await asyncio.sleep(1)
    await channel.send("2...")
    await asyncio.sleep(1)
    await channel.send("1...")
    await asyncio.sleep(1)
    wordList = ["Renatus","Kitpvp","Parkour","Janus","Coal","Developer","Voting","Gladiator","Diamond","Ores","Gems","Warden","Creative","Survival","Rac","Ends","Ben","Creative","Diamond","Iron","Emerald"]
    randWord = random.randint(0,len(wordList) - 1)
    global word
    word = wordList[randWord]
    wordSplit = []
    finalWord = []
    for a in word:
        wordSplit.append(a)
    for b in wordSplit:
        finalWord.append("-")
    stop = len(wordSplit) - 1
    x = 1
    while x <= stop:
        finalWord = hideWord(finalWord, wordSplit)
        await channel.send(cleanDbTable(finalWord))
        x = x + 1    
        await asyncio.sleep(6)
    await channel.send("The word is " + word + "!")
    guessWordGame.cancel()
    word = ""

#Checks special word message
word = ""
@client.listen('on_message')
async def on_message(message):
    global word
    global guessGame
    if (message.channel.id == 488567034712686602 and message.content.lower() == word.lower() and guessGame == True): 
        guessWordGame.cancel()
        person = message.author.mention
        id = message.author.id
        gemsEdit(id, 3, True)
        await message.channel.send(person + " Has guessed the word and was awarded 3 gems!")
        for role in message.author.roles:
            if str(role) == "VIP":
                await message.channel.send("You are a VIP and earned 2 extra gems.")
                gemsEdit(id, 2, True)
        word = ""
        guessGame = False
        await client.process_commands(message)
        return
    return

    #
    # Errors
    #

@client.command()
@has_permissions(manage_messages=True)
async def debug(ctx):
    embed=discord.Embed(title="Warden", description="Testing description", color=0xe10e63)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/O3UgL5cSIxuehkd98p3Esd-Vh7vQwnA4BVXtanKdzYc/%3Fsize%3D256/https/cdn.discordapp.com/avatars/679812786200510583/07fbc40bccdef5e7873f745ec719d69d.png")
    embed.add_field(name="Field 1", value="2", inline=False)
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_messages=True)
async def shop(ctx):
    # String will be pulled from db and determine the items that rotate 
    await ctx.send("""
                         ```   𝐈𝐭𝐞𝐦:              𝐂𝐨𝐬𝐭: 
 """ + "- Kitpvp Cash" + "      "  + "20 Gems per $" 
     +  '\n' + " - VIP Role" + "      "  + "50,000 Gems"
     +  '\n' + " - Warden Tag" + "      "  + "25,000 Gems"  +  """```""")

@client.command()
@has_permissions(manage_messages=True)
async def buy(ctx, *, state):
    wardenChannel = client.get_channel(849510501209473034)
    id = ctx.author.id
    c.execute('SELECT * FROM warden WHERE id IN (SELECT id FROM warden WHERE id = ?)', (id,))
    testId = c.fetchall()
    playerAmount = getInstanceInTuple(testId, 2)
    playerAmount =  float(playerAmount)
    args = state.split(" ")
    primaryCmd = args[0]
    secondaryCmd = args[1]
    if (primaryCmd.lower() == "kitpvp"):
        tertiaryCmd = args[2]
        cost = int(tertiaryCmd)
        if (playerAmount >= cost):
            gemsEdit(id,cost,False)
            await wardenChannel.send("""
            ```Discord name: """ + str(ctx.author) + 
            '\n' + """Kitpvp Cash Owed: """ + str(cost / 20) + """```""")
            await ctx.send(str(cost / 20) + " Kitpvp Cash purchased!")
        else:
            await ctx.send("Insufficient gems, you have " + str(playerAmount) + ".")
    if (primaryCmd.lower() == "vip"):
        cost = 500000
        if (playerAmount >= cost):
            gemsEdit(id,cost,False)
            member = ctx.message.author
            role = discord.utils.get(member.guild.roles, name = "VIP")
            await member.add_roles(role)
            await ctx.send("VIP role purchased!")
        else:
            await ctx.send("Insufficient gems, you have " + str(playerAmount) + ".")
    if (primaryCmd.lower() == "warden"):
        cost = 25000
        if (playerAmount >= cost):
            gemsEdit(id,cost,False)
            await wardenChannel.send("""
            ```Discord name: """ + str(ctx.author) + 
            '\n' + """Owed: """ + """Warden Tag""" + """```""")
            await ctx.send("Warden tag purchased!")
        else:
            await ctx.send("Insufficient gems, you have " + str(playerAmount) + ".")


@client.event
async def on_command_error(msg, error):
    await msg.channel.send(str(error))

# chatchecker()
client.run(token)