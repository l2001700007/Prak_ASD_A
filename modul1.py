#Nama  : Prihadina Ayunia Wardhani
#NIM   : L200170007
#Kelas : A
#Modul 1

#1.
for i in range (1,6) :
       print ("*" * i)

#2.
def gambarlahPersegiEmpat (x,y) :
    for i in range (x) :
        if i == 0 or i == x-1 :
            print ("@"*y)
        else :
            print ("@" + " " * (y-2) + "@")

#3.
#a.
def jumlahHurufVokal (s) :
    vok = 'aiueo'
    jumlah = 0
    for i in s :
        for z in vok:
            if i == z:
                jumlah += 1
    a = [len(s),jumlah]
    return a

#b.
def jumlahHurufKonsonan (s) :
    vok = 'aiueo'
    jumlah = 0
    for i in s :
        for z in vok:
            if i == z:
                jumlah += 1
    a = [len(s), len(s)-jumlah]
    return a

#4.
def rerata(b) :
    jumlah = 0
    for i in b :
        jumlah += i
    return jumlah/len (b)

#5.
from math import sqrt as sq
def apakahPrima (n) :
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil :
       return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n % i == 0:
                return False
            else:
                return True

#6.
def prime (x) :
    prim = True
    if x >= 2 :
        for i in range (2,x) :
            if x % i == 0 :
                prim = False
    else :
        prim = False
    return prim
    
for i in range (1,1001) :
    if prime (i):
        print (i)

#7.
def faktorPrima (x) :
    faktor = []
    loop = 2
    while loop <= x:
        if x%loop==0:
            x/=loop
            faktor.append(loop)
        else:
                loop+=1
    return faktor

#8.
def apakahTerkandung (a,b):
    if a in b:
       return True
    return False

#9.
for i in range (1,101):
    if i%3 == 0 and i%5 == 0:
        print ('Python UMS')
    elif i%3 == 0:
        print ('Python')
    elif i%5 == 0:
        print ('UMS')
    else:
        print (i)

#10.
from math import sqrt as akar
def selesaikanABC(a,b,c) :
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2-4*a*c
    if D < 0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real"
    else:
        x1 = (-b+akar(D))/(2*a)
        x2 = (-b-akar(D))/(2*a)
        hasil = (x1,x2)
        return hasil

#11.
def apakahKabisat(n):
    if (n%4==0 & n%100 == 0 & n%400 == 0):
        return True
    else :
        return False

#12.
import random
a = random.randint (0,100)
print ("Permainan tebak angka")
print ("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak")
b = -1
a = 58
while b != a :
    b = eval(input("Masukan tebakan:"))
    if b == a :
        print ("Ya.Anda Benar")
    elif b > a :
        print ("Itu terlalu besar.Coba lagi")
    else :
         print ("Itu terlalu kecil.Coba lagi")
    
#13.
angka = {1:'satu',2:'dua',3:'tiga',4:'empat',5:'lima',6:'enam',7:'tujuh',8:'delapan',9:'sembilan'}
b = ' puluh '
c = ' ratus '
d = ' ribu '
e = ' juta '
f = ' miliyar '
g = ' triliun '
def katakan (x) :
    y = str(x)
    n = len(y)
    if n <= 3 :
        if n == 1 :
            if y == '0' :
                return ''
            else :
                return angka [int(y)]
        elif n == 2:
            if y[0] == '1' :
                if y[1] == '1' :
                    return 'sebelas'
                elif y[0] == '0' :
                    x = y[1]
                    return katakan (x)
                elif y[1] == 0 :
                    return 'sepuluh'
                else :
                    return angka[int(y[1])] + ' belas'
            elif y[0] == '0' :
                x = y[1]
                return katakan(x)
            else :
                x = y[1]
                return angka [int(y[0])] + b + katakan(x)
        else :
            if y[0] == '1' :
                x = y[1:]
                return 'seratus ' + katakan (x)
            elif y[0] == '0' :
                x = y[1:]
                return katakan(x)
            else :
                x = y[1:]
                return angka [int(y[0])] + c + katakan(x)
    elif 3 < n <= 6:
        p = y[-3:]
        q = y[:-3]
        if q == '1' :
            return 'seribu' + katakan (p)
        elif q == '000' :
            return katakan (p)
        else :
            return katakan (q) + d + katakan(p)
    elif 6 < n <= 9:
        r = y[-6:]
        s = y[:-6]
        return katakan(s) + e + katakan(r)
    elif 9 < n <= 12 :
        t = y[-9:]
        u = y[:-9]
        return katakan(s) + f + katakan(t)
    else :
        v = y[-12:]
        w = y[:-12]
        return katakan(w) + g + katakan(s)
    
#14.
def formatRupiah (n):
    hasil = ""
    x = 0
    for i in str (n)[::-1]:
        if x < 3 :
            hasil += i
            x += 1
        else :
            hasil = hasil+"." +i
            x = 1
    return "Rp. " + hasil [::-1]

