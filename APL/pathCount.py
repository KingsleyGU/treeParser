import csv
from visualization import createGraph
from collections import OrderedDict
import json




# this function is to figure out all the possible paths in an attack tree
def processPathCount(nodesMap,profit):
	global finalPathList
	rootIndex = len(nodesMap) - 1
	pathList = []
	finalPathListLength = 0
	startList = []
	startList.append(rootIndex)
	pathList.append(startList)
	change = True;
	while change:
		change = False;
		while len(pathList)>0:
			childrenList = pathList.pop()
			childnode = -1
			tempList = []
			while len(childrenList)>0:
				childnode = childrenList.pop()
				# print("node index: {0}, isLeaf: {1}".format(childnode,isLeafNode(nodesMap,childnode)))
				if isLeafNode(nodesMap,childnode):
					tempList.append(childnode)
				else:
					change = True;
					# print("node index: {0}, connection: {1}".format(childnode,nodesMap[childnode]['connection']))
					if nodesMap[childnode]['connection'] == 'add':
						for child in nodesMap[childnode]['childrenSet']:
							tempList.append(child)
						pathList.append(tempList + childrenList)				
					else:
						# print("tempList: {0}".format(repr(tempList)))
						for child in nodesMap[childnode]['childrenSet']:
							# print("child: {0}".format(child))
							tempList.append(child)
							pathList.append(tempList + childrenList)
							tempList.pop()
							# tempList.pop()
						# tempList = []		
					break;
				# print("pathList: {0}".format(repr(pathList)))
				# print("tempList: {0}".format(repr(tempList)))
			if change:
				break;
			else:
				finalPathList[finalPathListLength] =  tempList
				finalPathListLength += 1

	# print("length of finalPathList: {0}".format(len(finalPathList)))
	# print("Final paths: {0}".format(repr(finalPathList)))

	# nodesMap['finalPathList'] = finalPathList
	processNodePathCount(nodesMap,profit)

# this function is to get all the nodes in each path
def processNodePathCount(nodesMap,profit):
	global finalNodesPathList
	global finalEdgesList
	global finalPathCost
	for index in finalPathList:
		finalNodesPathList[index] = []
		finalEdgesList[index] = []
		for node in finalPathList[index]:
			finalNodesPathList[index].append(node)
			tempNode = nodesMap[node]['parent']

			finalEdgesList[index].append([tempNode,node])
			while (tempNode != -1):
				if (nodesMap[tempNode]['parent'] != -1):
					finalEdgesList[index].append([nodesMap[tempNode]['parent'],tempNode])
				if tempNode not in finalNodesPathList[index]:
					finalNodesPathList[index].append(tempNode)
				tempNode = nodesMap[tempNode]['parent']
		finalPathCost[index] = calculatePathCost(nodesMap,index,profit)
	printPath(nodesMap)
	modelData = generateModelVisualiztionJson(nodesMap)
	print("modelData: {0}".format(repr(modelData)))
	createGraph(nodesMap,finalPathList,finalNodesPathList,finalEdgesList,finalPathCost,profit)
	# print("Final node paths: {0}".format(repr(finalNodesPathList)))

