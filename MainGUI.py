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
        arreglo = algoritmo.Crear_Arreglo(self.txt_Entrada.get())
        arreglo = sorted(arreglo, key=lambda x: x[2])
        algoritmo.tuppleArray = arreglo
        arbol = algoritmo.Crear_Arbol(arreglo)
        algoritmo.Crear_Tabla_Caracteres(arbol)
        tabla_caracteres = algoritmo.tabla_caracteres
        self.Mostrar_Tabla(arreglo[::-1], tabla_caracteres)
        self.compress(self.txt_Entrada.get(), arbol)
        containerSimulator = tk.Label(self.fr_tabla, text="")

    def Mostrar_Tabla(self, arreglo, tabla_caracteres):
        """Shows the table"""
        self.clearFrame(self.fr_tabla)
        tabla = ttk.Treeview(self.fr_tabla)
        tabla["columns"] = ("caracter", "frecuencia", "codigo")
        tabla.heading('#0', text='Caracter')
        tabla.column('#0')
        tabla.heading('#1', text='Frecuencia')
        tabla.column('#1')
        tabla.heading('#2', text='Codigo')
        tabla.column('#2')
        for registros in arreglo:
            if registros[0] in string.printable:
                tabla.insert('', 'end', text=registros[0], values=(
                    registros[2], tabla_caracteres[registros[0]]))

        tabla.pack()
        containerSimulator = tk.Label(self. fr_tabla, text="")
        containerSimulator.pack()

    def clearFrame(self, fr_principal):
        for widget in fr_principal.winfo_children():
            widget.destroy()

    def compress(self, txt_entrada, arbol):
        self.clearFrame(self.fr_salida)
        cadena_binaria = algoritmo.Generar_Cadena_Binario(txt_entrada)
        end = len(cadena_binaria) - 1
        originalLabel = tk.Label(self.fr_salida, text="Original " + txt_entrada)
        originalLabel.pack()
        compessedLabel = tk.Label(
            self.fr_salida, text="Codificada: " + cadena_binaria[0:end])
        compessedLabel.pack()
        efficiencyLabel = tk.Label( self.fr_salida,
            text="Eficiencia: " + self.Calculo_eficiencia(txt_entrada, cadena_binaria)
        )
        algoritmo.binStr = cadena_binaria
        efficiencyLabel.pack()

        treeWindow = tk.Toplevel(self.root)
        self.treeWindow = TreeWindow(treeWindow, arbol)

    def Calculo_eficiencia(self, base, binary):
        if base == "" or binary == "":
            return ""

        fixedCoding = (math.ceil(
            math.log2(len(''.join(set(base))))) * len(base)) / 8.0 + 0.0
        dynamicCoding = math.ceil(len(binary) / 8.0) + 0.0
        return str(round((dynamicCoding / fixedCoding) * 100, 2)) + "%"

    def logica(self, contenido):
        arreglo = algoritmo.Crear_Arreglo(contenido)
        arreglo = sorted(arreglo, key=lambda x: x[2])
        algoritmo.tuppleArray = arreglo
        tree = algoritmo.Crear_Arbol(arreglo)
        algoritmo.Crear_Tabla_Caracteres(tree)
        dictionary = algoritmo.tabla_caracteres
        return arreglo, algoritmo, tree, dictionary

    def openFile(self):
        self.root.withdraw()
        txt_ruta = filedialog.askopenfilename()
        with open(txt_ruta, 'r') as myfile:
            data = myfile.read().replace('\n', '')
        txt_contenido = data

        arreglo, huff, arbol, tabla_caracteres = logica(self, txt_contenido)

        self.Mostrar_Tabla(arreglo[::-1], tabla_caracteres)
        self.root.deiconify()
        self.compress(txt_contenido, arbol)

def main():
    root = tk.Tk()
    app = MainProgram(root)
    root.mainloop()

if __name__ == '__main__':
    main()
