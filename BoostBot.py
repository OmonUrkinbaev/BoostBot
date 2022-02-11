# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from datetime import date
import calendar


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='boost', help='Invoke this command if you are truly boosted')
async def nine_nine(ctx):
    boosted_quotes = [
        'You are boosted!',
        'Boost-bich!',
        (
            '^^This person is the most boosted bich in the game, '
            'bruh.'
        ),
    ]

    response = random.choice(boosted_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Rolls a dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='current_date', help='Tells you the current date and time')
async def curr_date(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


    response = dt_string
    await ctx.send(response)


bot.run(TOKEN)