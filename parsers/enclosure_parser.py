from variables import mapOfLayers, conventions
import re


def addEnclosure():

    with open('enclosure_rules.txt', 'r') as file:
        for line in file:
            layer = line.split('.')[0]
            variableName = conventions[layer]
            
            if (line.find("square") > 0):
                print("square via")
                viaDimensions = re.search(r'width = \d+\.\d+', line)
                width = float(viaDimensions.group().split()[2])

                for via in mapOfLayers[variableName].vias:
                    if(via.width == width and via.length == width):
                        print(via.name)

            elif (line.find("rectangular") > 0):
                print("rectangular via")

