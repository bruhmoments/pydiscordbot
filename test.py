import discord
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = '' #Get your token at https://discordapp.com/developers/applications/
client = commands.Bot(command_prefix = '') #MESSAGE PREFIX TO BE SEEN AS COMMANDS 

@client.event
async def on_ready():
    print('Ready!')
    
@client.command(pass_context=True)
async def test(ctx): #COMMAND test (e.g !test)
    channel = ctx.message.channel #Get the chat channel
    e = discord.Embed(title='Made in Heaven') #Message title
    await channel.send(embed=e, file=discord.File('')) #Embedding file/image 
    await channel.send("Sent by @"+str(ctx.message.author)) #Sending message

client.run(TOKEN)