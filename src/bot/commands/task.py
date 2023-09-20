
import discord
from discord.ext import commands

class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = {}

    @commands.command()
    async def add_task(self, ctx, *, task):
        if ctx.message.author.id not in self.tasks:
            self.tasks[ctx.message.author.id] = []
        self.tasks[ctx.message.author.id].append(task)
        await ctx.send(f'Task "{task}" added.')

    @commands.command()
    async def list_tasks(self, ctx):
        if ctx.message.author.id not in self.tasks or not self.tasks[ctx.message.author.id]:
            await ctx.send('No tasks found.')
        else:
            tasks = "\n".join(self.tasks[ctx.message.author.id])
            await ctx.send(f'Your tasks:\n{tasks}')

    @commands.command()
    async def remove_task(self, ctx, *, task):
        if ctx.message.author.id in self.tasks and task in self.tasks[ctx.message.author.id]:
            self.tasks[ctx.message.author.id].remove(task)
            await ctx.send(f'Task "{task}" removed.')
        else:
            await ctx.send('Task not found.')

def setup(bot):
    bot.add_cog(Task(bot))
