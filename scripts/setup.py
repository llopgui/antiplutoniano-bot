#!/usr/bin/env python3
"""
Script de Configuración Inicial
==============================

Script para configurar el entorno de desarrollo del Bot Antiplutoniano.

Autor: llopgui (https://github.com/llopgui/)
Licencia: CC BY-NC-SA 4.0
"""

import subprocess
import sys
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """
    Ejecuta un comando y maneja errores.

    Args:
        command: Comando a ejecutar
        description: Descripción de lo que hace el comando

    Returns:
        bool: True si el comando fue exitoso
    """
    print(f"📋 {description}...")
    try:
        subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e.stderr}")
        return False


def check_python_version() -> bool:
    """Verifica que la versión de Python sea compatible."""
    print("🐍 Verificando versión de Python...")

    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ es requerido")
        print(f"   Versión actual: {sys.version}")
        return False

    version_str = (
        f"{sys.version_info.major}.{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )
    print(f"✅ Python {version_str} es compatible")
    return True


def setup_virtual_environment() -> bool:
    """Configura el entorno virtual."""
    venv_path = Path(".venv")

    if venv_path.exists():
        print("ℹ️  Entorno virtual ya existe")
        return True

    return run_command("python -m venv .venv", "Creando entorno virtual")


def install_dependencies() -> bool:
    """Instala las dependencias del proyecto."""
    commands = [
        ("pip install --upgrade pip", "Actualizando pip"),
        (
            "pip install -r requirements.txt",
            "Instalando dependencias de producción",
        ),
        (
            "pip install -r requirements-dev.txt",
            "Instalando dependencias de desarrollo",
        ),
    ]

    for command, description in commands:
        if not run_command(command, description):
            return False

    return True


def create_env_file() -> bool:
    """Crea el archivo .env si no existe."""
    env_file = Path(".env")

    if env_file.exists():
        print("ℹ️  Archivo .env ya existe")
        return True

    env_template = """# Variables de entorno para el Bot Antiplutoniano
# Reemplaza 'tu_token_de_discord_aqui' con tu token real

DISCORD_TOKEN=tu_token_de_discord_aqui

# Configuraciones opcionales
# LOG_LEVEL=INFO
# MAX_RESPONSE_LENGTH=2000
# ENABLE_LOGGING=true
"""

    try:
        env_file.write_text(env_template)
        print("✅ Archivo .env creado")
        print("⚠️  IMPORTANTE: Edita .env y agrega tu token de Discord")
        return True
    except Exception as e:
        print(f"❌ Error creando .env: {e}")
        return False


def setup_git_hooks() -> bool:
    """Configura los git hooks."""
    if Path(".git").exists():
        return run_command("pre-commit install", "Configurando git hooks")
    else:
        print("ℹ️  No es un repositorio git, saltando git hooks")
        return True


def run_tests() -> bool:
    """Ejecuta los tests para verificar la instalación."""
    return run_command(
        "python -m pytest tests/ -v", "Ejecutando tests de verificación"
    )


def main() -> None:
    """Función principal del script de configuración."""
    print("🚀 Configurando Bot Antiplutoniano")
    print("=" * 50)

    steps = [
        ("Verificar Python", check_python_version),
        ("Configurar entorno virtual", setup_virtual_environment),
        ("Instalar dependencias", install_dependencies),
        ("Crear archivo .env", create_env_file),
        ("Configurar git hooks", setup_git_hooks),
        ("Ejecutar tests", run_tests),
    ]

    for step_name, step_func in steps:
        print(f"\n📋 {step_name}")
        if not step_func():
            print(f"❌ Fallo en: {step_name}")
            print(
                "💡 Revisa los errores arriba y ejecuta el script "
                "nuevamente"
            )
            sys.exit(1)

    print("\n" + "=" * 50)
    print("🎉 ¡Configuración completada exitosamente!")
    print("\n📝 Próximos pasos:")
    print("1. Edita el archivo .env con tu token de Discord")
    print("2. Ejecuta: python run.py")
    print("3. ¡Tu bot está listo!")
    print("\n💡 Para desarrollo, usa: pip install -e .")


if __name__ == "__main__":
    main()
