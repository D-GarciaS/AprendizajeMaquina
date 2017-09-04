import tkinter as tk
import networkx as nx
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class TreeWindow:
    def __init__(self, master, arbol):
        self.master = master
        self.frame = tk.Frame(self.master)

        huffTree, pos = self.Construir_Arbol(arbol)

        figure = Figure()
        a = figure.add_subplot(111)

        nx.draw(huffTree, pos=pos, with_labels=True, ax=a,
                node_color='g',  node_shape='s', alpha=0.5, arrows=True)
        labels = nx.get_edge_attributes(huffTree, 'weight')
        nx.draw_networkx_edge_labels(huffTree, pos, edge_labels=labels, ax=a, bbox=dict(
            facecolor='none', edgecolor='green', boxstyle='round'))

        self.plotFrame = tk.Frame(self.frame)
        self.plotFrame.pack()
        self.frame.pack()
        self.quitButton = tk.Button(
            self.frame, text='Salir',  command=self.Cerrar_Ventana)
        self.quitButton.pack()
        canvas = FigureCanvasTkAgg(figure, self.plotFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def Cerrar_Ventana(self):
        self.master.destroy()

    def Construir_Arbol(self, arbol):
        edges = Get_Vertices(arbol)

        G = nx.DiGraph()
        G.add_weighted_edges_from(edges)

        return G, hierarchy_pos(G, arbol[2])


def Get_Vertices(arbol):
    vertices = []
    Get_Vertices_Helper(arbol, arbol[2], 0, vertices)
    return vertices


def Get_Vertices_Helper(nodo, padre, valor, lista):
    if type(nodo[0]) is tuple:
        Get_Vertices_Helper(nodo[0], nodo[2], 0, lista)

    if padre != nodo[2]:
        n = (padre, nodo[2], valor)
        while n in lista:
            n = (padre, str(n[1]) + "'", valor)

        if type(nodo[0]) is str:
            n = (n[0], nodo[0] + ": " + str(n[1]), valor)
        lista.append(n)

    if type(nodo[1]) is tuple:
        Get_Vertices_Helper(nodo[1], nodo[2], 1, lista)


def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5,
                  pos=None, parent=None):
    if pos == None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    if parent != None and parent in neighbors:
        neighbors.remove(parent)
    if len(neighbors) != 0:
        dx = width / len(neighbors)
        nextx = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap,
                                vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos,
                                parent=root)
    return pos
