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
labels={}
labels[1]=r'$b$'
labels[2]=r'$c$'
G=nx.Graph()
colors=range(20)
G.add_node(1)
G.add_node(2)
# H=nx.path_graph(10)
# G.add_nodes_from(H)
# G.add_edges_from(H.edges())
# G.add_nodes_from([12,13])
G.add_edge(1,2)
# G.add_node(1)
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,
                       nodelist=[1],
                       node_color='r',
                       node_size=500,
                   alpha=0.8)
nx.draw_networkx_nodes(G,pos,
                       nodelist=[2],
                       node_color='b',
                       node_size=500,
                   alpha=0.8)
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
nx.draw_networkx_labels(G,pos,labels)
# nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
plt.axis('off')
plt.savefig("edge_colormap.png") # save as png
plt.show()