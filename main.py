<<<<<<< HEAD
# Proyecto: [Trabajo Phyton]
# Estudiante: [Fabian Alpizar]
# Fecha de Inicio: [4/2/2025]
=======
# Proyecto: [Nombre del Proyecto]
# Estudiante: Prof. Andrés
# Fecha de Inicio: 2025/02/24
>>>>>>> 9daceb449866e76d5e2e9948cf2e885771a085ce
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

<<<<<<< HEAD

from analisis_datos.estadisticas import media,calcular_mediana
lista_parametro = [1,4,2,3,5]
print("Media: ", media(lista_parametro))
print("Mediana: ", calcular_mediana(lista_parametro))
=======
# from analisis_datos.estadisticas import media,calcular_mediana #Importar modulos

from analisis_datos import *

lista_compras = generar_lista_de_compras()
print(lista_compras)
precios = [precio for _, precio in lista_compras]
print('Media: ', media(precios))
print('Mediana: ', calcular_mediana(precios)) 
>>>>>>> 9daceb449866e76d5e2e9948cf2e885771a085ce
