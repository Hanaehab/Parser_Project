class Enclosure:
    typeOfVia = ""
    metalDimensions = ""
    shortSide = 0.0
    longSide = 0.0
    metalPosition = ""
    ruleName = ""

    # If there are alternative values
    alternativeMode = 1
    altShortSide = "none"
    altLongSide = "none"

    def __init__(self, typeOfVia, metalWidth, shortSide, longSide, metalPosition, ruleName, altLongSide="none", altShortSide="none"):
        self.typeOfVia = typeOfVia
        self.metalDimensions = metalWidth
        self.shortSide = shortSide
        self.longSide = longSide
        self.metalPosition = metalPosition
        self.ruleName = ruleName
        self.altLongSide = altLongSide
        self.altShortSide = altShortSide

        self.alternativeMode = 1

    def __str__(self):

        if self.alternativeMode == 0 or self.altLongSide == "none":
            if len(self.ruleName.split()) > 1:
                return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} //{self.ruleName.split()[0]} //{self.ruleName.split()[1]}"
            else:
                return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} //{self.ruleName}"
        else:
            if len(self.ruleName.split()) > 1:
                return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} enc {self.altLongSide} {self.altShortSide} //{self.ruleName.split()[0]} //{self.ruleName.split()[1]}"
            else:
                return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} enc {self.altLongSide} {self.altShortSide} //{self.ruleName}"
