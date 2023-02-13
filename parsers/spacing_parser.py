from globals import mapOfLayers
from classes.spacing import SpacingBar, Spacing
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["test"]
mycol = mydb["parser"]

def addSpacings():
    global variableCombinations

    for key, value in mapOfLayers.items():

        for i in range(len(value.vias)):

            variableCombinations = []

            for j in range(i, len(value.vias)):

                if value.vias[i].name.find('BAR') > 0 or value.vias[j].name.find('BAR') > 0:

                    spacing = SpacingBar(
                        value.vias[j].name, 0.0, " ", 0.0, " ", " ")
                    variableCombinations.append(spacing)

                else:
                    spacing = Spacing(value.vias[j].name, 0.0, "", "")
                    variableCombinations.append(spacing)

                mycol.update_one({'name': key, f'vias.{i}.name' : value.vias[i].name}, {'$push': {f'vias.{i}.spacings': spacing.__dict__}})
            
            value.vias[i].spacings = variableCombinations
