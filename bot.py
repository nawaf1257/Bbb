import discord
from discord.ext import commands
import os

# قراءة التوكن من المتغير البيئي
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # ضروري لو البوت يقرأ الرسائل

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
