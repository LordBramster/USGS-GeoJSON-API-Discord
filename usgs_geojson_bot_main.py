import discord
from discord.ext import commands
from discord import app_commands
import random
import json
import usgs_geojson_bot_secret as usgs_bot_secret
import usgs_geojson_api as usgs_api
from datetime import datetime

DISCORD_BOT_TOKEN = usgs_bot_secret.TOKEN
USGS_API_QUERY_URL = usgs_api.api_get_query_url()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# EVENT: BOT READY
@bot.event
async def on_ready():
    print(f'READY :: {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"SYNC :: {len(synced)} commands")
    except Exception as err:
        print(err)


# CMD: QUAKES
@bot.command(name='quakes', help='Responds with Earthquakes in the last 24hours.')
async def quake(ctx):  # *, magnitude: str = None, interval: str = None):
    """ Responds with Earthquakes in an embed message. """

    arguments = "&starttime=now-1days"
    default_limit = 50
    default_arguments = f"&limit={default_limit}&orderby=time"

    USGS_API_QUERY_URL_ARGS = f"{USGS_API_QUERY_URL}{default_arguments}{arguments}"
    print(f"Query :: {USGS_API_QUERY_URL_ARGS}")

    api_raw = usgs_api.api_retrieve_feed(USGS_API_QUERY_URL_ARGS)
    quake_list, quake_str = usgs_api.geojson_get_quakes_titles(api_raw)

    send_embed_title = f'Earthquakes'
    send_embed_desc = f'{quake_str}'
    send_embed_color = discord.Color(int('B346F9', 16))

    if len(quake_list) >= default_limit:
        send_embed_desc += f'\n\n***Earthquake quantity exceeds limit of {default_limit}*** :warning:'

    emb = discord.Embed(title=send_embed_title, description=send_embed_desc, color=send_embed_color)
    await ctx.send(embed=emb)
    print(f"Sent :: {emb}")


# CMD: EARTHQUAKES
@bot.command(name='earthquakes', help='https://earthquake.usgs.gov/fdsnws/event/1/#parameters')
async def quake(ctx, *args):
    """ Responds with Earthquakes in an embed message. """
    print(args)
    arguments = ""
    default_limit = 50
    default_arguments = f"&limit={default_limit}"
    if args is not None:
        for parameter in args:
            arguments += f"&{parameter.split('=')[0]}={parameter.split('=')[1]}"

    USGS_API_QUERY_URL_ARGS = f"{USGS_API_QUERY_URL}{default_arguments}{arguments}"
    print(f"Query :: {USGS_API_QUERY_URL_ARGS}")

    api_raw = usgs_api.api_retrieve_feed(USGS_API_QUERY_URL_ARGS)
    quake_list, quake_str = usgs_api.geojson_get_quakes(api_raw)

    send_embed_title = f'Earthquakes'
    send_embed_desc = f'{quake_str}'
    send_embed_color = discord.Color(int('00CC99', 16))
    send_message_content = ''  # f'{USGS_API_QUERY_URL_ARGS}'

    if len(quake_list) >= default_limit:
        send_embed_desc += f'\n\n***Earthquake quantity exceeds limit of {default_limit}*** :warning:'

    emb = discord.Embed(title=send_embed_title, description=send_embed_desc, color=send_embed_color)
    await ctx.send(send_message_content, embed=emb)
    print(f"Sent :: {emb}")


'''
# EMBEDS OPTIONAL ADDITIONS
# Set the author of the embed (optional)
# embed.set_author(name="Game Bot")

# Set a thumbnail (optional)
# embed.set_thumbnail(url="https://example.com/thumbnail.png")

# Add additional fields if needed
# embed.add_field(name="Field Name", value="Field Value", inline=False)

# SLASH COMMAND
@bot.tree.command(name="quakes", description="Get today's earthquakes.")
async def quakes(interaction: discord.Interaction):
    """ Responds with an Earthquake using GeoJSON and USGS API as an embed message. """
    arguments = "&starttime=now-1days"
    default_arguments = "&limit=50"

    USGS_API_QUERY_URL_ARGS = f"{USGS_API_QUERY_URL}{default_arguments}{arguments}"
    print(USGS_API_QUERY_URL_ARGS)

    api_raw = usgs_api.api_retrieve_feed(USGS_API_QUERY_URL_ARGS)
    quake_list, quake_str = usgs_api.geojson_get_quakes(api_raw)

    send_embed_title = f'Earthquakes'
    send_embed_desc = f'{quake_str}'
    send_embed_color = discord.Color(int('B346F9', 16))

    emb = discord.Embed(title=send_embed_title, description=send_embed_desc, color=send_embed_color)
    # await interaction.response.send_message("command")
    await interaction.response.send_message(embed=emb, ephemeral=False)
'''

bot.run(DISCORD_BOT_TOKEN)
