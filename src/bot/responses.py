"""
Sistema de Respuestas del Bot Antiplutoniano
===========================================

Este módulo contiene todas las respuestas y la lógica de detección
para responder a usuarios que afirman que Plutón es un planeta.

Autor: llopgui (https://github.com/llopgui/)
Versión: 2.0.1
Fecha: 28/05/2025
Licencia: CC BY-NC-SA 4.0
"""

import re
from random import choice

# Patrones que indican que alguien piensa que Plutón es un planeta
PLUTO_PLANET_PATTERNS = [
    # Afirmaciones directas
    r"plutón es un planeta",
    r"pluton es un planeta",
    r"pluto es un planeta",
    r"plutón.*planeta",
    r"pluton.*planeta",
    r"pluto.*planeta",
    # Listas de planetas que incluyen Plutón
    r"nueve planetas",
    r"9 planetas",
    r"mercurio.*venus.*tierra.*marte.*júpiter.*saturno.*urano.*neptuno.*plutón",
    r"mercurio.*venus.*tierra.*marte.*jupiter.*saturno.*urano.*neptuno.*pluton",
    # Expresiones nostálgicas
    r"plutón.*devolver.*planeta",
    r"pluton.*devolver.*planeta",
    r"plutón.*debería.*planeta",
    r"pluton.*deberia.*planeta",
    r"extraño.*plutón.*planeta",
    r"extraño.*pluton.*planeta",
    # Referencias a reclasificación
    r"reclasificar.*plutón",
    r"reclasificar.*pluton",
    r"injusto.*plutón",
    r"injusto.*pluton",
    # Otros patrones comunes
    r"poor.*pluto",
    r"pobre.*plutón",
    r"pobre.*pluton",
]

# Respuestas categorizadas por tipo
RESPONSES = {
    "correcciones_cientificas": [
        (
            "🔬 **CORRECCIÓN CIENTÍFICA**: Plutón es un **planeta enano**, "
            "no un planeta. La Unión Astronómica Internacional lo reclasificó "
            "en 2006 por razones válidas."
        ),
        (
            "📏 **DATOS REALES**: Plutón es demasiado pequeño y no ha limpiado "
            "su órbita de otros objetos. Por eso es un planeta enano, "
            "no un planeta completo."
        ),
        (
            "🌌 **EDUCACIÓN ASTRONÓMICA**: Los planetas deben cumplir 3 criterios: "
            "orbitar el Sol, tener forma esférica, y limpiar su órbita. "
            "Plutón no cumple el tercero."
        ),
        (
            "⚖️ **ESTÁNDARES CIENTÍFICOS**: Si consideráramos a Plutón planeta, "
            "tendríamos que incluir a Eris, Ceres, Makemake y otros. "
            "¿Quieres 50+ planetas?"
        ),
    ],
    "respuestas_sarcasticas": [
        (
            "🙄 Ah sí, y supongo que también piensas que los tomates "
            "son vegetales, ¿verdad?"
        ),
        (
            "🤦‍♂️ *Suspira en científico* Plutón llamó, dice que está feliz "
            "siendo un planeta enano y que dejes de insistir en algo "
            "que ya se decidió hace 18 años."
        ),
        (
            "🎭 **TEATRO CÓSMICO**: 'Oh, Plutón, mi pequeño y helado drama queen, "
            "¿por qué la gente sigue sin entender tu verdadera naturaleza?'"
        ),
        (
            "📚 ¿Acabas de despertar de un coma desde 2005? "
            "Porque tengo noticias para ti..."
        ),
    ],
    "respuestas_educativas": [
        (
            "🎓 **DATO CURIOSO**: Plutón es más pequeño que nuestra Luna. "
            "¡Imagínate llamar planeta a algo más pequeño que nuestro satélite!"
        ),
        (
            "🔍 **DESCUBRIMIENTO**: En el cinturón de Kuiper hay muchos objetos "
            "similares a Plutón. ¿Deberíamos llamarlos a todos planetas también?"
        ),
        (
            "⭐ **CONTEXTO HISTÓRICO**: Plutón fue planeta durante 76 años "
            "porque no conocíamos mejor. La ciencia evoluciona, y ahora "
            "sabemos más sobre nuestro sistema solar."
        ),
        (
            "🌍 **COMPARACIÓN**: Plutón tiene solo el 18% de la masa de "
            "nuestra Luna. Es literalmente una pelota de nieve cósmica "
            "comparado con los planetas reales."
        ),
    ],
    "respuestas_humor": [
        (
            "😂 ¡Plutón para presidente! Oh wait, tampoco cumple "
            "los requisitos para eso..."
        ),
        (
            "🍕 Plutón es tan planeta como una pizza hawaiana es italiana: "
            "técnicamente posible en un universo alternativo, pero no en este."
        ),
        (
            "🎪 **BREAKING NEWS**: Persona local descubre que la ciencia "
            "no se basa en nostalgia. Más noticias a las 11."
        ),
        ("🧊 Plutón: el cubito de hielo más famoso del sistema solar " "desde 2006."),
    ],
    "respuestas_comprensivas": [
        (
            "💙 Entiendo la nostalgia por Plutón como planeta. Todos crecimos "
            "aprendiendo sobre los 'nueve planetas', pero la ciencia nos ayuda "
            "a entender mejor nuestro universo."
        ),
        (
            "🤗 Sé que es difícil aceptar el cambio, pero Plutón sigue siendo "
            "especial como planeta enano. ¡Es el más famoso de su categoría!"
        ),
        (
            "📖 No te sientas mal por extrañar los viejos tiempos. "
            "La reclasificación de Plutón nos ayudó a entender mejor "
            "los diferentes tipos de objetos en nuestro sistema solar."
        ),
    ],
    "saludos": [
        (
            "¡Hola, futuro defensor de la ciencia! 👋 Espero que hoy "
            "aprendas algo nuevo sobre nuestro fascinante sistema solar."
        ),
        (
            "¡Saludos, explorador cósmico! 🚀 ¿Sabías que hay objetos "
            "más interesantes que Plutón esperando ser descubiertos?"
        ),
    ],
    "despedidas": [
        (
            "¡Adiós! 👋 Recuerda: Plutón puede no ser un planeta, "
            "pero sigue siendo increíble."
        ),
        ("¡Hasta luego! 🌟 Que tengas un día más estable " "que la órbita de Plutón."),
        (
            "¡Nos vemos! 🚀 Mantén los pies en la Tierra y los ojos "
            "en las estrellas (no en Plutón)."
        ),
    ],
}

