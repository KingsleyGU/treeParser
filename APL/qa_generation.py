import re
from xml.dom.minidom import parse, parseString
from costCount import getQAComplexModel,getQASimpleModel,addCostMap,orCostMap,printCost
from occuranceCount import getPatternMap,getLabelCount,addCountMap,orCountMap,printOccurance
# from visualization import createGraph
# from occuranceCount import *
from pathCount import processPathCount
# from quantitative_annotations   import qa

def getFirstChildElement (node):
	for child in node.childNodes:
		if child.nodeType == child.ELEMENT_NODE:
			return child

def getNodeLabel (node):
	""" The TREsPASS xml format XSD does not specify if the <label> node must be the first child.
		Therefore in order to find the label we need to look through all the children
		and check for the nodeName to match <label>"""
		
	for child in node.childNodes:
		if child.nodeName.lower() == "label":
			return child.firstChild.data
	return ''
	
def getChildElements (node):
	""" Returns the label node and all the other child elements """
	label = None
	elements = []
	for child in node.childNodes:
		if child.nodeType == child.ELEMENT_NODE:
			if child.nodeName.lower() == "label":
				label = child.firstChild.data
			elif child.nodeName.lower() == "node":
				elements.append(child)
	return (label,elements)
			
def parseTree(node):
	global leafs
	global leafCount
	global nodeCount
	global nodesMap
	global currentId
	nodeCount += 1
	(label,children) = getChildElements(node)
	currentNodeProperty = {}
	nodeChildrenSet = set()
	nodeChildrenTotalCount = {}
	nodeCostCount = {}
	
	if len(children) == 0:
		leafCount += 1
		# leafs.add(label)
		nodeChildrenTotalCount = getLabelCount(label)
		nodeCostCount = getQAComplexModel(label)
		leafs.add(currentId)
	elif len(children) == 1:
		(childId,childrenCount,childCost)=parseTree(children[0])
		nodeChildrenSet.add(childId-1)
		nodeChildrenTotalCount = childrenCount
		nodeCostCount = childCost
	else:
		for c in children:
			(childId,childrenCount,childCost)=parseTree(c)
			nodeChildrenSet.add(childId-1)
			if node.getAttribute("refinement") == "conjunctive":
				nodeChildrenTotalCount = addCountMap(nodeChildrenTotalCount,childrenCount)
				nodeCostCount = addCostMap(nodeCostCount,childCost)
			else:
				nodeChildrenTotalCount = orCountMap(nodeChildrenTotalCount,childrenCount)
				nodeCostCount = orCostMap(nodeCostCount,childCost)
	if node.getAttribute("refinement") == "conjunctive":
		currentNodeProperty['connection'] = "add"
	else:
		currentNodeProperty['connection'] = "or"
	currentNodeProperty['childrenSet'] = nodeChildrenSet
	for childNode in nodeChildrenSet:
		nodesMap[childNode]['parent'] = currentId
	currentNodeProperty['childrenCount'] = nodeChildrenTotalCount
	currentNodeProperty['label'] = label
	currentNodeProperty['cost'] = nodeCostCount
	nodesMap[currentId] = currentNodeProperty
	nodesMap[currentId ]['parent'] = -1
	currentId += 1
	return (currentId,nodeChildrenTotalCount,nodeCostCount)









scenario = '/Users/gumin/Documents/thesis/APL/sample.xml'
#model = 'simple'
#scenario = 'Cloud/ANM-generated_TREsPASS_model_combined_refined.xml'
model = 'complex'

tree = parse(scenario)
xmlDocument = tree.documentElement
xmlRoot = getFirstChildElement(xmlDocument)
profit = xmlDocument.getAttribute("profit")
print("profit: {0}".format(profit))
leafCount = 0
nodeCount = 0
currentId = 0
leafs = set()
pathLeafs = set()
nodesMap = {}
# patternMap = {}
# patternMap['action'] = {}
# patternMap['assetKind'] = {}
# patternMap['targetKind'] = {}

parseTree(xmlRoot)

print("Node count: {0}".format(nodeCount))
print("Leaf count: {0}".format(leafCount))
print("nodesMap  length: {0}".format(len(nodesMap)))
# labelArray = getLabelCount(" FULFILL Fred trusts Margrethe ")
# print("{0}".format(labelArray))
# print(', '.join(labelArray.reverse()))
# print("1: {0} 2:{1} 3:{2} 4:{3}".format(labelArray[0],labelArray[1],labelArray[2],labelArray[3]))

# countMap = {}
# countMap = getLabelCount("MAKE Fred Margrethe IN Margrethe ITEM card x004 ACTOR Margrethe Margrethe")
# for k in countMap:
#     print("key:{0}, value:{1}".format(k,countMap[k]))


#print("Unique leafs: {0}".format(len(leafs)))
#for c in leafs:
# print("{0},".format(repr(nodesMap)))

# for node in nodesMap:
#     print("id:{0} count:{1} children:{2} connection:{3} label:{4} cost:{5}".format(node,repr(nodesMap[node]['childrenCount']),repr(nodesMap[node]['childrenSet']),nodesMap[node]['connection'],nodesMap[node]['label'],repr(nodesMap[node]['cost'])))

printOccurance(nodesMap)
printCost(nodesMap)
processPathCount(nodesMap,profit)
# createGraph(nodesMap)
print("{0}".format(repr(getPatternMap())))


# for leaf in leafs:
#     print("Unique leafs: {0}".format(leaf))

# print("costs: {0}".format(repr(getQAComplexModel("MAKE Fred Margrethe IN Margrethe ITEM card x004 ACTOR Margrethe Margrethe"))))

# tempMap = parseqa("FORCE Fred LOCATION door door")
# for k in tempMap:
#      print("key:{0}, value:{1}".format(k,tempMap[k]))

# print("result: {0}".format(parseqa("FORCE Fred LOCATION door door")))


