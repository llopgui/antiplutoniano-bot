from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# PASO 0: CARGAR NUESTRO TOKEN DE UN LUGAR SEGURO
load_dotenv(override=True)
TOKEN = os.getenv("DISCORD_TOKEN")
# Verificar si el token fue cargado correctamente
if not TOKEN:
    raise ValueError(
        "El token de Discord no se ha encontrado en las variables de entorno."
    )

# PASO 1: CONFIGURACIÓN DEL BOT
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)
# Lista de palabras requeridas
REQUIRED_WORDS = ["plutón", "pluton"]


# PASO 2: FUNCIONALIDAD DE MENSAJES
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print(
            "(El mensaje estaba vacío probablemente porque los intents no estaban habilitados)"
        )
        return

    # Si el mensaje no contiene REQUIRED_WORDS, no se responde.
    if not any(word in user_message.lower() for word in REQUIRED_WORDS):
        return

    is_private = user_message.startswith("?")
    if is_private:
        user_message = user_message[1:]

    try:
        # Usa directamente get_response() para manejar todas las respuestas"
        response: str = get_response(user_message)
        await send_response(message, response, is_private)
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")


async def send_response(message: Message, response: str, is_private: bool) -> None:
    try:
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")


# PASO 3: MANEJANDO EL INICIO DE NUESTRO BOT
@client.event
async def on_ready() -> None:
    print(f"{client.user} está en funcionamiento! ID: {client.user.id}")


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
    client.run(TOKEN)


if __name__ == "__main__":
    main()
