def registrarPersonas():
    individuo={}
    nombre= input("ingrese su nombre")
    individuo["nombre"]=nombre
    edad= int(input("ingrese su edad"))
    individuo["edad"]
    ciudad= input("ingrese la ciudad donde se encuentra ubicado")
    individuo["ciudad"]=ciudad
    genero=input("ingrese su genero")
    individuo["genero"]=genero
    generoBuscar=input("ingrese el genero en el que esta interesado")
    individuo["genero a buscar"]=generoBuscar
    edadMin=input("ingrese la edad minima para una posible pareja")
    individuo["edad minima"]=edadMin
    edadMax=input("ingrese la edad maxima para una posible pareja")
    individuo["edad maxima"]=edadMax
    listaIntereses=input("ingrese sus interes y hobbies")
    individuo["edad maxima"]=listaIntereses
    distanciaMax=input("ingrese la distancia maxima que esta dispuesta a aceptar(km)")
    individuo["distancia maxima"]=distanciaMax
    print(individuo)
    return individuo
    

   
 def mostrarPersonas(personas):
     print(personas)
     
   

def main():
    cuntasPersonas=int(input("cauntas personas se van a registrar"))
    #registrado de personas
    personas=()

    for i in range (0,cuantasPersonas):
        print("i",1)
        print(personas)
        personas[i]=registrarPersonas()

        #mostrar personas

        mostrarPersonas(personas)
        
main()


