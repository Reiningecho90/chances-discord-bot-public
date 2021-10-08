# Imports
import discord
import random
from discord import colour

from discord.embeds import Embed

# Bot setup information
bot_token = "REDACTED"

client = discord.Client()


# Bot events
@client.event # report bot online in terminal
async def on_ready():
    print("Bot is online") 

@client.event # messages for output (true/false boolean outcome messages)
async def on_message(message):

    print(message.channel)

    if str(message.channel) == 'chances-guessing-game':
        try:
            content = message.content
            if ':chances' in message.content:
                print('here')

                author = str(message.author.id)            
                usr_arg = content.lstrip(':chances ')
                comp_num = random.randint(0, 10)
                
                
                # Lists for randomized reactions
                fail_lst = (
                    f'<@{author}> you seemed to have picked the wrong number this time, not my fault youre not a pro gamer :sunglasses: I picked {comp_num} and you picked {usr_arg}!',
                    f'Welp <@{author}> it wasn\'t the same number. Not poggers.  I picked {comp_num} and you picked {usr_arg}!',
                    f'0/10, would not reccomend picking that number next time <@{author}>.  I picked {comp_num} and you picked {usr_arg}!',
                    f'Hey, <@{author}>, we didn\'t get the same number this time, maybe again?  I picked {comp_num} and you picked {usr_arg}!'
                )

                success_lst = (
                    f'Hey, <@{author}>...the numbers were equal! I picked {comp_num} and you picked {usr_arg}!',
                    f'Well, <@{author}> it looks like we got the same number! I picked {comp_num} and you picked {usr_arg}!',
                    f'<@{author}> we got the same number, is this good or bad?  I picked {comp_num} and you picked {usr_arg}!',
                    f'Guess what <@{author}>? we got the same number!  I picked {comp_num} and you picked {usr_arg}!'
                )


                # statement to decide a message


                if int(usr_arg) == comp_num:

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

            if content == ':help':

                help_embed = discord.Embed(
                    title = 'Helping you out!',
                    description = 'See our website for the help section! \n Check it out here: https://reiningecho90.github.io/chances-discord-bot-public/',
                    colour = discord.Colour(0xf1c40f)
                )

                await message.channel.send(embed = help_embed)

            
        except ValueError:

            print(f"{author} attempted to run command with {usr_arg} as argument.")
                

# run client
client.run(bot_token)
