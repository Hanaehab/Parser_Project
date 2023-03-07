from globals import conventions, mapOfLayers, numberOfVias, metalNumbers
import re
from classes.spacing_test import SpacingTest

def preprocessSpacing():

    spacingFile = open("files/spacing_rules.txt", "w")
    with open('spacing_example.txt', 'r') as file:
        for line in file:
            if re.search(r'\.S\.',line):
                try:
                    ruleName = line.split()[0]
                except:
                    continue

                viaNumber = ruleName.split('.')[0]
                if viaNumber in numberOfVias.keys():
                    afterPreprocessing = ruleName.replace(
                        viaNumber, numberOfVias[viaNumber])
                    afterPreprocessing += line[line.find("@")+1:]
                elif viaNumber in metalNumbers:
                    afterPreprocessing = ruleName.replace(
                        viaNumber, metalNumbers[viaNumber])
                    afterPreprocessing += line[line.find("@")+1:]
                    
                else:
                    afterPreprocessing = ""

                spacingFile.write(afterPreprocessing)


def getLayerName(ruleName):
    layer = ruleName.split('.')[0]

    if layer.find("VIA") >= 0:
        # layer[layer.find("VIA")+3:] -> gives the part that follows "VIA", EX: "VIAxa" will give "xa"
        layerName = conventions["VIA" + layer[layer.find("VIA")+3:]]
    elif layer.find("M") >= 0:
        if layer.find("M1") >= 0:
            layerName= "VIA0i"
        else:
            layerName = conventions["VIA" + layer[layer.find("M")+1:]]
    
    # print(layerName)
    return layerName


def getTypeOfVia(viaDimensions, layerName):
    # Get the type of via from the vias list inside the via layer
    viaDimensions = set(viaDimensions)
    for via in mapOfLayers[layerName].vias:
        toCompare = set([via.width, via.length])
        if (viaDimensions == toCompare):
            return via.name # (Ex: VIA0i, VIA0iLRG, VIA0iLRG2)


def getViasDimensions(line):
    # Get 2 arrays of the dimensions of each via
    try:
        viaDimensions = re.findall(r'edge length = \d+\.*\d+\s*/\s*\d+\.*\d+', line)

        fisrtViaDimension = re.findall(r'(\d+(?:\.\d+)?)', viaDimensions[0])
        secondViaDimenion = re.findall(r'(\d+(?:\.\d+)?)', viaDimensions[1])

        fisrtViaDimension = [float(x) for x in fisrtViaDimension]
        secondViaDimenion = [float(x) for x in secondViaDimenion]

        return fisrtViaDimension, secondViaDimenion

    except:
        return "NOT FOUND", "NOT FOUND"
    
def getRelationDirection(line):
    
    try:
        direction = re.search(r'in (horizontal|vertical) direction', line)
        if direction.group().find("vertical") > 0:
            return "vertical"
        else:
            return "horizontal"

    except:
        # print(f"=====> {line}")
        return "NOT FOUND"

def getViaDirection(viaDimensions):
    
    if viaDimensions[0] > viaDimensions[1]:
        return "horizontal"

    elif viaDimensions[1] > viaDimensions[0]:
        return "vertical"
    else:
        return "square"

def getEdgeRelation(viaDirection, relationDirection):
    if relationDirection == "NOT FOUND":
        return "NO RELATION"

    else:
        if viaDirection == "vertical" and relationDirection == "vertical":
            return "short Side"
        elif viaDirection == "vertical" and relationDirection == "horizontal":
            return "long Side"
        elif viaDirection == "horizontal" and relationDirection == "vertical":
            return "long Side"
        elif viaDirection == "horizontal" and relationDirection == "horizontal":
            return "short Side"
        elif viaDirection == "square":
            return "square Side"
def getPRL(line):
    try:
        prlRegx = re.search(r'\[PRL.*\]', line)
        prlValue = re.search(r'-?\d+(?:\.\d+)?', prlRegx.group()) # PRL could be negative value
        return float(prlValue.group())

    except:
        # print(f"=====> {line}")
        return "NOT FOUND"

def checkDiffNet(line):
    isDiffNet = line.find("different net")
    if isDiffNet > 0:
        return True
    else:
        return False
    
def getSpacingValue(line):
    listOfNumbers = re.findall(r'-?\d+(?:\.\d+)?', line)
    # Return the last value in the line
    return float(listOfNumbers[-1])

def parseSpacing():
    with open('files/spacing_rules.txt', 'r') as file:
        for line in file:
            ruleName = line.split()[0]
            layerName = getLayerName(ruleName)

            # Get the relation between the two vias (horizontal or vertical) relation
            relationDirection = getRelationDirection(line)

            # Get the dimensions of each via and the type
            fisrtViaDimension, secondViaDimenion = getViasDimensions(line)
            firstViaType = getTypeOfVia(fisrtViaDimension, layerName)
            secondViaType = getTypeOfVia(secondViaDimenion, layerName)

            # Get the direction of the vias from the order of their dimensions
            firstViaDirection = getViaDirection(fisrtViaDimension)
            secondViaDirection = getViaDirection(secondViaDimenion)

            firstViaEdge =  getEdgeRelation(firstViaDirection, relationDirection)
            secondViaEdge = getEdgeRelation(secondViaDirection, relationDirection)
            spacingValue = getSpacingValue(line)
            prl = getPRL(line)
            isDiffNet = checkDiffNet(line)
            record = SpacingTest(ruleName=ruleName, firstViaType=firstViaType, secondViaType=secondViaType, firstViaEdge=firstViaEdge, secondViaEdge=secondViaEdge, relationDirection=relationDirection, PRL=prl, diffNet=isDiffNet, spacingValue=spacingValue, comment=line)
            print(record)
            # print(f"{firstViaDirection} =====> {secondViaDirection}")
            # print(direction)

            # print(f"between {firstViaType} and {secondViaType}")
            
            

