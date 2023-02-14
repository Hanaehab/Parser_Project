import parsers.dimensions_parser as dimensions_parser
import parsers.spacing_parser as spacing_parser
import parsers.enclosure_parser as enclosure_parser
import preprocessing.N3_preprocessing as preprocessing
from globals import mapOfLayers

# Preprocessing (N3)
preprocessing.n3Preprocessing()

# calling the methods to add the values in the map
dimensions_parser.addDimensions()
spacing_parser.addSpacings()
enclosure_parser.addEnclosure()

# print(mapOfLayers['VIA0i'].vias[1].spacings[1])
# print(mapOfLayers['VIA0i'].vias)


# writing the map values into a text file
with open("output_files/variable_output.txt", 'w') as file:

    for key, value in mapOfLayers.items():

        file.write("//******************\n// " +
                   key + " Variables" + "\n//******************\n")

        # print dimesnions
        for via in value.vias:

            file.write("VARIABLE " + via.name + "_WIDTH " +
                       str(via.width) + "  //" + via.ruleName + '\n')

            file.write("VARIABLE " + via.name + "_LENGTH " +
                       str(via.length) + "  //" + via.ruleName + '\n')
            file.write('\n')

        # print spacings
        for via in value.vias:
            for spacing in via.spacings:
                if via.name.find('BAR') > 0 or spacing.via_name.find('BAR') > 0:
                    file.write("VARIABLE " + via.name + "_" + spacing.via_name +
                               "_SHORTEDGE_SPACE " + str(spacing.shortEdge_space))
                    file.write('\n')
                    file.write("VARIABLE " + via.name + "_" + spacing.via_name +
                               "_SHORTEDGE_SPACE_PRL " + str(spacing.shortEdge_spacePRL))
                    file.write('\n')
                    file.write("VARIABLE " + via.name + "_" + spacing.via_name +
                               "_LONGEDGE_SPACE " + str(spacing.longEdge_space))
                    file.write('\n')
                    file.write("VARIABLE " + via.name + "_" + spacing.via_name +
                               "_LONGEDGE_SPACE_PRL " + str(spacing.longEdge_spacePRL))
                else:
                    file.write("VARIABLE " + via.name + "_" +
                               spacing.via_name + "_SPACE " + str(spacing.space))
                    file.write('\n')
                    file.write("VARIABLE " + via.name + "_" +
                               spacing.via_name + "_SPACE_PRL " + str(spacing.spacePRL))
                file.write('\n\n')
            file.write('\n')

file.close()

# for via in mapOfLayers['VIA0i'].vias:
#     for enclosuer in via.lowerEnclosures:
#         print(enclosuer)

encOutput = open("output_files/enclosure_output.txt", 'w')
for key in mapOfLayers.keys():
    for via in mapOfLayers[key].vias:
        for enclosuer in via.lowerEnclosures:
            print(enclosuer)
            encOutput.write(str(enclosuer) + "\n")
