import re
from xml.dom.minidom import parse, parseString
from costCount import getQAComplexModel,getQASimpleModel,unionCostMap,intersectionCostMap,printCost
from occuranceCount import getLabelCount,unionCountMap,intersectionCountMap,printOccurance
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
    global leafCount
    global nodeCount
    global occuranceCountMap
    global currentId
    nodeCount += 1
    (label,children) = getChildElements(node)
    currentNodeProperty = {}
    nodeChildrenSet = set()
    nodeChildrenTotalCount = {}
    nodeCostCount = {}
    
    if len(children) == 0:
        leafCount += 1
        leafs.add(label)
        nodeChildrenTotalCount = getLabelCount(label)
        nodeCostCount = getQAComplexModel(label)
    
    for c in children:
        (childId,childrenCount,childCost)=parseTree(c)
        nodeChildrenSet.add(childId-1)
        if node.getAttribute("refinement") == "conjunctive":
            nodeChildrenTotalCount = unionCountMap(nodeChildrenTotalCount,childrenCount)
            nodeCostCount = unionCostMap(nodeCostCount,childCost)
        else:
            nodeChildrenTotalCount = intersectionCountMap(nodeChildrenTotalCount,childrenCount)
            nodeCostCount = intersectionCostMap(nodeCostCount,childCost)
    if node.getAttribute("refinement") == "conjunctive":
        currentNodeProperty['connection'] = "add"
    else:
        currentNodeProperty['connection'] = "or"
    currentNodeProperty['childrenSet'] = nodeChildrenSet
    currentNodeProperty['childrenCount'] = nodeChildrenTotalCount
    currentNodeProperty['label'] = label
    currentNodeProperty['cost'] = nodeCostCount
    occuranceCountMap[currentId] = currentNodeProperty
    currentId += 1
    return (currentId,nodeChildrenTotalCount,nodeCostCount)









scenario = '/Users/gumin/Documents/thesis/APL/sample.xml'
#model = 'simple'
#scenario = 'Cloud/ANM-generated_TREsPASS_model_combined_refined.xml'
model = 'complex'

tree = parse(scenario)
xmlDocument = tree.documentElement
xmlRoot = getFirstChildElement(xmlDocument)

leafCount = 0
nodeCount = 0
currentId = 0
leafs = set()
occuranceCountMap = {}

parseTree(xmlRoot)

print("Node count: {0}".format(nodeCount))
print("Leaf count: {0}".format(leafCount))
print("occuranceCountMap  length: {0}".format(len(occuranceCountMap)))
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
#    print("{0},".format(c))

for node in occuranceCountMap:
    print("id:{0} count:{1} children:{2} connection:{3} label:{4} cost:{5}".format(node,repr(occuranceCountMap[node]['childrenCount']),repr(occuranceCountMap[node]['childrenSet']),occuranceCountMap[node]['connection'],occuranceCountMap[node]['label'],repr(occuranceCountMap[node]['cost'])))

printOccurance(occuranceCountMap)
printCost(occuranceCountMap)

# print("costs: {0}".format(repr(getQAComplexModel("MAKE Fred Margrethe IN Margrethe ITEM card x004 ACTOR Margrethe Margrethe"))))

# tempMap = parseqa("FORCE Fred LOCATION door door")
# for k in tempMap:
#      print("key:{0}, value:{1}".format(k,tempMap[k]))

# print("result: {0}".format(parseqa("FORCE Fred LOCATION door door")))


