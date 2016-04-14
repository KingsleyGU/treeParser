try:
	import matplotlib.pyplot as plt
except:
	raise

import networkx as nx
from collections import OrderedDict
def createGraph(nodesMap,finalPathList,finalNodesPathList,finalEdgesList,finalPathCost,profit):
	G = nx.DiGraph()
	G.add_nodes_from(range(0,len(nodesMap)))
	nodeColorFactorList = []
	nodeColorList = []
	for i in range(0,len(nodesMap)):
		nodeColorFactorList.append(0)
	# print("color Factor list 1  {0},".format(repr(nodeColorFactorList)))
	for pathIndex in finalNodesPathList:
		for node in finalNodesPathList[pathIndex]:
			if nodeColorFactorList[node] < finalPathCost[pathIndex]['colorFactor']:
				nodeColorFactorList[node] = finalPathCost[pathIndex]['colorFactor']
	# print("color Factor list 2  {0},".format(repr(nodeColorFactorList)))
	labels = getLabelList(nodesMap)
	lowestResource = getSmallestResource(finalPathCost)
	largestColorFactor = getlargestColorFactor(finalPathCost)
	for edgeIndex in finalEdgesList:
		for edge in finalEdgesList[edgeIndex]:
			
			# if not G[(edge[0])][(edge[1])]['weight']:
				# G[edge[1]][edge[1]]['weight'] = (finalPathCost[edgeIndex]['cost']/100)
			# tempWeight = finalPathCost[edgeIndex]['cost']/lowestCost
			
			G.add_edge(edge[0], edge[1])
			# G.add_edge(edge[0], edge[1],,weight=(finalPathCost[edgeIndex]['cost']/lowestCost))
			# if (not G[edge[0]][edge[1]]) or (G[edge[0]][edge[1]] and (not G[edge[0]][edge[1]]['weight'])) or (G[edge[0]][edge[1]]['weight'] < (finalPathCost[edgeIndex]['cost']/100)):
			# 	G.add_edge(edge[0], edge[1],weight = tempWeight)
			# elif (finalPathCost[edgeIndex]['cost']/100) > G[(edge[0])][(edge[1])]['weight']:
			# 	G[(edge[0])][(edge[1])]['weight'] = (finalPathCost[edgeIndex]['cost']/100)
	# print("lowest resource: {0}".format(repr(lowestResource)))
	# pos=nx.spring_layout(G,scale=20)
	# edges=G.edges()
	# weights = [G[u][v]['weight'] for u,v in edges]
	# nx.draw_networkx_nodes(G,pos,node_size=150,linewidths=0)
	# nx.draw_networkx_edges(G,pos,edges=edges,width=weights,length=342.7)
	# nx.draw_networkx_labels(G,pos,labels,font_size=5)
	# T= nx.Graph(G) 
	# nx.draw(T) 
	A = nx.nx_agraph.to_agraph(G) 
	# A.write('test.dot') 
	for i in range(0,len(nodesMap)):
		tempfactor = nodeColorFactorList[i]/largestColorFactor
		nodeColorList.append("#" + getHexValue(int(round(255*tempfactor)))+getHexValue(int(round(255 -255*tempfactor)))+"00")	
	# print("lowest resource: {0}".format(repr(nodeColorList)))
	pos=nx.drawing.nx_agraph.graphviz_layout(G,prog='dot',root=(len(nodesMap)-1))
	# pos = hierarchy_pos(G,len(nodesMap)-1)
	# pos = hierarchy_pos(G,len(nodesMap)-1) 
	# nx.draw(G,pos,labels=labels,arrows=False)
	# edges=G.edges()
	# weights = [G[u][v]['weight'] for u,v in edges]
	# print("edges:".format(edges))
	# print("edges:".format(weights))
	# colors = [G[u][v]['color'] for u,v in edges]
	# print("colors".format(colors))
	# 
	B = nx.MultiGraph()
	B.add_nodes_from(range(0,len(nodesMap)))
	nx.draw_networkx_nodes(B,pos,node_size=250,linewidths=0,node_color=nodeColorList,alpha=0.6)
	# labels = getLabelList(nodesMap)
	# lowestCost = getSmallestCost(nodesMap)
	pathCost = OrderedDict(sorted(finalPathCost.items(),key=lambda kv: kv[1]['colorFactor']))
	for edgeIndex in pathCost:
		for edge in finalEdgesList[edgeIndex]:
			
			# if not G[(edge[0])][(edge[1])]['weight']:
				# G[edge[1]][edge[1]]['weight'] = (finalPathCost[edgeIndex]['cost']/100)
			# width = getwidth(finalPathCost[edgeIndex]['resource'],lowestResource)
			width = getwidth(finalPathCost[edgeIndex]['resource']/lowestResource)
			alpha = intepreterLevel(finalPathCost[edgeIndex]['likelihood'])/4
			# tempfactor = int(profit)*finalPathCost[edgeIndex]['resource']*intepreterLevel(finalPathCost[edgeIndex]['likelihood'])
			tempfactor = finalPathCost[edgeIndex]['colorFactor']/largestColorFactor
			print("width: {0}".format(width))
			color=("#" + getHexValue(int(round(255*tempfactor)))+getHexValue(int(round(255 -255*tempfactor)))+"00")
			# if tempWeight>5:
			# 	color = 'g'
			# elif tempWeight <5 and tempWeight >2:
			# 	color = 'b'
			# else:
			# 	color = 'r'
			
			# B.add_edge(edge[0], edge[1],weight=tempWeight)
			nx.draw_networkx_edges(B,pos,edgelist=[(edge[0], edge[1])],width=width,edge_color=color,edge_cmap=plt.cm.Blues,length=342,alpha=alpha)
	
	nx.draw_networkx_labels(B,pos,labels,font_size=5)
	plt.savefig('nx_test.png')

	# P = G.plot(layout='tree', tree_root=(len(nodesMap)-1)) 
	# P.show()
	# plt.axis('off')
	# plt.savefig("labels_and_colors.png") # save as png
	plt.show() # display

