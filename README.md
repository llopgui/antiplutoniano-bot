# 🤖 Bot Antiplutoniano v2.0

[![Licencia: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Autor**: [llopgui](https://github.com/llopgui/) | **Versión**: 2.0.0 | **Fecha**: 28/05/2025

Un bot de Discord educativo que detecta automáticamente cuando alguien afirma que **Plutón es un planeta** y responde con información científica precisa para corregir esta misconception común.

## 🎯 Misión

Educar a las personas sobre la correcta clasificación científica de Plutón como **planeta enano**, proporcionando información basada en evidencia de manera divertida y educativa.

## ✨ Características Principales

### 🔍 Detección Inteligente

- **Patrones avanzados**: Detecta múltiples formas de expresar que Plutón es un planeta
- **Expresiones regulares**: Reconoce variaciones como "plutón", "pluton", "pluto"
- **Contexto múltiple**: Identifica referencias directas, listas de planetas, y expresiones nostálgicas

### 💬 Respuestas Categorizadas

- **🔬 Científicas**: Explicaciones basadas en criterios astronómicos oficiales
- **🎓 Educativas**: Datos curiosos y comparaciones informativas
- **😄 Humorísticas**: Respuestas divertidas para mantener el engagement
- **🤗 Comprensivas**: Respuestas empáticas para usuarios nostálgicos
- **😏 Sarcásticas**: Para situaciones que requieren un toque de humor

### ⚡ Comandos Slash

- `/pluto_fact` - Obtén datos curiosos sobre Plutón
- `/stats` - Estadísticas del bot y correcciones realizadas
- `/help` - Información completa sobre el bot

### 📊 Estadísticas

- Contador de correcciones realizadas
- Tracking de servidores y usuarios alcanzados
- Logs detallados de actividad

## 🚀 Instalación y Configuración

### Prerequisitos

- Python 3.13+
- Token de bot de Discord
- Entorno virtual (recomendado)

### Paso a Paso

1. **Clonar el repositorio**

```bash
git clone https://github.com/llopgui/antiplutoniano-bot.git
cd antiplutoniano-bot
```

2. **Configurar entorno virtual**

```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/Mac:
source .venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
Crear archivo `.env` en el directorio raíz:

```env
DISCORD_TOKEN=tu_token_de_discord_aqui
```

5. **Ejecutar el bot**

```bash
python main.py
```

## 🔧 Configuración del Bot en Discord

### Crear Aplicación de Discord

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Crea una nueva aplicación
3. Ve a la sección "Bot"
4. Crea un bot y copia el token
5. Habilita las siguientes intents:
   - Message Content Intent
   - Server Members Intent (opcional)

### Permisos Requeridos

El bot necesita los siguientes permisos:

- ✅ Send Messages
- ✅ Use Slash Commands
- ✅ Read Message History
- ✅ Send Messages in Threads (opcional)
- ✅ Use External Emojis (opcional)

### Invitar el Bot

Usa el generador de enlaces en el Developer Portal o construye manualmente:

```
https://discord.com/api/oauth2/authorize?client_id=TU_CLIENT_ID&permissions=2048&scope=bot%20applications.commands
```

## 📁 Estructura del Proyecto

```
antiplutoniano-bot/
├── main.py              # Archivo principal del bot
├── responses.py         # Sistema de respuestas y detección
├── config.py           # Configuraciones centralizadas
├── requirements.txt    # Dependencias
├── .env               # Variables de entorno (crear)
├── README.md          # Este archivo
├── CHANGELOG.md       # Historial de cambios
├── LICENSE           # Licencia del proyecto
└── INSTALL.md        # Guía de instalación detallada
```

## 🛠️ Dependencias

- **discord.py** (≥2.4.1): Biblioteca principal para Discord
- **python-dotenv** (1.0.1): Manejo de variables de entorno
- **audioop-lts**: Compatibilidad con Python 3.13

## 🎨 Ejemplos de Uso

### Detección Automática

El bot responde automáticamente a mensajes como:

- "Plutón es un planeta"
- "Los nueve planetas del sistema solar"
- "Deberían reclasificar a Plutón como planeta"
- "Extraño cuando Plutón era un planeta"

### Comandos Slash

```
/pluto_fact
> 🧊 **Dato Plutoniano**: Plutón es tan frío que el nitrógeno se congela en su superficie.

/stats
> 📊 **Estadísticas del Bot Antiplutoniano**
> 🎯 Correcciones realizadas: 42
> 🤖 Estado: Activo y vigilando

/help
> 🤖 **Bot Antiplutoniano v2.0**
> **🎯 Misión**: Educar sobre la clasificación correcta de Plutón...
```

## 🔬 Base Científica

### Criterios para ser Planeta (IAU 2006)

1. ✅ Orbitar alrededor del Sol
2. ✅ Tener suficiente masa para forma esférica
3. ❌ **Haber limpiado su órbita de otros objetos**

Plutón cumple los primeros dos criterios pero **no el tercero**, por lo que es clasificado como **planeta enano**.

### Datos sobre Plutón

- **Tamaño**: Más pequeño que la Luna terrestre
- **Masa**: Solo 18% de la masa lunar
- **Temperatura**: Hasta -230°C (-382°F)
- **Lunas**: 5 conocidas (Caronte, Nix, Hidra, Cerbero, Estigia)
- **Período orbital**: 248 años terrestres

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la **Licencia Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International**.

[![Licencia: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Esto significa que puedes:**
- ✅ **Compartir** — copiar y redistribuir el material
- ✅ **Adaptar** — remezclar, transformar y construir sobre el material

**Bajo las siguientes condiciones:**
- 📝 **Atribución** — Debes dar crédito apropiado
- 🚫 **No Comercial** — No puedes usar el material para propósitos comerciales
- 🔄 **Compartir Igual** — Si remezclas, debes distribuir bajo la misma licencia

Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🐛 Reportar Problemas

Si encuentras algún problema o tienes sugerencias:

- Abre un [Issue](https://github.com/llopgui/antiplutoniano-bot/issues)
- Incluye información detallada sobre el problema
- Proporciona pasos para reproducir el error

## 🌟 Reconocimientos

- **NASA** y **ESA** por la información científica sobre Plutón
- **Unión Astronómica Internacional (IAU)** por las definiciones oficiales
- **Comunidad de Discord.py** por la excelente documentación

---

## 🚀 ¡Mantengamos la ciencia correcta!

*"Plutón puede no ser un planeta, pero sigue siendo increíble como planeta enano."*

### 📊 Estado del Proyecto

- ✅ Funcional con Python 3.13
- ✅ Comandos slash implementados
- ✅ Detección avanzada de patrones
- ✅ Respuestas categorizadas
- ✅ Sistema de logging
- 🔄 En desarrollo activo

### 👨‍💻 Créditos
**Desarrollado por**: [llopgui](https://github.com/llopgui/)
**Fecha**: 28/05/2025
**Versión**: 2.0.0

**¿Encontraste este proyecto útil? ¡Dale una ⭐ en GitHub!**
