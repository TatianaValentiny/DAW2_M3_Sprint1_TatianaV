'''
Som un concessionari i tenim stock, el stock sera el array en totes les 
marques que tenim i després vindrà el gerent i preguntara si tenim un coche especific i que 
torne el resultat si disposem de la marca o no
'''

stock = ['BMW', 'Ford', 'Cïtroen', 'Mercedes']
gerent = input ('Quina marca vols?')
gerentMayus = gerent.upper()

if gerentMayus in stock:
    print('Si tenim aquesta marca')
    
else:
    print('No tenim aquesta marca')
    
