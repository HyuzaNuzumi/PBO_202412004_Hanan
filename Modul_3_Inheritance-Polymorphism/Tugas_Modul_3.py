# class Karyawan
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def info_gaji(self):
        return f"Karyawan: {self.nama}, Gaji: {self.gaji}"

# class Manager
class Manager(Karyawan):
    def __init__(self, nama, gaji, tunjangan):
        # Gunakan super() untuk inisialisasi dari parent class
        super().__init__(nama, gaji)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total_gaji = self.gaji + self.tunjangan
        return f"Manager: {self.nama}, Gaji: {total_gaji} (Gaji Pokok: {self.gaji} + Tunjangan: {self.tunjangan})"

# class programer
class programer(Karyawan):
    def __init__(self, nama, gaji, bonus):
        # Gunakan super() untuk inisialisasi dari parent class
        super().__init__(nama, gaji)
        self.bonus = bonus
    
    def info_gaji(self):
        gaji_total = self.gaji + self.bonus
        return f"Programer: {self.nama}, Gaji: {gaji_total} (Gaji Pokok: {self.gaji} + Bonus: {self.bonus})"

# Compositon
class Departemen:
    def __init__(self, nama_departemen, karyawan):
        self.nama_departemen = nama_departemen
        self.karyawan = karyawan  # Objek Karyawan disimpan di sini

    def tambah_karyawan(self, karyawan_baru):
        self.karyawan.append(karyawan_baru)

    def tampilkan_karyawan(self):
        for k in self.karyawan:
            print(k.info_gaji())


#instansiasi
Manager_1 = Manager("Hyuza", 8000000, 2000000)
Manager_2 = Manager("Nuzumi", 8500000, 2500000)
programer_1 = programer("Hana", 6000000, 1500000)
programer_2 = programer("Hanan", 6200000, 1200000)

# Tambahkan ke dalam departemen
departemen_it = Departemen("IT", [Manager_1, Manager_2, programer_1, programer_2])

# Tampilkan info gaji semua karyawan
departemen_it.tampilkan_karyawan()
