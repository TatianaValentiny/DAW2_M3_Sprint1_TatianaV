class Dad:
    def __init__(self, name, firstname="Valentiny", lastname="Garaj"):
        #si fiquem __algo sira un atribut privat
        self.__firstname = firstname
        self.__lastname = lastname
        self.__name = name
        
    def getDadFirstName(self):
        return self.__firstname 
    
    def getDadFullName(self):
        return(f"El nom complet del meu pare és {self.__name} {self.__firstname} {self.__lastname}")
        

class Mom:
    def __init__(self, name, firstname ="Kufelova", lastname="Valentinyova"):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__name = name
    
    def getMomFirstName(self):
        return self.__firstname 
    
    def getMomFullName(self):
        return(f"El nom complet del meu mare és {self.__name} {self.__firstname} {self.__lastname}")
        
        
class Child (Dad, Mom):
    def __init__(self, name):
        self.__name = name
        Dad.__init__(self, "Vladislav")
        Mom.__init__(self,"Tatiana")
        
    def getFullName(self):
        return(f"El nom complet no complert és {self.__name} {Dad.getDadFirstName(self)} {Mom.getMomFirstName(self)}")

        
child = Child("Tatiana")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())
       

 
