#Nama  : Prihadina Ayunia Wardhani
#NIM   : L200170007
#Kelas : A
#Modul 2 (lanjutan)

import modul2          # Atau apapun file-nya yang kamu buat tadi

class MhsTIF(modul2.Mahasiswa):    # perhatikan class induknya : Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')

# Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?

# Jawab :
# Metoode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
# Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi
# semua properties dari Mahasiswa dan Manusia.
