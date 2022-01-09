import discord
from discord.ext import commands
import OpenAi
intents = discord.Intents().all()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

responses = 0
list_user = []

@client.event
async def on_message(message):
    if message.channel.id == message.author.dm_channel.id: # dm only
        #await message.channel.send('ping')
        list_user.append(message.author.id)
        question = message.content
        answer = OpenAi.ask(question)
        await message.channel.send(answer)


@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()


client.run("discord token")
