# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Autor**: [llopgui](https://github.com/llopgui/) | **Licencia**: CC BY-NC-SA 4.0

## [2.0.1] - 2025-01-28

### 🔧 Cambiado
- **Información del autor**: Actualizada con información real (llopgui)
- **Licencia**: Cambiada a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
- **URLs del repositorio**: Actualizadas a github.com/llopgui/antiplutoniano-bot
- **Documentación**: Mejorada con badges de licencia y créditos apropiados

### 🐛 Corregido
- **Comandos slash**: Corregido error de tipo en comando `/stats`
- **Imports**: Limpieza de imports no utilizados
- **Linter**: Corrección de algunos errores de formato

---

## [2.0.0] - 2025-01-28

### 🚀 Agregado
- **Sistema de detección avanzado**: Patrones de expresiones regulares para detectar múltiples formas de afirmar que Plutón es un planeta
- **Comandos slash**: `/pluto_fact`, `/stats`, `/help`
- **Respuestas categorizadas**: 5 tipos diferentes de respuestas (científicas, educativas, humorísticas, comprensivas, sarcásticas)
- **Sistema de estadísticas**: Contador de correcciones realizadas y tracking de servidores
- **Configuración centralizada**: Nuevo archivo `config.py` para constantes y configuraciones
- **Logging mejorado**: Logs detallados con emojis y mejor formato
- **Eventos de servidor**: Notificaciones cuando el bot se une o sale de servidores
- **Documentación completa**: README renovado con ejemplos y guías detalladas

### 🔧 Cambiado
- **Arquitectura**: Migrado de `discord.Client` a `discord.ext.commands.Bot` para soporte de comandos slash
- **Detección de palabras**: Expandida para incluir "pluto" además de "plutón" y "pluton"
- **Respuestas**: Sistema completamente renovado con múltiples categorías y variedad
- **Estructura del código**: Mejor organización con separación de responsabilidades
- **Type hints**: Mejorados y más específicos en todo el código
- **Documentación**: Docstrings completamente renovadas en español

### 🐛 Corregido
- **Compatibilidad Python 3.13**: Actualizado discord.py para resolver problemas con el módulo `audioop`
- **Manejo de errores**: Mejor gestión de excepciones y logging de errores
- **Performance**: Optimización en la detección de patrones y respuestas

### 🗑️ Removido
- Sistema de respuestas simple basado en diccionario básico
- Dependencia problemática en audioop para Python 3.13

---

## [1.0.0] - 2025-01-27

### 🚀 Agregado
- **Funcionalidad básica**: Bot que responde a menciones de Plutón como planeta
- **Palabras clave**: Detección de "plutón", "pluton", "planeta"
- **Respuestas básicas**: Sistema simple de respuestas predefinidas
- **Configuración por ambiente**: Uso de archivo `.env` para el token
- **Estructura inicial**: Archivos básicos del proyecto

### 🔧 Características iniciales
- Detección simple de palabras clave
- Respuestas estáticas predefinidas
- Logging básico de mensajes
- Soporte para mensajes privados con prefijo "?"

---

## Tipos de cambios
- `🚀 Agregado` para nuevas funcionalidades
- `🔧 Cambiado` para cambios en funcionalidades existentes
- `🐛 Corregido` para corrección de errores
- `🗑️ Removido` para funcionalidades eliminadas
- `⚠️ Deprecated` para funcionalidades que serán removidas pronto
- `🔒 Seguridad` para vulnerabilidades corregidas
