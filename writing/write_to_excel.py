from openpyxl import Workbook
  
def writeInExcel(listOfSpacing, excelName):
    # Workbook is created
    wb = Workbook()
    # grab the active worksheet
    ws = wb.active
    # add_sheet is used to create sheet.

    ws.append(["Rule", "VIA_1", "Edge_1", "VIA_2", "Edge_2", "Relation", "PRL", "Diff_Net", "Spacing", "Comment"])


    for item in listOfSpacing:
        writeRow(ws, item)

    wb.save(f'output_files/spacings/{excelName}.xlsx')


def writeRow(ws, item):
    ws.append([item.ruleName, item.firstViaType, item.firstViaEdge, 
               item.secondViaType, item.secondViaEdge, item.relationDirection,
               item.PRL, item.diffNet, item.spacingValue, item.comment])

mapOfSpacings = {}
def removeDuplicates(finalList):
    # Removing duplicates (VIA_LRG to VIA_BAR) is equal to (VIA_BAR to VIA_LRG). So, we need just one of them
    for rule in finalList:
        if rule.firstViaType == rule.secondViaType:
            relation = rule.firstViaType + '_' + rule.secondViaType
            if relation not in mapOfSpacings.keys():
                mapOfSpacings[relation] = []

            mapOfSpacings[relation] += [rule]

        else:
            # check variable is to check if the relation is already in the mapOfSpacings or not
            check = rule.secondViaType + '_' + rule.firstViaType
            if check in mapOfSpacings.keys():
                # switch rule values
                temp = rule.firstViaType
                rule.firstViaType = rule.secondViaType
                rule.secondViaType = temp

                temp = rule.firstViaEdge
                rule.firstViaEdge = rule.secondViaEdge
                rule.secondViaEdge = temp
                mapOfSpacings[check] += [rule]
                # continue
            else:
                relation = rule.firstViaType + '_' + rule.secondViaType
                if relation not in mapOfSpacings.keys():
                    mapOfSpacings[relation] = []

                mapOfSpacings[relation] += [rule]


###########################################################################################
def writeLineInFile(file, item):
    file.write(f"{item.ruleName} {item.firstViaType} {item.firstViaEdge} {item.secondViaType} {item.secondViaEdge} {item.relationDirection} {item.PRL} {item.diffNet} {item.spacingValue} {item.comment}")    

def writeInFile(listOfSpacing, fileName):
    file = open(f"output_files/spacings/{fileName}.txt", "w")
    file.write("Rule VIA_1 Edge_1 VIA_2 Edge_2 Relation PRL Diff_Net Spacing Comment")
    file.write("\n")

    for item in listOfSpacing:
        writeLineInFile(file, item)

    file.close()   

###########################################################################################
def writeFromMap(myMap):
    for relationName in myMap.keys():
        writeInExcel(listOfSpacing = myMap[relationName], excelName = relationName)
        writeInFile(listOfSpacing=myMap[relationName], fileName=relationName)


def prepareAndWriteToExcel(finalList):
    removeDuplicates(finalList=finalList)
    writeFromMap(myMap=mapOfSpacings)
