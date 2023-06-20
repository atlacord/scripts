import os
import discord
from dotenv import load_dotenv
load_dotenv()

from ignored_members import ignored_members

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')
    await purge()

async def purge():
    guild = client.get_guild(736344840253472830)
    print(guild)
    bans = [entry async for entry in guild.bans(limit=2000)]
    for ban in bans:
        if ban.user.id in ignored_members:
            print(f'Ignoring {ban.user}.')
        guild.unban(ban.user, 'Given another chance to appeal.')

client.run(TOKEN)