from xml.dom import NoModificationAllowedErr


class Resistor:
    def __init__(self, type, nom, power, accuracy):
        self.type = type
        self.nom = nom
        self.power = power
        self.accuracy = accuracy


    def show(self):
        print(f"type - {self.type};  nominal - {self.nom} Om;   power - {self.power} W;   accuracy - {self.accuracy} %")
  