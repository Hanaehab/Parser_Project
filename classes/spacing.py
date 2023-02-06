class Spacing:
    via_name = "" #name of via the space is betweem
    space = 0.0
    spacePRL = ""
    ruleName = ""

    def __init__(self, via_name, space, spacePRL, ruleName):
        self.via_name = via_name
        self.space = space
        self.spacePRL = spacePRL
        self.ruleName = ruleName

    def __str__(self):
        return f"{self.via_name} {self.space} {self.spacePRL} {self.ruleName}"


class SpacingBar:
    via_name = ""
    shortEdge_space = 0.0
    shortEdge_spacePRL = ""
    longEdge_space = 0.0
    longEdge_spacePRL = ""
    ruleName = ""


    def __init__(self, via_name, shortEdge_space, shortEdge_spacePRL, longEdge_space, longEdge_spacePRL, ruleName):
        self.via_name = via_name
        self.shortEdge_space = shortEdge_space
        self.shortEdge_spacePRL = shortEdge_spacePRL
        self.longEdge_space = longEdge_space
        self.longEdge_spacePRL = longEdge_spacePRL
        self.ruleName = ruleName

    def __str__(self):
        return f"{self.via_name} {self.shortEdge_space} {self.longEdge_space} {self.ruleName}"
