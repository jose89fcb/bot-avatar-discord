import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help


@bot.command()
async def avatar(ctx, *, member:discord.Member =None):
    if member == None:
            member = ctx.message.author

    await ctx.send(member.avatar_url)






@bot.event
async def on_ready():
    print("BOT listo!")


 
 
 
bot.run('')    #Crea un Token en => https://discord.com/developers/applications
