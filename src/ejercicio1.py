#Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás 
#hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.

def obtener_cadena(cadena):
    posicion = len(cadena) - 1
    cadena_inversa = ""

    while posicion >= 0:
        cadena_inversa += cadena[posicion] + "\n"
        posicion -= 1

    return cadena_inversa

if __name__ == "__main__":
    cadena = "Hola Adrian"
    resultado = obtener_cadena(cadena)
    print("Resultado:", resultado)