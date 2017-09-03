tabla_caracteres = {}
binStr = ""
tuppleArray = []

def Generar_Cadena_Binario(string):
    binary = ""
    for c in string:
        binary += tabla_caracteres[c]
    return binary + "1"


def Crear_Tabla_Caracteres(nodo_actual, codigo_actual=""):
    if type(nodo_actual[0]) != tuple:
        tabla_caracteres[nodo_actual[0]] = codigo_actual
    else:
        Crear_Tabla_Caracteres(nodo_actual[0], codigo_actual + "0")
        Crear_Tabla_Caracteres(nodo_actual[1], codigo_actual + "1")
    return


def Crear_Arbol(arrayTupla):
    for index in range(len(arrayTupla) - 1):
        arrayTupla = sorted(arrayTupla, key=lambda x: x[2])
        first = arrayTupla.pop(0)
        second = arrayTupla.pop(0)
        newTupple = (first, second, first[2] + second[2])
        arrayTupla.append(newTupple)

    newTree = arrayTupla[0]
    return newTree


def Crear_Arreglo(string):
    tuppleDictionary = {}
    for c in string:
        if c in tuppleDictionary:
            tuppleDictionary[c] += 1    
        else:
            tuppleDictionary[c] = 1

    tuppleArray = []
    for tupple in tuppleDictionary.items():
        newTuple = (tupple[0], tupple[0], tupple[1])
        tuppleArray.append(newTuple)

    return tuppleArray

