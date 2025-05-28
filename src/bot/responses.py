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

# Respuestas categorizadas por tipo - VERSIÓN MEJORADA: CIENTÍFICA, GRACIOSA Y TROLL
RESPONSES = {
    "correcciones_cientificas": [
        (
            "🔬 **ALERTA CIENTÍFICA**: Plutón es un **planeta enano** desde 2006. "
            "No, no es una conspiración de la NASA. Es porque su masa es solo "
            "0.007 veces la de la Tierra y no puede limpiar su órbita de escombros. "
            "**¡Las matemáticas no mienten!** 📊"
        ),
        (
            "🎯 **REALIDAD CHECK**: Los criterios IAU son claros:\n"
            "✅ Orbita el Sol (Plutón sí)\n"
            "✅ Forma esférica (Plutón sí)\n"
            "❌ **Domina su órbita (Plutón NO)**\n"
            "**2 de 3 = planeta enano.** Es matemática básica, no opinión. 🤓"
        ),
        (
            "⚖️ **EXPERIMENTO MENTAL**: Si Plutón fuera planeta, también lo serían "
            "Eris (más masivo), Ceres, Makemake, Haumea, Sedna... "
            "¿Quieres memorizar 50+ planetas? Porque eso es lo que tendríamos. "
            "**La IAU te salvó de ese trauma.** 🧠"
        ),
        (
            "🌌 **DATO CIENTÍFICO BRUTAL**: Plutón tiene una masa de "
            "1.31×10²² kg. Suena impresionante, ¿verdad? Pues es menos del "
            "18% de nuestra Luna. **Nuestra Luna no es planeta tampoco.** "
            "Coincidencia? No lo creo. 🌙"
        ),
        (
            "🔍 **LECCIÓN DE ASTRONOMÍA**: Plutón está en el Cinturón de Kuiper "
            "con miles de objetos similares. Llamarlo planeta sería como llamar "
            "'océano' a cada charco en el desierto. **Categorías existen por algo.** 🏜️"
        ),
    ],
    "respuestas_sarcasticas": [
        (
            "🙄 *Suspira en astrofísico* ¿También piensas que la Tierra es plana "
            "y que los dinosaurios vivieron con humanos? Porque Plutón-es-planeta "
            "está al mismo nivel de negación científica. **Welcome to reality.** 🌍"
        ),
        (
            "📞 **ÚLTIMA HORA**: Plutón acaba de llamar. Dice que está muy cómodo "
            "siendo planeta enano, tiene excelentes vecinos en el Cinturón de Kuiper "
            "y que por favor dejes de proyectar tu crisis existencial en él. 🎭"
        ),
        (
            "🤦‍♂️ *Llora en Neil deGrasse Tyson* ¿Sabías que hay gente que todavía "
            "piensa que Plutón es planeta? Es como insistir que MySpace es mejor "
            "que Instagram. **Técnicamente posible, pero... ¿en serio?** 📱"
        ),
        (
            "🎪 **BREAKING**: Persona local descubre que la nostalgia no cambia "
            "las leyes de la física. Los científicos están impactados por esta "
            "revelación. **En otras noticias, el agua sigue siendo mojada.** 💧"
        ),
        (
            "🧙‍♂️ *Usando voz de profesor condescendiente* Muy bien clase, "
            "¿quién puede decirme qué año estamos? Exacto, 2025. "
            "Plutón dejó de ser planeta en 2006. **Hagan las matemáticas.** 🧮"
        ),
        (
            "🎬 **PELÍCULA DE TERROR**: 'La venganza de Plutón: cuando la nostalgia "
            "ataca a la ciencia'. Spoiler alert: la ciencia siempre gana. "
            "**Rated R for Reality.** 🍿"
        ),
    ],
    "respuestas_educativas": [
        (
            "🎓 **MASTERCLASS ASTRONÓMICA**: Plutón tiene una órbita excéntrica "
            "de 248 años terrestres, a veces más cerca del Sol que Neptuno. "
            "Su mayor luna, Caronte, es tan grande que forman un sistema binario. "
            "**¡Es más cool como planeta enano!** 🎯"
        ),
        (
            "🔬 **CIENCIA REAL**: Plutón fue descubierto en 1930 por Clyde Tombaugh "
            "buscando el 'Planeta X'. Plot twist: resultó ser mucho más pequeño "
            "de lo esperado. **La ciencia se autocorrige, no es error, es evolución.** 📈"
        ),
        (
            "🌡️ **DATOS EXTREMOS**: En Plutón, el agua hierve instantáneamente "
            "en el vacío y se congela en microsegundos. Temperatura: -230°C. "
            "Gravedad: 6% de la Tierra. **Básicamente, un infierno helado espacial.** ❄️"
        ),
        (
            "🚀 **PERSPECTIVA CÓSMICA**: New Horizons tardó 9.5 años en llegar "
            "a Plutón (2006-2015). Ironía: durante todo ese viaje, Plutón ya "
            "no era planeta. **La nave llegó a visitar a un planeta enano.** 🛸"
        ),
        (
            "💎 **COMPARACIÓN ÉPICA**: Plutón: 2,374 km de diámetro. "
            "Estados Unidos: 4,500 km de ancho. **Plutón cabe dentro de Estados Unidos "
            "con espacio de sobra. ¿Y lo quieres llamar planeta?** 🗺️"
        ),
    ],
    "respuestas_humor": [
        (
            "😂 **JOKE OF THE DAY**: ¿Por qué Plutón no puede ser planeta? "
            "Porque ni siquiera puede limpiar su propia órbita, "
            "¡imagínate si fuera tu compañero de cuarto! 🏠"
        ),
        (
            "🍕 **ANALOGÍA CULINARIA**: Plutón es tan planeta como una pizza "
            "hawaiana es italiana: técnicamente alguien lo afirma, "
            "pero los italianos (científicos) dicen que no. **Case closed.** 🇮🇹"
        ),
        (
            "🎮 **GAMER LOGIC**: Plutón en el sistema solar es como ese jugador "
            "que insiste en que sigue siendo pro después de que lo banearon del torneo. "
            "**Sorry buddy, new rules.** 🕹️"
        ),
        (
            "☕ **MOOD**: Plutón tiene más drama que un reality show. "
            "'¡Yo era planeta!' 'Fui degradado injustamente!' 'Es una conspiración!' "
            "Relájate Plutón, **eres el Kardashian del sistema solar.** 📺"
        ),
        (
            "🧊 **SITUACIÓN ACTUAL**: Plutón es básicamente la bola de nieve "
            "más famosa del universo. **At least he's famous for something.** ⭐"
        ),
        (
            "💔 **RELATIONSHIP STATUS**: Plutón y el estatus de planeta = "
            "'It's complicated'. Más específicamente: 'We broke up in 2006 "
            "but some people haven't gotten over it yet.' 💀"
        ),
    ],
    "respuestas_comprensivas": [
        (
            "💙 **WITH LOVE**: Entiendo que duele. Todos crecimos con 'Mis Very "
            "Educated Mother Just Served Us Nine Pizzas'. Ahora es 'Nine Pickles' "
            "porque Plutón ya no cuenta. **But hey, la ciencia evoluciona y nosotros también.** 🌱"
        ),
        (
            "🤗 **GRUPO DE APOYO**: 'Hola, soy [tu nombre] y creo que Plutón "
            "sigue siendo planeta'. 'Hola [tu nombre]'. No estás solo en esto, "
            "pero sí estás científicamente equivocado. **Baby steps.** 👶"
        ),
        (
            "📚 **PERSPECTIVA HISTÓRICA**: Ceres fue planeta de 1801 a 1851. "
            "Se recuperó y ahora es el planeta enano más cool del cinturón de asteroides. "
            "**Plutón también se adaptará. Y tú también.** 💪"
        ),
        (
            "🌟 **SILVER LINING**: Plutón puede no ser planeta, pero es el único "
            "cuerpo celeste con un perro Disney de nombre. **That's something, right?** 🐕"
        ),
    ],
    "respuestas_troll_extremo": [
        (
            "🧠 **BIG BRAIN TIME**: Imagina ser tan rebelde que niegas 19 años "
            "de consenso científico internacional porque 'así aprendiste en la escuela'. "
            "Next: vas a decir que la velocidad de la luz no es constante "
            "porque en tu época los coches eran más lentos. **Physics has left the chat.** 🏃‍♂️💨"
        ),
        (
            "🎭 **PERFORMANCE ART**: Tu argumento de 'Plutón es planeta' es tan "
            "sólido como construir un castillo de arena en una lavadora. "
            "Técnicamente puedes intentarlo, pero **la realidad tiene otros planes.** 🏰🌊"
        ),
        (
            "🔮 **PLOT TWIST**: Acabas de activar mi carta trampa científica. "
            "Por afirmar que Plutón es planeta, ahora tienes que memorizar "
            "los nombres de los 50+ objetos del Cinturón de Kuiper que también "
            "califican bajo tu lógica. **Welcome to your new nightmare.** 📝💀"
        ),
        (
            "⚡ **POWER MOVE**: Voy a decirle a Neil deGrasse Tyson que alguien "
            "en Internet sigue insistiendo que Plutón es planeta. "
            "Se va a reír tanto que va a necesitar oxígeno. **You've been warned.** 😈"
        ),
    ],
    "saludos": [
        (
            "¡Hola, futuro convertido a la ciencia! 👋 Espero que hoy aprendas "
            "por qué Plutón es más cool como planeta enano. **Science is fun!** 🚀"
        ),
        (
            "¡Saludos, explorador cósmico! 🌌 ¿Listo para que destruya tus "
            "creencias infantiles sobre el sistema solar? **Just kidding... or am I?** 😏"
        ),
        (
            "¡Buenas! 🌟 Soy tu bot favorito para destrozar ilusiones sobre Plutón. "
            "**Armed with facts and ready to educate.** 🤓⚔️"
        ),
    ],
    "despedidas": [
        (
            "¡Adiós! 👋 Recuerda: Plutón puede no ser planeta, pero al menos "
            "no niega la ciencia como algunos humanos. **Be better than Plutón.** ⭐"
        ),
        (
            "¡Hasta luego! 🚀 Que tengas un día más estable que la órbita de Plutón "
            "y más científicamente preciso que tu conocimiento astronómico previo. **Burn!** 🔥"
        ),
        (
            "¡Nos vemos! 🌟 Mantén los pies en la Tierra, los ojos en las estrellas, "
            "y tu definición de planeta actualizada al siglo XXI. **Peace out!** ✌️"
        ),
    ],
}

