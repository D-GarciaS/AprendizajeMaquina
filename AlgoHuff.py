tabla_caracteres = {}
cadena_binaria = ""
arreglo_nodos = []


def Crear_Arbol(arreglo_nodos):
    for i in range(len(arreglo_nodos) - 1):
        arreglo_nodos = sorted(arreglo_nodos, key=lambda x: x[2])
        primero = arreglo_nodos.pop(0)
        segundo = arreglo_nodos.pop(0)
        nuevo_nodo = (primero, segundo, primero[2] + segundo[2])
        arreglo_nodos.append(nuevo_nodo)

    nuevo_arbol = arreglo_nodos[0]
    return nuevo_arbol


def Crear_Arreglo(cadena):
    nuevo_tabla_nodos = {}
    for c in cadena:
        if c in nuevo_tabla_nodos:
            nuevo_tabla_nodos[c] += 1
        else:
            nuevo_tabla_nodos[c] = 1

    nuevo_arreglo_nodos = []
    for caracter in nuevo_tabla_nodos.items():
        nuevo_nodo = (caracter[0], caracter[0], caracter[1])
        nuevo_arreglo_nodos.append(nuevo_nodo)

    return nuevo_arreglo_nodos


def Generar_Cadena_Binario(cadena):
    binary = ""
    for c in cadena:
        binary += tabla_caracteres[c]
    return binary + "1"


def Crear_Tabla_Caracteres(nodo_actual, codigo_actual=""):
    if type(nodo_actual[0]) != tuple:
        tabla_caracteres[nodo_actual[0]] = codigo_actual
    else:
        Crear_Tabla_Caracteres(nodo_actual[0], codigo_actual + "0")
        Crear_Tabla_Caracteres(nodo_actual[1], codigo_actual + "1")
    return
