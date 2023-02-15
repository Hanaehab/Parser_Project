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

    def __init__(self, typeOfVia, metalWidth, shorSide, longSide, metalPosition, ruleName, altLongSide="none", altShortSide="none"):
        self.typeOfVia = typeOfVia
        self.metalDimensions = metalWidth
        self.shortSide = shorSide
        self.longSide = longSide
        self.metalPosition = metalPosition
        self.ruleName = ruleName
        self.altLongSide = altLongSide
        self.altShortSide = altShortSide

        self.alternativeMode = 1

    def __str__(self):
        
        # # print(type(self.alternativeMode))
        # if self.alternativeMode == 0:
        #     return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} //{self.ruleName}"

        # else:
        if self.alternativeMode == 0 or self.altLongSide == "none":
            print(f"alternative is {self.alternativeMode}")
            return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} {self.shortSide} //{self.ruleName}"
        else:
            print(f"alternativeaaasdasdaa is {self.alternativeMode}")
            return f"{self.typeOfVia} {self.metalPosition} width {self.metalDimensions} enc {self.longSide} / {self.altLongSide} {self.shortSide} / {self.altShortSide} //{self.ruleName}"
