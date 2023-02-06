from globals import *
import re

def getTypeOfVia(line, variableName):
    # If we found "square" in the line
    if(line.find("square") > 0):

        viaDimensions = re.search(r'width\s*=\s*\d+\.*\d+', line)

        # Get the length of the side
        width = float(viaDimensions.group().split('=')[1])

        for via in mapOfLayers[variableName].vias:
            if(via.width == width and via.length == width):
                return via.name
        return "NOT FOUND"

    # If we found "rectangualr" in the line
    elif(line.find("rectangular") > 0):
        viaDimensions = re.search(r'width/length = (\d+(\.\d+)*)/(\d+(\.\d+)*)', line)
        viaDimensions =  viaDimensions.group().split()[2].split('/')
        width = float(viaDimensions[0])
        length = float(viaDimensions[1])

        for via in mapOfLayers[variableName].vias:
            if(via.width == width and via.length == length):
                return via.name

        return "NOT FOUND"
    else:
        return "NOT FOUND"

def getMetalPosistion(line):
    if(line.find("Lower_Metal") > 0):
        return "M_LOWER"
    else:
        return "M_UPPER"


def addEnclosure():

    with open('enclosure_rules.txt','r') as file:
        for line in file:

            layer = line.split('.')[0]
            variableName = conventions[layer]

            output = ""
            typeOfVia = getTypeOfVia(line = line, variableName = variableName)
            output += typeOfVia
            metalPosition = getMetalPosistion(line = line)
            output += " " + metalPosition + " width"

            layerDimensions = re.search(r'\[\s*width\s*(/\s*length)*\s*(>=|=<|>|<)\s*(\d+(\.\d+)*(\s*/\s*\d+(\.\d+))*)', line)
            # print(layerDimensions.group().split())

            print(output)

            # for word in line.split():
            #     print(word)