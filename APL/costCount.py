import csv
from pathCount import mergeDifficulties,mergeLikelihood,mergeTime

def getQASimpleModel(s):
    # time: HR means hour, MT means minute, DY means day, MN means month, 
    # difficulty & likelihood: V means very high, H means high, M means medium, L means Low
    difficulty = likelihood = time = 'TODO'
    cost = 0

    if not s.lstrip().startswith('MAKE'):
        if s.lstrip().startswith('FULFILL'):
            if 'trusts' in s:
                cost = 500
                difficulty = 'H'
                likelihood = 'H'
                time = 'DY'
            elif 'role' in s:
                cost = 1000
                difficulty = 'H'
                likelihood = "L"
                time = 'MN'
        elif s.lstrip().startswith('FORCE') or s.lstrip().startswith('MOVE'):
            if 'LOCATION door' in s:
                cost = 100
                difficulty = "L"
                likelihood = "H"
                time = "MT"
            else:
                cost = 300
                difficulty = "M"
                likelihood = "L"
                time = "HR"
        elif s.lstrip().startswith('IN'):
            if 'ACTOR' in s:
                cost = 100
                difficulty = "L"
                likelihood = "V"
                time = "MT"
            elif 'LOCATION' in s:
                cost = 500
                difficulty = "L"
                likelihood = "V"
                time = "MT"                
            else:
                cost = 700
                difficulty = "L"
                likelihood = "V"
                time = "MT"                
        parameterMap = {}
        parameterMap['cost'] = cost
        parameterMap['likelihood'] = likelihood
        parameterMap['difficulty'] =  difficulty
        parameterMap['time'] = time

        return parameterMap
    else:
        parameterMap = {}
        parameterMap['cost'] = 200
        parameterMap['likelihood'] = "L"
        parameterMap['difficulty'] =  "H"
        parameterMap['time'] = "HR"
        labelArray = s.split()
        tempParameterMap = getQASimpleModel(s[s.index(labelArray[3]):])
        parameterMap['cost'] = parameterMap['cost']  +  tempParameterMap['cost']
        parameterMap['difficulty'] = mergeDifficulties(parameterMap['difficulty'],tempParameterMap['difficulty'])
        parameterMap['likelihood'] = mergeLikelihood(parameterMap['likelihood'],tempParameterMap['likelihood'])
        parameterMap['time'] = mergeTime(parameterMap['time'],tempParameterMap['time'])
        return parameterMap
    # print("cost: {0}".format(cost))
def getQAComplexModel(s):
    parameterMap = {}
    parameterMap['cost'] = getLabelCost(s)
    parameterMap['likelihood'] = getLabelLikelihood(s)
    parameterMap['difficulty'] =  getLabelDifficulty(s)
    parameterMap['time'] = getLabelTime(s)
    return parameterMap
