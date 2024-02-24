import discord
from discord.ext import commands
from datetime import datetime
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


def manage_albumfile():
    current_month = str(datetime.now().month)
    with open("albums.json", "r") as f:
        data = json.load(f)
        current_album = data[current_month]

    return current_album


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def add(ctx, *, newalbum):
    current_month = str(datetime.now().month)
    await ctx.send(f'{newalbum} has been added to the queue')
    with open("albums.json", "r+") as albumfile:
        data = json.load(albumfile)
        data[current_month] = str(newalbum)
        albumfile.seek(0)
        json.dump(data, albumfile)
        albumfile.truncate()


@bot.command()
async def current(ctx):
    await ctx.send(f'The current album is {manage_albumfile()}')

bot.run(os.environ.get('TORTIE_TOKEN'))
