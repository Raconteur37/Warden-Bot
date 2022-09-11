import asyncio
import os
import discord
# python3 -m pip install (package).py fixes many problems
import time
import datetime
from discord import message
from discord import user
from discord import channel
from discord import client
from discord.enums import SpeakingState  
from discord.ext import commands
from discord.ext import tasks, commands

from discord.ext.commands import has_permissions, MissingPermissions


class Commands:
    
    async def runCommand(name:str,user:discord.user):
        
        if (name == "purge"):
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
        async def commandsList(ctx):
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
                    
                    
        @client.command()
        @has_permissions(manage_messages=True)
        async def debug(ctx):
            embed=discord.Embed(title="Warden", description="Testing description", color=0xe10e63)
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/O3UgL5cSIxuehkd98p3Esd-Vh7vQwnA4BVXtanKdzYc/%3Fsize%3D256/https/cdn.discordapp.com/avatars/679812786200510583/07fbc40bccdef5e7873f745ec719d69d.png")
            embed.add_field(name="Field 1", value="2", inline=False)
            await ctx.send(embed=embed)