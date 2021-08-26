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
async def on_member_join(member: discord.Member):
    await member.send(WELCOME_MESSAGE)
    role = discord.utils.get(member.guild.roles, name=STARTED_ROLE)
    await member.add_roles(role)

@bot.command()
async def add_role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'O membro {member.mention} foi adicionado ao cargo {role}')

@bot.command()
async def remove_role(ctx, member: discord.Member, role:discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'O membro {member.mention} foi removido do cargo {role}')

bot.run(TOKEN_BOT)

