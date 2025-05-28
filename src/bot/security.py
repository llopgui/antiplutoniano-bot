"""
Módulo de Seguridad del Bot Antiplutoniano
==========================================

Contiene funciones de validación y protecciones de seguridad.

Autor: llopgui (https://github.com/llopgui/)
Versión: 2.0.1
Fecha: 28/05/2025
Licencia: CC BY-NC-SA 4.0
"""

import hashlib
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

logger: logging.Logger = logging.getLogger(__name__)

# Patrones de contenido potencialmente malicioso
MALICIOUS_PATTERNS: List[str] = [
    r"<script.*?>",  # Scripts
    r"javascript:",  # JavaScript URLs
    r"data:.*base64",  # Data URLs con base64
    r"@everyone",  # Menciones masivas
    r"@here",  # Menciones de canal
    r"(?:https?://)?discord\.gg/\w+",  # Enlaces de invitación
]

# Límites de seguridad
MAX_MESSAGE_LENGTH: int = 2000
MAX_COMMAND_RATE: int = 5  # Comandos por minuto por usuario
MAX_RESPONSE_LENGTH: int = 2000

# Cache para rate limiting
user_command_cache: Dict[str, List[float]] = {}


def validate_token(token: str) -> bool:
    """
    Valida que el token de Discord tenga un formato correcto.

    Args:
        token: Token a validar

    Returns:
        bool: True si el token parece válido
    """
    if not token or not isinstance(token, str):
        return False

    # Token de Discord: formato básico
    # Bot tokens: MTxxxxx.xxxxxx.xxxxxxx (base64 encoded parts)
    # User tokens: mfa.xxxxxxxxx (deprecated, pero validamos formato)

    # Verificar longitud mínima
    if len(token) < 50:
        return False

    # Verificar que no contenga espacios o caracteres no válidos
    if " " in token or "\n" in token or "\t" in token:
        return False

    # Verificar formato básico de bot token
    if token.startswith("MT") and token.count(".") >= 2:
        parts: list[str] = token.split(".")
        if len(parts) >= 3:
            return True

    # Verificar formato de user token (legacy)
    if token.startswith("mfa.") and len(token) > 20:
        return True

    # Verificar que sea alfanumérico con guiones y puntos
    if re.match(r"^[A-Za-z0-9._-]+$", token):
        return True

    return False


def sanitize_message(message: str) -> str:
    """
    Sanitiza un mensaje removiendo contenido potencialmente malicioso.

    Args:
        message: Mensaje a sanitizar

    Returns:
        str: Mensaje sanitizado
    """
    if not message:
        return ""

    # Truncar mensaje si es muy largo
    if len(message) > MAX_MESSAGE_LENGTH:
        message = message[: MAX_MESSAGE_LENGTH - 3] + "..."

    # Remover patrones maliciosos
    for pattern in MALICIOUS_PATTERNS:
        message = re.sub(
            pattern, "[CONTENT_REMOVED]", message, flags=re.IGNORECASE
        )

    # Escapar caracteres especiales de Discord
    message = message.replace("@", "@\u200b")  # Zero-width space

    return message


def check_rate_limit(user_id: str) -> bool:
    """
    Verifica si un usuario está dentro de los límites de rate limiting.

    Args:
        user_id: ID del usuario

    Returns:
        bool: True si está dentro del límite
    """
    import time

    current_time = time.time()

    if user_id not in user_command_cache:
        user_command_cache[user_id] = []

    # Limpiar comandos antiguos (más de 1 minuto)
    user_command_cache[user_id] = [
        cmd_time
        for cmd_time in user_command_cache[user_id]
        if current_time - cmd_time < 60
    ]

    # Verificar límite
    if len(user_command_cache[user_id]) >= MAX_COMMAND_RATE:
        logger.warning(f"Rate limit exceeded for user {user_id}")
        return False

    # Agregar comando actual
    user_command_cache[user_id].append(current_time)
    return True


def validate_file_path(
    file_path: str, allowed_dirs: Optional[List[str]] = None
) -> bool:
    """
    Valida que una ruta de archivo sea segura.

    Args:
        file_path: Ruta a validar
        allowed_dirs: Directorios permitidos (opcional)

    Returns:
        bool: True si la ruta es segura
    """
    if not file_path:
        return False

    try:
        path: Path = Path(file_path).resolve()

        # Verificar que no sea un path traversal
        if ".." in str(path) or str(path).startswith("/"):
            return False

        # Verificar directorios permitidos
        if allowed_dirs:
            for allowed_dir in allowed_dirs:
                allowed_path: Path = Path(allowed_dir).resolve()
                # Verificar si el path está dentro del directorio permitido
                try:
                    path.relative_to(allowed_path)
                    return True
                except ValueError:
                    # Path no está dentro del directorio permitido
                    continue
            return False

        return True

    except (ValueError, OSError):
        return False


