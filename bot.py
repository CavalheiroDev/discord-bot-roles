import os
import discord
import dotenv
from discord.ext import commands


dotenv.load_dotenv(dotenv.find_dotenv())


bot = discord.Client()

intents = discord.Intents().all()
PREFIX = os.environ['PREFIX']

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    print('TA NO AR CLÃ!!')

@bot.command()
async def prefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f'O prefixo foi mudado para "{prefix}".')



@bot.event
async def on_member_join(member: discord.Member):
    role = discord.utils.get(member.guild.roles, name='randons')

bot.run('ODgwMjUzMjgwODEzNDYxNTM1.YSblwA.A59QrPhL9bfZ4UeoLwP52edDqKI')

