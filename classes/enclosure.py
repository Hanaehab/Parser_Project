class Enclosure:
    typeOfVia = ""
    metalDimensions = ""
    shortSide = 0.0
    longSide = 0.0
    metalPosition = ""
    ruleName = ""

    # If there are alternative values
    altShortSide = "none"
    altLongSide = "none"

    def __init__(self, typeOfVia, metalWidth, shorSide, longSide, metalPosition, ruleName, altLongSide="none", altShortSide="none"):
        self.typeOfVia = typeOfVia
        self.metalDimensions = metalWidth
        self.shortSide = shorSide
        self.longSide = longSide
        self.metalPosition = metalPosition
        self.ruleName = ruleName
        self.altLongSide = altLongSide
        self.altShortSide = altShortSide

    def __str__(self):
        if self.altLongSide == "none":
            return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} //{self.ruleName}"
        else:
            return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide}/{self.altLongSide} {self.shortSide}/{self.altShortSide} //{self.ruleName}"
