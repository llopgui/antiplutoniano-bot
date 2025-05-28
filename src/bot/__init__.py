"""
Bot Antiplutoniano Package
=========================

Paquete principal del Bot Antiplutoniano.

Autor: llopgui (https://github.com/llopgui/)
Licencia: CC BY-NC-SA 4.0
"""

__version__ = "2.0.0"
__author__ = "llopgui"
__license__ = "CC BY-NC-SA 4.0"

from .config import BOT_NAME, BOT_VERSION
from .main import main
from .responses import detect_pluto_planet_claim, get_pluto_fact, get_response

__all__ = [
    "main",
    "get_response",
    "detect_pluto_planet_claim",
    "get_pluto_fact",
    "BOT_VERSION",
    "BOT_NAME",
]
