# Imports
from typing import final
import discord
import random
from discord import colour
import time as t
import datetime

# Bot setup information
bot_token = "REDACTED"

client = discord.Client()

# information day to day
daily_data = ['--DAILY DATA LIST--']
server_channel_lst = ['chances-guessing-game', 'chances-bot', 'what-are-the-chaces', 'guessing-bot']

reset_time = 3
false_time = 4
log_for_day = False

while 1:

    if t.strftime("%H") == reset_time and log_for_day == False:
        print(t.strftime('%H'))
        print(daily_data)

        log_channel_id = client.get_channel(898757086161293332)

        log_channel_id.send(f'{daily_data}')

        log_for_day = True

    if t.strftime("%H") == false_time and log_for_day == True:
        log_channel_id = client.get_channel(898757086161293332)

        log_channel_id.send(f'{daily_data}')

        log_for_day = False

        

    # Bot events
    @client.event # report bot online in terminal
    async def on_ready():
        print("Bot is online") 

    @client.event # messages for output (true/false boolean outcome messages)
    async def on_message(message):

        if str(message.channel) in server_channel_lst:
            try:
                content = message.content
                if ':chances' in message.content:

                    author = str(message.author.id)            
                    usr_arg = content.lstrip(':chances ')
                    comp_num = random.randint(0, 10)
                    
                    
                    # Lists for randomized reactions
                    fail_lst = (
                        f'<@{author}> you seemed to have picked the wrong number this time, not my fault youre not a pro gamer :sunglasses: I picked {comp_num} and you picked {usr_arg}!',
                        f'Welp <@{author}> it wasn\'t the same number. Not poggers.  I picked {comp_num} and you picked {usr_arg}!',
                        f'0/10, would not reccomend picking that number next time <@{author}>.  I picked {comp_num} and you picked {usr_arg}!',
                        f'Hey, <@{author}>, we didn\'t get the same number this time, maybe again?  I picked {comp_num} and you picked {usr_arg}!',
                        f'Well it looks like that\'s another failure <@{author}>. You should seek counseling if you are sad.  I picked {comp_num} and you picked {usr_arg}!',
                        f'Welp <@{author}> it looks like that\'s another failure for the books!  I picked {comp_num} and you picked {usr_arg}!',
                        f'Not the same number <@{author}>, all your base are belong to us. (If you are uncultured see this link: https://knowyourmeme.com/memes/all-your-base-are-belong-to-us)   I picked {comp_num} and you picked {usr_arg}!',
                        f'No luck <@{author}>. Step away from the keyboard and no one gets addicted.  I picked {comp_num} and you picked {usr_arg}!'
                    )

                    success_lst = (
                        f'Hey, <@{author}>...the numbers were equal! I picked {comp_num} and you picked {usr_arg}!',
                        f'Well, <@{author}> it looks like we got the same number! I picked {comp_num} and you picked {usr_arg}!',
                        f'<@{author}> we got the same number, is this good or bad?  I picked {comp_num} and you picked {usr_arg}!',
                        f'Guess what <@{author}>? we got the same number!  I picked {comp_num} and you picked {usr_arg}!',
                        f'This is a sucess story, <@{author}>! Thanks for the data! :person_running: :dash:  I picked {comp_num} and you picked {usr_arg}!',
                        f'Hey, <@{author}>! you won! Wait, what?...I thought you were supposed to bring the trophies!?  I picked {comp_num} and you picked {usr_arg}!',
                        f'Won you have, <@{author}>, tried you have not. Yet sucess you have achieved.  I picked {comp_num} and you picked {usr_arg}!',
                        f'Hey, <@{author}> you did it! Now do homework and battle that gambling addiction of yours!  I picked {comp_num} and you picked {usr_arg}!'
                    )


                    # statement to decide a message


                    if int(usr_arg) == comp_num:

                        match_embed = discord.Embed(
                            title = 'Your Results',
                            description = random.choice(success_lst),
                            colour = discord.Colour(0x2ecc71)
                        )

                        await message.channel.send(embed = match_embed)

                        time = datetime.datetime.now()
                        daily_data.append(f'{message.author.id}: {time}, {str(message.content)}')
                        print('data added to list')

                    else:

                        fail_embed = discord.Embed(
                            title = 'Your Results',
                            description = random.choice(fail_lst),
                            colour = discord.Colour(0xe74c3c)
                        )

                        await message.channel.send(embed = fail_embed)

                        time = datetime.datetime.now()
                        daily_data.append(f'{message.author.id}: {time}, {str(message.content)}')
                        print('data added to list')
                    
                if content == ':help':

                    help_embed = discord.Embed(
                        title = 'Helping you out!',
                        description = 'See our website for the help section! \n Check it out here: https://reiningecho90.github.io/chances-discord-bot-public/',
                        colour = discord.Colour(0xf1c40f)
                    )

                    await message.channel.send(embed = help_embed)

                    time = datetime.datetime.now()
                    daily_data.append(f'{message.author.id}: {time}, {str(message.content)}')
                    print('data added to list')

                if content == ':leaderboard':

                    lead_embed = discord.Embed(
                        title = 'Leaderboard_Not_Found',
                        description = '''Leaderboards don\t count in this kind of game. I do have some hororable mentions though...
                        
                        1. EnderPearlMandy (BFF+Asked me nicely and is kinda a god...)
                        2. Jasper! (First public server the bot got into's owner!)''',
                        colour = discord.Colour(0x3498db)
                    )

                    await message.channel.send(embed = lead_embed)

                    time = datetime.datetime.now()
                    daily_data.append(f'{message.author.id}: {time}, {str(message.content)}')
                    print('data added to list')

                
            except ValueError:

                print(f"{author} attempted to run command with {usr_arg} as argument.")


    # run client
    client.run(bot_token)