# def getwidth(originalResource,lowestResource):
# 	return int(round(originalWidth/(1+4/originalWidth)))
def getwidth(originalWidth):
	# if originalWidth >5:
	# 	return 5
	# elif originalWidth <1:
	# 	return 1
	# else:
	return 5/(1+4/originalWidth)
def addEdgeWithWeight(vectorStart,vectorEnd,weight):
	return false
def getSmallestResource(finalPathCost):
	resource = 1;
	for index in finalPathCost:
		if finalPathCost[index]['resource'] < resource:
			resource = finalPathCost[index]['resource']
	return resource
# def interpreteTime(timeLabel):
def getlargestColorFactor(finalPathCost):
	colorFactor = 0
	for index in finalPathCost:
		if colorFactor < finalPathCost[index]['colorFactor']:
			colorFactor = finalPathCost[index]['colorFactor']
	return colorFactor
def getHexValue(decimalValue):
	return format(int(round(decimalValue)), '02x')
	# return hex(int(round(decimalValue))).split('x')[1]
def getLabelList(nodesMap):
	labels={}
	for nodeName in nodesMap:
		label = nodesMap[nodeName]['label']
		if len(label) >20 :
			labels[nodeName] = label[0:19] +"/n" + label[20:]
		else:
			labels[nodeName] = label
	return labels
def interpreterTime(timeLabel):
	if timeLabel == "MT":
		return 1
	elif timeLabel == "HR":
		return 2
	elif timeLabel == "DY":
		return 3
	else:
		return 4
def intepreterLevel(levelLable):
	if levelLable == "V":
		return 4
	elif levelLable == "H":
		return 3
	elif levelLable == "M":
		return 2
	else:
		return 1
