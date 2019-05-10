#Nama : Prihadina Ayunia Wardhani
#NIM : L200170007
#Kelas : A

import re
f = open('Indonesia.txt','r', encoding='latin1')
teks = f.read()
f.close()
p=r'me\w+'
string = re.findall(p,teks)
print(string)
