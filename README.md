# laughing-pancake
Pyhton code for Cesar cipher with and withoout key.

File cesar.py is for cipher the plain text, for deschipher knowing the key just change this line:
cifFinal+=alf[(alf.index(c)+k)%(len(alf))]
for this:
cifFinal+=alf[(alf.index(c)-k)%(len(alf))]

File cesarWhitoutK.py is for decipher coded text into plain text without knowing the key.
