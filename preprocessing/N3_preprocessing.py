from globals import *
import re


def analyzeMetalStack(typesString):
    numberOfVias["VIA0"] = "VIA0"
    conventions["VIA0"] = "VIA0i"
    conventions2["0"] = "VIA0i"
    typesOccurrences = re.findall(r'\d+', typesString)
    types = re.findall(r'[a-zA-Z]+', typesString)
    counter = 1
    for index, type in enumerate(types):
        noOfOccurrences = int(typesOccurrences[index])
        for n in range(noOfOccurrences):
            viaLayerName = "VIA" + str(counter)
            viaTypeName = "VIA" + type.lower() if type.lower() != "ap" else "RV"
            numberOfVias[viaLayerName] = viaTypeName
            conventions[viaTypeName] = "V" + type.lower()
            if(type.lower() == "ap"):
                conventions2["AP"] = "RV"
            else:
                conventions2[type.lower()] = "V" + type.lower()
            counter += 1


def n3Preprocessing(ruleDeckPath):

    encFile = open("files/enclosure_rules.txt", "w")
    dimFile = open("files/variable_rules.txt", "w")

    with open(ruleDeckPath, 'r') as file:  # Path of the rule deck
        for line in file:
            # if (line.find(".EN.") > 0):
            if(re.search(r'^VIA\d*.EN.',line) or re.search(r'^M\d*.EN.',line) or re.search(r'^RV.EN.',line) or re.search(r'^AP.EN.',line) ):
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

            # elif (((line.split('.')[0]).find("VIA") >= 0 or (line.split('.')[0]).find("RV") >= 0) and line.find(".W.1") > 0):
            elif(re.search(r'^VIA\d*.W.1',line) or re.search(r'^RV.W.1',line)):
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