def getOldQASimpleModel(s):
    difficulty = likelihood = time = 'TODO'
    cost = '0'
    
    if 'bypases authentication in' in s:
        difficulty = likelihood = 'M'
        time = 'HR'
        if 'Laptop' in s: cost = '150'
        elif 'VM1' in s: cost = '200'
        elif 'VM2' in s: cost = '300'
        
    elif 'becomes friends with' in s:
        time = 'D'
        if s.endswith('Sydney'):
            difficulty = 'V'
            likelihood = 'L'
            cost = '1000'
        elif s.endswith('Ethan') or s.endswith('Finn'):
            difficulty = 'H'
            likelihood = 'M'
            cost = '600'
        elif s.endswith('Terry'):
            difficulty = 'M'
            likelihood = 'H'
            cost = '300'
            
    elif 'escalates privileges in' in s:
        difficulty = likelihood = 'M'
        time = 'HR'
        if 'Laptop' in s: cost = '800'
        elif 'VM1' in s: cost = '900'
        elif 'VM2' in s: cost = '1000'
        
    elif s.startswith('\s*IN'):
        if 'ITEM Server' in s and 'LOCATION RoomDatacenter' in s:
            difficulty = 'M' 
            likelihood = 'L'
            time = 'HR'
            cost = '50'
        if ('ITEM Switch' in s or 'ITEM Laptop' in s) and 'LOCATION Room' in s:
            difficulty = 'L' 
            likelihood = 'H'
            time = 'MT'
            cost = '0'
        if 'ITEM VM' in s and 'ITEM Server' in s:
            difficulty = 'L' 
            likelihood = 'V'
            time = 'MT'
            cost = '0'
        if 'DATA fileX' in s and 'ITEM Switch' in s:
            difficulty = 'H' 
            likelihood = 'L'
            time = 'D'
            cost = '500'
        if 'ITEM idcard' in s and 'ACTOR' in s:
            difficulty = 'L' 
            likelihood = 'M'
            time = 'MT'
            cost = '0'
        if 'DATA pin' in s and 'ITEM idcard' in s:
            difficulty = 'V' 
            likelihood = 'L'
            time = 'D'
            cost = '2000'
        if 'DATA pin' in s and 'ACTOR' in s:
            difficulty = 'M' 
            likelihood = 'H'
            time = 'HR'
            cost = '50'
        
    elif s.endswith('impersonates technician'):
        difficulty = 'L' 
        likelihood = 'M'
        time = 'HR'
        cost = '0'
    elif s.endswith('impersonates administrator'):
        difficulty = 'H' 
        likelihood = 'L'
        time = 'D'
        cost = '0'	
    elif s.endswith('impersonates authority'):
        difficulty = 'V' 
        likelihood = 'L'
        time = 'D'
        cost = '0'
        
    elif s.endswith('equips with required items to impersonate technician'):
        difficulty = 'L' 
        likelihood = 'M'
        time = 'HR'
        cost = '500'
    elif s.endswith('equips with required items to impersonate administrator'):
        difficulty = 'L' 
        likelihood = 'L'
        time = 'D'
        cost = '5000'	
    elif s.endswith('equips with required items to impersonate authority'):
        difficulty = 'L' 
        likelihood = 'L'
        time = 'D'
        cost = '7000'
        
    elif 'launches a phishing attack targeted at' in s:
        time = 'D'
        if 'targeted at Sydney' in s or 'targeted at Ethan' in s:
            difficulty = 'M' 
            likelihood = 'L'
            cost = '300'
        if 'targeted at Terry' in s or 'targeted at Finn' in s:
            difficulty = 'L' 
            likelihood = 'M'
            cost = '200'
            
    elif 'finds fileX in the file system of' in s or 'mounts the hd of' in s:
        difficulty = 'L' 
        likelihood = 'V'
        time = 'MT'
        cost = '0'
        
    elif 'Sydney orders' in s:
        difficulty = 'H' 
        likelihood = 'L'
        time = 'MT'
        cost = '0'	
    elif 'Ethan orders' in s or 'Finn orders' in s:
        difficulty = 'V' 
        likelihood = 'L'
        time = 'MT'
        cost = '0'
        
    elif 'tricks' in s:
        cost = '0'
        time = 'HR'
        if s.startswith('Sydney'):
            difficulty = 'M' 
            likelihood = 'H'
        if s.startswith('Ethan') or s.startswith('Finn'):
            difficulty = 'H' 
            likelihood = 'M'
        if s.startswith('Terry'):
            difficulty = 'V' 
            likelihood = 'L'
        
    elif 'bribes Sydney' in s:
        difficulty = 'V' 
        likelihood = 'L'
        time = 'D'
        cost = '50000'
    elif 'bribes Ethan' in s:
        difficulty = 'H' 
        likelihood = 'L'
        time = 'D'
        cost = '20000'
    elif 'bribes Finn' in s:
        difficulty = 'H' 
        likelihood = 'M'
        time = 'D'
        cost = '10000'
    elif 'bribes Terry' in s:
        difficulty = 'M' 
        likelihood = 'M'
        time = 'HR'
        cost = '2000'
        
    elif ' threatens ' in s:
        difficulty = 'M' 
        likelihood = 'H'
        time = 'HR'
        cost = '50'
        
    elif ' blackmails ' in s:
        difficulty = 'H' 
        likelihood = 'L'
        time = 'D'
        cost = '10000'
        
    elif 'collects some intel about' in s or 'collects information about' in s:
        difficulty = 'M' 
        likelihood = 'H'
        time = 'D'
        cost = '1000'
        
    return "\t\t'<parameter name=\"cost\" class=\"numeric\">{0}</parameter>' +\n\t\t'<parameter name=\"likelihood\" class=\"ordinal\">{1}</parameter>' +\n\t\t'<parameter name=\"difficulty\" class=\"ordinal\">{2}</parameter>' +\n\t\t'<parameter name=\"time\" class=\"ordinal\">{3}</parameter>' +\n".format(cost, likelihood, difficulty, time)
    
