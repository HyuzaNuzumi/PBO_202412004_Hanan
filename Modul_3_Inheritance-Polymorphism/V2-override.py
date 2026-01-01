import math

# Kriteria a: Class Bentuk dengan method luas() yang mengembalikan 0
class Bentuk:
    def luas(self):
        return 0

# Kriteria b: Class Persegi meng-override method luas()
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        # Rumus luas persegi: sisi * sisi
        return self.sisi * self.sisi

# Kriteria b: Class Lingkaran meng-override method luas()
class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        # Rumus luas lingkaran: pi * r^2
        return math.pi * (self.jari_jari ** 2)

# Kriteria c: Demonstrasi pemanggilan method luas()
bentuk_dasar = Bentuk()
kotak = Persegi(5)        # Persegi dengan sisi 5
piring = Lingkaran(7)     # Lingkaran dengan jari-jari 7

# Menyimpan objek dalam list untuk menunjukkan polymorphism
daftar_bentuk = [bentuk_dasar, kotak, piring]

print("--- Hasil Luas ---")
for b in daftar_bentuk:
    # Memanggil method yang sama (luas), tapi hasilnya berbeda (Polymorphism)
    print(f"Luas {type(b).__name__}: {b.luas():.2f}")
    