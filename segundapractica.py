def validacionEdad() :
    # Imprimir tu nombre
    nombre = input("Introduce tu nombre: ")
    # Concatenación - Poner una variable junto con un texto plano
    print(f"Hola {nombre}")
    print("Hola {}".format(nombre))
    print("Hola " + nombre)

    # entero
    edad = input("Ahora introduce tu edad: ")
    # flotante - decimales
    estatura = 1.75
    #convertir flotante 
    edadString = str(edad) # Palabra que contiene el 2 y el 5 (25)
    booleanos = False # True

    print(type(edad))
    print(type(edadString))

    #Transformar string o palabra a entero
    edad = int(edad)

    # Estructura de control IF
    if edad >= 18 and edad < 100 : # Si edad es mayor o igual a 18 y menor a 100
        print("Hola {} pasale por tu Tonayán".format(nombre))
    elif edad >= 100 : # Si no, entonces ¿Edad es mayor o igual a 100?
        print("¿Acaso eres Chabelo?")
    elif edad <= 0 : # Si no, entonces ¿Edad es menor o igual a 0;
        print("No existes")
    else : # Si no - Si no se cumple ninguna de las anteriores
        print("Tas bebe") 



# Estructura de control FOR
while True :
    validacionEdad()
