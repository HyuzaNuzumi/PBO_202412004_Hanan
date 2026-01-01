# Kriteria a: Class Penulis dengan atribut nama
class Penulis:
    def __init__(self, nama):
        self.nama = nama

    def info_penulis(self):
        return self.nama

# Kriteria b: Class Buku yang memiliki Penulis (Composition)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # Objek Penulis disimpan di sini

    def info_buku(self):
        # Mengakses atribut 'nama' milik objek penulis dari dalam class Buku
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"

# Kriteria c: Demonstrasi cara mengakses data penulis dari objek buku
# 1. Membuat objek Penulis terlebih dahulu
penulis_1 = Penulis("Hyuza Nuzumi")

# 2. Memasukkan objek Penulis ke dalam objek Buku
buku_1 = Buku("Death Note", penulis_1)

# 3. Menampilkan hasil
print(buku_1.info_buku())

# Cara akses langsung dari luar class (opsional untuk pemahaman):
print(f"Akses manual: {buku_1.penulis.nama}")