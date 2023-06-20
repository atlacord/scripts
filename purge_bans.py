import os
import discord
from dotenv import load_dotenv
load_dotenv()

from ignored_members import ignored_members

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('zhu li, do the thing!'):
        await message.channel.send('o7')
        await purge_bans()

async def purge_bans():
    # Fetches bans from the Lake Laogai server, and unbans all users who are not part of the Ignored Member list.
    print('Unbanning users from Lake Laogai.')
    guild = client.get_guild(736344840253472830)
    bans = [entry async for entry in guild.bans(limit=2000)]
    for ban in bans:
        if ban.user.id in ignored_members:
            print(f'Ignoring {ban.user}, they will not be unbanned.')
            continue
        print(f'Unbanning {ban.user}.')
        await guild.unban(ban.user)

client.run(TOKEN)