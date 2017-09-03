tabla_caracteres = {}
cadena_binaria = ""
arreglo_nodos = []

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


def Crear_Arbol(arreglo_nodos):
    for i in range(len(arreglo_nodos) - 1):
        arreglo_nodos = sorted(arreglo_nodos, key=lambda x: x[2])
        primero = arreglo_nodos.pop(0)
        segundo = arreglo_nodos.pop(0)
        nuevo_nodo = (primero, segundo, primero[2] + segundo[2])
        arreglo_nodos.append(nuevo_nodo)

    nuevo_arbol = arreglo_nodos[0]
    return nuevo_arbol


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

