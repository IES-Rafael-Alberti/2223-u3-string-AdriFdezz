#Hay un método de cadenas llamado count que es similar a find.
#escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.

def contar_letra_count(cadena, letra):
    contar = cadena.count(letra)
    return contar

if __name__ == "__main__":
    palabra = "banana"
    letra = "a"
    resultado = contar_letra_count(palabra, letra)
    print("La letra ", letra, " aparece ", resultado, " veces en la palabra ", palabra)
