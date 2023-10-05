class Compte:
    def __init__(self, nom, DNI_NIE, telefon, email, quantitat_diners):
        self.nom = nom
        self.DNI_NIE = DNI_NIE
        self.telefon = telefon
        self.email = email
        self.quantitat_diners = quantitat_diners

    def mostrar_dades(self):
        print(f"Nom: {self.nom}")
        print(f"DNI o NIE {self.DNI_NIE}")
        print(f"Telèfon:{self.telefon}")
        print(f"Email:{self.email}")
        print(f"Quantitat de diners: {self.quantitat_diners}")


class Estalvi(Compte):
    def __init__(self, nom, DNI_NIE, telefon, email, quantitat_diners):
        super().__init__(nom, DNI_NIE, telefon, email, quantitat_diners)

    def mostrar_estalvis(self):
        print(f"Estalvis del client: {self.nom}")
        print(f"Quantitat de diners estalviats: {self.quantitat_diners}")


class Fixe(Compte):
    def __init__(self, nom, DNI_NIE, telefon, email, quantitat_diners, plaç, interès):
        super().__init__(nom, DNI_NIE, telefon, email, quantitat_diners)
        self.plaç = plaç
        self.interès = interès

    def calcular_interès(self):
        return self.quantitat_diners * self.interès / 100

    def mostrar_informació(self):
        print(f"Informació del compte fixe:")
        print(f"Titular: {self.nom}")
        print(f"Plaç: {self.plaç}")
        print(f"Interès: {self.interès}")
        print(f"Total: {self.quantitat_diners} {self.calcular_interès()}")


clients = []
compte_fixe = Fixe("Xavi","5677889Y", "187303254", "xavi@eiesmontsia.com", 10000, 17, 90.4)
compte_estalvi = Estalvi("Tatiana","X6984886Q", "543276547", "tatiana@iesmontsia.com", 999999)
#se utilitza generalment per a agregar elements a una llista
clients.append(compte_fixe)
clients.append(compte_estalvi)

# Función para agregar un cliente
def afegir_client():
    nom = input("Nom del client: ")
    DNI_NIE = input ("DNI o NIE del client: ")
    telefon = input("Telèfon del client: ")
    email = input("Email del client: ")
    quantitat_diners = float(input("Quantitat de diners del client: "))

    tipus_compte = input("Tipus de compte (estalvi o fixe): ")

    if tipus_compte == "estalvi":
        compte = Estalvi(nom, DNI_NIE, telefon, email, quantitat_diners)
    elif tipus_compte == "fixe":
        plaç = int(input("Plaç del compte fixe (en mesos): "))
        interès = float(input("Interès del compte fixe (%): "))
        compte = Fixe(nom, DNI_NIE, telefon, email, quantitat_diners, plaç, interès)
    else:
        print("Tipus de compte no vàlid.")
        return

    clients.append(compte)
    print("Client agregat amb èxit.")


# Función para mostrar todos los clientes
def llistar_clients():
    print("Llista de clients:")
    for compte in clients:
        print(compte.nom)


# Función para mostrar los datos de un cliente
def mostrar_dades_client(compte):
    compte.mostrar_dades()

    if isinstance(compte, Estalvi):
        compte.mostrar_estalvis()
    elif isinstance(compte, Fixe):
        compte.mostrar_informació()


# Función para buscar un cliente
def buscar_client():
    DNI_NIE = input("DNI o NIE del client: ")
    trobat = False

    for compte in clients:
        if compte.DNI_NIE == DNI_NIE:
            mostrar_dades_client(compte)
            trobat = True
            break

    if not trobat:
        print("No s'ha trobat cap client amb aquest DNI o NIE.")


# Función para editar un cliente
def editar_client():
    nom = input("Nom del client: ")
    trobat = False

    for compte in clients:
        if compte.nom == nom:
            print("Dades actuals del client:")
            mostrar_dades_client(compte)

            nou_nom = input("Nou nom del client (deixa en blanc si no vols modificar): ")
            if nou_nom != "":
                compte.nom = nou_nom

            nou_telefon = input("Nou telèfon del client (deixa en blanc si no vols modificar): ")
            if nou_telefon != "":
                compte.telefon = nou_telefon

            nou_email = input("Nou email del client (deixa en blanc si no vols modificar): ")
            if nou_email != "":
                compte.email = nou_email

            print("Dades actualitzades del client:")
            mostrar_dades_client(compte)

            trobat = True
            break

    if not trobat:
        print(f"No s'ha trobat cap client amb aquest nom.")


# Función para eliminar un cliente
def eliminar_client():
    nom = input("Nom del client: ")
    trobat = False

    for compte in clients:
        if compte.nom == nom:
            clients.remove(compte)
            print(f"Client eliminat amb èxit.")
            trobat = True
            break

    if not trobat:
        print("No s'ha trobat cap client amb aquest nom.")


while True:
    print(f"\n1. Afegir un client")
    print(f"2. Llistar clients")
    print(f"3. Mostrar les dades d'un client amb la quantitat que té a plaç fix i estalviat")
    print(f"4. Editar client")
    print(f"5. Eliminar client")
    print(f"6. Sortir")

    opcio = input("\nSelecciona una opció que vulguessiu: ")

    if opcio == "1":
        afegir_client()
        
    elif opcio == "2":
        llistar_clients()

    elif opcio == "3":
        buscar_client()

    elif opcio == "4":
        editar_client()

    elif opcio == "5":
        eliminar_client()

    elif opcio == "6":
        print("Adéu!")
        break

    else:
        print(f"Opció no vàlida. Selecciona una opció vàlida.")
