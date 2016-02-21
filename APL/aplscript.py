# This is the script that extends the WP1 attack tree with attack descriptions
# coming from the Attack Pattern Library

from __future__ import print_function
import sys
import datetime

from util import    log, closeLogging, getFirstChildElement, \
                    getNodeLabel, parseTreemakerOutput, \
                    fixTreemakerOutput, refineTreemakerOutput, \
                    annotateTreemakerOutput

def processTreemakerOutput (path):
    
    log('Processing scenario {0}'.format(path))
    
    xmlDocument = None
    xmlRoot = None
    
    #Step 1: Parsing Treemaker Output
    
    try:
        print('Parsing Treemaker output... ',end="",flush=True)
        log('Parsing Treemaker output')
        xmlDocument = parseTreemakerOutput(path)
        xmlRoot = getFirstChildElement(xmlDocument)
        log('Root element detected: {0}'.format(getNodeLabel(xmlRoot)))
        log()
        print('Done')
    except (TypeError, AttributeError) as e:
        print('Fail')
        log('Error parsing scenario: {0}'.format(e))
        print(e)
        sys.exit()
        
    #Step 2: Fixing Treemaker Output
        
    try:
        print('Fixing Treemaker output... ',end='',flush=True)
        fixTreemakerOutput(xmlRoot)    
        outputFile = '{0}_fixed{1}'.format(path[:path.rindex('.')],path[-4:])
        xmlDocument.writexml(open(outputFile, 'w'), indent="  ", newl="", addindent="  ")
        log()
        print('Done')
    except IOError:
        print('Fail')
        log('Error while writing output to {0}. {1}'.format(outputFile,e))
        print('Error while writing output to {0}. {1}'.format(outputFile,e))
        sys.exit()
    except Exception as e:
        print('Fail')
        log(e)
        print(e)
        sys.exit()
    
    #Step 3: Refining Treemaker Output (with patterns)
    
    try:
        print('Refining Treemaker output with patterns... ',end='',flush=True)
        refineTreemakerOutput(xmlRoot, 'patterns')
        outputFile = '{0}_refined{1}'.format(path[:path.rindex('.')],path[-4:])
        global scenario_refined
        scenario_refined = outputFile
        xmlDocument.writexml(open(outputFile, 'w'), indent="  ", newl="", addindent="  ")
        log()
        print('Done')
    except IOError:
        print('Fail')
        log('Error while writing output to {0}. {1}'.format(outputFile,e))
        print('Error while writing output to {0}. {1}'.format(outputFile,e))
        sys.exit()
    except Exception as e:
        print('Fail')
        log(e)
        print(e)
        sys.exit()
        
    xmlDocument.unlink()
    closeLogging()
    
def annotateRefinedTree (path):

    xmlDocument = None
    xmlRoot = None
    
    #Step 1: Parsing refined tree
    
    try:
        print('Parsing refined tree... ',end="",flush=True)
        xmlDocument = parseTreemakerOutput(path)
        xmlRoot = getFirstChildElement(xmlDocument)
        print('Done')
    except (TypeError, AttributeError) as e:
        print('Fail')
        print(e)
        sys.exit()
        
        #Step 2: Annotating the tree (with quantitative annotations)
    
    try:
        print('Annotating Treemaker output... ',end='',flush=True)
        xmlDocument.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        xmlDocument.setAttribute("xsi:noNamespaceSchemaLocation", "http://research.cyber.ee/~antonc/adtree.xsd")
        xmlDocument.setAttribute("profit", "1000000")
        annotateTreemakerOutput(xmlRoot)
        outputFile = '{0}_annotated_qa{1}'.format(path[:path.rindex('_')],path[-4:])
        xmlDocument.writexml(open(outputFile, 'w'), indent="  ", newl="", addindent="  ")
        print('Done')
    except IOError:
        print('Fail')
        print('Error while writing output to {0}. {1}'.format(outputFile,e))
        sys.exit()
    except Exception as e:
        print('Fail')
        print(e)
        sys.exit()
        
scenario = '/Users/gumin/Documents/thesis/IPTV/result/TREsPASS_IPTV_model_Fred.xml'
#scenario = 'Cloud/ANM-generated_TREsPASS_model_combined.xml'
scenario_refined = '/Users/gumin/Documents/thesis/APL/new.xml'
processTreemakerOutput(scenario)
annotateRefinedTree(scenario_refined)
