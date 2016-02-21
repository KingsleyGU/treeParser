# This is the script that extends the WP1 attack tree with attack descriptions
# coming from the Attack Pattern Library

from __future__ import print_function
import sys
import datetime

from util import    log, closeLogging, getFirstChildElement, \
                    getNodeLabel, parseTreemakerOutput, \
                    fixTreemakerOutput, refineTreemakerOutput

def processTreemakerOutput (path):
   
    log('Processing scenario {0}'.format(path))
    
    xmlDocument = None
    xmlRoot = None
    
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
        log('Error parsing scenario: {0}',format(e))
        print(e)
        sys.exit()

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
    
    try:
        print('Refining Treemaker output... ',end='',flush=True)
        refineTreemakerOutput(xmlRoot)
        outputFile = '{0}_refined{1}'.format(path[:path.rindex('.')],path[-4:])
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
        
    #refine(root)
    
        
    xmlDocument.unlink()
    closeLogging()
    
scenario = scenario = '../../ATA/Cloud Complex/ANM-generated_TREsPASS_model_combined.xml'
processTreemakerOutput(scenario)

