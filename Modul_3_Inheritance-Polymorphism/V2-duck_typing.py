# Kriteria a: Dua class berbeda (Laptop, Smartphone) dengan method nyalakan()
class Laptop:
    def nyalakan(self):
        return "Laptop booting... Masuk ke Desktop."

class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala... Logo Android muncul."

# Kriteria b: Buat fungsi tes_nyala(obj) yang memanggil method nyalakan()
def tes_nyala(obj):
    # Fungsi ini tidak peduli obj itu Laptop atau Smartphone,
    # asalkan objek tersebut punya method 'nyalakan'
    print(obj.nyalakan())

# Kriteria c: Demonstrasi Duck Typing
perangkat1 = Laptop()
perangkat2 = Smartphone()

print("--- Hasil Tes Nyala ---")
tes_nyala(perangkat1)  # Output untuk Laptop
tes_nyala(perangkat2)  # Output untuk Smartphone