def getOldQAComplexModel(s):
    difficulty = likelihood = time = 'TODO'
    cost = '0';

    s = s.lower()

    if 'bypases authentication' in s and 'virtualmachine' in s:
        difficulty = 'H'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif 'Fred' in s and 'door' in s:
        difficulty = 'L'
        likelihood = 'H'
        time = 'MT'
        cost = 0
    elif 'fred' in s and 'location door' in s:
        difficulty = 'H'
        likelihood = 'L'
        time = 'MT'
        cost = '200'
    elif ('sydney' in s or 'administrator' in s) and 'mounts the hd' in s and 'virtualmachine' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif 'sydney' not in s or 'administrator' not in s and 'mounts the hd' in s and 'virtualmachine' in s:
        difficulty = 'H'
        likelihood = 'L'
        time = 'MT'
        cost = '500'
    elif 'hostsystem' in s and 'network' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif ('sydney' in s or 'administrator' in s) and 'virtualmachine' in s and 'datastore' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif ('sydney' in s or 'administrator' in s ) and 'virtualmachine' in s and 'network' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif 'sydney' not in s and 'administrator' not in s and 'virtualmachine' in s and 'network' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '200'
    elif ('sydney' not in s or 'administrator' not in s) and 'hostsystem' in s and 'network' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '200'
    elif 'sydney' not in s and 'administrator' not in s and 'hostsystem' in s and 'roomdatacenter' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif 'sydney' not in s and 'administrator' not in s and 'datastore' in s and 'roomdatacenter' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '300'
    elif ('sydney' in s or 'administrator' not in s) and 'datastore' in s and 'roomdatacenter' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif ('sydney' in s or 'administrator' in s) and 'escalates privileges in' in s and 'virtualmachine' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif ('sydney' not in s and 'administrator' not in s) and 'escalates privileges in virtualmachine' in s:
        difficulty = 'H'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif 'sydney' not in s and 'administrator' not in s and 'hostsystem' in s and 'datastore' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif 'sydney' not in s and 'administrator' not in s and 'virtualmachine' in s and 'datastore' in s:
        difficulty = 'M'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif 'finds filex' in s and 'virtualmachine' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif ('sydney' in s or 'administrator' in s) and 'virtualmachine' in s and 'hostsystem' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'
    elif 'sydney' not in s and 'administrator' not in s and 'virtualmachine' in s and 'hostsystem' in s:
        difficulty = 'H'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif ('sydney' in s or 'administrators' in s) and 'hostsystem' in s:
        difficulty = 'L'
        likelihood = 'V'
        time = 'MT'
        cost = '0'


    parameterMap = {}
    parameterMap['cost'] = cost
    parameterMap['likelihood'] = likelihood
    parameterMap['difficulty'] =  difficulty
    parameterMap['time'] = time

    return parameterMap
    # return "\t\t'<parameter name=\"cost\" class=\"numeric\">{0}</parameter>' +\n\t\t'<parameter name=\"likelihood\" class=\"ordinal\">{1}</parameter>' +\n\t\t'<parameter name=\"difficulty\" class=\"ordinal\">{2}</parameter>' +\n\t\t'<parameter name=\"time\" class=\"ordinal\">{3}</parameter>' +\n".format(cost, likelihood, difficulty, time)
def addCostMap(mainCostMap,subCostMap):
    if not mainCostMap:
        mainCostMap['cost'] = subCostMap['cost']
    else:
        mainCostMap['cost'] = int(mainCostMap['cost']) + int(subCostMap['cost'])
    return mainCostMap

def orCostMap(mainCostMap,subCostMap):
    if not mainCostMap:
        mainCostMap['cost'] = subCostMap['cost']
    elif int(mainCostMap['cost']) > int(subCostMap['cost']):
        mainCostMap['cost'] = int(subCostMap['cost'] ) 
    return mainCostMap  
