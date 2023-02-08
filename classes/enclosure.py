class Enclosure:
    typeOfVia = ""
    metalDimensions = ""
    shortSide = 0.0
    longSide = 0.0
    metalPosition = ""
    ruleName = ""

    def __init__(self, typeOfVia, metalWidth, shorSide, longSide, metalPosition, ruleName):
        self.typeOfVia = typeOfVia
        self.metalDimensions = metalWidth
        self.shortSide = shorSide
        self.longSide = longSide
        self.metalPosition = metalPosition
        self.ruleName = ruleName

    def __str__(self):
        return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} //{self.ruleName}"
