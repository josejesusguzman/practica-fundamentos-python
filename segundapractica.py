# Imprimir tu nombre
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")
print("Hola, {}".format(nombre))

# entero
edad = 25
# flotante - decimales
altura = 1.75
#convertir flotante 
edadString = str(edad)
boolleanos = False

print(edad + edad)
print(edadString + edadString)

print(type(edad))

tuEdad = input("Introduce tu edad: ")
tuEdad = int(tuEdad)

# Estructura de control IF
if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad >= 100:
    print("¿Eres inmortal?")
elif tuEdad <= 0:
    print("No existes")
else:
    print("Eres menor de edad")

# Estructura de control FOR
for i in range(0, 10):
    print(i)

