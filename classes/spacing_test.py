class SpacingTest:
    ruleName = ""
    firstViaType = ""
    secondViaType = ""

    firstViaEdge = ""
    secondViaEdge = ""

    relationDirection = ""
    PRL = "NO PRL"
    comment = ""

    def __init__(self, ruleName, firstViaType, secondViaType, firstViaEdge, secondViaEdge, relationDirection, PRL, comment):
        self.ruleName = ruleName
        self.firstViaType = firstViaType
        self.secondViaType = secondViaType
        self.firstViaEdge = firstViaEdge
        self.secondViaEdge = secondViaEdge
        self.relationDirection = relationDirection
        self.PRL = PRL
        self.comment = comment

    def __str__(self):
        
        return f"{self.firstViaType} {self.firstViaEdge} ===> {self.secondViaType} {self.secondViaEdge} with relation {self.relationDirection} with prl = {self.PRL}"

