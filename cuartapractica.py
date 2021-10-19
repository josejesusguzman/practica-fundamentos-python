# Uso de la Poke API
# -> https://pokeapi.co/
# Importamos la librerías
import requests
import matplotlib.pyplot as plt
import matplotlib.image as img

# El usuario introduce en la terminal el nombre del pokémon
pokemon = input("Introduce el nombre de un pokémon: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
# Se hace la perición a la URL formada en la linea anterior
res = requests.get(url)

# Si no salió bien la petición (Status diferente a 200) Se termina el programa
if res.status_code != 200 :
    print("Pokémon no encontrado")
    exit()

# Accedemos al nivel sprites y obtenemos la URL de la imagen
imagen = img.imread(res.json()['sprites']['front_default'])
plt.title(res.json()['name'])
# Construimos la imagen
imgplot = plt.imshow(imagen)
# Mostramos la imagen al usuario
plt.show()