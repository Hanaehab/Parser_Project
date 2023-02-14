from globals import conventions, mapOfLayers
from classes.layer import Layer
from classes.via import Via
import itertools

# Variables to count how many sqaures and how many bars
squareCounter = 0
barCounter = 1
ruleName = ""                               

def addDimensions():

    global squareCounter, barCounter, ruleName
    dimensions = []  # will contain lists [W,L] of all exsiting dimensions
    flag = 0  # This flag is to trace the "=" operator and get the dimensions after it

    with open('files/variable_rules.txt', 'r') as file:
        for line in file:
            flag = 0
            dimensions.clear()
            ruleName = line.split()[0]
            variableName = conventions[ruleName.split('.')[0]]
            # print(f"variable name in map of layers is {variableName}")

            mapOfLayers[variableName] = Layer(variableName)

            for word in line.split():

                if (word == '='):
                    flag = 1
                    continue

                if (flag == 1):

                    # word[-1] gets last element in the string and word [:-1] removes last element from string
                    # split string by '/' to get list [W,H]
                    dimensionSplit = word[:-1].split(
                        '/') if word[-1] == ',' else word.split('/')
                    dimensionSplit = [float(i) for i in dimensionSplit]
                    dimensions.append(sorted(dimensionSplit))

            # removing duplicates from array
            dimensions = list(dimensions for dimensions,
                              _ in itertools.groupby(dimensions))

            # Reset the variables for the new line (rule)
            squareCounter = 0
            barCounter = 1
            layerVias = []
            # for each dimension in dimensions:
            for dimension in dimensions:
                getDimensions(dimension, layerVias, variableName)

            mapOfLayers[variableName].vias = layerVias


def getDimensions(dimension, layerVias, variableName):

    global squareCounter, barCounter, mapOfVariables
    width = dimension[0]
    length = dimension[1]

    if width == length:

        if (squareCounter < 1):  # smallest dimension

            via = Via(variableName, width, length, ruleName)

        else:
            typeOfVia = "LRG" + (str(squareCounter)
                                 if squareCounter > 1 else '')
            via = Via(variableName + typeOfVia, width, length, ruleName)

        squareCounter += 1

    elif width > length or length > width:
        if (barCounter < 2):
            typeOfVia = "BAR"

        else:
            typeOfVia = "BAR" + str(barCounter)

        via = Via(variableName + typeOfVia, width, length, ruleName)
        barCounter += 1

    layerVias.append(via)
