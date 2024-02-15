def separar_personajes(personajes):
    humanos = ["Obama", "Rajoy","Trump", "Forrest"]
    no_humanos = ["Sonic", "Pikachu", "Goku", "Mickey"]
    
    for personaje in personajes:
        if es_personaje_humano(personaje):
            humanos.append(personaje)
        else:
            no_humanos.append(personaje)
    
    humanos.sort()
    no_humanos.sort()
    
    return humanos, no_humanos

def es_personaje_humano(personaje):
    respuesta = input(f"¿Es {personaje} un personaje humano? (si/no): ")
    if respuesta.lower() == "si":
        return True
    elif respuesta.lower() == "no":
        return False
    else:
        print("Respuesta inválida. Se asumirá que el personaje no es humano.")
        return False

personajes = ["Mario", "Luigi", "Sonic", "Pikachu", "Goku", "Mickey", "Obama", "Rajoy", "Trump", "Forrest"]
humanos, no_humanos = separar_personajes(personajes)

print("Lista de personajes humanos:", humanos)
print("Lista de personajes no humanos:", no_humanos)
