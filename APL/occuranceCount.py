import csv
#define a function to get the count for each label
def getLabelCount(label):
    countMap = {}
    # format for FULFILL is fulfill actor trusts actor
    if label.strip().upper().startswith('FULFILL'):
        labelArray = label.split()
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[3])
        return countMap
    # format for FORCE or MOVE is force/move actor location locality
    elif label.strip().upper().startswith('FORCE') or label.strip().upper().startswith('MOVE'):
        labelArray = label.split()
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[4])
        return countMap     
    # format for IN or IN actor component Actor/Location some extra stuff also be added 
    elif label.strip().upper().startswith('IN'):
        labelArray = label.split()
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[4])
        countMap = updateCountMap(countMap,labelArray[7])
        return countMap   
    # the format of MAKE is MAKE actor victim + previous cases
    elif label.strip().upper().startswith('MAKE'):
        labelArray = label.split()
        countMap = updateCountMap(countMap,labelArray[1])
        countMap = updateCountMap(countMap,labelArray[2])
        return unionCountMap(countMap,getLabelCount(label[label.index(labelArray[3]):]))

# make the count union of two count map 
def unionCountMap(mainCountMap,subCountMap):
    for key in subCountMap:
        if key in mainCountMap:
            mainCountMap[key] += subCountMap[key]
        else:
            mainCountMap[key] = subCountMap[key]
    return mainCountMap

def intersectionCountMap(mainCountMap,subCountMap):
    for key in subCountMap:
        if key in mainCountMap:
            if(mainCountMap[key] < subCountMap[key]):
                mainCountMap[key] = subCountMap[key]
        else:
            mainCountMap[key] = subCountMap[key]
    return mainCountMap  


def updateCountMap(countMap,componentName):
    if componentName in countMap:
        countMap[componentName] += 1
    else:
        countMap[componentName] = 1
    return countMap


def printOccurance(occuranceCountMap):
    occuranceData = [['id', 'Count','children','connection','label']]
    for nodeName in occuranceCountMap:
        # print("id:{0} count:{1} children:{2} connection:{3} label:{4}".format(nodeName,repr(occuranceCountMap[nodeName]['childrenCount']),repr(occuranceCountMap[nodeName]['childrenSet']),occuranceCountMap[nodeName]['connection'],occuranceCountMap[nodeName]['label']))
        occuranceElement = []
        occuranceElement.append(nodeName)
        occuranceElement.append(repr(occuranceCountMap[nodeName]['childrenCount']))
        occuranceElement.append(repr(occuranceCountMap[nodeName]['childrenSet']))
        occuranceElement.append(occuranceCountMap[nodeName]['connection'])
        occuranceElement.append(occuranceCountMap[nodeName]['label'])
        occuranceData.append(occuranceElement)
    with open('occurance.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(occuranceData)