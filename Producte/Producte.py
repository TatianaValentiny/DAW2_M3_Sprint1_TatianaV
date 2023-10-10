class producte:
    #Constructor
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price
        
    def getGain(self):
        return f"La ganancia {self.price - self.cost} €"
