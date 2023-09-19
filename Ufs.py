'''Exercici càlcul nota final M3
Demanar per consola les notes de les 3 UFS i retornar la nota final

UF4 50%
UF5 25%
UF6 25%

M3 = not_uf4 * 0,5 + nota_uf5 * 0,25 + nota_uf6 * 0,25
'''

    
def nota(ufs):
    while True:
        try:
            nota = float(input(ufs))
            return nota
        except ValueError:
            print("Te has equivocat te que ser un numero, tornau a intentar")

uf4 = nota("Nota UF4 es: ")
uf4M = uf4 * 0.5

uf5 = nota("Nota UF5 es: ")
uf5M = uf5 * 0.25

uf6 = nota("Nota UF6 es: ")
uf6M = uf6 * 0.25

NotaF = uf4M + uf5M + uf6M

print(f"La nota final es: {NotaF}")
print("Final")


    

