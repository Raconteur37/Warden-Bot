

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