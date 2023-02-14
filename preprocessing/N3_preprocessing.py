from globals import *
import re

def n3Preprocessing():
   
    encFile = open("files/enclosure_rules.txt", "w")
    dimFile = open("files/variable_rules.txt", "w")
    
    with open('files/rule_deck.txt', 'r') as file: # Path of the rule deck
        for line in file:
            if(line.find(".EN.") > 0):
                regexp = re.compile(r'with the other 2\s*(long)?\s*sides(.*)')
                if regexp.search(line):
                    ruleName = line.split()[0]
                    viaNumber = ruleName.split('.')[0]
                    if viaNumber in numberOfVias.keys():
                        afterPreprocessing = ruleName.replace(viaNumber, numberOfVias[viaNumber][0])
                        afterPreprocessing += line[line.find("@")+1:]
                    else:
                        afterPreprocessing = ruleName + line[line.find("@")+1:]

                    encFile.write(afterPreprocessing)

            elif(line.find(".W.") > 0):
                ruleName = line.split()[0]
                viaNumber = ruleName.split('.')[0]
                if viaNumber in numberOfVias.keys():
                    afterPreprocessing = ruleName.replace(viaNumber, numberOfVias[viaNumber][0])
                    afterPreprocessing += line[line.find("@")+1:]
                else:
                    afterPreprocessing = ruleName + line[line.find("@")+1:]

                dimFile.write(afterPreprocessing)


    encFile.close()
    dimFile.close()

