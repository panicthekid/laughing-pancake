#definimos una variable para el texto a cifrar
cod = "dor"
#verificamos si el texto esta en mayusculas o minulaculas
#y asignamos un alfabeto

if cod==cod.upper():
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    alf = "abcdefghijklmnopqrstuvwxyz"

#creamos una cadena para guardar el texto cifrado
cifFinal= ""
k=3
for c in cod:
    if c in alf:
        cifFinal+=alf[(alf.index(c)+k)%(len(alf))] #
    else:
            cifFinal+=c
print("El texto cifrado es: {}".format(cifFinal))
print("\n")

