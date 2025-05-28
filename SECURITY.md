# 🔒 Política de Seguridad

## 🛡️ Versiones Soportadas

Actualmente, solo la última versión del Bot Antiplutoniano recibe actualizaciones de seguridad:

| Versión | Soportada          |
| ------- | ------------------ |
| 2.0.x   | ✅ Sí             |
| 1.x     | ❌ No             |

## 🚨 Reportar Vulnerabilidades

Si descubres una vulnerabilidad de seguridad en el Bot Antiplutoniano, por favor repórtala de manera responsable:

### 📧 Contacto

- **Email**: Crea un issue en GitHub con la etiqueta `security`
- **Respuesta**: Nos comprometemos a responder dentro de 48 horas

### 📋 Información a Incluir

Por favor incluye la siguiente información en tu reporte:

1. **Descripción**: Descripción detallada de la vulnerabilidad
2. **Pasos**: Pasos específicos para reproducir el problema
3. **Impacto**: Evaluación del impacto potencial
4. **Solución**: Solución propuesta (si la tienes)

### 🔄 Proceso de Divulgación

1. **Reporte inicial** - Recibes confirmación en 48 horas
2. **Investigación** - Analizamos y validamos el reporte (1-7 días)
3. **Desarrollo** - Desarrollamos y testamos la corrección
4. **Notificación** - Te notificamos cuando esté lista la corrección
5. **Liberación** - Publicamos la corrección y créditos

## ⚠️ Vulnerabilidades NO Consideradas

Las siguientes NO se consideran vulnerabilidades de seguridad:

- Spam o rate limiting en Discord (es responsabilidad de Discord)
- Problemas de configuración del usuario (tokens incorrectos, etc.)
- Issues relacionados con permisos de Discord mal configurados
- Problemas con dependencias que ya tienen parches disponibles

## 🛠️ Mejores Prácticas de Seguridad

### Para Usuarios

1. **Token seguro**: Nunca compartas tu token de Discord
2. **Permisos mínimos**: Solo da al bot los permisos necesarios
3. **Actualizaciones**: Mantén el bot actualizado a la última versión
4. **Monitoreo**: Revisa los logs regularmente

### Para Desarrolladores

1. **Dependencias**: Mantén las dependencias actualizadas
2. **Validación**: Valida toda entrada de usuario
3. **Logging**: No registres información sensible
4. **Rate limiting**: Implementa límites apropiados

## 🔐 Características de Seguridad Implementadas

### ✅ Validaciones

- ✅ Validación de formato de token Discord
- ✅ Sanitización de mensajes entrantes
- ✅ Rate limiting por usuario
- ✅ Validación de permisos de Discord
- ✅ Protección contra path traversal

### ✅ Protecciones

- ✅ Filtrado de contenido malicioso
- ✅ Escapado de menciones masivas (@everyone)
- ✅ Hashing de datos sensibles en logs
- ✅ Límites de longitud de mensaje
- ✅ Middleware de seguridad

### ✅ Monitoreo

- ✅ Logging seguro de actividades
- ✅ Tracking de advertencias por usuario
- ✅ Bloqueo automático por violaciones
- ✅ Alertas de seguridad en logs

## 📚 Recursos Adicionales

- [Documentación de Seguridad de Discord](https://discord.com/developers/docs/topics/security)
- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)

## 🏆 Reconocimientos

Agradecemos a los siguientes investigadores de seguridad:

- *Ninguno hasta ahora - ¡sé el primero!*

---

**Nota**: Esta política de seguridad puede ser actualizada. Revisa regularmente para mantenerte informado de los cambios.
