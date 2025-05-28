"""
Bot de Discord Antiplutoniano
=============================

Este bot responde automáticamente a mensajes que contienen las palabras
"plutón" o "pluton" con respuestas predefinidas del módulo responses.
También incluye comandos slash para interacciones más avanzadas.

Autor: llopgui (https://github.com/llopgui/)
Versión: 2.0.1
Fecha: 28/05/2025
Licencia: CC BY-NC-SA 4.0
Compatibilidad: Python 3.13+ con discord.py 2.4.1+
"""

import asyncio
import logging
import os
import sys
from pathlib import Path
from typing import Final, Optional

import discord
from discord import Intents, Message
from discord.ext import commands
from dotenv import load_dotenv

from .config import (
    BOT_VERSION,
    EMOJIS,
    LOG_CORRECTIONS,
    LOG_MESSAGES,
    MAX_RESPONSE_LENGTH,
    REQUIRED_WORDS,
)
from .responses import detect_pluto_planet_claim, get_pluto_fact, get_response

# Configurar logging con soporte UTF-8 para Windows
try:
    # Para Windows, configurar la codificación UTF-8
    import io

    # Configurar stdout/stderr para UTF-8
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("bot.log", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
        force=True,  # Sobrescribir configuración existente
    )
except Exception as e:
    # Fallback sin emojis si hay problemas con UTF-8
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )

logger = logging.getLogger(__name__)


# PASO 0: CARGAR CONFIGURACIÓN DE FORMA SEGURA
def load_environment() -> str:
    """
    Carga y valida las variables de entorno de forma segura.

    Returns:
        str: Token de Discord validado

    Raises:
        ValueError: Si el token no es válido o está ausente
    """
    # Buscar archivo .env en el directorio padre
    env_path = Path(__file__).parent.parent.parent / ".env"
    load_dotenv(env_path, override=True)

    token = os.getenv("DISCORD_TOKEN")

    if not token:
        raise ValueError(
            "❌ Token de Discord no encontrado. "
            "Verifica que el archivo .env contenga DISCORD_TOKEN."
        )

    # Validación básica del formato del token
    if (
        len(token) < 50
        or not token.replace(".", "")
        .replace("-", "")
        .replace("_", "")
        .isalnum()
    ):
        raise ValueError(
            "❌ El token de Discord parece inválido. "
            "Verifica que sea un token válido de Discord."
        )

    logger.info("✅ Token de Discord cargado correctamente")
    return token


# Configurar el bot con mejoras de seguridad
class AntiplutonianoBot(commands.Bot):
    """Bot Antiplutoniano con funcionalidades mejoradas."""

    def __init__(self):
        # Configurar intents de forma segura
        intents = Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None,  # Usaremos nuestro comando personalizado
            case_insensitive=True,
            strip_after_prefix=True,
        )

        self.corrections_made = 0
        self.start_time = None

    async def setup_hook(self):
        """Configuración inicial del bot."""
        logger.info("🔧 Configurando bot...")
        self.start_time = discord.utils.utcnow()

        # Sincronizar comandos slash
        try:
            synced = await self.tree.sync()
            logger.info(f"🔄 Sincronizados {len(synced)} comandos slash")
        except Exception as e:
            logger.error(f"❌ Error al sincronizar comandos: {e}")


# Instancia global del bot
bot = AntiplutonianoBot()


# PASO 2: FUNCIONALIDAD DE MENSAJES MEJORADA
async def send_message(message: Message, user_message: str) -> None:
    """
    Procesa y responde a un mensaje del usuario si contiene referencias
    a Plutón.

    Args:
        message (Message): El objeto mensaje de Discord
        user_message (str): El contenido del mensaje del usuario

    Returns:
        None
    """
    if not user_message:
        logger.warning("Mensaje vacío recibido")
        return

    # Verificar si contiene palabras clave de Plutón
    if not any(word in user_message.lower() for word in REQUIRED_WORDS):
        return

    # Verificar si es un mensaje privado (comienza con "?")
    is_private: bool = user_message.startswith("?")
    if is_private:
        user_message = user_message[1:]

    try:
        # Obtener respuesta del módulo responses mejorado
        response: str = get_response(user_message)

        # Truncar respuesta si es muy larga
        if len(response) > MAX_RESPONSE_LENGTH:
            response = response[: MAX_RESPONSE_LENGTH - 3] + "..."

        # Si se detectó una afirmación pro-Plutón, incrementar contador
        if detect_pluto_planet_claim(user_message):
            bot.corrections_made += 1
            if LOG_CORRECTIONS:
                logger.info(f"📊 Corrección #{bot.corrections_made} realizada")

        await send_response(message, response, is_private)

        # Log de actividad
        if LOG_MESSAGES:
            username = str(message.author)
            channel = str(message.channel)
            logger.info(f"🎯 Respuesta enviada a {username} en {channel}")

    except discord.Forbidden:
        logger.warning("❌ Sin permisos para enviar mensaje")
    except discord.HTTPException as e:
        logger.error(f"❌ Error HTTP al enviar mensaje: {e}")
    except Exception as e:
        logger.error(f"❌ Error inesperado: {e}")


