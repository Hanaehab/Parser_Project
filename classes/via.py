class Via:
    name = ""
    width = 0.0
    length = 0.0
    ruleName = ""
    lowerEnclosures = []  # List of "enclosure" objects
    upperEnclosures = []  # List of "enclosure" objects
    spacings = []  # List of "spacing" objects

    def __init__(self, name, width, length, ruleName):
        self.name = name
        self.width = width
        self.length = length
        self.ruleName = ruleName
        self.lowerEnclosures = []
        self.upperEnclosures = []
        self.spacings = []

    def __str__(self):
        return f"{self.name} {self.width} {self.length} {self.ruleName}"
