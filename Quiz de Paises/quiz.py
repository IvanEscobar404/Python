capitals = {
    "Argentina": "Buenos Aires",
    "Mexico": "Ciudad de Mexico",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Chile" : "Santiago",
    "España": "Madrid"
}

def quiz_capitals():
    print("Bienvenido al cuestionario de capitales del mundo!")
    score = 0

    for country, capital in capitals.items():

        print(f"Pregunta: cual es la capital de {country}?")
        user_answer = input("Tu respuesta: ")

        if user_answer.lower() == capital.lower():
            print("Correcto, haz ganado un punto")
            score +=1
            
        else:
            print(f"""Incorrecto bot.
                    La capital de {country} es: {capital}.\n""")
            
    print(f"Tu puntuacion final es: {score}/{len(capitals)}")

quiz_capitals()