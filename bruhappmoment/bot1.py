import os
import discord
import requests
import json
import sqlite3

from discord import app_commands
from discord.ext import commands

TOKEN = "MY TOKEN MY PRECIOUS TOKEN"
intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix=".", intents=intents)
# tree = app_commands.CommandTree(client)

# def get_quote():
#     response = requests.get("https://api.yomomma.info/api/random")
#     json_data = json.loads(response.text)
#     quote = json_data[0]["q"] + " -" + json_data[0]["a"]
#     return quote


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

# @tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=687306498614755363))
@client.command()
async def search(ctx):
    bruh = ctx.message.content
    bruh = bruh.replace(".search", "").strip()
    print(bruh)
    bruhr = find_skin_by_name(bruh, False)
    print(bruhr)

    await ctx.send(f"searching for {bruh}: {bruhr} ")


@client.command()
async def searchst(ctx):
    bruh2 = ctx.message.content
    bruh2 = bruh2.replace(".searchst", "").strip()
    print(bruh2)
    rhubarb = find_skin_by_name(bruh2, True)
    print(rhubarb)

    await ctx.send(f"searching for ST{bruh2}: {rhubarb}")


def find_skin_by_name(name: str, is_stattrak: bool):
    print(name)
    con = sqlite3.connect("steamskinsdata.db")
    command = f"""
    SELECT name, sell_price, sell_listings
    FROM skins
    WHERE name LIKE "%{name}%"
    """
    # if is_case:
    #  command = command + """ AND name LIKE "%CASE%" """ 
    # else:
    #  command = command + """ AND name LIKE "%KEY%" """ 
    conditions = []
    for token in name.split():
     conditions.append(f'name LIKE "%{token}%"')
    where_statement = " AND ".join(conditions)
    command = f"""
    SELECT name, sell_price, sell_listings
    FROM skins
    WHERE {where_statement}
    """

    if is_stattrak:
     command = command + """ AND name LIKE "%StatTrak™%" """ 
    else:
     command = command + """ AND name NOT LIKE "%StatTrak™%" """ 
    cur = con.cursor()


    skins = cur.execute(command).fetchall()
    
    print(f" ten skin:{skins[0:]}")
    return skins

client.run(TOKEN)
