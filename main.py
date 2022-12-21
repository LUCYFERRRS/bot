import discord
from discord.ext import commands, tasks

from itertools import cycle
import os
import asyncio

client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

bot_status = cycle(["Im here to help", "Dont stress, u got this", "Youve got an A for being AMAZING!", "Everything going ok?"])

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")
    change_status.start()

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.command()
async def ping(ctx):
    await ctx.send("Bong!")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
             await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
	async with client:
		await load()
		await client.start("TOKEN")

asyncio.run(main()) 