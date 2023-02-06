class Via:
    name = " "
    width = 0.0
    length = 0.0
    sizeRule = ""
    lowerEnclosures = []
    upperEnclosures = []
    spacings = []

    def __init__(self,name, width, length, size_rule):
        self.name = name
        self.width = width
        self.length = length
        self.sizeRule = size_rule
        self.lowerEnclosures = []
        self.upperEnclosures = []
        self.spacings = []

    def __str__(self):
        return f"{self.name} {self.width} {self.length} {self.sizeRule} {self.spacings}"