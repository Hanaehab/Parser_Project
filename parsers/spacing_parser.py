import re
from variables import mapOfLayers
from classes.spacing import SpacingBar, Spacing


def addSpacings():
    global variableCombinations

    for key, value in mapOfLayers.items():

        for i in range(len(value.vias)):

            variableCombinations = []

            for j in range(i, len(value.vias)):

                if value.vias[i].name.find('BAR') > 0 or value.vias[j].name.find('BAR') > 0:

                    spacing = SpacingBar(
                        value.vias[j].name, 0.0, " ", 0.0, " ", " ")
                    variableCombinations.append(spacing)

                else:
                    spacing = Spacing(value.vias[j].name, 0.0, "", "")
                    variableCombinations.append(spacing)

            value.vias[i].spacings = variableCombinations
