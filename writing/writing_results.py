from globals import mapOfLayers

def writeVariableFile():
    # writing the map values into a text file
    with open("output_files/variable_output.txt", 'w') as variablesFile:

        for key, value in mapOfLayers.items():

            variablesFile.write("//******************\n// " +
                    key + " Variables" + "\n//******************\n")

            # print dimesnions
            for via in value.vias:

                variablesFile.write("VARIABLE " + via.name + "_WIDTH " +
                        str(via.width) + "  //" + via.ruleName + '\n')

                variablesFile.write("VARIABLE " + via.name + "_LENGTH " +
                        str(via.length) + "  //" + via.ruleName + '\n')
                variablesFile.write('\n')

            # print spacings
            for via in value.vias:
                for spacing in via.spacings:
                    if via.name.find('BAR') > 0 or spacing.via_name.find('BAR') > 0:
                        variablesFile.write("VARIABLE " + via.name + "_" + spacing.via_name +
                                "_SHORTEDGE_SPACE " + str(spacing.shortEdge_space))
                        variablesFile.write('\n')
                        variablesFile.write("VARIABLE " + via.name + "_" + spacing.via_name +
                                "_SHORTEDGE_SPACE_PRL " + str(spacing.shortEdge_spacePRL))
                        variablesFile.write('\n')
                        variablesFile.write("VARIABLE " + via.name + "_" + spacing.via_name +
                                "_LONGEDGE_SPACE " + str(spacing.longEdge_space))
                        variablesFile.write('\n')
                        variablesFile.write("VARIABLE " + via.name + "_" + spacing.via_name +
                                "_LONGEDGE_SPACE_PRL " + str(spacing.longEdge_spacePRL))
                    else:
                        variablesFile.write("VARIABLE " + via.name + "_" +
                                spacing.via_name + "_SPACE " + str(spacing.space))
                        variablesFile.write('\n')
                        variablesFile.write("VARIABLE " + via.name + "_" +
                                spacing.via_name + "_SPACE_PRL " + str(spacing.spacePRL))
                    variablesFile.write('\n\n')
                variablesFile.write('\n')

    variablesFile.close()

def writeEnclosureFile(enclosureAltMode):
        encOutput = open("output_files/enclosure_output.txt", 'w')
        for key in mapOfLayers.keys():
                encOutput.write("//" + key + "\n")
                for via in mapOfLayers[key].vias:
                        for enclosuer in via.lowerEnclosures:
                                enclosuer.alternativeMode = int(enclosureAltMode)
                                # print(enclosuer)
                                encOutput.write(str(enclosuer) + "\n")

                        encOutput.write("\n")

                        for enclosuer in via.upperEnclosures:
                                enclosuer.alternativeMode = int(enclosureAltMode)
                                # print(enclosuer)
                                encOutput.write(str(enclosuer) + "\n")

                encOutput.write("\n")

        encOutput.close()