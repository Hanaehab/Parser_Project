from globals import *
from classes import enclosure
import re


def getTypeOfVia(line, layerName):
    # If we found "square" in the line
    if (line.find("square") > 0):

        # Regex to get the length of the side of the square via
        viaDimensions = re.search(r'width\s*=\s*\d+\.*\d+', line)
        width = float(viaDimensions.group().split('=')[1])

        for via in mapOfLayers[layerName].vias:
            if (via.width == width and via.length == width):
                return via.name  # Type of via (Ex: VIA0i, VIA0iLRG, VIA0iLRG2)

        return "NOT FOUND"

    # If we found "rectangualr" in the line
    elif (line.find("rectangular") > 0):

        # Regex to get the length of the sides of the rectangular via
        viaDimensions = re.search(
            r'width/length = (\d+(\.\d+)*)/(\d+(\.\d+)*)', line)
        viaDimensions = viaDimensions.group().split()[2].split('/')
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


def getLayerDimension(line):

    regexOfDimensions = re.search(r'by Lower_Metal\s*\[.*\]', line)

    # If we want to save the string of the dimensions
    # x = layerDimensions.group()[layerDimensions.group().find("[") + 1 :-1]
    # print(x)

    metalDimensions = re.findall(r'(\d+\.\d+)', regexOfDimensions.group())

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



def addEnclosure():

    with open('enclosure_rules.txt', 'r') as file:
        for line in file:

            ruleName = line.split()[0]
            layer = line.split('.')[0]
            layerName = conventions[layer]

            output = ""
            typeOfVia = getTypeOfVia(line = line, layerName = layerName)
            output += typeOfVia
            
            metalPosition = getMetalPosistion(line = line)
            output += " " + metalPosition + " width "

            metalDimensions = getLayerDimension(line = line)
            output += metalDimensions

            # print(output)

            en = enclosure.Enclosure(typeOfVia = typeOfVia, metalWidth = metalDimensions, metalPosition = metalPosition, ruleName = ruleName, shorSide = 0.0, longSide = 0.0)
            # print(en)
            for via in mapOfLayers[layerName].vias:
                if via.name == typeOfVia:
                    if metalPosition == "M_LOWER":
                        via.lowerEnclosures.append(en)
                    elif metalPosition == "M_UPPER":
                        via.upperEnclosures.append(en)


