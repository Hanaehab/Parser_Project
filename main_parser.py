import parsers.dimensions_parser as dimensions_parser
import parsers.spacing_parser as spacing_parser
import parsers.enclosure_parser as enclosure_parser
import parsers.spacing_test as spacing
import preprocessing.N3_preprocessing as preprocessing
import writing.writing_results as writing
import sys

ruleDeckPath = sys.argv[1]
metalStack = sys.argv[2]
# The alternatives values of the enclosure rules (0 -> not printing them, 1 -> printing them)
enclosureAltMode = sys.argv[3]

# Generating a map with each via number and preprocess the rule deck (N3)
preprocessing.analyzeMetalStack(metalStack)
preprocessing.n3Preprocessing(ruleDeckPath=ruleDeckPath)

# calling the methods to add the values in the map
dimensions_parser.parseDimensions()
# spacing_parser.addSpacings()
enclosure_parser.parseEnclosure()

# Parsing spacing rules and writing in excel
spacing.parseSpacing()

# Writing the map values into a text file  
writing.writeVariableFile()
writing.writeEnclosureFile(enclosureAltMode=enclosureAltMode)