async def send_response(
    message: Message, response: str, is_private: bool
) -> None:
    """
    Envía la respuesta al canal apropiado (público o privado).

    Args:
        message (Message): El objeto mensaje original
        response (str): La respuesta a enviar
        is_private (bool): Si la respuesta debe ser privada

    Returns:
        None
    """
    try:
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except discord.Forbidden:
        logger.warning("Sin permisos para enviar mensaje")
    except discord.HTTPException as e:
        logger.error(f"Error HTTP: {e}")
    except Exception as e:
        logger.error(f"Error al enviar respuesta: {e}")


# PASO 3: COMANDOS SLASH MEJORADOS
@bot.tree.command(
    name="pluto_fact", description="Obtén un dato curioso sobre Plutón"
)
async def pluto_fact_command(interaction: discord.Interaction):
    """Comando para obtener datos curiosos sobre Plutón."""
    try:
        fact = get_pluto_fact()
        await interaction.response.send_message(fact)
        logger.info(f"💡 Dato de Plutón enviado a {interaction.user}")
    except Exception as e:
        logger.error(f"Error en comando pluto_fact: {e}")
        await interaction.response.send_message(
            "❌ Error al obtener dato de Plutón", ephemeral=True
        )


@bot.tree.command(name="stats", description="Ver estadísticas del bot")
async def stats_command(interaction: discord.Interaction):
    """Comando para ver estadísticas del bot."""
    try:
        # Calcular usuarios alcanzados de forma segura
        total_users = sum(guild.member_count or 0 for guild in bot.guilds)

        # Calcular uptime
        uptime = "Desconocido"
        if bot.start_time:
            delta = discord.utils.utcnow() - bot.start_time
            hours, remainder = divmod(int(delta.total_seconds()), 3600)
            minutes, _ = divmod(remainder, 60)
            uptime = f"{hours}h {minutes}m"

        embed = discord.Embed(
            title=f"{EMOJIS['stats']} Estadísticas del Bot Antiplutoniano",
            color=0x3498DB,
            timestamp=discord.utils.utcnow(),
        )
        embed.add_field(
            name="🎯 Correcciones", value=bot.corrections_made, inline=True
        )
        embed.add_field(
            name="🌌 Servidores", value=len(bot.guilds), inline=True
        )
        embed.add_field(name="👥 Usuarios", value=total_users, inline=True)
        embed.add_field(name="⏱️ Uptime", value=uptime, inline=True)
        embed.add_field(name="🔧 Versión", value=BOT_VERSION, inline=True)
        embed.add_field(
            name="🐍 Python",
            value=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            inline=True,
        )
        embed.set_footer(text="💡 Usa /pluto_fact para datos curiosos")

        await interaction.response.send_message(embed=embed)
        logger.info(f"📊 Stats enviadas a {interaction.user}")

    except Exception as e:
        logger.error(f"Error en comando stats: {e}")
        await interaction.response.send_message(
            "❌ Error al obtener estadísticas", ephemeral=True
        )


