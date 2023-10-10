#Importar les classes de unaltre fitxer 
from Calendari import calendari
from Rellotge import rellotge
class Event(calendari, rellotge):
    def __init__(self, day, month, year, hour, minute, second):
        calendari.__init__(self, day, month, year)
        rellotge.__init__(self, hour, minute, second)
        
    def getDate(self):
        return calendari.getDate(self)
    def getHour(self):
        return rellotge.getTime(self)


event = Event(10, 10, 2023, 15, 30, 45)
print(event.getDate())
print(event.getTime())
