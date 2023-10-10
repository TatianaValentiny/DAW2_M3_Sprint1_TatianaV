#nom de arxiu va primer i despres el nom de la classe
from Producte import producte
from Beguda import beguda

class Aigua(producte, beguda):
    def __init__(self, nom, marca, alchol, cost, price):
        producte.__init__(self, cost, price)
        beguda.__init__(self, nom)
        self.marca = marca
        self.alchol = alchol
        
    def getDetail(self):
        return f"Nom del producte: {self.nom}\n Marca del producte: {self.marca}\n Quantitat d'alchol: {self.alchol}\n Preu producte {self.price} \n Preu final {self.cost}"
        
aigua = Aigua ("Aigua", "Solan de Cabres", 0.0, 0.25, 1.0)
print(aigua.getDetail())
print(aigua.getGain())
