import os
import discord
import requests
import json
import random
client = discord.Client()

sad=['depressun','aks','nub','sad','loser','miserable']
encourage=['eruma madu','overa scene ah podatha','savu da naiye']


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0] ['q'] + '-' +    json_data[0] ['a']
    return(quote)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game('Made by prad with lube❤️'))
    print("We have logged in sucessfully as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    msg = message.content

    if msg.startswith('%help'):
        await message.channel.send('\n\nCommands are:\n1.aks\n2.vebev\n3.ani\n4.prash\n5.prad\n6.quote\n7.sp\n8.rup\n9.vish\n\n')
    if msg.startswith('%quote'):
        await message.channel.send(get_quote())
    
    if msg.startswith('%god'):
        await message.channel.send('PRAD')

    if msg.startswith('%aks'):
        await message.channel.send('DEPRESSUN')
    
    if msg.startswith('%vebev'):
        await message.channel.send('NUB')

    if msg.startswith('%ani'):
        await message.channel.send('NONONOONONONO')

    if msg.startswith('%prash'):
        await message.channel.send('PERO')

    if msg.startswith('%prad'):
        await message.channel.send('GOD')

    if msg.startswith('%sp'):
        await message.channel.send('💀')
    
    if msg.startswith('%rup'):
        await message.channel.send('.......')  
    if msg.startswith('%vish'):
        await message.channel.send('king gay')
    if msg.startswith('vebev'):
        await message.channel.send('KUMARAN')
    
@client.listen('on_message')
async def on_ping(message):
    if message.mention_everyone:
        return
    else:
        print("Prefix is %")


client.run(os.environ["token"])
