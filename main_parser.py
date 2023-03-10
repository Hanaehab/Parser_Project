import parsers.dimensions_parser as dimensions_parser
import parsers.spacing_parser as spacing_parser
import parsers.enclosure_parser as enclosure_parser
import parsers.spacing_test as spacing
import preprocessing.N3_preprocessing as preprocessing
import writing.writing_results as writing
import sys
import os

# Create the output folders if any one not exist 
def createIfNotExist():
    outputFolder = "output_files"
    spacingFolder = "output_files/spacings"
    preprocessedFolder = "preprocessedFiles"

    outputFolderCheck = os.path.exists(outputFolder)
    spacingFolderCheck = os.path.exists(spacingFolder)
    preprocessedFolderCheck = os.path.exists(preprocessedFolder)

    if not outputFolderCheck:
        os.makedirs(outputFolder)

    if not spacingFolderCheck:
        os.makedirs(spacingFolder)

    if not preprocessedFolderCheck:
        os.makedirs(preprocessedFolder)


ruleDeckPath = sys.argv[1]
metalStack = sys.argv[2]
# The alternatives values of the enclosure rules (0 -> not printing them, 1 -> printing them)
enclosureAltMode = sys.argv[3]

# Create the output folders if any one not exist 
createIfNotExist()

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