import networkx as nx
import matplotlib.pyplot as plt
import json
from pprint import pprint
def draw_graph(G,graph, labels=None, graph_layout='shell',
			   node_size=2000, node_color='blue', node_alpha=0.3,
			   node_text_size=12,
			   edge_color='blue', edge_alpha=0.3, edge_tickness=1,
			   edge_text_pos=0.3,
			   text_font='sans-serif'):

	for edge in graph:
		G.add_edge(edge[0], edge[1])

	# these are different layouts for the network you may try
	# shell seems to work best
	if graph_layout == 'spring':
		graph_pos=nx.spring_layout(G)
	elif graph_layout == 'spectral':
		graph_pos=nx.spectral_layout(G)
	elif graph_layout == 'random':
		graph_pos=nx.random_layout(G)
	else:
		graph_pos=nx.shell_layout(G)

	graph_pos=nx.drawing.nx_agraph.graphviz_layout(G,prog='neato',root=0) #neato or dot
	print("position {0}".format(graph_pos[0][1]))
	# draw graph
	H = nx.DiGraph()
	H_pos = {}
	# for index in range(0,len(G.nodes()))
	par = 15
	gap = par + par/2
	for index in G.nodes():
		for i in range(0,12):
			# print("i {0}".format(i))
			H.add_node(12*index+i)
			if i < 3 :
				H_pos[12*index+i] = (graph_pos[index][0]+gap,graph_pos[index][1]+(i-1/2)*par)
			elif i < 6 :
				H_pos[12*index+i] = (graph_pos[index][0]-par*(i-3.5),graph_pos[index][1]+gap)
			elif i < 9 :
				H_pos[12*index+i] = (graph_pos[index][0]-gap,graph_pos[index][1]-par*(i-6.5))
			else:
				H_pos[12*index+i] = (graph_pos[index][0]+par*(i-9.5),graph_pos[index][1]-gap)
			if i<11 :
				H.add_edge(12*index+i,12*index+i+1)
			else:
				H.add_edge(12*index+i,12*index)

	nx.draw_networkx_nodes(H,H_pos,node_size=0,alpha=1,node_color='b',node_shape='s',linewidths=0)
	nx.draw_networkx_edges(H,H_pos,width=2,edge_color='b',style="solid",arrows=False)
	for edge in graph:
		# print("tellPosition {0}".format(tellPosition(edge[0],edge[1],graph_pos,gap)))
		if tellPosition(edge[0],edge[1],graph_pos,gap) == 1:
			if(graph_pos[edge[0]][0] > graph_pos[edge[1]][0]):
				edgeFrom = 12*edge[0]+ 5
				edgeTo = 12*edge[1]+10
			else:
				edgeFrom = 12*edge[0]+ 3
				edgeTo = 12*edge[1]+ 8
			H.add_edge(edgeFrom,edgeTo)
			nx.draw_networkx_edges(H,H_pos,edgelist=[(edgeFrom,edgeTo)],width=2,edge_color='b',style="dashed",arrows=True)
		elif tellPosition(edge[0],edge[1],graph_pos,gap) == 2:
			if(graph_pos[edge[0]][0] > graph_pos[edge[1]][0]):
				edgeFrom = 12*edge[0]+ 9
				edgeTo = 12*edge[1]+2
			else:
				edgeFrom = 12*edge[0]+ 11
				edgeTo = 12*edge[1]+ 4
			H.add_edge(edgeFrom,edgeTo)
			nx.draw_networkx_edges(H,H_pos,edgelist=[(edgeFrom,edgeTo)],width=2,edge_color='b',style="dashed",arrows=True)			
		elif tellPosition(edge[0],edge[1],graph_pos,gap) == 3:
			if(graph_pos[edge[0]][1] > graph_pos[edge[1]][1]):
				edgeFrom = 12*edge[0]+ 0
				edgeTo = 12*edge[1]+5
			else:
				edgeFrom = 12*edge[0]+ 2
				edgeTo = 12*edge[1]+ 7
			H.add_edge(edgeFrom,edgeTo)
			nx.draw_networkx_edges(H,H_pos,edgelist=[(edgeFrom,edgeTo)],width=2,edge_color='b',style="dashed",arrows=True)			
		else:
			if(graph_pos[edge[0]][1] > graph_pos[edge[1]][1]):
				edgeFrom = 12*edge[0]+ 8
				edgeTo = 12*edge[1]+1
			elif(graph_pos[edge[0]][1] < graph_pos[edge[1]][1]):
				edgeFrom = 12*edge[0]+ 6
				edgeTo = 12*edge[1]+ 11

			H.add_edge(edgeFrom,edgeTo)
			nx.draw_networkx_edges(H,H_pos,edgelist=[(edgeFrom,edgeTo)],width=2,edge_color='b',style="dashed",arrows=True)			
			
	# nx.draw_networkx_nodes(G,graph_pos,node_size=8000,alpha=0.5,node_color='#ff0000',node_shape='s',linewidths=0)
	# nx.draw_networkx_edges(G,graph_pos,width=2,edge_color='b',style="solid",arrows=False)

	nx.draw_networkx_labels(G,graph_pos,labels,font_size=16)
	# nx.draw_networkx_edges(H,H_pos,width=2,edge_color='b',style="solid",arrows=False)
	# nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,font_family=text_font)


	plt.show()
def tellPosition(start,end,G_pos,gap):
	if G_pos[start][0]+gap < G_pos[end][0]-gap: 
		return 3
	elif G_pos[start][0]-gap > G_pos[end][0]+gap: 
		return 4
	# to see if the edge is from down to up:
	elif G_pos[start][1]+ gap < G_pos[end][1]-gap: 
		return 1 
	# to see if the edge is from up to down:
	# elif G_pos[start][1]-gap > G_pos[end][1]+gap: 
	else:
		return 2	
	# to see if the edge is from left to right:


with open('model.json') as data_file:    
    data = json.load(data_file)

modelLocations = data['MODELnodes']
locationIdMap = {}
LocationGraph = []
labels = {}
G=nx.Graph()
for index in range(0,len(modelLocations)):
	print("model node {0}".format(modelLocations[index]))
	locationIdMap[modelLocations[index]] = index
	labels[index] = modelLocations[index]
	G.add_node(index)
for location in modelLocations:
	edgeList = data[location]
	for node in edgeList:
		if (locationIdMap[location],locationIdMap[node]) not in LocationGraph:
			LocationGraph.append((locationIdMap[location],locationIdMap[node]))
		if location in data[node]:
			if (locationIdMap[node],locationIdMap[location]) not in LocationGraph:
				LocationGraph.append((locationIdMap[node],locationIdMap[location]))	
print("lowest resource: {0}".format(repr(labels)))
print("graph edges: {0}".format(repr(LocationGraph)))


# LocationGraph = [(1,4),(4,1),(0, 2),(2,0),(4,2),(2,3),(3,2),(1,3)]
LocationGraph = [(0,1),(0,2),(2,0),(0, 4),(4,0),(3,0),(1,3)]

# you may name your edge labels
# labels = {}
# labels[0] = "A1"
# labels[1] = "Door"
# labels[2] = "City"
# labels[3] = "Bank"
# labels[4] = "Home"
# labels[5] = "School"
#draw_graph(graph, labels)

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
draw_graph(G,LocationGraph,labels)


