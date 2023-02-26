from globals import *
import re


def analyzeMetalStack(typesString):
    numberOfVias["VIA0"] = "VIA0"
    conventions["VIA0"] = "VIA0i"
    conventions["0"] = "VIA0i"

    metalNumbers["M1"] = "M1" 

    # conventions2["0"] = "VIA0i"
    typesOccurrences = re.findall(r'\d+', typesString)
    types = re.findall(r'[a-zA-Z]+', typesString)
    counter = 1
    for index, type in enumerate(types):
        noOfOccurrences = int(typesOccurrences[index])
        for n in range(noOfOccurrences):
            viaLayerName = "VIA" + str(counter) if type.lower() != "ap" else "RV"
            viaTypeName = "VIA" + type.lower() if type.lower() != "ap" else "RV"
            numberOfVias[viaLayerName] = viaTypeName
            conventions[viaTypeName] = "V" + type.lower()
            if(type.lower() == "ap"):
                metalNumbers["AP"] = "RV"
            else:
                # conventions2[type.lower()] = "V" + type.lower()
                counter += 1
                metalNumbers["M" + str(counter)] = "M" + type.lower()



    # print(metalNumbers)

def n3Preprocessing(ruleDeckPath):

    encFile = open("files/enclosure_rules.txt", "w")
    dimFile = open("files/variable_rules.txt", "w")
    typesWritten = []  #to avoid writting same type multiple times

    with open(ruleDeckPath, 'r') as file:  # Path of the rule deck
        
    # M1.EN.82.1.T { @ Short side enclosure of rectangular Lower_VIA [width/length = 0.020/0.039 um] 
    # by M1 [width < 0.039 um] with the other 2 long sides >= 0.0060 / 0.11111111111111111 um >= 0.0290 / 0.22222222222

        for line in file:
            if(re.search(r'^VIA\d*.EN.',line) or re.search(r'^M\d*.EN.',line) or re.search(r'^RV.EN.',line) or re.search(r'^AP.EN.',line) ):
                regexp = re.compile(r'with the other 2\s*(long)?\s*sides(.*)')
                if regexp.search(line):
                    ruleName = line.split()[0] # EX: M1.EN.82.1.T
                    viaNumber = ruleName.split('.')[0] # EX: M1
                    if viaNumber in numberOfVias.keys():
                        afterPreprocessing = ruleName.replace(
                            viaNumber, numberOfVias[viaNumber])
                        afterPreprocessing += line[line.find("@")+1:]
                    else:
                        afterPreprocessing = ruleName.replace(
                            viaNumber, metalNumbers[viaNumber])
                        afterPreprocessing += line[line.find("@")+1:]
                        # print(afterPreprocessing)
                    
                    reg = re.compile(r'\(Except.*\)')
                    if reg.search(afterPreprocessing):
                        toRemove = re.search(r'\(Except.*\)', afterPreprocessing)
                        afterPreprocessing = afterPreprocessing.replace(toRemove.group(), "")

                    encFile.write(afterPreprocessing)

            elif(re.search(r'^VIA\d*.W.1',line) or re.search(r'^RV.W.1',line)):
                ruleName = line.split()[0]
                viaNumber = ruleName.split('.')[0]
                if viaNumber in numberOfVias.keys():
                    if(numberOfVias[viaNumber] in typesWritten):  #Find if the extracted type is already written
                        continue
                    afterPreprocessing = ruleName.replace(
                        viaNumber, numberOfVias[viaNumber])
                    afterPreprocessing += line[line.find("@")+1:]
                else:
                    afterPreprocessing = ruleName + line[line.find("@")+1:]
                
                typesWritten.append(numberOfVias[viaNumber])
                dimFile.write(afterPreprocessing)

    encFile.close()
    dimFile.close()
