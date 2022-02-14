# Imports
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
server_channel_lst = ['chances-guessing-game', 'chances-bot', 'what-are-the-chances', 'guessing-bot', 'bot-testing']


# Bot events
@client.event # report bot online in terminal
async def on_ready():
    print("Bot is online") 

@client.event # messages for output (true/false boolean outcome messages)
async def on_message(message):

    if str(message.channel) in server_channel_lst or 'bot' in str(message.content):
        content = message.content
        try:

            if ':chances' in message.content:

                author = str(message.author.id)            
                usr_arg = content.lstrip(':chances ')
                comp_num = random.randint(0, 10)
                
                if author == '"REDACTED"':
                    if usr_arg == comp_num:
                        await message.channel.send(f'Love ya m8. :heart:, but also you picked {usr_arg} and I went with {comp_num}. To me it doesn\'t matter if you won or lost (hint: you won)')
                    else:
                        await message.channel.send(f'Love ya m8. :heart:, but also you picked {usr_arg} and I went with {comp_num}. To me it doesn\'t matter if you won or lost (hint: you lost)')
                
                # Lists for randomized reactions
                fail_lst = (
                    f'<@{author}> you seemed to have picked the wrong number this time, not my fault youre not a pro gamer :sunglasses: I picked {comp_num} and you picked {usr_arg}!',
                    f'Welp <@{author}> it wasn\'t the same number. Not poggers. I picked {comp_num} and you picked {usr_arg}!',
                    f'0/10, would not recommend picking that number next time <@{author}>. I picked {comp_num} and you picked {usr_arg}!',
                    f'Hey, <@{author}>, we didn\'t get the same number this time, maybe again? I picked {comp_num} and you picked {usr_arg}!',
                    f'Well it looks like that\'s another failure <@{author}>. You should seek counseling if you are sad.  I picked {comp_num} and you picked {usr_arg}!',
                    f'Welp <@{author}> it looks like that\'s another failure for the books! I picked {comp_num} and you picked {usr_arg}!',
                    f'Not the same number <@{author}>, all your base are belong to us. (If you are uncultured see this link: https://knowyourmeme.com/memes/all-your-base-are-belong-to-us)   I picked {comp_num} and you picked {usr_arg}!',
                    f'No luck <@{author}>. Step away from the keyboard and no one gets addicted. I picked {comp_num} and you picked {usr_arg}!',
                    f'<@{author}>, use this special power to try again. I picked {comp_num} and you picked {usr_arg}!',
                    f'<@{author}>, numbers don\'t match, but that doesn\'t mean I dont love you! I picked {comp_num} and you picked {usr_arg}!',
                    f'Awww, <@{author}>, you\'re so cute, apparently that doesn\'t help your luck. I picked {comp_num} and you picked {usr_arg}!',
                    f'Woah, didn\'nt see you there <@{author}>. Luck isn\'t so good on the game, but it\'s Valentine\'s day! I picked {comp_num} and you picked {usr_arg}!',
                )

                success_lst = (
                    f'Hey, <@{author}>...the numbers were equal! I picked {comp_num} and you picked {usr_arg}!',
                    f'Well, <@{author}> it looks like we got the same number! I picked {comp_num} and you picked {usr_arg}!',
                    f'<@{author}> we got the same number, is this good or bad?  I picked {comp_num} and you picked {usr_arg}!',
                    f'Guess what <@{author}>? we got the same number!  I picked {comp_num} and you picked {usr_arg}!',
                    f'This is a sucess story, <@{author}>! Thanks for the data! :person_running: :dash: I picked {comp_num} and you picked {usr_arg}!',
                    f'Hey, <@{author}>! you won! Wait, what?...I thought you were supposed to bring the trophies!? I picked {comp_num} and you picked {usr_arg}!',
                    f'Won you have, <@{author}>, tried you have not. Yet sucess you have achieved. I picked {comp_num} and you picked {usr_arg}!',
                    f'Hey, <@{author}> you did it! Now do homework and battle that gambling addiction of yours! I picked {comp_num} and you picked {usr_arg}!',
                    f'WOAH, <@{author}> this room just heated up! We have a winner! I picked {comp_num} and you picked {usr_arg}!',
                    f'Ooh, <@{author}> we might have something in common! JK its these odds. I picked {comp_num} and you picked {usr_arg}!',
                    f'Hey <@{author}> you sound nice. HMU at this ip: https://www.youtube.com/watch?v=dQw4w9WgXcQ. I picked {comp_num} and you picked {usr_arg}!',
                    f'Okay, <@{author}> I admit it...you do look kinda nice ig... I picked {comp_num} and you picked {usr_arg}!',
                )


                # statement to decide a message


                if int(usr_arg) == comp_num:

                    match_embed = discord.Embed(
                        title = 'Your Results',
                        description = random.choice(success_lst),
                        colour = discord.Colour().from_rgb(236, 79, 132)
                    )

                    await message.channel.send(embed = match_embed)

                    time = datetime.datetime.now()
                    message_channel = client.get_channel("REDACTED")
                    print(f"Got channel {message_channel}")
                    await message_channel.send(f'{message.author.id}, {time}, {str(message.content)};')

                else:

                    fail_embed = discord.Embed(
                        title = 'Your Results',
                        description = random.choice(fail_lst),
                        colour = discord.Colour.from_rgb(228, 26, 74)
                    )

                    await message.channel.send(embed = fail_embed)

                    time = datetime.datetime.now()
                    message_channel = client.get_channel("REDACTED")
                    print(f"Got channel {message_channel}")
                    await message_channel.send(f'{message.author.id}, {time}, {str(message.content)};')
                
            if content == ':help':

                help_embed = discord.Embed(
                    title = 'Helping you out!',
                    description = 'See our website for the help section! \n Check it out here: https://reiningecho90.github.io/chances-discord-bot-public/ \n \n Have a happy holiday season!',
                    colour = discord.Colour(0xf1c40f)
                )

                await message.channel.send(embed = help_embed)

                time = datetime.datetime.now()
                message_channel = client.get_channel("REDACTED")
                print(f"Got channel {message_channel}")
                await message_channel.send(f'{message.author.id}, {time}, {str(message.content)};')

            if content == ':leaderboard':

                lead_embed = discord.Embed(
                    title = 'Leaderboard_Not_Found',
                    description = 
                    '''Leaderboards don\'t count in this kind of game. I do have some hororable mentions though...
                    
                    1. EnderPearlMandy (BFF+Asked me nicely and is kinda a god...)
                    2. Jasper! (First public server the bot got into's owner!)''',
                    colour = discord.Colour(0x3498db)
                )

                await message.channel.send(embed = lead_embed)

                time = datetime.datetime.now()
                message_channel = client.get_channel("REDACTED")
                print(f"Got channel {message_channel}")
                await message_channel.send(f'{message.author.id}, {time}, {str(message.content)};')

            if content == ':serverlst':
                server_lst = list(client.guilds)
                await message.channel.send(f"Connected on {str(len(server_lst))} servers:")
                await message.channel.send('\n'.join(guild.name for guild in server_lst))

            if ':battlestart' in content:
                global host
                host = message.author.id
                user_dm = await client.fetch_user(host)

                try:
                    msg_lst = content.split()

                    range = int(msg_lst[1])
                    global event_num 
                    event_num = int(msg_lst[2])
                except:
                    await user_dm.send('Please input a range and a correct answer! For more info see our help section: https://reiningecho90.github.io/chances-discord-bot-public/! \n Example: :battlestart 10 5 \n Thanks for being so generous!')
                    return

                await user_dm.send('Please remember to delete your message! Don\'t want people to see the answers do we... ;)')

                global event_num_guessed
                event_num_guessed = False

                start_embed = discord.Embed(
                    title = f'<@{host.id}> has the holiday spirit! Guess the number to get a prize!',
                    description = f'Guess the number! Hint the max guess is {range}',
                    colour = discord.Colour().from_rgb(236, 79, 132)
                )

                await message.channel.send(embed = start_embed)
                print(event_num)
                await message.delete()

            if ':guess' in content and event_num_guessed == False:
                if int(content.lstrip(':guess ')) == event_num:
                    user = message.author.id
                    user_dm = await client.fetch_user(user)
                    event_num_guessed = True

                    event_end_embed = discord.Embed(
                        title = 'We Have a Winner!',
                        description = f'<@{user}> has guessed the number! Dm the host for your present!',
                        colour = discord.Colour().from_rgb(236, 79, 132)
                    )

                    
                    await message.channel.send(embed = event_end_embed)

                    await client.wait_until_ready()

                    await user_dm.send('You have won the competition. DM the host for your prize! Happy holidays and happy 2022!')

                else:
                    print('not guessed properly')
                    print(event_num)

        except ValueError:

            print(f"{author} attempted to run command with {usr_arg} as argument.")


# run client and timed script
client.run(bot_token)
