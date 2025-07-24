from logic import Pokemon
import os
from dotenv import load_dotenv
import requests

import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.environ.get("DISCORD_BOT")
CURRENCY_API_KEY = os.environ.get("CURRENCY_API_KEY")

izinler = discord.Intents.all()
izinler.message_content = True
izinler.members = True


piton = commands.Bot(command_prefix="/", intents=izinler)

@piton.event
async def on_ready():
    print(f"{piton.user.name} is ready")

@piton.event
async def on_message(msg):
    if msg.author.bot:
        return
    if "http" in msg.content:
        await msg.delete()
        await msg.guild.ban(msg.author, reason="Reklam")


    await piton.process_commands(msg)

@piton.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        await channel.send(f"Hoş geldiniz, {member.mention}!")
        break

@piton.command()
async def merhaba(ctx):
    await ctx.send("Merhaba!")

@piton.command()
async def naber(ctx):
    await ctx.send("İyidir Senden?")

@piton.command()
async def add(ctx, a: float, b: float):
    await ctx.send(f"{a} + {b} = {a + b}")

@piton.command("at")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    if member:
        if ctx.author.top_role <= member.top_role:
            await ctx.send("Senden büyüğü atamazsın")
        else:
            await ctx.guild.ban(member)
            await ctx.send(f"{member.name} atıldı")

# @piton.command("go")
# async def go(ctx):
#     author = ctx.author.name
#     if author not in Pokemon.pokemons.keys():
#         pokemon = Pokemon(author)
#         image_url = await pokemon.show_img()
#         if image_url:
#             embed = discord.Embed()
#             embed.set_image(url=image_url)
#             await ctx.send(embed=embed)
#         else:
#             await ctx.send("Pokémonun görüntüsü yüklenemedi!")
#     else:
#         await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")


@piton.command("go")
async def go(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)
        pokemon.set_stats()
        Pokemon.pokemons[author] =pokemon
        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")

@piton.command()
async def attack(ctx):
    target =ctx.message.mentions[0] if ctx.message.mentions else None
    if target:
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy =Pokemon.pokemons[target.name]
            attacker =Pokemon.pokemons[ctx.author.name]
            result = await attacker.perform_attack(enemy)
            await ctx.send(result)
        else: 
            return



@piton.command()
async def kur(ctx):
    url = "https://api.currencyapi.com/v3/latest?base_currency=USD&currencies=TRY"
    headers = {'apikey': CURRENCY_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    rate = data["data"]["TRY"]["value"]
    await ctx.send(f"1 DOLAR = {rate:.2f} TL")

piton.run(TOKEN)
