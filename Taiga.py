# This is a sample Python script.
import discord
import random
from datetime import datetime


#listDates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#dayOfTheWeek = datetime.today().weekday()

now = datetime.now()
current_time = now.strftime("%I:%M %p")

TOKEN = 'OTY5NzYwMDA1MjgyNzUwNDc0.YmyFYg.mbJa3QtmsFNE7eqV7jThQLpk9Go'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:#bot wont respond to itself
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'bye bye {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(100000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'rana':
            await message.channel.send('I dont wannna know 🐸')
            return
        elif user_message.lower() == '!time':
            await message.channel.send(f'This the time {current_time}')
            return
        elif user_message.lower() == '!day':
            await message.channel.send(f'Today is {datetime.today().strftime("%A")}!')#datetime.today().strftime('%A') listDates[dayOfTheWeek]
            return

     #can be used anywhere
    if user_message.lower() == 'daniel':
        await message.channel.send('Echale Daniel, con la guitarra 😂')
        return
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return
    if user_message.lower() == "!man":
        await message.channel.send('Man shut the fuck up!')
        return
    if user_message.lower() == 'lalo':
        await message.channel.send('Whats up everybody 🤡')
        return
client.run(TOKEN)
