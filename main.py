from ast import alias
from pydoc import cli
import os
import discord
from discord.ext import commands
import tweepy


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="%", intents=intents)
auth = tweepy.OAuth2AppHandler(os.environ["consumer_key"],os.environ["consumer_secret"])
api = tweepy.API(auth)
user=api.get_user(screen_name="GenshinImpact")


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

#tweepy intergation
@client.command()
async def info(ctx , u):
    user=api.get_user(screen_name=u)
    await ctx.send(f"{user.screen_name} has {user.followers_count} followers")

client.run(os.environ["token"])