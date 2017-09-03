import huffman as algoritmo
import math
import string
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from TreeWindow import TreeWindow


class MainProgram:
    def __init__(self, root):
        self.root = root
        self.fr_principal = tk.Frame(self.root)

        self.fr_input = tk.Frame(self.fr_principal)
        self.fr_tabla = tk.Frame(self.fr_principal)
        self.fr_salida = tk.Frame(self.fr_principal)

        self.lbl_introducir = tk.Label(self.fr_input, text="Introduzca el texto a codificar")
        self.txt_Entrada = tk.StringVar()
        self.tbx_Entrada = tk.Entry(self.fr_input, textvar=self.txt_Entrada)
        self.btn_comprimir = tk.Button(
            self.fr_input, text="Comprimir", command=self.Comprimir_Entrada)
        self.lbl_archivo = tk.Button(
            self.fr_input, text="Seleccione un archivo de texto a codificar", command=self.openFile)

        self.fr_input.pack()
        self.fr_salida.pack()
        self.fr_tabla.pack()
        self.lbl_introducir.pack()
        self.tbx_Entrada.pack()
        self.btn_comprimir.pack()
        self.lbl_archivo.pack()

        self.fr_principal.pack()

    def Comprimir_Entrada(self):
        array = algoritmo.createArray(self.txt_Entrada.get())
        array = sorted(array, key=lambda x: x[2])
        algoritmo.tuppleArray = array
        tree = algoritmo.createTree(array)
        algoritmo.createDictionary(tree)
        dictionary = algoritmo.characterTable
        self.showTable(array[::-1], dictionary)
        self.compress(self.txt_Entrada.get(), tree)
        containerSimulator = tk.Label(self.fr_tabla, text="")

    def showTable(self, array, dictionary):
        """Shows the table"""
        self.clearFrame(self.fr_tabla)
        table = ttk.Treeview(self.fr_tabla)
        table["columns"] = ("freq", "code")
        table.heading('#0', text='Caracter')
        table.column('#0')
        table.heading('freq', text='Frecuencia')
        table.column('freq')
        table.heading('code', text='Codigo')
        table.column('code')
        counter = 0
        for tuples in array:
            if tuples[0] in string.printable:
                table.insert('', 'end', text=tuples[0], values=(
                    tuples[2], dictionary[tuples[0]]))
                counter += 1

        table.pack()
        containerSimulator = tk.Label(self. fr_tabla, text="")
        containerSimulator.pack()

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def compress(self, textStr, tree):
        self.clearFrame(self.fr_salida)
        binary = algoritmo.createBinary(textStr)
        end = len(binary) - 1 
        originalLabel = tk.Label(self.fr_salida, text="Original " + textStr)
        originalLabel.pack()
        compessedLabel = tk.Label(
            self.fr_salida, text="Codificada: " + binary[0:end])
        compessedLabel.pack()
        efficiencyLabel = tk.Label(
            self.fr_salida,
            text="Eficiencia: " + self.getEfficiency(textStr, binary)
        )
        efficiencyLabel.pack()
        algoritmo.binStr = binary

        treeWindow = tk.Toplevel(self.root)
        self.treeWindow = TreeWindow(treeWindow, tree)

    def getEfficiency(self, base, binary):
        if base == "" or binary == "":
            return ""

        fixedCoding = (math.ceil(
            math.log2(len(''.join(set(base))))) * len(base)) / 8.0 + 0.0
        dynamicCoding = math.ceil(len(binary) / 8.0) + 0.0
        return str(round((dynamicCoding / fixedCoding) * 100, 2)) + "%"

    def logica(self, contents):
        array = algoritmo.createArray(contents)
        array = sorted(array, key=lambda x: x[2])
        algoritmo.tuppleArray = array
        tree = algoritmo.createTree(array)
        algoritmo.createDictionary(tree)
        dictionary = algoritmo.characterTable
        return array, algoritmo, tree, dictionary


    def openFile(self):
        self.root.withdraw()
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r') as myfile:
            data = myfile.read().replace('\n', '')
        fileContents = readFromFile(file_path)

        array, huff, tree, dictionary = logica(self, fileContents)

        self.showTable(array[::-1], dictionary)
        self.root.deiconify()
        self.compress(fileContents, tree)
    

def main():
    root = tk.Tk()
    app = MainProgram(root)
    root.mainloop()

if __name__ == '__main__':
    main()
