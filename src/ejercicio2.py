#Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]?

def significado_fruta(fruta):
    resultado = fruta[:]
    return resultado

fruta = "manzana, sandia, uvas"
resultado = significado_fruta(fruta)
print("fruta[:] significa:", resultado)
print("Quiere decir que se copiara toda la cadena como se ve en el ejemplo de arriba")
