from random import choice, randint

# Diccionario de respuestas
responses = {
    'orbita despejada': ['Plutón no despeja su órbita de otros objetos, lo cual es un criterio esencial para ser considerado un planeta según la IAU.'],
    'cinturón kuiper': ['Plutón es parte del cinturón de Kuiper, una región del sistema solar llena de objetos similares en tamaño y composición.'],
    'masa': ['La masa de Plutón es significativamente menor comparada con la de los planetas tradicionales del sistema solar.'],
    'orbita elíptica': ['Plutón tiene una órbita muy elíptica, lo que significa que su distancia al Sol varía considerablemente.'],
    'orbita inclinada': ['La órbita de Plutón está inclinada respecto al plano de la eclíptica, que es el plano en el que orbitan los ocho planetas principales.'],
    'planeta enano': ['En 2006, Plutón fue reclasificado como un planeta enano por la Unión Astronómica Internacional debido a sus características orbitales y de masa.'],
    'dominio gravitacional': ['Plutón no domina gravitacionalmente su entorno, compartiendo su órbita con otros cuerpos similares en tamaño y masa.'],
    'compartir orbita': ['Plutón comparte su órbita con otros objetos en el cinturón de Kuiper, lo que no ocurre con los planetas tradicionales que despejan sus órbitas.'],
    'tamaño': ['Plutón es demasiado pequeño en comparación con los otros planetas del sistema solar, incluso es más pequeño que algunas lunas.'],
    'composición': ['La composición de Plutón es similar a la de los cometas, con una mezcla de roca y hielo, en lugar de ser predominantemente rocoso o gaseoso como los planetas.'],
    'orbita no circular': ['La órbita de Plutón no es circular como la de los otros planetas, sino altamente excéntrica, lo que le lleva a cruzar la órbita de Neptuno.'],
    'cinturón de kuiper': ['Plutón tiene muchas similitudes con otros objetos del cinturón de Kuiper, tanto en composición como en comportamiento orbital.'],
    'criterios IAU': ['Según los criterios establecidos por la IAU en 2006, Plutón no cumple con todos los requisitos para ser considerado un planeta.'],
    'objeto mas grande': ['Plutón no es el objeto más grande en su órbita, ya que comparte su trayectoria con otros cuerpos del cinturón de Kuiper.'],
    'satélites planetarios': ['Plutón es menor en tamaño que algunos satélites planetarios como Ganímedes o Titán, lo que cuestiona su clasificación como planeta.'],
    'influencia gravitacional': ['La influencia gravitacional de Plutón es insuficiente para limpiar su órbita de otros objetos.'],
    'revisión': ['La clasificación de Plutón ha sido revisada debido a los descubrimientos recientes de otros objetos similares en el cinturón de Kuiper.'],
    'limpiar orbita': ['Plutón no tiene suficiente masa para limpiar su órbita de otros cuerpos, un criterio esencial para la definición de planeta.'],
    'planetas enanos': ['Plutón está clasificado junto a otros planetas enanos como Eris y Haumea, que también comparten características similares.'],
    'distancia al sol': ['Plutón está demasiado lejos del Sol, lo que contribuye a sus características únicas y su clasificación como planeta enano.']
}


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Vaya, estás terriblemente silencioso...'
    else:
        for key, value in responses.items():
            if key in lowered:
                return choice(value)  # Selecciona una respuesta aleatoria de la lista
        # Respuesta por defecto si no se encuentra ninguna clave
        return choice(['No entiendo...',
                       '¿De qué estás hablando?',
                       '¿Te importaría reformular eso?'])
