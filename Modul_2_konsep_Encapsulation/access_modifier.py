class ProgramStudi:
    def __init__(self, kode, ketua):
        self.kode = kode              # public
        self._ketua = ketua           # protected
        self.__anggaran = 500000000   # private

    # Getter protected
    def get_ketua(self):
        return self._ketua

    # Setter protected
    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    # Getter private (wajib karena __anggaran private)
    def get_anggaran(self):
        return self.__anggaran

    # Setter private
    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        
        # Logika validasi saldo
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
            
        self.__anggaran -= jumlah
        return self.__anggaran

class Mahasiswa:
    def __init__(self, nim, nama, semester=1, ipk=0.0):
        # Public
        self.nim = nim
        self.nama = nama

        # Protected (convention)
        self._semester = semester

        # Private (name mangling)
        self.__ipk = ipk

    # Getter for private IPK
    def get_ipk(self):
        return self.__ipk

    # Setter for private IPK with validation
    def set_ipk(self, value):
        if not (0.0 <= value <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0")
        self.__ipk = round(value, 2)

    # Accessor for protected semester
    def get_semester(self):
        return self._semester

    def set_semester(self, s):
        if s < 1:
            raise ValueError("Semester tidak boleh kurang dari 1")
        self._semester = s

# Contoh penggunaan
if __name__ == "__main__":
    ps = ProgramStudi("TI", "Pak Wayan")

    print(f"Kode: {ps.kode}")
    print(f"Ketua Prodi: {ps.get_ketua()}")
    # Format angka dengan pemisah ribuan agar mudah dibaca
    print(f"Anggaran: Rp {ps.get_anggaran():,}") 

    print("-" * 20)

    # Mengubah ketua prodi
    ps.set_ketua("Bu Diah")
    print(f"Ketua Prodi (baru): {ps.get_ketua()}")

    # Mengurangi anggaran
    try:
        ps.kurangi_anggaran(100000000)
        print(f"Anggaran Tersisa: Rp {ps.get_anggaran():,}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Demo Mahasiswa ---")
    # Mahasiswa demo: nim and nama public, semester protected, ipk private
    m1 = Mahasiswa("23010", "Rina", semester=8, ipk=3.8)
    m2 = Mahasiswa("23011", "Anton", semester=7, ipk=3.4)

    for idx, m in enumerate((m1, m2), start=1):
        print(f"\nMahasiswa {idx}:")
        print(f"  NIM: {m.nim}")
        print(f"  Nama: {m.nama}")
        # Access protected (by convention) and private via getter
        print(f"  Semester: {m.get_semester()}")
        print(f"  IPK: {m.get_ipk()}")

    # Update one student's values as an example
    m1.set_ipk(3.85)
    m1.set_semester(3)
    print("\nSetelah update pada Mahasiswa 1:")
    print(f"  Semester: {m1.get_semester()}")
    print(f"  IPK: {m1.get_ipk()}")