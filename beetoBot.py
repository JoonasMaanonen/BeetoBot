import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot = commands.Bot(command_prefix="B!", description="Hyva botti!")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)

@bot.command()
async def hello():
    await bot.say("Hei! Taahan toimii!")

@bot.command()
async def best():
    await bot.say("https://cdn.discordapp.com/emojis/375014254853619712.png")

bot.run("Mzc1MzYxNDExMzI2NTQxODI0.DNuzyg.JFGA_q8vX1fCMN9UsYFWtxmIUQw")
