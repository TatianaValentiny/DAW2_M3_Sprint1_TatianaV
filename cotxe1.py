'''
Som un concessionari i tenim stock, el stock sera el array en totes les 
marques que tenim i després vindrà el gerent i preguntara si tenim un coche especific i que 
torne el resultat si disposem de la marca o no
'''

stock = ['BMW', 'Ford', 'Cïtroen', 'Mercedes']
gerent = input ('Quina marca vols agregar? ')
gerentMayus = gerent.upper()
'''Agregar'''
stock.append(gerentMayus)
print(f"Aqui tenim tots els cotxe {stock}")


'''Eliminar'''
eliminar = input("Quina marca vols traure del stock? ")
eliminarMayus = eliminar.upper()
stock.remove(eliminarMayus)
print(f"Aqui tenim tots els cotxe {stock}")



'''Eliminar per posicio'''
while True:
    try:
        eliminarP = int (input("Quina posicio vols eliminar del stock? "))
        stock.pop(eliminarP)
        print(f"Aqui tenim tots els cotxe {stock}")
        break
    except ValueError:
            print("Te has equivocat te que ser un numero, tornau a intentar")