# this function is for printing all the detail path information to a csv file
def printPath(nodesMap):
	pathData = [['ID', 'Path_Leafs','Path_Nodes','Path_Edges','Path_Weight_Measurement']]
	pathCost = OrderedDict(sorted(finalPathCost.items(),key=lambda kv: kv[1]['colorFactor'], reverse=True))
	for pathIndex in pathCost:
		# print("id:{0} count:{1} children:{2} connection:{3} label:{4}".format(nodeName,repr(nodesMap[nodeName]['childrenCount']),repr(nodesMap[nodeName]['childrenSet']),nodesMap[nodeName]['connection'],nodesMap[nodeName]['label']))
		pathElement = []
		pathElement.append(pathIndex)
		pathElement.append(repr(finalPathList[pathIndex]))
		pathElement.append(repr(finalNodesPathList[pathIndex]))
		pathElement.append(repr(finalEdgesList[pathIndex]))
		pathElement.append(repr(pathCost[pathIndex]))
		pathData.append(pathElement)
	with open('path.csv', 'w', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(pathData)





def getSmallestResource():
	resource = 1;
	for index in finalPathCost:
		if finalPathCost[index]['resource'] < resource:
			resource = finalPathCost[index]['resource']
	return resource
def getlargestColorFactor():
	colorFactor = 0
	for index in finalPathCost:
		if colorFactor < finalPathCost[index]['colorFactor']:
			colorFactor = finalPathCost[index]['colorFactor']
	return colorFactor
def getwidth(factor):
	return 4/(1+1/factor)	



# Located in pathCount.py
# this is the function for mapping attack tree to model , 
# it would use some information regarding the paths in the attack tree
# It would produce a json file which could be used for model visualization
def generateModelVisualiztionJson(nodesMap):
	pathCost = OrderedDict(sorted(finalPathCost.items(),key=lambda kv: kv[1]['colorFactor'], reverse=True))
	with open('model_element.json') as data_file:
		data = json.load(data_file)
	modelData = {}
	modelData['nodes'] = {}
	modelData['edges'] = {}
	modelNodeList = data['MODELnodes'] + data['MODELactors'] + data['MODELassets']
	smallestResource = getSmallestResource()
	largestColorFactor = getlargestColorFactor()
	for pathIndex in pathCost:
		for leaf in finalPathList[pathIndex]:
			for modelNode in modelNodeList:
				if modelNode+" " in nodesMap[leaf]['label']:
					modelData['nodes'][modelNode] = {}
					modelData['nodes'][modelNode]['likelihood'] = intepreterLevel(pathCost[pathIndex]['likelihood'])
					modelData['nodes'][modelNode]['resource'] = int(round(getwidth(pathCost[pathIndex]['resource']/smallestResource)))
					modelData['nodes'][modelNode]['colorFactor'] = int(round(4*pathCost[pathIndex]['colorFactor']/largestColorFactor))
					modelNodeList.remove(modelNode)
			if "MOVE" in nodesMap[leaf]['label'] or "FORCE" in nodesMap[leaf]['label']:
				label = nodesMap[leaf]['label']
				labelArray = label.split()
				endNode = labelArray[len(labelArray)-1]
				startNode = labelArray[len(labelArray)-2]
				# print("11111111{0}".format(startNode))
				while(startNode not in data['MODELnodes']):
					startNode = data[startNode][0]	
				# print("2222222222222{0}".format(startNode))
				if endNode not in data[startNode]:
					endNode = "city"
				if startNode+endNode not in modelData['edges']:
					if startNode not in modelData['nodes']:
						modelData['nodes'][startNode] = {}
						modelData['nodes'][startNode]['likelihood'] = intepreterLevel(pathCost[pathIndex]['likelihood'])
						modelData['nodes'][startNode]['resource'] = int(round(getwidth(pathCost[pathIndex]['resource']/smallestResource)))
						modelData['nodes'][startNode]['colorFactor'] = int(round(4*pathCost[pathIndex]['colorFactor']/largestColorFactor))						
					if endNode not in modelData['nodes']:
						modelData['nodes'][endNode] = {}
						modelData['nodes'][endNode]['likelihood'] = intepreterLevel(pathCost[pathIndex]['likelihood'])
						modelData['nodes'][endNode]['resource'] = int(round(getwidth(pathCost[pathIndex]['resource']/smallestResource)))
						modelData['nodes'][endNode]['colorFactor'] = int(round(4*pathCost[pathIndex]['colorFactor']/largestColorFactor))											
					modelData['edges'][startNode+endNode]={}
					modelData['edges'][startNode+endNode]['likelihood'] = intepreterLevel(pathCost[pathIndex]['likelihood'])
					modelData['edges'][startNode+endNode]['resource'] = int(round(getwidth(pathCost[pathIndex]['resource']/smallestResource)))
					modelData['edges'][startNode+endNode]['colorFactor'] = int(round(4*pathCost[pathIndex]['colorFactor']/largestColorFactor))

		if len(modelNodeList) == 0:
			break
	with open('model_visualization.json', 'w') as outfile:
		json.dump(modelData, outfile)
	return modelData





















def calculatePathCost(nodesMap,pathIndex,profit):
	global finalPathList
	cost = 0
	difficulty = "L"
	likelihood = "H"
	time = "MT"
	parameterMap = {}
	for nodeIndex in finalPathList[pathIndex]:
		cost = mergeCost(cost,nodesMap[nodeIndex]['cost']['cost'])
		difficulty = mergeDifficulties(difficulty,nodesMap[nodeIndex]['cost']['difficulty'])
		likelihood = mergeLikelihood(likelihood,nodesMap[nodeIndex]['cost']['likelihood'])
		time = mergeTime(time,nodesMap[nodeIndex]['cost']['time'])
	parameterMap['cost'] = cost
	parameterMap['likelihood'] = likelihood
	parameterMap['difficulty'] =  difficulty
	parameterMap['time'] = time
	parameterMap['resource'] = 1/(cost*interpreterTime(time)*intepreterLevel(difficulty))
	parameterMap['colorFactor'] = int(profit)*interpreterTime(likelihood)*parameterMap['resource']
	# finalPathCost['cost'] = parameterMap
	return parameterMap	
def mergeDifficulties(mainDifficulty,subDifficulty):
	if mainDifficulty == 'V' or subDifficulty == "V":
		return 'V'
	elif mainDifficulty == 'H' or subDifficulty == "H":
		return 'H'
	elif mainDifficulty == 'M' or subDifficulty == "M":
		return 'M'
	else:
		return 'L'	
def mergeLikelihood(mainLikelihood,subLikelihood):
    if mainLikelihood == 'L' or subLikelihood == "L":
        return 'L'
    elif mainLikelihood == 'M' or subLikelihood == "M":
        return 'M'
    elif mainLikelihood == 'H' or subLikelihood == "H":
        return 'H'
    else:
        return 'V'  
def mergeTime(mainTime,subTime):
    if mainTime == 'MN' or subTime == "MN":
        return 'MN'
    elif mainTime == 'DY' or subTime == "DY":
        return 'DY'
    elif mainTime == 'HR' or subTime == "HR":
        return 'HR'
    else:
        return 'MT'  
def mergeCost(mainCost,subCost):
    if subCost > mainCost:
        mainCost = subCost
    return mainCost

def isLeafNode(nodesMap,nodeIndex):
	if not nodesMap[nodeIndex]['childrenSet']:
		return True
	else:
		return False
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

finalPathList = {}
finalNodesPathList = {}
finalEdgesList = {}
finalPathCost = {}
