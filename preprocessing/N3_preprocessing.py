from globals import *
import re


def analyzeMetalStack(typesString):
    numberOfVias["VIA0"] = "VIA0"
    typesOccurrences = re.findall(r'\d+', typesString)
    types = re.findall(r'[a-zA-Z]+', typesString)
    counter = 1
    for index, type in enumerate(types):
        noOfOccurrences = int(typesOccurrences[index])
        for n in range(noOfOccurrences):
            viaLayerName = "VIA" + str(counter)
            viaTypeName = "VIA" + type.lower() if type.lower() != "RV" else "AP"
            numberOfVias[viaLayerName] = viaTypeName
            counter += 1


def n3Preprocessing(ruleDeckPath):

    encFile = open("files/enclosure_rules.txt", "w")
    dimFile = open("files/variable_rules.txt", "w")

    with open(ruleDeckPath, 'r') as file:  # Path of the rule deck
        for line in file:
            if (line.find(".EN.") > 0):
                regexp = re.compile(r'with the other 2\s*(long)?\s*sides(.*)')
                if regexp.search(line):
                    ruleName = line.split()[0]
                    viaNumber = ruleName.split('.')[0]
                    if viaNumber in numberOfVias.keys():
                        afterPreprocessing = ruleName.replace(
                            viaNumber, numberOfVias[viaNumber])
                        afterPreprocessing += line[line.find("@")+1:]
                    else:
                        afterPreprocessing = ruleName + line[line.find("@")+1:]
                    
                    reg = re.compile(r'\(Except.*\)')
                    if reg.search(afterPreprocessing):
                        toRemove = re.search(r'\(Except.*\)', afterPreprocessing)
                        afterPreprocessing = afterPreprocessing.replace(toRemove.group(), "")

                    encFile.write(afterPreprocessing)

            elif (line.find(".W.1.") > 0):
                ruleName = line.split()[0]
                viaNumber = ruleName.split('.')[0]
                if viaNumber in numberOfVias.keys():
                    afterPreprocessing = ruleName.replace(
                        viaNumber, numberOfVias[viaNumber])
                    afterPreprocessing += line[line.find("@")+1:]
                else:
                    afterPreprocessing = ruleName + line[line.find("@")+1:]

                dimFile.write(afterPreprocessing)

    encFile.close()
    dimFile.close()
