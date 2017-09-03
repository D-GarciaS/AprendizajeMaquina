characterTable = {}
binStr = ""
tuppleArray = []

def createBinary(string):
    binary = ""
    for c in string:
        binary += characterTable[c]
    return binary + "1"


def createDictionary(currentNode, currentCode=""):
    if type(currentNode[0]) != tuple:
        characterTable[currentNode[0]] = currentCode
    else:
        createDictionary(currentNode[0], currentCode + "0")
        createDictionary(currentNode[1], currentCode + "1")
    return


def createTree(arrayTupla):
    for index in range(len(arrayTupla) - 1):
        arrayTupla = sorted(arrayTupla, key=lambda x: x[2])
        first = arrayTupla.pop(0)
        second = arrayTupla.pop(0)
        newTupple = (first, second, first[2] + second[2])
        arrayTupla.append(newTupple)

    newTree = arrayTupla[0]
    return newTree


def createArray(string):
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

