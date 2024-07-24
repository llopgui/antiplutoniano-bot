# Instalación

Este documento proporciona instrucciones detalladas sobre cómo instalar y configurar el proyecto en tu entorno local.

## Requisitos previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

Antes de comenzar, asegúrate de tener instalado Python 3.12 o una versión superior en tu sistema. Puedes verificar la versión de Python con el siguiente comando:

```bash
python --version

o

python3 --version
```

Si Python no está instalado, visita python.org para descargar e instalar la versión adecuada para tu sistema operativo.

# Clonar el repositorio
Primero, deberás clonar el repositorio de GitHub en tu máquina local. Puedes hacerlo con el siguiente comando:

Asegúrate de reemplazar https://github.com/llopgui/antiplutoniano-bot con la URL actual del repositorio de GitHub.

# Instalar dependencias
Navega hasta el directorio del proyecto clonado y ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Este comando instalará las siguientes bibliotecas requeridas para el proyecto:

- discord.py: Una biblioteca de Python para interactuar con la API de Discord.
- python-dotenv: Una biblioteca de Python para cargar variables de entorno desde un archivo .env.

# Configurar variables de entorno
Crea un archivo .env en el directorio raíz del proyecto y agrega las siguientes variables de entorno:

Asegúrate de reemplazar your_discord_bot_token_here con tu token real de Discord.

# Ejecutar el bot
Una vez completados los pasos anteriores, estás listo para ejecutar el bot. Hazlo con el siguiente comando:

```bash
python main.py

o

python3 main.py
```

¡Eso es todo! Tu bot de Discord debería estar funcionando correctamente.

Este archivo INSTALL.md proporciona una guía paso a paso para que los usuarios configuren el proyecto desde cero, asegurándose de tener todas las herramientas y dependencias necesarias para ejecutar el proyecto sin problemas.

