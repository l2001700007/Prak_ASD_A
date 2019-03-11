#Nama  : Prihadina Ayunia Wardhani
#NIM   : L200170007
#Kelas : A
#Modul 2

class Pesan(object) :
    """Sebuah kelas bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
#1.a
    def apakahTerkandung (self,a):
        if a in self.teks:
            return True
        return False
#1.b
    def hitungKonsonan (self):
        x = "bcdfghjklmnpqrstvwqyzBCDFGHJKLMNPQRSTVWXYZ"
        Ko = 0
        for i in self.teks:
            if i in x :
                Ko += 1
        return Ko
#1.c
    def hitungVokal(self):
        x = "aiueoAIUEO"
        Vo = 0
        for i in self.teks:
            if i in x :
                Vo += 1
        return Vo

class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama +', NIM ' + str(self.NIM)\
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + ' tiap bulannya.' 
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
#2.a
    def ambilkotaTinggal(self):
        return self.kotaTinggal
#2.b
    def perbaruiKotaTinggal (self, kotatinggalbaru):
        self.kotaTinggal = kotatinggalbaru
#2.c
    def tambahUangSaku(self, tambah):
        return self.uangSaku + tambah
#4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
#5
    def hapusKuliah(self, hapuslah):
        self.listKuliah.remove(hapuslah)
        
m1 = Mahasiswa ('Jamil', 234, 'Surakarta', 250000 )
#3
print("\nNomer 3")
print("Silahkan Masukkan Data Mahasiswa Di bawah Ini :")
a = input ('Nama :')
b = input ('NIM :')
c = input ('Kota Tinggal :')
d = input ('Uang Saku :')
x = Mahasiswa (a,b,c,d)

#6
class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, uangJajan, alamat):
        self.nama = nama
        self.nis = NIS
        self.uangJajan = uangJajan
        self.alamat = alamat
    def __str__(self):
        s = "Nama : " + str(self.nama) \
            + "NIS : " + str(self.nis) \
            + "Alamat : " + str(self.alamat)\
            + "Uang Jajan : " + str(self.uangJajan)
        return s

