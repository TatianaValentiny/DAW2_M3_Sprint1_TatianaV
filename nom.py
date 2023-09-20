
'''
(els que vulgue) i imprimiu per pantalla
Les seves Keys i els seus values per separat
Imprimiu el valor d'una key en concret, per exemple name'''

stock = {'name':'tatiana','edat':20, 'sexe':'no','drets':False, 'Telefon': 45678}

print(stock.values())
print(stock["sexe"])
stock['sexe'] = "si"
print(stock["sexe"])