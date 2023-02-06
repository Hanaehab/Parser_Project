class Spacing:
    via_name = "" #name of via the space is betweem
    space = 0.0
    space_PRL = ""
    rule_name = ""

    def __init__(self, via_name, space, space_PRL, rule_name):
        self.via_name = via_name
        self.space = space
        self.space_PRL = space_PRL
        self.rule_name = rule_name

    def __str__(self):
        return f"{self.via_name} {self.space} {self.space_PRL} {self.rule_name}"


class SpacingBar:
    via_name = ""
    shortEdge_space = 0.0
    shortEdge_space_PRL = ""
    longEdge_space = 0.0
    longEdge_space_PRL = ""
    rule_name = ""


    def __init__(self, via_name, shortEdge_space, shortEdge_space_PRL, longEdge_space, longEdge_space_PRL, rule_name):
        self.via_name = via_name
        self.shortEdge_space = shortEdge_space
        self.shortEdge_space_PRL = shortEdge_space_PRL
        self.longEdge_space = longEdge_space
        self.longEdge_space_PRL = longEdge_space_PRL
        self.rule_name = rule_name

    def __str__(self):
        return f"{self.via_name} {self.shortEdge_space} {self.longEdge_space} {self.rule_name}"
