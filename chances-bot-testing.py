# Imports
import discord
import random
from discord import colour

from discord.embeds import Embed

# Bot setup information
bot_token = "TOKEN"

client = discord.Client()


# Bot events
@client.event # report bot online in terminal
async def on_ready():
    print("Bot is online") 

@client.event # messages for output (true/false boolean outcome messages)
async def on_message(message):

    if str(message.channel) == 'general':

        if ':chances' in message.content:
            author = str(message.author.id)            
            content = message.content
            number = content.lstrip(':chances ')
            comp_num = random.randint(0, 10)
            
            
            # Lists for randomized reactions
            fail_lst = (
                f'<@{author}> you seemed to have picked the wrong number this time, not my fault youre not a pro gamer :sunglasses: I picked {comp_num} and you picked {number}!',
                f'Welp <@{author}> it wasn\'t the same number. Not poggers.  I picked {comp_num} and you picked {number}!',
                f'0/10, would not reccomend picking that number next time <@{author}>.  I picked {comp_num} and you picked {number}!',
                f'Hey, <@{author}>, we didn\'t get the same number this time, maybe again?  I picked {comp_num} and you picked {number}!'
            )

            success_lst = (
                f'Hey, <@{author}>...the numbers were equal! I picked {comp_num} and you picked {number}!',
                f'Well, <@{author}> it looks like we got the same number! I picked {comp_num} and you picked {number}!',
                f'<@{author}> we got the same number, is this good or bad?  I picked {comp_num} and you picked {number}!',
                f'Guess what <@{author}>? we got the same number!  I picked {comp_num} and you picked {number}!'
            )


            # statement to decide a message
            if int(number) == comp_num:
                match_embed = discord.Embed(
                    title = 'Your Results',
                    description = random.choice(success_lst),
                    colour = discord.Colour(0x2ecc71)
                )

                await message.channel.send(embed = match_embed)

            else:
                fail_embed = discord.Embed(
                    title = 'Your Results',
                    description = random.choice(fail_lst),
                    colour = discord.Colour(0xe74c3c)
                )

                await message.channel.send(embed = fail_embed)
                

# run client
client.run(bot_token)
