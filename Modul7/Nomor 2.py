#Nama : Prihadina Ayunia Wardhani
#NIM : L200170007
#Kelas : A

import re
f = open('Indonesia.txt','r', encoding='latin1')
teks2 = f.read()
f.close()
pola2 = r"di\w+"
tampilan2 = re.findall(pola2,teks2)
print(tampilan2)


