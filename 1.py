import discord
from discord.ext import commands
from discord.ui import Button, View
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@bot.command()
async def rules(ctx):
    embed = discord.Embed(
        title="Welcome to Psycho Battlegrounds!",
        description=(
            "To ensure a safe and enjoyable environment for everyone, we have created a detailed list of rules below. "
            "Please make sure to read through all the sections so that you know what is allowed and not allowed here.\n\n"
            "This is primarily an English-speaking server, so please avoid speaking in any other language. "
            "We want to create a safe and enjoyable environment, which is only possible if our moderators know and understand what you are saying;so sorry for inconvenience.\n\n"
            "**NOTICE**\n"
            ">Please do note that the Server Rules  are just a general idea of punishments. Based off the severity of situation, staff members may alter given punishments at their own discretion."
        ),
        color=0x2F3136
    )
    view = View()
    view.add_item(Button(label="Important", style=discord.ButtonStyle.danger, emoji="\U0001F6A8", custom_id="important"))
    view.add_item(Button(label="Warning System", style=discord.ButtonStyle.primary, emoji="\u26A0\uFE0F", custom_id="warning"))
    await ctx.send(embed=embed, view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component:
        custom_id = interaction.data.get("custom_id")
        if custom_id == "important":
            await interaction.response.send_message(
                "**Important**\n"
                ">All members, including staff and contributors, must follow rules.\n"
                ">Staff have the final say. Do not argue.\n"
                ">Do not try to loophole rules.\n"
                "Speak in English only for moderation clarity.",
                ephemeral=True
            )
        elif custom_id == "warning":
            await interaction.response.send_message(
                "**Warning System**\n"
                "1st Warning = No Punishment\n"
                "2nd Warning = 30 Minute Mute\n"
                "3rd Warning = 2 Hour Mute\n"
                "4th Warning = 4 Hour Mute\n"
                "5th Warning = 12 Hour Mute\n"
                "6th Warning = 7 Day Mute",
                ephemeral=True
            )

bot_token = os.getenv("MTM4MzAwODQ2ODgxODIwMjY1NA.GkCJUJ.Ss1r5RDzPer3jL-fYuQsIrSJMqa0wTi3-W6a_8")
if not bot_token:
    raise ValueError("DISCORD_BOT_TOKEN environment variable not set.")
bot.run(bot_token)