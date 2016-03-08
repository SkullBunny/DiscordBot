import discord
import asyncio
import config
import userhelper

client = discord.Client()
uh = userhelper.userhelper(client)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!poop'):
        await client.send_message(message.channel, 'Pooping...')
    elif message.content.startswith('!bruce'):
        member = uh.getUser("roxas")
        for channel in client.get_all_channels():
            if channel.name == "afk":
                await client.move_member(member, channel)

client.run(config.USERNAME, config.PASSWORD)