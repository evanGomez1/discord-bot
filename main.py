import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="bienvenidas")
    if canal:
        embed = discord.Embed(
            title="🎉 Nuevo miembro",
            description=f"Bienvenido {member.mention} al servidor.\nAhora somos **{member.guild.member_count}** miembros.",
            color=discord.Color.green()
        )
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        await canal.send(embed=embed)

bot.run(os.getenv("TOKEN"))
