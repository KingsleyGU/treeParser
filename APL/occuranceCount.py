import csv
# from qa_generation import patternMap
#define a function to get the count for each label
# def getPatternMap():
#     return patternMap
def __init__(self):
    patternMap = {}
    patternMap['action'] = {}
    patternMap['assetKind'] = {}
    patternMap['targetKind'] = {}
def getPatternMap():
    return patternMap
def getLabelCount(label):
    countMap = {}
    global patternMap
    # Format: FULFILL is fulfill actor trusts actor
    labelArray = label.split()
    updateActionPatternMap(labelArray[0])
    if label.strip().upper().startswith('FULFILL'):       
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[3])
        return countMap
    # Format: force/move actor location locality
    elif label.strip().upper().startswith('FORCE') or label.strip().upper().startswith('MOVE'):
        # updateTargetPatternMap(labelArray[3])
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[2])
        return countMap     
    # Format: IN actor component Actor/Location some extra stuff also be added 
    elif label.strip().upper().startswith('IN'):
        # updateAssetPatternMap(labelArray[3])
        # updateTargetPatternMap(labelArray[6])
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[2])
        countMap = updateCountMap(countMap,labelArray[3])
        return countMap   
    # Format:  MAKE actor victim + previous cases
    elif label.strip().upper().startswith('MAKE'):
        countMap = updateCountMap(countMap,labelArray[1])
        # countMap = updateCountMap(countMap,labelArray[2])
        return addCountMap(countMap,getLabelCount(label[label.index(labelArray[3]):]))

# make the count add of two count map 
def updateActionPatternMap(actionName):
    updatePatternMap('action',actionName)
def updateAssetPatternMap(assetName):
    updatePatternMap('assetKind',assetName)
def updateTargetPatternMap(targetName):
    updatePatternMap('targetKind',targetName)
def updatePatternMap(patternType,patternName):
    global patternMap
    if patternName in patternMap[patternType]:
        patternMap[patternType][patternName] +=1
    else:
        patternMap[patternType][patternName] = 1


# This is the main function to get the elements count in a leaf label
def getLabelCount(label):
    countMap = {}
    global patternMap
    # Format: FULFILL is fulfill actor trusts actor
    labelArray = label.split()
    updateActionPatternMap(labelArray[0])
    if label.strip().upper().startswith('FULFILL'):       
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[3])
        return countMap
    # Format: force/move actor location locality
    elif label.strip().upper().startswith('FORCE') or label.strip().upper().startswith('MOVE'):
        # updateTargetPatternMap(labelArray[3])
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[2])
        return countMap     
    # Format: IN actor component Actor/Location some extra stuff also be added 
    elif label.strip().upper().startswith('IN'):
        # updateAssetPatternMap(labelArray[3])
        # updateTargetPatternMap(labelArray[6])
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[2])
        countMap = updateCountMap(countMap,labelArray[3])
        return countMap   
    # Format:  MAKE actor victim + previous cases
    elif label.strip().upper().startswith('MAKE'):
        countMap = updateCountMap(countMap,labelArray[1])
        # countMap = updateCountMap(countMap,labelArray[2])
        return addCountMap(countMap,getLabelCount(label[label.index(labelArray[3]):]))

# This function is to get the occurrence for non-leaf conjunctive nodes
def addCountMap(mainCountMap,subCountMap):    
    for key in subCountMap:
        if key in mainCountMap:
            mainCountMap[key]['min'] += subCountMap[key]['min']
            mainCountMap[key]['max'] += subCountMap[key]['max']
        else:
            mainCountMap[key] = {}
            mainCountMap[key]['min'] = subCountMap[key]['min']
            mainCountMap[key]['max'] = subCountMap[key]['max']
    return mainCountMap

# This function is to get the occurrence for non-leaf disjunctive nodes
def orCountMap(mainCountMap,subCountMap):
    if not mainCountMap:
       for key in subCountMap:
            mainCountMap[key] = {}
            mainCountMap[key]['min'] = subCountMap[key]['min']
            mainCountMap[key]['max'] = subCountMap[key]['max']
    else:
        for key in subCountMap:
            if key in mainCountMap:
                if(mainCountMap[key]['min'] > subCountMap[key]['min']):
                    mainCountMap[key]['min'] = subCountMap[key]['min']
                if(mainCountMap[key]['max'] < subCountMap[key]['max']):
                    mainCountMap[key]['max'] = subCountMap[key]['max']
            else:
                mainCountMap[key] = {}
                mainCountMap[key]['min'] = 0
                mainCountMap[key]['max'] = subCountMap[key]['max']
        for key in mainCountMap:
            if key not in subCountMap:
                mainCountMap[key]['min'] = 0
    return mainCountMap

# A function for updating the occurrence count map, this function would be called by getLabelCount
def updateCountMap(countMap,componentName):
    if componentName in countMap:
        countMap[componentName]['min'] += 1
        countMap[componentName]['max'] += 1
    else:
        countMap[componentName] = {}
        countMap[componentName]['min'] = 1
        countMap[componentName]['max'] = 1
    return countMap

# This function is for printing all the emlemt count occurrence to a csv file
def printOccurance(nodesMap):
    occuranceData = [['ID', 'Node_Occurrence_Count','Children','Node_Type','Label','Parent']]
    for nodeName in nodesMap:
        # print("id:{0} count:{1} children:{2} connection:{3} label:{4}".format(nodeName,repr(nodesMap[nodeName]['childrenCount']),repr(nodesMap[nodeName]['childrenSet']),nodesMap[nodeName]['connection'],nodesMap[nodeName]['label']))
        occuranceElement = []
        occuranceElement.append(nodeName)
        occuranceElement.append(repr(nodesMap[nodeName]['childrenCount']))
        occuranceElement.append(repr(nodesMap[nodeName]['childrenSet']))
        occuranceElement.append(nodesMap[nodeName]['connection'])
        occuranceElement.append(nodesMap[nodeName]['label'])
        occuranceElement.append(nodesMap[nodeName]['parent'])
        occuranceData.append(occuranceElement)
    with open('occurance.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(occuranceData)



patternMap = {}
patternMap['action'] = {}
patternMap['assetKind'] = {}
patternMap['targetKind'] = {}