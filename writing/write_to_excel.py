import xlwt
from xlwt import Workbook
  
def writeInExcel(listOfSpacing, excelName):
    # Workbook is created
    wb = Workbook()
    
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 1, 'Rule')
    sheet1.write(0, 2, 'VIA_1')
    sheet1.write(0, 3, 'Edge_1')
    sheet1.write(0, 4, 'VIA_2')
    sheet1.write(0, 5, 'Edge_2')
    sheet1.write(0, 6, 'Relation')
    sheet1.write(0, 7, 'PRL')
    sheet1.write(0, 8, 'Diff_Net')
    sheet1.write(0, 9, 'Spacing')
    sheet1.write(0, 10, 'Comment')

    rowNumber = 1
    for item in listOfSpacing:
        writeRow(sheet1, rowNumber, item)
        rowNumber += 1

    wb.save(f'output_files/spacings/{excelName}.xls')


def writeRow(sheet1, rowNumber, item):
    sheet1.write(rowNumber, 1, item.ruleName)
    sheet1.write(rowNumber, 2, item.firstViaType)
    sheet1.write(rowNumber, 3, item.firstViaEdge)
    sheet1.write(rowNumber, 4, item.secondViaType)
    sheet1.write(rowNumber, 5, item.secondViaEdge)
    sheet1.write(rowNumber, 6, item.relationDirection)
    sheet1.write(rowNumber, 7, item.PRL)
    sheet1.write(rowNumber, 8, item.diffNet)
    sheet1.write(rowNumber, 9, item.spacingValue)
    sheet1.write(rowNumber, 10, item.comment)


mapOfSpacings = {}
def removeDuplicates(finalList):
    # Removing duplicates (VIA_LRG to VIA_BAR) is equal to (VIA_BAR to VIA_LRG). So, we need just one of them
    for rule in finalList:
        if rule.firstViaType == rule.secondViaType:
            relation = rule.firstViaType + rule.secondViaType
            if relation not in mapOfSpacings.keys():
                mapOfSpacings[relation] = []

            mapOfSpacings[relation] += [rule]

        else:
            # check variable is to check if the relation is already in the mapOfSpacings or not
            check = rule.secondViaType + rule.firstViaType
            if check in mapOfSpacings.keys():
                # switch rule values
                temp = rule.firstViaType
                rule.firstViaType = rule.secondViaType
                rule.secondViaType = temp

                temp = rule.firstViaEdge
                rule.firstViaEdge = rule.secondViaEdge
                rule.secondViaEdge = temp
                
                mapOfSpacings[check] += [rule]
                continue
            else:
                relation = rule.firstViaType + rule.secondViaType
                if relation not in mapOfSpacings.keys():
                    mapOfSpacings[relation] = []

                mapOfSpacings[relation] += [rule]


def writeFromMap(myMap):
    for relationName in myMap.keys():
        writeInExcel(listOfSpacing = myMap[relationName], excelName = relationName)


def prepareAndWriteToExcel(finalList):
    removeDuplicates(finalList=finalList)
    writeFromMap(myMap=mapOfSpacings)
