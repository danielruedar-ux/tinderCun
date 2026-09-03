def registrarPersonas():
    #Variables
    individuo = {}
    nombre = input("como te llamas: ")
    individuo["Nombre"] = nombre

    edadValida = False
    while not edadValida:
        edad = int(input("ingrese su edad: "))
        if edad < 18:
            print("no aceptamos menores de 18")
        else:
            edadValida = True
            individuo["Edad"] = edad

    ciudad = input("¿En que ciudad vives?: ")
    individuo["Ciudad"] = ciudad

    generos = ["hombre", "mujer"]
    generoValido = False
    while not generoValido:
        print(generos)
        genero = input("Cual es tu genero: ")
        if genero in generos:
            individuo["Genero"] = genero
            generoValido = True

    generoQueBusca = ["hombre", "mujer"]
    generoValido = False
    while not generoValido:
        print(generoQueBusca)
        genero = input("¿Cual es tu genero de interes?: ")
        if genero in generoQueBusca:
            individuo["GeneroInteres"] = genero  
            generoValido = True

    edadMinima = 18
    edadMaxima = 100
    individuo["RangoEdadBuscado"] = (edadMinima, edadMaxima)

    listaDeIntereses = input("ingrese sus intereses(hobbies, signo zodiacal, cosas favoritas)") 
    individuo["Intereses"] = listaDeIntereses

    print(individuo)
    return individuo


def mostrarPersonas(personas):
    print(personas)


def main():
    opciones = "1. registrar personas  \n2. mostrar las personas \n9. salir"
    print(opciones)
    opcion = int(input("digite la opcion que necesita: "))

    personas = {}  

    while opcion != 9:
        if opcion == 1:
            cuantasPersonas = int(input("¿Cuantas Personas se van a registrar?: "))
            for i in range(cuantasPersonas):
                print("i", i)
                personas[len(personas)] = registrarPersonas()   
            mostrarPersonas(personas)

        elif opcion == 2:
            mostrarPersonas(personas) 

        else:
            print("Opcion invalida")

        print(opciones)
        opcion = int(input("digite la opcion que necesita: "))

    print("GRACIAS")  


main()
