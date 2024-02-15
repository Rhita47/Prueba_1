def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    inventario.append(item)
    return inventario

# Ejemplo de uso
inventario = ["ordenador", "cargador", "movil"]
try:
    agregar_item(inventario, "reloj")
    print(inventario)
    agregar_item(inventario, "cargador")
except ValueError as e:
    print(e)
