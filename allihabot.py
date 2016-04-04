import discord
import asyncio
import sys
import urllib.request
import os.path

client = discord.Client()
prefix = "_"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        messageSplit = message.content.split()
        command = messageSplit[0][1:]
        await handle_command(command, message, messageSplit)

async def handle_command(command, message, messageSplit):

    if command == 'help':
        await client.send_message(message.channel, '_addimage [url] [name] will create a command for the image at the url\
                                                        \n_[name] will showcase that image\
                                                        \n_quit will make the bot leave the server and stop the script')

    #if command == 'test':
    #    counter = 0
    #    tmp = await client.send_message(message.channel, 'Calculating messages...')
    #    async for log in client.logs_from(message.channel, limit=100):
    #        if log.author == message.author:
    #            counter += 1
    #    await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif command == 'what':
        await client.send_file(message.channel, 'img\what.png')

    elif command == 'addimage':
        urllib.request.urlretrieve(messageSplit[1], 'img\\' + messageSplit[2] + '.png')

    #elif command == 'sleep':
    #    await asyncio.sleep(5)
    #    await client.send_message(message.channel, 'Done sleeping')

    elif command == 'quit':
        #await client.send_message(message.channel, 'Bye-bye')
        sys.exit(1)

    else:
        if os.path.isfile('img\\' + command + '.png'):
            await client.send_file(message.channel, 'img\\' + command + '.png')

client.run('botemail', 'botpassword')
