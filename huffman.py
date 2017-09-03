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
    tabla_nodos = {}
    for c in string:
        if c in tabla_nodos:
            tabla_nodos[c] += 1    
        else:
            tabla_nodos[c] = 1

    nuevo_arreglo_nodos = []
    for nuevo_nodo in tabla_nodos.items():
        newTuple = (nuevo_nodo[0], nuevo_nodo[0], nuevo_nodo[1])
        nuevo_arreglo_nodos.append(newTuple)

    return nuevo_arreglo_nodos

