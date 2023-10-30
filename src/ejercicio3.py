#Tienes este código:

#palabra = 'banana'
#contador = 0
#for letra in palabra:
    #if letra == 'a':
        #contador = contador + 1
#print(contador)

#Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.

def cuenta(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

if __name__ == "__main__":
    palabra = 'banana'
    letra = 'a'
    resultado = cuenta(palabra, letra)
    print("La letra ", letra, " aparece ", resultado, " veces en la palabra ", palabra)

