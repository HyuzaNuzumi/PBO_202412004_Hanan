class Mahasiswa:
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def perkenalan_diri(self):
        print(f"Nama       : {self.nama}")
        print(f"NIM        : {self.nim}")
        print(f"Jurusan    : {self.jurusan}")
        print(f"IPK        : {self.ipk:.2f}")
        print(f"Universitas: {self.universitas}")

    def update_ipk(self, ipk_baru):
        try:
            ipk_baru = float(ipk_baru)
        except (TypeError, ValueError):
            print("Nilai IPK tidak valid.")
            return
        lama = self.ipk
        self.ipk = ipk_baru
        print(f"IPK {self.nama} diperbarui: {lama:.2f} -> {self.ipk:.2f}")

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


if __name__ == "__main__":
    # Instansiasi 3 mahasiswa dengan data berbeda
    m1 = Mahasiswa("hana", "202412004", "Teknik Informatika", 3.85)
    m2 = Mahasiswa("hanan", "202412002", "Teknik Informatika", 3.20)
    m3 = Mahasiswa("HyuzaNuzumi", "202412007", "Teknik Informatika")  # ipk default 0.0

    # Demonstrasi method perkenalan_diri dan predikat_kelulusan
    print("=== Mahasiswa 1 ===")
    m1.perkenalan_diri()
    print("Predikat:", m1.predikat_kelulusan(), end="\n\n")

    print("=== Mahasiswa 2 ===")
    m2.perkenalan_diri()
    print("Predikat:", m2.predikat_kelulusan(), end="\n\n")

    print("=== Mahasiswa 3 (sebelum update) ===")
    m3.perkenalan_diri()
    print("Predikat:", m3.predikat_kelulusan(), end="\n\n")

    # Demonstrasi update_ipk kemudian cek lagi predikat
    print("Update IPK Mahasiswa 3 menjadi 2.6")
    m3.update_ipk(2.6)
    print("=== Mahasiswa 3 (sesudah update) ===")
    m3.perkenalan_diri()
    print("Predikat:", m3.predikat_kelulusan())