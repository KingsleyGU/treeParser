"""
Draw a graph with matplotlib, color edges.
You must have matplotlib>=87.7 for this to work.
"""
# Author: Aric Hagberg (hagberg@lanl.gov)
try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=1)
# B.add_nodes_from(['a','b','c'], bipartite=1)
# B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a')])
B.add_edges_from([(1,2),(2,3),(3,4)])

pos=nx.spring_layout(B)

nx.draw(B,pos,width=1.0,alpha=0.5)
# nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
plt.axis('off')
plt.savefig("edge_colormap.png") # save as png
plt.show()