#definimos una variable para el texto a cifrar
#se puede pedir el texto a cifrar al usuario
cod = "dor"
#verificamos si el texto esta en mayusculas o minulaculas
#y asignamos un alfabeto

if cod==cod.upper():
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    alf = "abcdefghijklmnopqrstuvwxyz"

#creamos una cadena para guardar el texto cifrado
cifFinal= ""
for i in range (26):
    for c in cod:
        if c in alf:
            cifFinal+=alf[(alf.index(c)-i)%(len(alf))] #
        else:
                cifFinal+=c
    print("El texto cifrado es: {} con k: {}".format(cifFinal,i))
    print("\n")
    cifFinal=""

