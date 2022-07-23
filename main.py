import os
import discord
from discord.ext import commands
import tweepy
from tweet import get_tweet_urls
from genshin import *

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="%", intents=intents,status=discord.Status.dnd,activity=discord.Game(name="%help"), )
auth = tweepy.OAuth2AppHandler(os.environ["consumer_key"],os.environ["consumer_secret"])
api = tweepy.API(auth)

def term2_marks(g:float,h:float,x:float):
    y=round((5*(g-h)-3*x)/7)
    return y


@client.event
async def on_ready():
    print("Up and running")


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*1000)}ms")

@client.command()
async def term2(ctx,theory:float,practicals:float,term1:float):
    y=term2_marks(theory,practicals,term1)
    await ctx.send(f"Your term2 marks is: {y}")

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


client.run(os.environ["token"])
