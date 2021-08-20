# Libreria para generar datos aleatorios
import random

# Libreria para generar graficas
# Para instalar esto necesitas copiar, pegar y ejecutar en tu terminal:
# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as plt

# Generar un numero aleatoreo y lo imprime
print(random.randrange(10, 100, 2))

# Declara la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Imprime la lista
print('Lista original', lista)

# Mezcla los elementos de la lista al azar
random.shuffle(lista)
# Imprime la lista mezclada
print('Lista mixeada', lista)

# Genera una grafica de campana de GAUSS
# Genera los datos de la grafica
campana = [random.gauss(1,0.5) for i in range(1000)]
print(campana)
# Arma la grafica
plt.hist(campana, bins=15)
# Muestra la grafica
plt.show()
