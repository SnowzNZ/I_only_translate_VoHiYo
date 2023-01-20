import asyncio

import discord
from discord.ext import commands

TOKEN = (
    "MTA0NDEzNDI2MjE1ODM5NzUxMA.GT3Ah9.-dYZ6wY29J1rMIHa9mkAJHpM4WIpQoiL9Gwb80"
)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

translations = {
    1: "Yes `or` VoHiYo",
    2: "No",
    3: "Hi `or` Maybe",
    4: "bye",
    5: "Thanks `or` You're welcome",
    6: "Sorry",
    7: "Waifu",
    8: "Natsuki *`or` I'm about to spell a bit.ly link",
    9: "gunLove",
    10: "10/10",
    11: "gunLewd",
    12: "I have a question",
    13: "I'm going to spell",
    14: "I don't know",
    15: "osu",
    16: ":3",
    17: "Silly https://i.imgur.com/uVEKTT9h.jpg",
    18: "vovoLuv (see https://static-cdn.jtvnw.net/emoticons/v1/154031/3.0 for the emote)",
    19: "Sleepy",
    20: "twitch.tv",
    21: "AngryVoHiYo (see https://www.frankerfacez.com/emoticon/264508/AngryVoHiYo for the emote)",
    22: "https://cdn.discordapp.com/attachments/434454241269121025/436192133725159435/IMG_20180210_032715.jpg",
    23: "https://cdn.discordapp.com/attachments/405820421280104449/477444757019295768/ehc0dnhp99111.png",
    24: "xD",
    25: "[undiscovered]",
    26: "[undiscovered]",
    27: "I have made a mistake",
}


@client.event
async def on_ready():
    print("VoHiYo!")


# Store the count of "VoHiYo" messages
count = 0

# Store the timestamp of the last "VoHiYo" message
last_message_time = None


@client.event
async def on_message(message):
    global count, last_message_time

    # Check if the message is "VoHiYo"
    if message.content == "VoHiYo":
        count += 1
        last_message_time = message.created_at
    else:
        # Check if there hasn't been a "VoHiYo" message in the last 3 seconds
        if (
            last_message_time is not None
            and (message.created_at - last_message_time).total_seconds() > 3
        ):
            if count == 1:
                await asyncio.sleep(3)
                await message.channel.send("A")
                count = 0
                last_message_time = None


@client.command()
async def translate(ctx, *, message: str):
    print()


client.run(TOKEN)