@bot.tree.command(name="help", description="Información sobre el bot")
async def help_command(interaction: discord.Interaction):
    """Comando de ayuda mejorado."""
    try:
        embed = discord.Embed(
            title="🤖 Bot Antiplutoniano v2.0",
            description="Educando sobre la correcta clasificación de Plutón",
            color=0x1ABC9C,
            timestamp=discord.utils.utcnow(),
        )

        embed.add_field(
            name="🎯 Misión",
            value="Educar sobre Plutón como planeta enano",
            inline=False,
        )

        embed.add_field(
            name="⚡ Funcionamiento",
            value=(
                "• Respondo cuando mencionas que Plutón es un planeta\n"
                "• Proporciono información científica actualizada\n"
                "• Ofrezco datos curiosos sobre Plutón"
            ),
            inline=False,
        )

        embed.add_field(
            name="🛠️ Comandos",
            value=(
                "`/pluto_fact` - Dato curioso sobre Plutón\n"
                "`/stats` - Estadísticas del bot\n"
                "`/help` - Esta ayuda"
            ),
            inline=False,
        )

        embed.add_field(
            name="📚 Palabras clave",
            value='"plutón", "pluton", "pluto"',
            inline=False,
        )

        embed.set_footer(
            text="👨‍💻 Creado por llopgui | 📄 Licencia: CC BY-NC-SA 4.0"
        )

        await interaction.response.send_message(embed=embed)
        logger.info(f"ℹ️ Ayuda enviada a {interaction.user}")

    except Exception as e:
        logger.error(f"Error en comando help: {e}")
        await interaction.response.send_message(
            "❌ Error al mostrar ayuda", ephemeral=True
        )


# PASO 4: EVENTOS DEL BOT MEJORADOS
@bot.event
async def on_ready() -> None:
    """Evento que se ejecuta cuando el bot se conecta exitosamente."""
    if bot.user is not None:
        logger.info("🚀" + "=" * 50)
        logger.info(f"🤖 {bot.user} está en funcionamiento!")
        logger.info(f"📝 ID del bot: {bot.user.id}")
        logger.info(f"🔍 Palabras clave: {', '.join(REQUIRED_WORDS)}")
        logger.info(f"🌌 Conectado a {len(bot.guilds)} servidores")
        logger.info("👨‍💻 Creado por: llopgui")
        logger.info("✅ Bot listo para defender la ciencia!")
        logger.info("=" * 52)


@bot.event
async def on_message(message: Message) -> None:
    """Evento que se ejecuta cada vez que se recibe un mensaje."""
    # Ignorar mensajes del propio bot y de otros bots
    if message.author.bot:
        return

    # Procesar comandos primero
    await bot.process_commands(message)

    # Obtener información del mensaje
    user_message: str = message.content

    # Log del mensaje recibido (solo si contiene palabras clave)
    if any(word in user_message.lower() for word in REQUIRED_WORDS):
        if LOG_MESSAGES:
            logger.info(
                f'📨 [{message.channel}] {message.author}: "{user_message}"'
            )

        # Procesar el mensaje
        await send_message(message, user_message)


@bot.event
async def on_guild_join(guild):
    """Evento cuando el bot se une a un nuevo servidor."""
    logger.info(f"🎉 Nuevo servidor: {guild.name} ({guild.id})")
    logger.info(f"👥 Miembros: {guild.member_count}")


@bot.event
async def on_guild_remove(guild):
    """Evento cuando el bot es removido de un servidor."""
    logger.info(f"😢 Removido de: {guild.name} ({guild.id})")


@bot.event
async def on_error(event, *args, **kwargs):
    """Manejo de errores globales."""
    logger.error(f"❌ Error en evento {event}: {args}", exc_info=True)


@bot.event
async def on_command_error(ctx, error):
    """Manejo de errores de comandos."""
    logger.error(f"❌ Error en comando: {error}")


# PASO 5: PUNTO DE ENTRADA PRINCIPAL MEJORADO
async def main_async() -> None:
    """Función principal asíncrona."""
    try:
        token = load_environment()
        logger.info("🚀 Iniciando Bot Antiplutoniano v2.0...")
        logger.info("👨‍💻 Creado por: llopgui")
        logger.info("📄 Licencia: CC BY-NC-SA 4.0")
        logger.info("🔬 Sistema de detección: ACTIVADO")
        logger.info("⚡ Comandos slash: HABILITADOS")
        logger.info("🔒 Modo seguro: ACTIVADO")

        async with bot:
            await bot.start(token)

    except KeyboardInterrupt:
        logger.info("🛑 Bot detenido por el usuario")
    except Exception as e:
        logger.error(f"❌ Error crítico: {e}")
        raise


def main() -> None:
    """Función principal que inicia el bot."""
    try:
        if sys.version_info < (3, 8):
            raise RuntimeError("❌ Python 3.8+ requerido")

        asyncio.run(main_async())
    except KeyboardInterrupt:
        logger.info("👋 ¡Hasta luego!")
    except Exception as e:
        logger.error(f"❌ Error al iniciar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
