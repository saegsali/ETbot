import discord
import asyncio
import json
import datetime
from secrets import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def sendLink(message):
    with open('data.json') as f:
        data = json.load(f)

    for course in data['courses']:
        if message.content == course['key']:
            print(course['name'], course['link'])
            channel = message.channel
            text = "Da de link für d " + course['name']
            await channel.send(text)
            await channel.send(course['link'])
            await channel.send(course['message'])

@client.event
async def on_message(message):
    if message.content.startswith('test'):
        channel = message.channel
        await channel.send('selber test!')
    
    if message.content.startswith('help'):
        with open('data.json') as f:
            data = json.load(f)
            
        text = "Possible commands: "
        
        for course in data['courses']:
            text += course['key']
            text += ", "
        
        channel = message.channel
        await channel.send(text)
    print(message.channel)
    
    await sendLink(message)

async def time_check():
    await client.wait_until_ready()
    channel = client.get_channel(message_channel_id)
    while client.is_ready:
        tday = datetime.datetime.now()
        print(tday.strftime("%H:%M"))
        
        with open('data.json') as f:
            data = json.load(f)
        
        time = 10
        for course in data['courses']:
            if course['time'] == tday.strftime("%H:%M") and course['day'] == tday.strftime("%A"):
                message = "Da de Link für di hüttigi " + course['name'] + ":"
                await channel.send(message)
                await channel.send(course['link'])
                await channel.send(course['message'])
                time = 90
        await asyncio.sleep(time)

client.loop.create_task(time_check())
client.run(token)