class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def info(self):
        return f"{self.nama} (Nim: {self.nim}) - IPK: {self.ipk}"

# class Buku:
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun})"


daftar_buku = [
    Buku('Hantu', 'hana', '2020'),
    Buku('Yonko', 'hanan', '2021'),
    Buku('Momo', 'Nan', '2022'),
    Buku('Night Hunter', 'hyuza', '2024'),
    Buku('The Great Adventure', 'nuzumi', '2025'),
]


# megakses list of objects
print("\n === Daftar Buku ===")
for buku in daftar_buku:
    print(buku.info())

# filter buku dicari 
print ('\n=== Pencarian Buku ===')
cari = input('Masukkan Nama penulis yang dicari: ')

print (f"\nSedang mencari buku karya '{cari}'....")

#proses pencarian 
hasil_pencarian = []

for buku in daftar_buku:
    if cari.lower() in buku.penulis.lower():
        hasil_pencarian.append(buku)

if not hasil_pencarian:
    print(f"X Tidak ada buku dari penulis '{cari}'")
else:
    print(f'\nDitemukan {len(hasil_pencarian)} buku:')
    for hasil in hasil_pencarian:
        print(f'-{hasil.info()}')
        

# Membuat list of objects
daftar_mahasiswa = [
    Mahasiswa('Hana', 'IT001', 3.5),
    Mahasiswa('Hanan', 'IT002', 3.7),
    Mahasiswa('Nan', 'IT003', 4.0),
]

# Mengakses list of objects
print("\n=== Mahasiswa dengan IPK > 3.5 ===")
for mhs in daftar_mahasiswa:
    print(mhs.info())

# Filter berdasarkan IPk
print("\n=== Mahasiswa dengan IPK > 3.5 ===")
for mhs in daftar_mahasiswa:
    if mhs.ipk > 3.5:
        print(mhs.info())