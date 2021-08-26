import discord
from discord.ext import commands
from environment_variables import PREFIX, WELCOME_MESSAGE, STARTED_ROLE, TOKEN_BOT


bot = discord.Client()

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    print('TA NO AR CLÃ!!')


@bot.command()
async def prefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f'O prefixo foi mudado para "{prefix}".')


@bot.event
@commands.has_role('Admin')
async def on_member_join(member: discord.Member):
    await member.send(WELCOME_MESSAGE)
    role = discord.utils.get(member.guild.roles, name=STARTED_ROLE)
    await member.add_roles(role)

@bot.command()
async def move_role(ctx, user: discord.Member, role: discord.Role):
    pass

bot.run(TOKEN_BOT)

