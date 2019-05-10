#Nama : Prihadina Ayunia Wardhani
#NIM : L200170007
#Kelas : A

import re
f = open('Indonesia.txt','r', encoding='latin1')
teks3 = f.read()
f.close()
pola3 = r"di \w+"
tampilan3 = re.findall(pola3,teks3)
print(tampilan3)



