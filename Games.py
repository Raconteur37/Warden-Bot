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
from discord.client import client
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


# TODO refactor this entire class, for now though we wont need game so it can be ignored



class Games:
    
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
