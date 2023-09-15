from settings import settings
import discord
# import * - adalah cara cepat untuk mengimpor semua file di perpustakaan
from bot_logic import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan memindahkan hak istimewa
client = discord.Client(intents=intents)


# Setelah bot siap, ia akan mencetak namanya!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Hello!'):
        await message.channel.send('Hiya! Im Military Unit so what you want Join Faction? (say to $faction)')
    elif message.content.startswith('$Emoji!'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$Combat!'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$Faction!'):
        await message.channel.send(gen_faction())
    else:
        await message.channel.send("Sorry i cant do that but you only can command $Emoji!, $Combat!, And $Faction!")

client.run(settings["TOKEN"])