def printCost(nodesMap):
    occuranceData = [['id', 'Cost','children','connection','label']]
    for nodeName in nodesMap:
        # print("id:{0} count:{1} children:{2} connection:{3} label:{4}".format(nodeName,repr(nodesMap[nodeName]['childrenCount']),repr(nodesMap[nodeName]['childrenSet']),nodesMap[nodeName]['connection'],nodesMap[nodeName]['label']))
        occuranceElement = []
        occuranceElement.append(nodeName)
        occuranceElement.append(repr(nodesMap[nodeName]['cost']))
        occuranceElement.append(repr(nodesMap[nodeName]['childrenSet']))
        occuranceElement.append(nodesMap[nodeName]['connection'])
        occuranceElement.append(nodesMap[nodeName]['label'])
        occuranceData.append(occuranceElement)
    with open('cost.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(occuranceData)

def getLabelTime(label):
    global TimeMap
    time = 'MT'
    labelArray = label.split()
    for keyword in labelArray:
        if keyword in TimeMap['MN']:
            time = mergeTime(time,'MN')
        elif keyword in TimeMap['DY']:
            time = mergeTime(time,'DY')
        elif keyword in TimeMap['HR']:
            time = mergeTime(time,'HR')
    return time
def getLabelLikelihood(label):
    global LikelihoodMap
    likelihood = 'V'
    labelArray = label.split()
    for keyword in labelArray:
        if keyword in LikelihoodMap['L']:
            likelihood = mergeLikelihood(likelihood,'L')
        elif keyword in LikelihoodMap['M']:
            likelihood = mergeLikelihood(likelihood,'M')
        elif keyword in LikelihoodMap['H']:
            likelihood = mergeLikelihood(likelihood,'H')
    return likelihood
def getLabelDifficulty(label):
    global DifficultyMap
    difficulty = 'L'
    labelArray = label.split()
    for keyword in labelArray:
        if keyword in DifficultyMap['V']:
            difficulty = mergeDifficulties(difficulty,'V')
        elif keyword in DifficultyMap['H']:
            difficulty = mergeDifficulties(difficulty,'H')
        elif keyword in DifficultyMap['M']:
            difficulty = mergeDifficulties(difficulty,'M')
    return difficulty
def getLabelCost(label):
    global CostMap
    cost = 100
    labelArray = label.split()
    for keyword in labelArray:
        if keyword in CostMap['1000']:
            cost = mergeCost(cost,1000)
        elif keyword in CostMap['500']:
            cost = mergeCost(cost,500)
        elif keyword in CostMap['300']:
            cost = mergeCost(cost,300)
    return cost
def mergeCost(mainCost,subCost):
    if subCost > mainCost:
        mainCost = subCost
    return mainCost








def createQA(leafs, model):
    file = open("quantitative_annotations.py", "w")
    qa = "\t#################\n\t# Quantitative Annotations #\n\t#################\nqa = {\n"
    
    for c in leafs:
        label = c
        if c.startswith(' IN'):
            label = c[1:]
            c = label
        qa += "\tr'{0}':\n\t'<node refinement=\"disjunctive\">' +\n\t\t'<label>{1}</label>' +\n".format(c, label)
        
        if model == 'simple':
            qa += getQASimpleModel(c)
        elif model == 'complex':
            qa += getQAComplexModel(c)
            
        qa += "\t'</node>',\n\n"
        
    qa += "}"
    file.write(qa)  
    file.close()

def parseParameter(node):
    parameterMap = {}
    for child in node.childNodes:
        if child.nodeName.lower() == "label":
            parameterMap['label'] = child.firstChild.data
        elif child.nodeName.lower() == "parameter":
            if child.getAttribute("name") == "cost":
                parameterMap['cost'] = child.firstChild.data
            elif child.getAttribute("name") == "likelihood":
                parameterMap['likelihood'] = child.firstChild.data
            elif child.getAttribute("name") == "difficulty":
                parameterMap['difficulty'] = child.firstChild.data
            elif child.getAttribute("name") == "time":
                parameterMap['time'] = child.firstChild.data                
    return parameterMap

def parseqa(label):
    label = label.strip()
    for key, replacement in qa.items():
        # matchObj = re.match(key.strip(),label, re.M | re.I)
        if key.strip() == label:
            # for i in range(len(matchObj.groups())+1):
            #     replacement = re.sub('\['+str(i)+'\]', 
            #     matchObj.group(i), replacement)
                # print("qa replacement: {0}".format(replacement))
            # return replacement
            xml = parseString(replacement)
            return parseParameter(getFirstChildElement(xml))
TimeMap = {}
TimeMap['MT'] = ['move','door','card','in','fred','item','pin']
TimeMap['HR'] = ['fulfill','force','charlie','margrethe']
TimeMap['DY'] = ['trust','x004']
TimeMap['MN'] = ['role']
DifficultyMap = {}
DifficultyMap['V'] = ['pin','margrethe','x004']
DifficultyMap['H'] = ['card','force','role']
DifficultyMap['M'] = ['trust','item','fred','fulfill']
DifficultyMap['L'] = ['charlie','in','move','door']
LikelihoodMap = {}
LikelihoodMap['V'] = ['charlie','in','move','door']
LikelihoodMap['H'] = ['trust','item','fred','fulfill']
LikelihoodMap['M'] = ['card','force','role']
LikelihoodMap['L'] = ['pin','margrethe','x004']
CostMap = {}
CostMap['100'] = ['door','move','in','pin','x004']
CostMap['300'] = ['fred','trust','fulfill','force','item','card']
CostMap['500'] = ['charlie','role']
CostMap['1000'] = ['margrethe']

