class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def info(self):
        return f"{self.nama} (Nim: {self.nim}) - IPK: {self.ipk}"

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