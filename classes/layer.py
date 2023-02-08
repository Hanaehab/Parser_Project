class Layer:
    vias = [] # List of "via" objects
    name = "" # Name of the layer

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} {self.vias}"