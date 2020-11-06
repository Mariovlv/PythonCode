import os
from dotenv import load_dotenv
from discord.ext import commands
import urllib.request
import json

# Discord Token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# bot
bot = commands.Bot(command_prefix = '!') # Prefijo

# Youtube API
KEY = os.getenv('API_YOUTUBE')

# Funciones
@bot.command(name = 'subs')
async def subscriptores(ctx,username):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + KEY).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)

@bot.command(name ='suma')
async def sumar(ctx, num1, num2):
	response = int(num1) + int(num2)
	await ctx.send(response)

# Run bot
bot.run(TOKEN)