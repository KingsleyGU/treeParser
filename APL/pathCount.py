import csv
from visualization import createGraph
from collections import OrderedDict
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
	createGraph(nodesMap,finalPathList,finalNodesPathList,finalEdgesList,finalPathCost,profit)
	# print("Final node paths: {0}".format(repr(finalNodesPathList)))
def printPath(nodesMap):
	pathData = [['id', 'Path Leaves','Path Nodes','path edges','cost']]
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

def calculatePathCost(nodesMap,pathIndex,profit):
	global finalPathList
	cost = 0
	difficulty = "L"
	likelihood = "H"
	time = "MT"
	parameterMap = {}
	for nodeIndex in finalPathList[pathIndex]:
		cost = cost + nodesMap[nodeIndex]['cost']['cost']
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
