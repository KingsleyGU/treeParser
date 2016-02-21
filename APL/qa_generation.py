from xml.dom.minidom import parse

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
    nodeChildrenTotalCount = 0
    
    if len(children) == 0:
        leafCount += 1
        leafs.add(label)
        nodeChildrenTotalCount = currentId
    
    for c in children:
        (childId,childrenCount)=parseTree(c)
        nodeChildrenSet.add(childId-1)
        nodeChildrenTotalCount += childrenCount
    currentNodeProperty['childrenSet'] = nodeChildrenSet
    currentNodeProperty['childrenCount'] = nodeChildrenTotalCount
    currentNodeProperty['label'] = label
    occuranceCountMap[currentId] = currentNodeProperty
    currentId += 1
    return (currentId,nodeChildrenTotalCount)
  
def createQA(leafs, model):
    file = open("quantitative_annotations.py", "w")
    qa = "\t#################\n\t# Quantitative Annotations #\n\t#################\nqa = {\n"
    
    for c in leafs:
        label = c
        if c.startswith(' IN'):
            label = c[1:]
            c = '\s*' + label
        qa += "\tr'({0})':\n\t'<node refinement=\"disjunctive\">' +\n\t\t'<label>{1}</label>' +\n".format(c, label)
        
        if model == 'simple':
            qa += getQASimpleModel(c)
        elif model == 'complex':
            qa += getQAComplexModel(c)
            
        qa += "\t'</node>',\n\n"
        
    qa += "}"
    file.write(qa)	
    file.close()

def getQASimpleModel(s):
    difficulty = cost = likelihood = time = 'TODO'
    
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
    
def getQAComplexModel(s):
    difficulty = cost = likelihood = time = 'TODO'

    s = s.lower()

    if 'bypases authentication' in s and 'virtualmachine' in s:
        difficulty = 'H'
        likelihood = 'M'
        time = 'MT'
        cost = '500'
    elif 'network' in s and 'roomdatacenter' in s:
        difficulty = 'L'
        likelihood = 'H'
        time = 'MT'
        cost = 0
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
    elif ('sydney' in s or 'administrator' in s) and 'virtualmachine' in s and 'network' in s:
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




    return "\t\t'<parameter name=\"cost\" class=\"numeric\">{0}</parameter>' +\n\t\t'<parameter name=\"likelihood\" class=\"ordinal\">{1}</parameter>' +\n\t\t'<parameter name=\"difficulty\" class=\"ordinal\">{2}</parameter>' +\n\t\t'<parameter name=\"time\" class=\"ordinal\">{3}</parameter>' +\n".format(cost, likelihood, difficulty, time)


scenario = '/Users/gumin/Documents/thesis/IPTV/result/TREsPASS_IPTV_model_Fred.xml'
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
#print("Unique leafs: {0}".format(len(leafs)))
#for c in leafs:
#    print("{0},".format(c))

for node in occuranceCountMap:
    print("id:{0} count:{1} children:{2} label:{3}".format(node,occuranceCountMap[node]['childrenCount'],repr(occuranceCountMap[node]['childrenSet']),occuranceCountMap[node]['label']))
createQA(leafs, model)



