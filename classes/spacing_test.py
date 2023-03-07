class SpacingTest:
    ruleName = ""
    firstViaType = ""
    secondViaType = ""

    firstViaEdge = ""
    secondViaEdge = ""

    relationDirection = ""
    PRL = "NO PRL"
    diffNet = False
    spacingValue = 0.0
    comment = ""

    def __init__(self, ruleName, firstViaType, secondViaType, firstViaEdge, secondViaEdge, relationDirection, PRL, comment, diffNet, spacingValue):
        self.ruleName = ruleName
        self.firstViaType = firstViaType
        self.secondViaType = secondViaType
        self.firstViaEdge = firstViaEdge
        self.secondViaEdge = secondViaEdge
        self.relationDirection = relationDirection
        self.PRL = PRL
        self.diffNet = diffNet
        self.spacingValue = spacingValue
        self.comment = comment

    def __str__(self):
        
        return f"{self.ruleName} BETWEEN ({self.firstViaType} {self.firstViaEdge}) AND ({self.secondViaType} {self.secondViaEdge}) ({self.relationDirection}) (PRL = {self.PRL}) ({self.diffNet}) (Spacing value = {self.spacingValue})"

