
import discord
from discord.ext import commands
from commands import note, task, info_retrieval

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        await self.process_commands(message)

bot = Bot()

bot.add_cog(note.Note(bot))
bot.add_cog(task.Task(bot))
bot.add_cog(info_retrieval.InfoRetrieval(bot))

bot.run('your-token-here')
