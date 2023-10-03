class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.abilities = []

    def add_ability(self, ability):
        #se utilitza generalment per a agregar elements a una llista
        self.abilities.append(ability)

    def info(self):
        return f"{self.firstname} {self.lastname}."


class Candidate(Person):
    def __init__(self, firstname, lastname, gender):
        super().__init__(firstname, lastname)
        self.gender = gender

    def info(self):
        if self.gender == "male":
            return(f"He is {Person.info(self)}")
        elif self.gender == "female":
            return(f"She is {Person.info(self)}")


c1 = Candidate('Manel', 'Cantells', 'male')
c1.add_ability('JavaScript')
c1.add_ability('Python')
c2 = Candidate('Maria', 'Gironés', 'female')
c2.add_ability('PHP')

#array
print(c1.info())
print(c1.abilities)
print(c2.info())
print(c2.abilities)
