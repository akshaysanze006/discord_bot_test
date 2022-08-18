import discord
import random
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client =discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_messaage(message):
    username = str(message.auther).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message}({channel})')
    if message.auther == client.user:
        return
    if message.channel.name == 'bot_test':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'see you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number:{random.randrange(100000)}'
            await message.channel.send(response)
            return
        if user_message.lower() == '!anywhere':
            await  message.channel.send('This can be used anywhere!')
            return


    client.run(TOKEN)
