import discord
from discord.ext import commands
from genshin import gen
import genshinstats as gs

uid_vebev = 847213220
uid_prad = 819444987
uid_sp = 821562362
uid_vishwo = 849428945
cookies=[[99240317,"JUrf9aCcBftSWAz1MyCyecoJU1vht5A2teWul9g9"],[106636367,"cPffZ7lhs86TK8IeunowmyesVKvCpNOuQrqPveaw"],[187431981,"2mOXqPN3bSvA1y72mA66PZmEzdKqqjX5jliPBc5C"],[179475140,"StlmWKguPcluX8kNSlJBONwmrSkS9pqPrOmUpeGg"]]
uids=[819444987,821562362,849428945,847213220]
acc=dict(zip(uids,cookies))
a={}
def stats_prad():
    gs.set_cookie(ltuid=99240317,ltoken="JUrf9aCcBftSWAz1MyCyecoJU1vht5A2teWul9g9")
    stats = gs.get_user_stats(819444987)['stats']
    for field, value in stats.items():
        a[str(field)]=str(value)


def stats_sp():
    gs.set_cookie(ltuid=106636367,ltoken="cPffZ7lhs86TK8IeunowmyesVKvCpNOuQrqPveaw")
    stats = gs.get_user_stats(821562362)['stats']
    for field, value in stats.items():
        a[str(field)]=str(value)


def stats_vishwo():
    gs.set_cookie(ltuid=187431981,ltoken="2mOXqPN3bSvA1y72mA66PZmEzdKqqjX5jliPBc5C")
    stats = gs.get_user_stats(849428945)['stats']
    for field, value in stats.items():
        a[str(field)]=str(value)

def stats_vebev():
    gs.set_cookie(ltuid=179475140,ltoken="StlmWKguPcluX8kNSlJBONwmrSkS9pqPrOmUpeGg")
    stats = gs.get_user_stats(847213220)['stats']
    for field, value in stats.items():
        a[str(field)]=str(value)
        
def calccv(x: float, y: float):
    return x*2+y


class Genshin(commands.Cog):
    @commands.command(aliases=["cv"])
    async def critvalue(self, ctx, critrate: float, critdmg: float):
        cv=calccv(critrate,critdmg)
        await ctx.send(f"Your crit value is {cv}")


    @commands.Cog.listener()
    async def on_message(self,message):
        for i in gen:
            if i in message.content:
                await message.channel.send("Yes")
                break
    
    @commands.command()
    async def stats_prad(self,ctx):
        stats_prad()
        for i,j in a.items():
            await ctx.send(f"{i}:{j}")

    @commands.command()
    async def stats_vishwo(self,ctx):
        stats_vishwo()
        for i,j in a.items():
            await ctx.send(f"{i}:{j}")

    @commands.command()
    async def stats_sp(self,ctx):
        stats_sp()
        for i,j in a.items():
            await ctx.send(f"{i}:{j}")

    @commands.command()
    async def stats_vebev(self,ctx):
        stats_vebev()
        for i,j in a.items():
            await ctx.send(f"{i}:{j}")

async def setup(client):
    await client.add_cog(Genshin(client))