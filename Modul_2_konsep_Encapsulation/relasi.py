from typing import List

# 1. Class Nilai (Objek independen)
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

# 2. Class MataKuliah
class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama

# 3. Class Mahasiswa (Agregasi dengan Nilai)
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        # Agregasi: Mahasiswa punya daftar nilai, tapi Nilai adalah objek terpisah
        self.daftar_nilai: List[Nilai] = [] 

    def tambah_nilai(self, nilai: Nilai):
        self.daftar_nilai.append(nilai)
    
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        total = sum(n.skor for n in self.daftar_nilai)
        return total / len(self.daftar_nilai)

# 4. Class ProgramStudi (Agregasi dengan MataKuliah)
class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        # Agregasi: Prodi menampung referensi ke objek MataKuliah
        self.daftar_matakuliah: List[MataKuliah] = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)

# 5. Class Universitas (Composition dengan ProgramStudi)
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs: List[ProgramStudi] = []

    def buat_program(self, nama_prodi):
        # Composition: Objek ProgramStudi dibuat DI DALAM Universitas
        # Jika Universitas hancur, ProgramStudi ini juga dianggap hilang konteksnya
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

# Fungsi Laporan (Helper Function)
def report_program(prodi: ProgramStudi, semua_mahasiswa: List[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")
    
    # List comprehension untuk mengambil kode MK
    daftar_kode = [mk.kode for mk in prodi.daftar_matakuliah]
    print("Matakuliah:", ", ".join(daftar_kode) or "-")
    
    print("Mahasiswa dan rata-rata nilai:")
    for m in semua_mahasiswa:
        # Filter nilai: Hanya ambil nilai untuk matakuliah di prodi ini
        nilai_relevan = [n.skor for n in m.daftar_nilai if n.kode_mk in daftar_kode]
        if nilai_relevan:
            rata_rata = sum(nilai_relevan) / len(nilai_relevan)
            print(f" - {m.nama} (NIM: {m.nim}): {rata_rata:.2f}")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat Universitas
    univ = Universitas("Universitas Teknologi")
    
    # Membuat 2 Program Studi baru
    prodi_ti = univ.buat_program("Teknik Informatika")
    prodi_ak = univ.buat_program("Akuntansi")
    
    # Menampilkan Program Studi yang telah dibuat
    print(f"Universitas: {univ.nama}")
    print(f"Jumlah Program Studi: {len(univ.programs)}")
    print("Daftar Program Studi:")
    for prodi in univ.programs:
        print(f"  - {prodi.nama}")
    
    print("\n" + "-" * 40)
    
    # Tambah Mata Kuliah ke Teknik Informatika (minimal 2)
    print("\nTambah Mata Kuliah pada Teknik Informatika:")
    mk_ti1 = MataKuliah("PBO101", "Pemrograman Berorientasi Objek")
    mk_ti2 = MataKuliah("BD101", "Basis Data")
    mk_ti3 = MataKuliah("WEB101", "Pengembangan Web")
    
    prodi_ti.tambah_matakuliah(mk_ti1)
    prodi_ti.tambah_matakuliah(mk_ti2)
    prodi_ti.tambah_matakuliah(mk_ti3)
    
    for mk in prodi_ti.daftar_matakuliah:
        print(f"  - {mk.kode}: {mk.nama}")
    
    # Tambah Mata Kuliah ke Akuntansi (minimal 2)
    print("\nTambah Mata Kuliah pada Akuntansi:")
    mk_ak1 = MataKuliah("AK101", "Akuntansi Dasar")
    mk_ak2 = MataKuliah("AK201", "Akuntansi Manajemen")
    
    prodi_ak.tambah_matakuliah(mk_ak1)
    prodi_ak.tambah_matakuliah(mk_ak2)
    
    for mk in prodi_ak.daftar_matakuliah:
        print(f"  - {mk.kode}: {mk.nama}")
    
    print("\n" + "-" * 40)
    
    # Buat 3 Mahasiswa
    print("\nBuat 3 Mahasiswa:")
    m1 = Mahasiswa("23001", "Budi Santoso")
    m2 = Mahasiswa("23002", "Siti Nurhaliza")
    m3 = Mahasiswa("23003", "Ahmad Wijaya")
    
    daftar_mahasiswa = [m1, m2, m3]
    for m in daftar_mahasiswa:
        print(f"  - {m.nim}: {m.nama}")
    
    print("\n" + "-" * 40)
    
    # Buat objek Nilai dan tambahkan ke Mahasiswa
    print("\nTambah Nilai ke Mahasiswa:")
    
    # Mahasiswa 1 (Budi) - ambil nilai dari TI
    print(f"\nMahasiswa: {m1.nama}")
    n1_1 = Nilai("PBO101", 85.0)
    n1_2 = Nilai("BD101", 78.5)
    n1_3 = Nilai("WEB101", 88.0)
    
    m1.tambah_nilai(n1_1)
    m1.tambah_nilai(n1_2)
    m1.tambah_nilai(n1_3)
    print(f"  Nilai ditambahkan: {[(n.kode_mk, n.skor) for n in m1.daftar_nilai]}")
    
    # Mahasiswa 2 (Siti) - ambil nilai dari TI dan Akuntansi
    print(f"\nMahasiswa: {m2.nama}")
    n2_1 = Nilai("PBO101", 92.0)
    n2_2 = Nilai("AK101", 88.5)
    n2_3 = Nilai("AK201", 85.0)
    
    m2.tambah_nilai(n2_1)
    m2.tambah_nilai(n2_2)
    m2.tambah_nilai(n2_3)
    print(f"  Nilai ditambahkan: {[(n.kode_mk, n.skor) for n in m2.daftar_nilai]}")
    
    # Mahasiswa 3 (Ahmad) - ambil nilai dari Akuntansi
    print(f"\nMahasiswa: {m3.nama}")
    n3_1 = Nilai("AK101", 80.0)
    n3_2 = Nilai("AK201", 82.5)
    n3_3 = Nilai("BD101", 75.0)
    
    m3.tambah_nilai(n3_1)
    m3.tambah_nilai(n3_2)
    m3.tambah_nilai(n3_3)
    print(f"  Nilai ditambahkan: {[(n.kode_mk, n.skor) for n in m3.daftar_nilai]}")
    
    print("\n" + "-" * 40)
    
    # Tampilkan rata-rata nilai setiap mahasiswa
    print("\nRata-rata Nilai Setiap Mahasiswa:")
    for m in daftar_mahasiswa:
        rata_rata = m.rata_rata()
        print(f"  {m.nama} ({m.nim}): {rata_rata:.2f}")
    
    print("\n" + "=" * 40)
    
    # Panggil fungsi report_program untuk setiap Program Studi
    print("\nLAPORAN PROGRAM STUDI")
    print("=" * 40)
    
    report_program(prodi_ti, daftar_mahasiswa)
    
    print("\n" + "-" * 40)
    
    report_program(prodi_ak, daftar_mahasiswa)