# Palabras clave para diferentes tipos de respuesta
KEYWORDS = {
    "saludos": ["hola", "hi", "hello", "buenos días", "buenas tardes", "buenas noches"],
    "despedidas": ["adiós", "adios", "bye", "chao", "hasta luego", "nos vemos"],
    "agradecimientos": ["gracias", "thanks", "thank you"],
}


def detect_pluto_planet_claim(text: str) -> bool:
    """
    Detecta si el texto contiene afirmaciones de que Plutón es un planeta.

    Args:
        text (str): El texto a analizar

    Returns:
        bool: True si se detecta una afirmación pro-Plutón planeta
    """
    text_lower = text.lower()

    # Buscar patrones específicos
    for pattern in PLUTO_PLANET_PATTERNS:
        if re.search(pattern, text_lower):
            return True

    return False


def get_response_category(text: str) -> str:
    """
    Determina la categoría de respuesta más apropiada basada en el texto.

    Args:
        text (str): El texto del usuario

    Returns:
        str: La categoría de respuesta a usar
    """
    text_lower = text.lower()

    # Verificar saludos
    if any(keyword in text_lower for keyword in KEYWORDS["saludos"]):
        return "saludos"

    # Verificar despedidas
    if any(keyword in text_lower for keyword in KEYWORDS["despedidas"]):
        return "despedidas"

    # Si detecta afirmación pro-Plutón, elegir tipo de respuesta
    if detect_pluto_planet_claim(text_lower):
        # Alternar entre diferentes tipos de respuesta para variedad
        response_types = [
            "correcciones_cientificas",
            "respuestas_educativas",
            "respuestas_sarcasticas",
            "respuestas_humor",
            "respuestas_comprensivas",
        ]
        # Usar hash del texto para consistency pero con variedad
        index = hash(text_lower) % len(response_types)
        return response_types[index]

    return "default"


def get_response(user_input: str) -> str:
    """
    Genera una respuesta apropiada basada en la entrada del usuario.

    Args:
        user_input (str): El mensaje del usuario

    Returns:
        str: La respuesta del bot
    """
    if not user_input.strip():
        return (
            "🤔 Vaya, estás terriblemente silencioso... "
            "¿Acaso Plutón se llevó tu voz?"
        )

    category = get_response_category(user_input)

    if category in RESPONSES:
        return choice(RESPONSES[category])

    # Respuestas por defecto si no se encuentra una categoría específica
    default_responses = [
        (
            "🤷‍♂️ No estoy seguro de qué hablas, pero si es sobre "
            "Plutón siendo un planeta, déjame parar ese pensamiento ahí mismo..."
        ),
        (
            "🔍 Hmm, no detecté ninguna herejía astronómica en tu mensaje. "
            "¡Bien por ti!"
        ),
        (
            "📡 ERROR 404: Contexto planetario no encontrado. "
            "¿Podrías ser más específico?"
        ),
        (
            "🌌 No entiendo completamente, pero si necesitas datos "
            "sobre planetas enanos, ¡estoy aquí para ayudar!"
        ),
    ]

    return choice(default_responses)


def get_pluto_fact() -> str:
    """
    Retorna un dato curioso sobre Plutón.

    Returns:
        str: Un dato interesante sobre Plutón
    """
    facts = [
        (
            "🧊 **Dato Plutoniano**: Plutón es tan frío que el nitrógeno "
            "se congela en su superficie."
        ),
        (
            "⏰ **Dato Temporal**: Un día en Plutón dura 6.4 días terrestres, "
            "y un año dura 248 años terrestres."
        ),
        (
            "💕 **Dato Romántico**: Plutón y su luna Caronte están "
            "'bloqueados tidalmente', siempre se muestran la misma cara."
        ),
        (
            "🏔️ **Dato Geográfico**: Plutón tiene montañas de hielo de agua "
            "de hasta 3.5 km de altura."
        ),
        (
            "🌡️ **Dato Extremo**: La temperatura en Plutón puede llegar "
            "a -230°C (-382°F)."
        ),
        (
            "👥 **Dato Familiar**: Plutón tiene 5 lunas conocidas: "
            "Caronte, Nix, Hidra, Cerbero y Estigia."
        ),
    ]

    return choice(facts)
