'''Exercici càlcul nota final M3
Demanar per consola les notes de les 3 UFS i retornar la nota final

UF4 50%
UF5 25%
UF6 25%

M3 = not_uf4 * 0,5 + nota_uf5 * 0,25 + nota_uf6 * 0,25
'''

uf4 = int(input("Nota UF4: "))
uf4M = int(uf4 * 0.5)

uf5 = int(input("Nota UF5: "))
uf5M = int(uf5 * 0.25)

uf6 = int(input("Nota UF6: "))
uf6M = int(uf6 * 0.25)

NotaF = (uf4M + uf5M + uf6M)

print (f"La nota final es: {NotaF}")

    

