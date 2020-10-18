import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set()
G=nx.Graph()
sub_G=nx.Graph()
reader_points =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\Boruvka_Algorithm\kashan\kashan_points.xlsx')
reader_cost =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\Boruvka_Algorithm\kashan\kashan_cost.xlsx')
matrix_cost=np.array(reader_cost)
matrix_points=np.array(reader_points)
for i in range(matrix_points.shape[0]):
    G.add_node(i,pos=(matrix_points[i,1],matrix_points[i,2]))
for i in range (matrix_cost.shape[0]):
    G.add_edge(matrix_cost[i,0],matrix_cost[i,1], weight=matrix_cost[i,2]) 
pos=nx.get_node_attributes(G,'pos')
weight=nx.get_edge_attributes(G,'weight')
mst=list(tree.minimum_spanning_edges(G,algorithm='boruvka',data=False))
print(list(mst))

for i in range(matrix_points.shape[0]):
    sub_G.add_node(i,pos=(matrix_points[i,1],matrix_points[i,2]))
sub_G.add_edges_from(mst)

plt.figure()
nx.draw_networkx(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=weight,font_color='brown')
nx.draw_networkx_edges(G,pos,edgelist=mst,edge_color='r',width=5)
