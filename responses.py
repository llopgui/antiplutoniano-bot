from random import choice

responses = {
    "hola": [
        "Hola hermano odiador de Plutón, no olvides odiar a esa piedra congelada flotante siempre que lo desees."
    ],
    "adiós": ["¡Adiós!", "¡Hasta luego!", "¡Nos vemos!"],
    "planeta": [
        "Plutón NO es un planeta, esa maldita piedra congelada flotante en el espacio, no debe serlo, sino, podemos llamar planeta hasta a los cubitos de hielo de mi nevera si flotaran en el espacio..."
    ],
    # Añadir más palabras clave y respuestas según sea necesario
}


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Vaya, estás terriblemente silencioso..."

    # Comprobar si el mensaje contiene alguna de las palabras clave del diccionario
    for key, value in responses.items():
        if key in lowered:
            return choice(value)

    # Respuesta por defecto si no se encuentra ninguna clave
    return choice(
        [
            "No entiendo...",
            "¿De qué estás hablando?",
            "¿Te importaría reformular eso?",
        ]
    )
