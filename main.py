"""from ast import alias
from pydoc import cli
import os
import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="%", intents=intents)

def calccv(x: float, y: float):
    return x*2+y

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game('Made by prad ❤️'))
    print("We have logged in sucessfully as {0.user}".format(client))

@client.event
async def on_message(message):
    if "<@872795608770052116>" in message.content:
        await message.channel.send("Prefix is %! For help say %help_<command name>.This bot has currently only two features one is %cv and %ping. More features will be released soon!! Stay tuned")
    
@client.command()
async def help_ping(ctx):
    await ctx.send(f"Shows the current ping in your discord client")

@client.command()
async def help_cv(ctx):
    await ctx.send(f"Syntax: %cv <crit rate> <crit value>")

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*100)}ms")

@client.command(aliases=["cv"])
async def critvalue(ctx, x: float, y: float):
    cv=calccv(x,y)
    await ctx.send(f"Your crit value is {cv} !")
"""
from ast import alias
from pydoc import cli
import os
import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="?", intents=intents)

def calccv(x: float, y: float):
    return x*2+y

@client.event
async def on_ready():
    print("Up and running")

@client.event
async def on_member_join(member):
    print(f'Welcome to our server! {member}')

@client.event
async def on_member_remove(member):
    print(f'See ya soon! {member}')

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*100)}ms")

@client.command(aliases=["cv"])

async def critvalue(ctx, x: float, y: float):
    cv=calccv(x,y)
    await ctx.send(f"Your crit value is {cv}")

client.run(os.environ["token"])


