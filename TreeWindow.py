import tkinter as tk
import networkx as nx
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class TreeWindow:
  def __init__(self, master, tree):
    self.master = master
    self.frame = tk.Frame(self.master)
    
    huffTree, pos = self.buildTree(tree)

    f = Figure(figsize=(15, 8))
    a = f.add_subplot(111)

    nx.draw(huffTree, pos=pos, with_labels=True, ax=a, node_color='g',  node_shape='v', alpha=0.5, arrows=True)
    labels = nx.get_edge_attributes(huffTree, 'weight')
    nx.draw_networkx_edge_labels(huffTree, pos, edge_labels=labels, ax=a , bbox=dict(facecolor='none', edgecolor='green', boxstyle='round'))

    self.plotFrame = tk.Frame(self.frame)
    self.plotFrame.pack()
    self.frame.pack()
    self.quitButton = tk.Button(self.frame, text = 'Salir', width = 25, command = self.close_windows)
    self.quitButton.pack()
    canvas = FigureCanvasTkAgg(f, self.plotFrame)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

  def close_windows(self):
    self.master.destroy()

  def buildTree(self, tree):
    edges = getEdges(tree)

    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    
    return G, hierarchy_pos(G, tree[2])

def getEdges(tree):
  edges = []
  _getEdges(tree, tree[2], 0, edges)
  return edges

def _getEdges(node, parent, value, list):
  if type(node[0]) is tuple:
    _getEdges(node[0], node[2], 0, list)
  
  if parent != node[2]:
    n = (parent, node[2], value)
    while n in list:
      n = (parent, str(n[1]) + "'", value)
    
    if type(node[0]) is str:
      n = (n[0], node[0] + ": " + str(n[1]), value)
    list.append(n)

  if type (node[1]) is tuple:
    _getEdges(node[1], node[2], 1, list)

def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, 
                  pos = None, parent = None):
  '''If there is a cycle that is reachable from root, then this will see infinite recursion.
      G: the graph
      root: the root node of current branch
      width: horizontal space allocated for this branch - avoids overlap with other branches
      vert_gap: gap between levels of hierarchy
      vert_loc: vertical location of root
      xcenter: horizontal location of root
      pos: a dict saying where all nodes go if they have been assigned
      parent: parent of this branch.'''
  if pos == None:
      pos = {root:(xcenter,vert_loc)}
  else:
      pos[root] = (xcenter, vert_loc)
  neighbors = G.neighbors(root)
  if parent != None and parent in neighbors:
      neighbors.remove(parent)
  if len(neighbors)!=0:
      dx = width/len(neighbors) 
      nextx = xcenter - width/2 - dx/2
      for neighbor in neighbors:
          nextx += dx
          pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap, 
                              vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos, 
                              parent = root)
  return pos