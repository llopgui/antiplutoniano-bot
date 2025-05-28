"""
Configuración del Bot Antiplutoniano
===================================

Este archivo contiene todas las configuraciones centralizadas del bot.

Autor: llopgui (https://github.com/llopgui/)
Versión: 2.0.1
Fecha: 28/05/2025
Licencia: CC BY-NC-SA 4.0
"""

from typing import Final, List

# Información del bot
BOT_VERSION: Final[str] = "2.0.1"
BOT_NAME: Final[str] = "Bot Antiplutoniano"
BOT_DESCRIPTION: Final[str] = "Bot educativo que corrige ideas sobre Plutón"

# Prefijo para comandos tradicionales (aunque usamos principalmente slash)
COMMAND_PREFIX: Final[str] = "!"

# Palabras clave que activan las respuestas del bot
REQUIRED_WORDS: Final[List[str]] = ["plutón", "pluton", "pluto"]

# Configuración de logging
LOG_MESSAGES: Final[bool] = True
LOG_CORRECTIONS: Final[bool] = True

# Límites y configuraciones
MAX_RESPONSE_LENGTH: Final[int] = 2000  # Límite de Discord
CORRECTION_COOLDOWN: Final[int] = 0  # Sin límite por defecto

# Emojis para diferentes tipos de respuesta
EMOJIS = {
    "science": "🔬",
    "education": "🎓",
    "humor": "😄",
    "warning": "⚠️",
    "success": "✅",
    "error": "❌",
    "stats": "📊",
    "info": "ℹ️",
    "rocket": "🚀",
    "planet": "🌌",
    "pluto": "🧊",
}

# Configuración de embed colores (en formato hexadecimal)
COLORS = {
    "primary": 0x3498DB,  # Azul
    "success": 0x2ECC71,  # Verde
    "warning": 0xF39C12,  # Naranja
    "error": 0xE74C3C,  # Rojo
    "info": 0x9B59B6,  # Púrpura
    "science": 0x1ABC9C,  # Turquesa
}
