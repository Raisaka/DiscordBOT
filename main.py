# This is a sample Python script.
import discord
from discord.ext import commands
import random
from datetime import datetime

class Chucky:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

list = []
list.append(Chucky('Jafet','January, 19th'))
list.append(Chucky('Patricia','March, 17th'))
list.append(Chucky('Arturo','May, 6th'))
list.append(Chucky('Rita','May, 22nd'))
list.append(Chucky('Andy','July, 2nd'))
list.append(Chucky('Monse','September, 7th'))
list.append(Chucky('Jesus','September, 7th'))
list.append(Chucky('Karla','October, 9th'))
list.append(Chucky('Chris','October, 14th'))
list.append(Chucky('Jonathan','October, 14th'))
list.append(Chucky('Raul','October, 30th and 31st'))
list.append(Chucky('Cachu','November, 30th'))
list.append(Chucky('Daniel','December, 22nd'))
list.append(Chucky('Jared','December, 30th'))
#listDates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#dayOfTheWeek = datetime.today().weekday()

now = datetime.now()
current_time = now.strftime("%I:%M %p")

TOKEN = 'OTY5NzYwMDA1MjgyNzUwNDc0.YmyFYg.mbJa3QtmsFNE7eqV7jThQLpk9Go'

#client = discord.Client()
client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def bday(ctx, *args):
    #response = args
    response = ''
    for arg in args:
        response = response + arg
    #print(response)
    ans = ''
    for obj in list:
        #print(obj.name)
        if obj.name == response:
            ans = "Their birthday is " + obj.birthday
            #print("here")
            await ctx.channel.send(ans)
    if(ans == ''):
        await ctx.channel.send("I don't know 💀")


@client.command()
async def bing(ctx):
    await ctx.channel.send('BONG')

@client.command()
async def echo(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)

@client.command()
async def sortNames(ctx, *args):
    list = []
    for arg in args:
        list.append(arg)
    list.sort()
    await ctx.channel.send(list)

@client.command()
async def sort(ctx, *args):
    list = []
    for arg in args:
        list.append(int(arg))
    list.sort()
    await ctx.channel.send(list)

@client.command()
async def math(ctx, *args):
    res = 0
    left, mid, right = args
    if mid == '+':
        res = int(left) + int(right)
    elif mid == '-':
        res = int(left) - int(right)
    elif mid == '/':
        res = int(left) / int(right)
    elif mid == '*':
        res = int(left) * int(right)

    await ctx.channel.send(res)

@client.command()
async def quote(ctx):
    quotes = ["It doesn’t matter if you grew up without parents, and it doesn’t matter if you don’t believe in God. There’s someone out there watching over you.",
              "Stop living in the past like an old man.", "I hate waiting, but if waiting means being able to be with you I’ll wait for as long as forever.",
              "It’s not about being right or being wrong. There are more important things than that. That’s why apologies and forgiveness become necessary.",
              "I dreamed that you were a dog. And the dog was my husband. Anyway, it was the worst dream ever.",
              "Well, I’d better get back to my seat. The unmarried woman with her unmarried face is about to come to start the unmarried homeroom.",
              "A dog’s happiness is measured by how useful he is to his master.", "The thing you wished for the most, is something you’ll never get."]
    response = random.randrange(len(quotes))
    await ctx.channel.send(quotes[response] + ' - Taiga Aisaka')
@client.command()
async def spuds(ctx):
    await ctx.channel.send('SHIT 💩')
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    print('This is the message' + user_message)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    print('This is the message' + user_message)

    if message.author == client.user:#bot wont respond to itself
        return
    #intents = discord.Intents.default()
    #intents.message_content = True
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
    if user_message.lower() == 'what do you think of tottenham':
        await message.channel.send('SHIT')
        return
    if user_message.lower() == 'what do you think of shit':
        await message.channel.send('Tottenham')
        return
    if user_message.lower() == '-thank you':
        await message.channel.send('Thats alright, \nWe hate Tottenham, \nWe hate Tottenham, \nWe hate Tottenham, \nWe hate Tottenham, \nWe hate Tottenham, \nWe hate Tottenham, \nWe are the Tottenham haters')
        return

    await client.process_commands(message)#allows us to use commands :)
client.run(TOKEN)