def hash_sensitive_data(data: str) -> str:
    """
    Genera un hash de datos sensibles para logging seguro.

    Args:
        data: Datos a hashear

    Returns:
        str: Hash de los datos
    """
    if not data:
        return "empty"

    return hashlib.sha256(data.encode()).hexdigest()[:8]


def validate_environment_vars(required_vars: List[str]) -> Dict[str, Any]:
    """
    Valida que las variables de entorno requeridas estén presentes.

    Args:
        required_vars: Lista de variables requeridas

    Returns:
        dict: Diccionario con el estado de las variables
    """
    import os

    result: Dict[str, Any] = {
        "valid": True,
        "missing": [],
        "empty": [],
        "present": [],
    }

    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            result["missing"].append(var)
            result["valid"] = False
        elif not value.strip():
            result["empty"].append(var)
            result["valid"] = False
        else:
            result["present"].append(var)

    return result


def secure_log_message(message: str, user_id: Optional[str] = None) -> str:
    """
    Prepara un mensaje para logging de forma segura.

    Args:
        message: Mensaje original
        user_id: ID del usuario (opcional)

    Returns:
        str: Mensaje seguro para logging
    """
    # Truncar mensaje largo
    if len(message) > 100:
        safe_message: str = message[:97] + "..."
    else:
        safe_message: str = message

    # Hashear información sensible
    if user_id:
        user_hash: str = hash_sensitive_data(user_id)
        return f"User {user_hash}: {safe_message}"

    return safe_message


def validate_discord_permissions(
    permissions: int, required: List[str]
) -> bool:
    """
    Valida que el bot tenga los permisos necesarios.

    Args:
        permissions: Permisos actuales (bitfield)
        required: Lista de permisos requeridos

    Returns:
        bool: True si tiene todos los permisos necesarios
    """
    # Mapping de permisos de Discord
    DISCORD_PERMISSIONS: dict[str, int] = {
        "send_messages": 2048,
        "read_messages": 1024,
        "use_slash_commands": 2147483648,
        "embed_links": 16384,
        "read_message_history": 65536,
        "add_reactions": 64,
        "use_external_emojis": 262144,
    }

    for permission in required:
        if permission in DISCORD_PERMISSIONS:
            if not (permissions & DISCORD_PERMISSIONS[permission]):
                logger.warning(f"Missing permission: {permission}")
                return False

    return True


class SecurityMiddleware:
    """Middleware de seguridad para el bot."""

    def __init__(self) -> None:
        self.blocked_users: Set[str] = set()
        self.warning_count: dict[str, dict[str, int]] = {}

    def check_message_security(self, message: str, user_id: str) -> bool:
        """
        Verifica la seguridad de un mensaje.

        Args:
            message: Mensaje a verificar
            user_id: ID del usuario

        Returns:
            bool: True si el mensaje es seguro
        """
        # Verificar usuario bloqueado
        if user_id in self.blocked_users:
            return False

        # Verificar rate limiting
        if not check_rate_limit(user_id):
            self.add_warning(user_id, "rate_limit")
            return False

        # Verificar contenido malicioso
        for pattern in MALICIOUS_PATTERNS:
            if re.search(pattern, message, re.IGNORECASE):
                self.add_warning(user_id, "malicious_content")
                return False

        return True

    def add_warning(self, user_id: str, reason: str) -> None:
        """Agrega una advertencia a un usuario."""
        if user_id not in self.warning_count:
            self.warning_count[user_id] = {}

        if reason not in self.warning_count[user_id]:
            self.warning_count[user_id][reason] = 0

        self.warning_count[user_id][reason] += 1

        # Bloquear después de muchas advertencias
        total_warnings: int = sum(self.warning_count[user_id].values())
        if total_warnings >= 5:
            self.blocked_users.add(user_id)
            logger.warning(
                f"User {hash_sensitive_data(user_id)} blocked for "
                f"security violations"
            )

    def unblock_user(self, user_id: str) -> None:
        """Desbloquea un usuario."""
        self.blocked_users.discard(user_id)
        if user_id in self.warning_count:
            del self.warning_count[user_id]
