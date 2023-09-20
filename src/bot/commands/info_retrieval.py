
import discord
from discord.ext import commands
import requests

class InfoRetrieval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info', help='Retrieves information from the internet.')
    async def info(self, ctx, *, query: str):
        response = requests.get(f"https://www.google.com/search?q={query}")
        await ctx.send(response.text)

def setup(bot):
    bot.add_cog(InfoRetrieval(bot))
