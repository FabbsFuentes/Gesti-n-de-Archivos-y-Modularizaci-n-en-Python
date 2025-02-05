import random
def generar_lista_de_compras():
    productos = {
        "manzanas": 1000,
        "Banano": 150,
        "cereza": 2000,
        "naranjas": 900,
        "pan": 2275,
        "leche": 900,
        "huevos": 3400,
        "queso": 4500
    }
    seleccion = random.sample(list(productos.items()),k=5) #seleccinar 5 prductos de la lista de compras
    return seleccion