
import discord
from discord.ext import commands

class Note(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def add_note(self, ctx, *, content: str):
        """Adds a note with the provided content."""
        await ctx.send('Note added: {}'.format(content))

    @commands.command()
    async def view_notes(self, ctx):
        """Views all notes."""
        await ctx.send('Displaying all notes.')

def setup(bot):
    bot.add_cog(Note(bot))
