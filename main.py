from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# PASO 0: CARGAR NUESTRO TOKEN DE UN LUGAR SEGURO
load_dotenv(override=True)
TOKEN = os.getenv('DISCORD_TOKEN')

# PASO 1: CONFIGURACIÓN DEL BOT
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# PASO 2: FUNCIONALIDAD DE MENSAJES
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(El mensaje estaba vacío probablemente porque los intents no estaban habilitados)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        # Usa directamente get_response() para manejar todas las respuestas, incluidas las menciones a "Plutón"
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)


# PASO 3: MANEJANDO EL INICIO DE NUESTRO BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} está en funcionamiento!')


# PASO 4: MANEJO DE MENSAJES ENTRANTE
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# PASO 5: PUNTO DE ENTRADA PRINCIPAL
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()