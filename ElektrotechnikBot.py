import discord
import asyncio
import json
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
            await channel.send("vill spass:)")

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
    
    await sendLink(message)


client.run(token)