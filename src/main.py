
import discord
from discord.ext import commands
from bot.commands.note import Note
from bot.commands.task import Task
from bot.commands.info_retrieval import InfoRetrieval

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

bot = MyBot()

bot.add_cog(Note(bot))
bot.add_cog(Task(bot))
bot.add_cog(InfoRetrieval(bot))

bot.run("your-token-here")