# Palabras clave para diferentes tipos de respuesta
KEYWORDS = {
    "saludos": [
        "hola",
        "hi",
        "hello",
        "buenos días",
        "buenas tardes",
        "buenas noches",
    ],
    "despedidas": [
        "adiós",
        "adios",
        "bye",
        "chao",
        "hasta luego",
        "nos vemos",
    ],
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
            "respuestas_troll_extremo",
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
            "🧊 **Dato Plutoniano BRUTAL**: Plutón es tan frío (-230°C) que "
            "tu aliento se congelaría instantáneamente y caería como nieve. "
            "**Literal death by conversation.** ❄️💀"
        ),
        (
            "⏰ **Dato Temporal ÉPICO**: Un año en Plutón = 248 años terrestres. "
            "Plutón no ha completado ni UNA órbita desde su descubrimiento en 1930. "
            "**Talk about being slow to the party.** 🐌🎉"
        ),
        (
            "💕 **Dato Romántico CIENTÍFICO**: Plutón y Caronte están en 'tidal locking', "
            "siempre viendo la misma cara del otro. Es el ultimate long-distance relationship "
            "del sistema solar. **Forever eye contact. Awkward.** 👀💙"
        ),
        (
            "🏔️ **Dato Geográfico INSANO**: Las montañas de Plutón están hechas de "
            "HIELO DE AGUA flotando en nitrógeno sólido. Imagínate esquiar en agua "
            "congelada sobre océanos de nitrógeno. **Extreme sports much?** ⛷️"
        ),
        (
            "🌡️ **Dato Extremo LETAL**: A -230°C, el aire de la Tierra sería "
            "nieve sólida en Plutón. Tu cuerpo se convertiría en una estatua "
            "en segundos. **Not exactly vacation material.** 🗿❄️"
        ),
        (
            "👥 **Dato Familiar CONFUSO**: Plutón tiene 5 lunas: Caronte (enorme), "
            "Nix, Hidra, Cerbero y Estigia. Para un 'no-planeta', tiene más familia "
            "que algunos planetas reales. **Overachiever much?** 👨‍👩‍👧‍👦🎭"
        ),
        (
            "💎 **Dato Comparativo SAVAGE**: Plutón (2,374 km) vs Texas (1,244 km de ancho). "
            "Texas cabría en Plutón con espacio de sobra. Y Texas ya es ridículamente grande. "
            "**Yet still not a planet. Ouch.** 🤠🌌"
        ),
        (
            "🚀 **Dato Espacial MIND-BLOWN**: New Horizons viajó 9.5 años para llegar "
            "a Plutón y solo tuvo unas horas para estudiarlo en el flyby. "
            "**Ultimate one-night stand with science.** 📸✨"
        ),
        (
            "⚖️ **Dato de Gravedad WEAK**: En Plutón pesas solo el 6% de tu peso terrestre. "
            "Si pesas 70kg, allí serías 4.2kg. Finalmente podrías hacer parkour "
            "como en los videojuegos. **Silver lining?** 🏃‍♂️💨"
        ),
        (
            "🌅 **Dato Solar DEPRESSING**: El Sol desde Plutón se ve como una estrella "
            "brillante, no como el disco que conocemos. Solar panels = useless. "
            "**Eternal cosmic winter vibes.** ☀️😢"
        ),
        (
            "🎭 **Dato Drama QUEEN**: Plutón tiene una atmósfera que 'respira': "
            "se expande cuando está cerca del Sol y se colapsa cuando se aleja. "
            "**Even its atmosphere is more dramatic than most people.** 🎪🌬️"
        ),
        (
            "🧬 **Dato Químico WILD**: La superficie de Plutón tiene metano, "
            "nitrógeno y monóxido de carbono congelados. Básicamente, "
            "es una nevera cósmica llena de gases tóxicos. **Chef's nightmare.** 👨‍🍳💀"
        ),
        (
            "📐 **Dato Matemático HARSH**: Plutón tiene 0.006 la masa de la Tierra. "
            "Para igualar la masa terrestre necesitarías ~167 Plutones. "
            "**Quantity over quality, am I right?** 🔢📊"
        ),
        (
            "🎪 **Dato Histórico IRONIC**: Plutón fue nombrado por una niña de 11 años "
            "(Venetia Burney) en 1930. Una niña le dio nombre a lo que se convertiría "
            "en el cuerpo celeste más controversial del sistema solar. **Kids, man.** 👧🎭"
        ),
        (
            "🔄 **Dato Orbital CHAOTIC**: La órbita de Plutón es tan excéntrica "
            "que a veces está más cerca del Sol que Neptuno. Imagínate ser tan "
            "rebelde que ni siquiera respetas el orden planetario. **Chaos energy.** 🌀"
        ),
        (
            "💔 **Dato Emocional BRUTAL**: Clyde Tombaugh, quien descubrió Plutón, "
            "murió en 1997. Sus cenizas viajaron a Plutón en New Horizons. "
            "**He finally got to visit his discovery... sort of.** 🚀💫"
        ),
    ]

    return choice(facts)
