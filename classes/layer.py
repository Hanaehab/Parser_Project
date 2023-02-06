class Layer:
    vias = []
    name = " "

    def __init__(self, name):
        self.name = name
        self.vias = []

    def __str__(self):
        return f"{self.name} {self.vias}"