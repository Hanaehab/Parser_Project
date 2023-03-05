import parsers.dimensions_parser as dimensions_parser
import parsers.spacing_parser as spacing_parser
import parsers.enclosure_parser as enclosure_parser
import preprocessing.N3_preprocessing as preprocessing
import writing.writing_results as writing
import globals
import sys
from globals import conventions, mapOfLayers, numberOfVias, metalNumbers
from classes.layer import Layer
from classes.via import Via
import itertools
import re

def preprocessSpacing():

    # print(globals.numberOfVias)
    # print(globals.conventions)
    # print(globals.metalNumbers)

    # for i in mapOfLayers['Vxk'].vias:
    #     # print(mapOfLayers['Vxk'].vias)
    #     print(f"{i.name} --> {i.length} {i.width}")

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
    for via in mapOfLayers[layerName].vias:
        toCompare = set([via.width, via.length])
        if (viaDimensions == toCompare):
            return via.name  # Type of via (Ex: VIA0i, VIA0iLRG, VIA0iLRG2)


def getViasDimensions(line):
    try:
        viaDimensions = re.findall(r'edge length = \d+\.*\d+\s*/\s*\d+\.*\d+', line)

        fisrtViaDimension = re.findall(r'(\d+(?:\.\d+)?)', viaDimensions[0])
        secondViaDimenion = re.findall(r'(\d+(?:\.\d+)?)', viaDimensions[1])

        fisrtViaDimension = [float(x) for x in fisrtViaDimension]
        secondViaDimenion = [float(x) for x in secondViaDimenion]

        fisrtViaDimension = set(fisrtViaDimension)
        secondViaDimenion = set(secondViaDimenion)

        return fisrtViaDimension, secondViaDimenion

    except:
        return "NOT FOUND", "NOT FOUND"

def parseSpacing():
    with open('files/spacing_rules.txt', 'r') as file:
        for line in file:
            ruleName = line.split()[0]
            layerName = getLayerName(ruleName)
            fisrtViaDimension, secondViaDimenion = getViasDimensions(line)
            firstViaType = getTypeOfVia(fisrtViaDimension, layerName)
            secondViaType = getTypeOfVia(secondViaDimenion, layerName)

            # print(f"between {firstViaType} and {secondViaType}")
            
            

