class Person:
    # Kriteria b: Class Person dengan atribut nama dan umur
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Person: {self.nama}, Umur: {self.umur} tahun"

class Mahasiswa(Person):
    # Kriteria c: Class Mahasiswa mewarisi Person, tambah atribut nim
    def __init__(self, nama, umur, nim):
        # Kriteria d: Gunakan super() untuk inisialisasi dari parent class
        super().__init__(nama, umur)
        self.nim = nim

    # Override method info untuk menampilkan detail mahasiswa
    def info(self):
        return f"Mahasiswa: {self.nama}, NIM: {self.nim}, Umur: {self.umur} tahun"

# Kriteria e: Instansiasi objek dan panggil method info()
orang = Person("Hanan", 20)
mahasiswa = Mahasiswa("Hana", 20, "202412004")

print(orang.info())
print(mahasiswa.info())