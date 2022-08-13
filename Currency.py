import asyncio
from asyncio.windows_events import NULL
import os
import Utils
import SQLQeuries
import discord
import time
import datetime
import sqlite3
import random
from time import sleep
from discord.ext import tasks, commands
from discord.client import client


utils = Utils()
queries = SQLQeuries()

class Currency:

    
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def addGems(ctx, *, state):
        args = state.split(" ")
        victim = args[0]
        vicId = utils.getIdFromMention(victim)
        vicId = int(vicId)
        vicName = args[0]
        vicName = str(vicName)
        num = args[1]
        num = int(num)
        queries.addgems(num,vicId)
        await ctx.send("Added " + str(num) + " gems to " + vicName)

    # Removes set amount of gems
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def removeGems(ctx, *, state):
        args = state.split(" ")
        victim = args[0]
        vicId = utils.getIdFromMention(victim)
        vicName = args[0]
        vicName = str(vicName)
        num = args[1]
        num = int(num)
        testTable = queries.getTupleFromId(vicId)
        currentAmount = int(utils.getInstanceInTuple(testTable, 2))
        if currentAmount - num < 0:
            num = currentAmount
        queries.removegems(num,vicId)
        await ctx.send("Removed " + str(num) + " gems from " + vicName)

    # Sets amount of gems you want
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def setGems(ctx, *, state):
        args = state.split(" ")
        victim = args[0]
        vicId = utils.getIdFromMention(victim)
        vicName = args[0]
        vicId = int(vicId) 
        num = args[1]
        num = int(num)
        queries.setgems(num,vicId)
        await ctx.send("Set " + str(vicName) + "'s gems to " + str(num))

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def getGems(ctx): #clean to give gems amount
        id = ctx.author.id
        testId = queries.getTupleFromId(id)
        amount = utils.getInstanceInTuple(testId, 2)
        playerName = ctx.author
        if (testId == []):
            await ctx.send("You have no gems!")
            return
        else:
            embed=discord.Embed(title=str(playerName), color=0xe10e63)
            embed.add_field(name=str(amount) + " Gems", value="Warden", inline=True)
            await ctx.send(embed=embed)
