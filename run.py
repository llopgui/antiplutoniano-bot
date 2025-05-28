#!/usr/bin/env python3
"""
Bot Antiplutoniano - Launcher
=============================

Script principal para ejecutar el Bot Antiplutoniano.

Autor: llopgui (https://github.com/llopgui/)
Versión: 2.0.1
Fecha: 28/05/2025
Licencia: CC BY-NC-SA 4.0
"""

import sys
from pathlib import Path

# Agregar src al path para imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from bot.main import main

    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("💡 Asegúrate de haber instalado las dependencias:")
    print("   pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    sys.exit(1)
