class calendari:
    #Constructor
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def getDate(self):
        return f"Avui estem al dia {self.day} al mes {self.month} l'any {self.year}"
