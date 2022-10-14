import os
import discord
from discord.ext import commands
import tweepy
from tweet import get_tweet_urls
import asyncio
import sqlite3
import genshinstats as gs

client = commands.Bot(command_prefix="%", intents=discord.Intents.all(),status=discord.Status.dnd,activity=discord.Game(name="%help"), )
auth = tweepy.OAuth2AppHandler(os.environ["consumer_key"],os.environ["consumer_secret"])
api = tweepy.API(auth)
con=sqlite3.connect("genshin.db")
cur=con.cursor()
cur.execute("create table if not exists gen(author_id int,uid int,ltuid int,ltoken varchar)")
con.commit()


def term2_marks(g:float,h:float,x:float):
    y=round((5*(g-h)-3*x)/7)
    return y

b={}
def stats1(a):
    cur.execute(f"select*from gen where author_id={a}")
    try:
        uid=int(cur.fetchall()[0][1])
        cur.execute(f"select*from gen where author_id={a}")
        ltuid=str(cur.fetchall()[0][2])
        cur.execute(f"select*from gen where author_id={a}")
        ltoken=str(cur.fetchall()[0][3])
        gs.set_cookie(ltuid=ltuid,ltoken=ltoken)
        stats = gs.get_user_stats(uid)['stats']
        for field, value in stats.items():
            b[str(field)]=str(value)
    except IndexError:
        print("Not registered")


@client.event
async def on_ready():
    print("Up and running")


@client.command()
async def ping(ctx):
    await ctx.reply(f"{round(client.latency*1000)}ms")

@client.command()
async def term2(ctx,theory:float,practicals:float,term1:float):
    y=term2_marks(theory,practicals,term1)
    await ctx.reply(f"Your term2 marks is: {y}")


@client.command()
async def new(ctx):
    ids=[]
    cur.execute("select author_id from gen")
    id_for_checking=cur.fetchall()[0]
    if ctx.author.id in id_for_checking:
        await ctx.send("User already registered in database")
#---------------------------------------------------------------------
    else:
        await ctx.send("Hi!Please enter requested ids to register your genshin account to the bot.The timeout is 1min.")
        await ctx.send("Enter UID")
        def check1(m):
            return m.author==ctx.author and m.channel==ctx.channel
        uid=await client.wait_for("message",timeout=60,check=check1)
        if uid:
            await ctx.send("Got it successfully")
            
        else:
            await ctx.send("Please enter appropriate UID")
    #---------------------------------------------------------------------
        await ctx.send("Enter ltuid")
        def check2(m):
            return m.author==ctx.author and m.channel==ctx.channel
        luid=await client.wait_for("message",timeout=60,check=check2)
        if luid:
            await ctx.send("Got it successfully")
        else:
            await ctx.send("Please enter appropriate luid")
    #----------------------------------------------------------------------
        await ctx.send("Enter ltoken")
        def check3(m):
            return m.author==ctx.author and m.channel==ctx.channel
        ltoken=await client.wait_for("message",timeout=60,check=check3)
        author_id=None
        if ltoken:
            await ctx.send("Got it successfully")
            author_id= ctx.author.id
        else:
            await ctx.send("Please enter appropriate ltoken")
        new=(author_id,uid.content,luid.content,ltoken.content)
        await ctx.reply("Done thank you for registering")
        cur.execute("insert into gen values(?,?,?,?)",new)
        con.commit()
    

@client.command()
async def stats(ctx):
    stats1(ctx.author.id)
    for i,j in b.items():
        await ctx.send(f"{i}:{j}")

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.reply("Loaded successfully")

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.reply("Unloaded successfully")

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
async def main():
    async with client:
        await load_extensions()
        await client.start(os.environ["token"])

asyncio.run(main())