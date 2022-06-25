import discord
from discord.ext import commands

from genshin import gen

def calccv(x: float, y: float):
    return x*2+y


class Genshin(commands.Cog):
    @commands.command(aliases=["cv"])
    async def critvalue(self, ctx, x: float, y: float):
        cv=calccv(x,y)
        await ctx.send(f"Your crit value is {cv}")


    @commands.Cog.listener()
    async def on_message(self,message):
        for i in gen:
            if i in message.content:
                await message.channel.send("Yes")
                break


def setup(client):
    client.add_cog(Genshin(client))