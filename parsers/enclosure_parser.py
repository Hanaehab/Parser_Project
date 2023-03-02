from globals import *
from classes import enclosure
import re


def getLayerName(ruleName):
    layer = ruleName.split('.')[0]
    if layer.find("VIA") >= 0:
        layerName = conventions["VIA" + layer[layer.find("VIA")+3:]]
    elif layer.find("M") >= 0:
        if layer.find("M1") >= 0:
            layerName= "VIA0i"
        else:
            layerName = conventions["VIA" + layer[layer.find("M")+1:]]
    
    # print(layerName)
    return layerName


def getTypeOfVia(line, layerName):
    # If we found "square" in the line
    if (line.find("square") > 0):

        # Regex to get the length of the side of the square via
        viaDimensions = re.search(r'width\s*=\s*\d+\.*\d+', line)
        try:
            width = float(viaDimensions.group().split('=')[1])
        except:
            print(f"the line is ---> {line}")
            return "NOT FOUND"

        for via in mapOfLayers[layerName].vias:
            if (via.width == width and via.length == width):
                return via.name  # Type of via (Ex: VIA0i, VIA0iLRG, VIA0iLRG2)

        return "NOT FOUND"

    # If we found "rectangualr" in the line
    elif (line.find("rectangular") > 0):

        # Regex to get the length of the sides of the rectangular via
        viaDimensions = re.search(
            r'width/length = (\d+(\.\d+)*)/(\d+(\.\d+)*)', line)
        try:
            viaDimensions = viaDimensions.group().split()[2].split('/')
        except:
            print(f"the line is ---> {line}")
            return "NOT FOUND"
        width = float(viaDimensions[0])
        length = float(viaDimensions[1])

        for via in mapOfLayers[layerName].vias:
            if (via.width == width and via.length == length):
                # Type of via (Ex: VIA0iBAR, VIA0iBAR2, VIA0iBAR3)
                return via.name

        return "NOT FOUND"
    else:
        return "NOT FOUND"


def getMetalPosistion(line):
    if (line.find("Lower_Metal") > 0):
        return "M_LOWER"
    else:
        return "M_UPPER"


def getLayerDimension(line, metalPosition):

    if metalPosition == "M_LOWER":
        regexOfDimensions = re.search(r'by Lower_Metal\s*\[.*\]', line)
    else:
        regexOfDimensions = re.search(r'by M(\d+|.*)\s*\[.*\]', line)

    # If we want to save the string of the dimensions
    # x = layerDimensions.group()[layerDimensions.group().find("[") + 1 :-1]
    # print(x)

    metalDimensions = re.findall(r'(\d+(?:\.\d+)?)', regexOfDimensions.group()[5:])
    # print(metalDimensions)

    # layerDimension = [float(number) for number in layerDimension]

    operatorName = ""
    if len(metalDimensions) < 2:
        if regexOfDimensions.group().find("<=") > 0:
            operatorName = "lessOrequal "
        elif regexOfDimensions.group().find(">=") > 0:
            operatorName = "moreOrequal "
        elif regexOfDimensions.group().find("<") > 0:
            operatorName = "less "
        elif regexOfDimensions.group().find(">") > 0:
            operatorName = "more "

        return operatorName + metalDimensions[0]

    else:
        return metalDimensions[0] + " " + metalDimensions[1]

def getEnclosureDimensions(line):
    if (line.find("square") > 0):
        regexOfEnclosures = re.search(r'with the other 2\s*(opposite)?\s*sides(.*)', line)
        
        # Regex to get the part that have the dimensions only (to ignore the '2' in the "2 sides")
        regexOfEnclosures = regexOfEnclosures.group()[regexOfEnclosures.group().find("sides"):]
        shortAndLongSides = re.findall(r'(\d+(?:\.\d+)?)', regexOfEnclosures)

    elif (line.find("rectangular") > 0):
        regexOfEnclosures = re.search(r'with the other 2 long sides(.*)', line)
        
        # Regex to get the part that have the dimensions only (to ignore the '2' in the "2 sides")
        regexOfEnclosures = regexOfEnclosures.group()[regexOfEnclosures.group().find("sides"):]
        shortAndLongSides = re.findall(r'(\d+(?:\.\d+)?)', regexOfEnclosures)
    
    shortAndLongSides = [float(i) for i in shortAndLongSides]
    return shortAndLongSides

def addEnclosure():

    with open('files/enclosure_rules.txt', 'r') as file:
        for line in file:

            ruleName = line.split()[0]
            layerName = getLayerName(ruleName=ruleName)

            typeOfVia = getTypeOfVia(line=line, layerName=layerName)
            # print(f"type of via is {typeOfVia}")

            metalPosition = getMetalPosistion(line=line)
            try:
                metalDimensions = getLayerDimension(line=line, metalPosition=metalPosition)
            except:
                print(line)
                print("Metal dimension function has an error")

            shortAndLongSides = getEnclosureDimensions(line = line)
            # print(shortAndLongSides)

            # With no alternative values
            if len(shortAndLongSides) == 2:
                longSide = shortAndLongSides[0]
                shortSide = shortAndLongSides[1]
                enc = enclosure.Enclosure(typeOfVia=typeOfVia, metalWidth=metalDimensions,
                                     metalPosition=metalPosition, ruleName=ruleName, shorSide=shortSide, longSide=longSide)

            # With alternative values
            elif len(shortAndLongSides) == 4:
                longSide = shortAndLongSides[0]
                altLongSide = shortAndLongSides[1]
                shortSide = shortAndLongSides[2]
                altShortSide = shortAndLongSides[3]
                enc = enclosure.Enclosure(typeOfVia=typeOfVia, metalWidth=metalDimensions,
                                     metalPosition=metalPosition, ruleName=ruleName, shorSide=shortSide, longSide=longSide, altLongSide=altLongSide, altShortSide=altShortSide)
            
            else:
                print("there is an error on creating an enclosure object")

            for via in mapOfLayers[layerName].vias:
                # print(f"{via.name} -----> {typeOfVia}")
                if via.name == typeOfVia:
                    if metalPosition == "M_LOWER":
                        via.lowerEnclosures.append(enc)
                    elif metalPosition == "M_UPPER":
                        via.upperEnclosures.append(enc)
