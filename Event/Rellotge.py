class rellotge:
    #Constructor
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def getTime(self):
        return f"L'hore es {self.hour} els minut/s {self.minute} i el/els segon/s {self.second}"
