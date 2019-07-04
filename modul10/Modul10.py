## Nama    : Prihadina Ayunia W
## NIM     : L200170007
## Kelas   : A


import timeit
import matplotlib.pyplot as plt

#fungsi nested loop yang akan diuji:
def kalangBersusuh(n):
     for i in range(n):
         for j in range(n):
              i+j

#fungsi pengujinya:
def ujiKalangBersusuh(n):
    ls=[]
    jangkauan = range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        #print(’i =’,i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("kalangBersusuh(" + str(i) +")", setup=siap, number=1)
        ls.append(t)
    return ls

#pemanggilan pengujian
n = 1000
LS = ujiKalangBersusuh(n) #dari 1 sampai 1000.
#LS adalah list hasil uji kecepatan, dari n sedikit ke banyak

#menggambar grafik. Di bawah ini saja yang diulang saat me-nyetel skala
plt.plot(LS) #memplot hasil uji
skala = 7700000 #setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range(1,n+1)]) #grafik x^2 untuk pembanding.
plt.show() #tunjukkan plotnya
