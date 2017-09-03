import tkinter as tk
import tkinter.ttk as ttk
import huffman as huff
import math
import bitstring
import codecs
import string
from tkinter import filedialog
from TreeWindow import TreeWindow


class MainProgram:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(self.root)

        self.inputFrame = tk.Frame(self.frame)
        self.tableFrame = tk.Frame(self.frame)
        self.codedTextFrame = tk.Frame(self.frame)
        self.textLabel = tk.Label(self.inputFrame, text="Introduzca el texto a codificar")
        self.textToCompress = tk.StringVar()
        self.textBox = tk.Entry(self.inputFrame, textvar=self.textToCompress)
        self.textButton = tk.Button(
            self.inputFrame, text="Comprimir", command=self.compressText)
        self.fileLabel = tk.Button(
            self.inputFrame, text="Seleccione un archivo de texto a codificar", command=self.openFile)

        self.inputFrame.pack()
        self.codedTextFrame.pack()
        self.tableFrame.pack(side=tk.BOTTOM)
        self.textLabel.pack()
        self.textBox.pack()
        self.textButton.pack()
        self.fileLabel.pack()

        self.frame.pack()

    def compressText(self):
        """Compresses text from the textbox"""
        if self.textToCompress.get() == "":
            return
        array = huff.createArray(self.textToCompress.get())
        array = sorted(array, key=lambda x: x[2])
        huff.tuppleArray = array
        tree = huff.createTree(array)
        huff.createDictionary(tree)
        dictionary = huff.characterTable
        self.showTable(array[::-1], dictionary)
        self.compress(self.textToCompress.get(), tree)
        containerSimulator = tk.Label(self.tableFrame, text="")

    def showTable(self, array, dictionary):
        """Shows the table"""
        self.clearFrame(self.tableFrame)
        table = ttk.Treeview(self.tableFrame)
        table["columns"] = ("freq", "code")
        table.heading('#0', text='Caracter', anchor='center')
        table.column('#0', anchor='center')
        table.heading('freq', text='Frecuencia')
        table.column('freq', anchor='center', width=80)
        table.heading('code', text='Codigo')
        table.column('code', anchor='center', width=80)
        counter = 0
        for tuples in array:
            if tuples[0] in string.printable:
                table.insert('', 'end', text=tuples[0], values=(
                    tuples[2], dictionary[tuples[0]]))
                counter += 1

        table.pack()
        containerSimulator = tk.Label(self. tableFrame, text="")
        containerSimulator.pack()

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def compress(self, textStr, tree):
        self.clearFrame(self.codedTextFrame)
        binary = huff.createBinary(textStr)
        end = len(binary)
        originalLabel = tk.Label(self.codedTextFrame, text="Original " + textStr )
        originalLabel.pack()
        compessedLabel = tk.Label(
            self.codedTextFrame, text="Codificada: " + binary[0:end])
        compessedLabel.pack()
        efficiencyLabel = tk.Label(
            self.codedTextFrame,
            text="Eficiencia: " + self.getEfficiency(textStr, binary)
        )
        efficiencyLabel.pack()
        huff.binStr = binary

        treeWindow = tk.Toplevel(self.root)
        self.treeWindow = TreeWindow(treeWindow, tree)

    def getEfficiency(self, base, binary):
        if base == "" or binary == "":
            return ""

        fixedCoding = (math.ceil(
            math.log2(len(''.join(set(base))))) * len(base)) / 8.0 + 0.0
        dynamicCoding = math.ceil(len(binary) / 8.0) + 0.0
        return str(round((dynamicCoding / fixedCoding) * 100, 2)) + "%"

    def openFile(self):
        self.root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path == "":
            self.root.deiconify()
            return

        fileContents = huff.readFromFile(file_path)
        array = huff.createArray(fileContents)
        array = sorted(array, key=lambda x: x[2])
        huff.tuppleArray = array
        tree = huff.createTree(array)
        huff.createDictionary(tree)
        dictionary = huff.characterTable
        self.showTable(array[::-1], dictionary)
        self.root.deiconify()
        self.compress(fileContents, tree)

def main():
    root = tk.Tk()
    app = MainProgram(root)
    root.mainloop()


if __name__ == '__main__':
    main()
