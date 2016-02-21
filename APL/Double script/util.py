# This is the utility script 
# facilitating Attack Pattern Library operations

import datetime
import re
from xml.dom.minidom import parse, parseString
from patterns import patterns
        
logHandle = None

def ts ():
    return datetime.datetime.now().strftime('[%H:%M:%S.%f]:')

def log (message=''):
    global logHandle
    if logHandle == None:
        try:
            logHandle = open('aplscript.log','w') 
        except IOError as e:
            print('Failed to initialize logging. ', e)
            sys.exit()
    print('{0} {1}'.format(ts(),message), file=logHandle)

def closeLogging ():
    global logHandle
    if logHandle != None:
        logHandle.close()
    
def parseTreemakerOutput (file):
    tree = parse(file)
    return tree.documentElement

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

def fixTreemakerOutput (node): 
    """ The function processess all the leaves of the subtree
        and eliminates intermediate nodes which do not 
        correspond to the propositional Boolean semantics 
        e.g.: unary AND and unary OR operators """
    
    # Obtain the children of the current node
    (label,childNodes) = getChildElements(node)
    
    # 0 child nodes - leaf -- Stop (in this case the only child will be a label node)
    # 1 child node -- bug -- fix and stop
    # 2 or more child nodes -- proceed recursively deeper
    if len(childNodes) == 0:  # we are reising in a leaf
        return
    if len(childNodes) == 1: # we are residing in a node with a single child
        # Descend down to the leaf until we reach a normal node or a leaf
        cur = node
        log('Found element containing 1 child: {0}'.format(label))
        print(label)
        while True:
            (l,n) = getChildElements(cur)
            log('Descending into element {0}'.format(l))
            if len(n) != 1:
                log('Leaf detected: {0}'.format(l))
                break
            cur = n[0]
        # at this point cur contains the new child
        # node.parent contains the new parent
        # we need to link them together by calling 
        # node.parentNode.replaceChild(newChild, oldChild)
        log('Replacing {0} with {1}'.format(label,getNodeLabel(cur)))
        node.parentNode.replaceChild(cur,node)
    for child in childNodes:
        fixTreemakerOutput(child)
        
def refineTreemakerOutput (node):
    ''' The function replaces all the leaves 
    of the tree with the subtrees 
    it finds among the patterns '''
    
    (label,childNodes) = getChildElements(node)
    if len(childNodes) == 0: # we have found a leaf
        label = getNodeLabel(node).strip(' \t\n\r')
        log('Refining leaf {0}'.format(label))
        #print(label)
        for key, replacement in patterns.items():
            matchObj = re.match(key,label, re.M | re.I)
            if matchObj:
                log('Matched to {0}'.format(key))
                for i in range(len(matchObj.groups())+1):
                    replacement = re.sub('\['+str(i)+'\]', 
                    matchObj.group(i), replacement)
                log('Replacing {0} with {1}'.format(label,replacement))
                xml = parseString(replacement)
                node.parentNode.replaceChild(getFirstChildElement(xml),node)    
                xml.unlink()
                break
        return
    for child in childNodes:
        refineTreemakerOutput(child)
