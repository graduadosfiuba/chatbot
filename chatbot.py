import discord
from  dotenv import load_dotenv
import os
import openai 


load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

openai.api_key = OPENAI_TOKEN

def chatGPT(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}],
        temperature = 0.5,
        max_tokens = 2048,        
        )
    return response.choices[0].message.content



class Cliente_bot(discord.Client):
    async def on_ready(self):
        print("cliente_bot conectado")
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("CHATGPT/"):
            await message.channel.send(chatGPT(message.content[7:]))


intents = discord.Intents.default()
intents.message_content = True
cliente_bot = Cliente_bot(intents=intents) 
cliente_bot.run(DISCORD_TOKEN)       






