class Via:
    name = " "
    width = 0.0
    length = 0.0
    size_rule = ""
    lower_enclosure = []
    upper_enclosure = []
    spacings = []

    def __init__(self,name, width, length, size_rule):
        self.name = name
        self.width = width
        self.length = length
        self.size_rule = size_rule
        self.lower_enclosure = []
        self.upper_enclosure = []
        self.spacings = []

    def __str__(self):
        return f"{self.name} {self.width} {self.length} {self.size_rule} {self.spacings}"