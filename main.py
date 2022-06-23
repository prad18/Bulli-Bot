import os
import discord
from discord.ext import commands
import tweepy
from tweet import get_tweet_urls
from genshin import *

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="%", intents=intents,status=discord.Status.dnd,activity=discord.Game(name="%help"))
auth = tweepy.OAuth2AppHandler(os.environ["consumer_key"],os.environ["consumer_secret"])
api = tweepy.API(auth)


def calccv(x: float, y: float):
    return x*2+y


@client.event
async def on_ready():
    print("Up and running")

@client.command()
async def help_ping(ctx):
    await ctx.send(f"Shows the current ping in your discord client")

@client.command()
async def help_cv(ctx):
    await ctx.send(f"Syntax: %cv <crit rate> <crit value>")


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*1000)}ms")

@client.command(aliases=["cv"])
async def critvalue(ctx, x: float, y: float):
    cv=calccv(x,y)
    await ctx.send(f"Your crit value is {cv}")


@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded successfully")
@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloaded successfully")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#@client.event
#async def on_message(message):
#    if message.author==client.user:
#        return
#    for i in gen:
#        if i in message.content:
#            await message.channel.send("Yes")
#           break

client.run(os.environ["token"])
