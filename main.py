from ast import alias
from pydoc import cli
import os
import nextcord
from nextcord.ext import commands
import tweepy
from tweet import get_tweet_urls
from genshin import *

intents = nextcord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="%", intents=intents,status=nextcord.Status.dnd,activity=nextcord.Game(name="%help"))
auth = tweepy.OAuth2AppHandler(os.environ["consumer_key"],os.environ["consumer_secret"])
api = tweepy.API(auth)
user=api.get_user(screen_name="GenshinImpact")


def calccv(x: float, y: float):
    return x*2+y

def rod(x:float):
    return x/1000000

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
async def info(ctx , username):
    user=api.get_user(screen_name=username)
    count=user.followers_count
    if count>1000000 or count==1000000:
        follow=int(rod(user.followers_count))
        await ctx.send(f"{user.screen_name} has {round(follow)}M followers")
    else:
        await ctx.send(f"{user.screen_name} has {count} followers")

@client.command()
async def tweet(ctx, username):
    urls=get_tweet_urls(username)
    for url in urls:
        await ctx.send(url)

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    for i in gen:
        print("works")
        if i in message.content:
            print("Works")
            await message.channel.send("Yes")
            break

client.run(os.environ["token"])
