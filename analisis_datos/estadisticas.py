<<<<<<< HEAD
# estadisticas.py[mid]
def media(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
=======
# estadisticas.py
def media(datos):
    """Esta funcion calcula la media aritmetica de un lista con valores numericos

    Args:
        datos (Lista): Lista de numeros

    Returns:
        Float: Flotante de la media aritmetica
    """
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    """_summary_

    Args:
        datos (_type_): _description_

    Returns:
        _type_: _description_
    """
>>>>>>> 9daceb449866e76d5e2e9948cf2e885771a085ce
    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
<<<<<<< HEAD
        return datos_sorted
=======
        return datos_sorted[mid]
>>>>>>> 9daceb449866e76d5e2e9948cf2e885771a085ce
