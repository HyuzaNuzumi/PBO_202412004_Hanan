class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []  # List untuk menyimpan objek Mahasiswa

    def tambah_mahasiswa(self, mhs):
        # Memastikan yang ditambahkan adalah objek Mahasiswa (opsional tapi disarankan)
        if isinstance(mhs, Mahasiswa):
            self.mahasiswa.append(mhs)
        else:
            print("Error: Objek harus berupa instance dari class Mahasiswa")

    def daftar_mahasiswa(self):
        # List comprehension untuk mengambil nama dari setiap objek mahasiswa
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)

# Bagian Utama Program
if __name__ == "__main__":
    # 1. Membuat 2 objek MataKuliah
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")

    # 2. Membuat 3 objek Mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Ahmad")

    # 3. Menambahkan mahasiswa ke mata kuliah pertama (Agregasi)
    mk1.tambah_mahasiswa(m1)
    mk1.tambah_mahasiswa(m2)

    # 4. Menambahkan mahasiswa ke mata kuliah kedua (Agregasi)
    mk2.tambah_mahasiswa(m2)
    mk2.tambah_mahasiswa(m3)

    # 5. Menampilkan daftar mahasiswa mata kuliah pertama
    print(f"Mata Kuliah: {mk1.nama}")
    print(f"Daftar Mahasiswa: {mk1.daftar_mahasiswa()}")
    print(f"Jumlah Mahasiswa: {mk1.jumlah_mahasiswa()}")
    print()

    # 6. Menampilkan daftar mahasiswa mata kuliah kedua
    print(f"Mata Kuliah: {mk2.nama}")
    print(f"Daftar Mahasiswa: {mk2.daftar_mahasiswa()}")
    print(f"Jumlah Mahasiswa: {mk2.jumlah_mahasiswa()}")