'''
Reminder Bot v1.0

Developed for personal use by Vithraldor.

This bot was created for a private Discord server where members take turns asking the server a "question of the day".
Each member has an assigned day.
This bot is designed to remind a particular user that it's their turn to ask a question.

'''

import discord
from discord.ext import commands, tasks
import asyncio
import datetime

# Replace this mock channel ID with the question-of-the-day channel.
global channelID 
channelID = 1234

# Replace this mock channel ID with the channel you wish to provide hydration reminders in.
global announcementChannelID
announcementChannelID = 3456

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
    startMessage = "20 Questions"
    await client.change_presence(activity = discord.Streaming(name = startMessage, url = "https://github.com/Vithraldor"))
    
# Test command to see if the ping by ID function works (it does!)
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! **{round(client.latency * 1000)}** ms")

# Number generator for the day of the week. Returns a number: 0 for Monday, 6 for Sunday
dayOfTheWeek = datetime.datetime.today().weekday()

# Recurring message that reminds people to drink water.
@tasks.loop(hours = 1)
async def waterReminder():
    await client.wait_until_ready()
    announcementChannel = client.get_channel(announcementChannelID)

    await announcementChannel.send("This is a friendly reminder to drink water and stay hydrated!")
    
@tasks.loop(hours = 24)
async def rolecallCommand():

    global channelID
    
    UTCToESTOffset = 4

    await client.wait_until_ready()
    messageChannel = client.get_channel(testChannelID)

    # ID of all the users participating
    user1ID = 'put user ID here'
    user2ID = 'put user ID here'
    user3ID = 'put user ID here'
    user4ID = 'put user ID here'
    user5ID = 'put user ID here'
    user6ID = 'put user ID here'
    user7ID = 'put user ID here'

    # Gets current time - need this for calculations
    # The reason why I subtracted an extra 1 when calculating the hours to wait was to account for the minute offset.
    # This converts UTC time to EST (ex: 8 PM EST = midnight UTC)
    currentHourUTC = datetime.datetime.now().hour + UTCToESTOffset
    hoursToWait = 24 - currentHourUTC - 1

    if hoursToWait < 0 or hoursToWait == 24:
       hoursToWait = 0

    currentMinute = datetime.datetime.now().minute
    minutesToWait = 60 - currentMinute

    delayInSeconds = (hoursToWait * 3600) + (minutesToWait * 60)

    if currentHourUTC == 20 & currentMinute == 0:
        timeToPost = True
    else:
        timeToPost = False

    if timeToPost == True:
        # Messages to be sent on each day
        if dayOfTheWeek == 0:
            await messageChannel.send("Happy Monday! It's %s's turn to ask a question!" % user1ID)

        elif dayOfTheWeek == 1:
            await messageChannel.send("Happy Tuesday! It's %s's turn to ask a question!" % user2ID)

        elif dayOfTheWeek == 2:
            await messageChannel.send("Happy Wednesday! It's %s's turn to ask a question!" % user3ID)

        elif dayOfTheWeek == 3:
            await messageChannel.send("Happy Thursday! It's %s's turn to ask a question!" % user4ID)

        elif dayOfTheWeek == 4:
            await messageChannel.send("Happy Friday! It's %s's turn to ask a question!" % user5ID)

        elif dayOfTheWeek == 5:
            await messageChannel.send("Happy Saturday! It's %s's turn to ask a question!" % user6ID)

        elif dayOfTheWeek == 6:
            await messageChannel.send("Happy Sunday! It's %s's turn to ask a question!" % user7ID)

        else:
            await messageChannel.send("This isn't a case I was coded to cover. Perhaps this is a bug?\n(Send bugs to Vithraldor#3645)")

    elif timeToPost == False:
        print("Not valid time. Sleeping...")
        await asyncio.sleep(delayInSeconds)
         
    else:
        await messageChannel.send("This isn't a case I was coded to cover. Send bugs to Vithraldor#3645.")


rolecallCommand.start()
waterReminder.start()

client.run('')
