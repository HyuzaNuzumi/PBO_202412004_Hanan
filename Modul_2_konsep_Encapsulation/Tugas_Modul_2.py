from typing import List
from datetime import datetime, timedelta

# 1. Class Buku
class Buku:
    def __init__(self, kode_buku, judul, penulis, stok=5, lokasi_rak="A1"):
        # Public attributes
        self.kode_buku = kode_buku
        self.judul = judul
        self.penulis = penulis
        
        # Protected attribute
        self._stok = stok
        
        # Private attribute
        self.__lokasi_rak = lokasi_rak
    
    # Getter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak
    
    # Setter lokasi rak
    def set_lokasi_rak(self, lokasi):
        if not lokasi:
            raise ValueError("Lokasi rak tidak boleh kosong")
        self.__lokasi_rak = lokasi
    
    # Tambah stok
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah stok tidak boleh negatif")
        self._stok += jumlah
        print(f"Stok {self.judul} ditambah {jumlah}. Stok sekarang: {self._stok}")
    
    # Kurangi stok
    def kurangi_stok(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah stok tidak boleh negatif")
        if jumlah > self._stok:
            raise ValueError(f"Stok tidak mencukupi. Stok tersedia: {self._stok}")
        self._stok -= jumlah
        print(f"Stok {self.judul} dikurangi {jumlah}. Stok sekarang: {self._stok}")
    
    def info_buku(self):
        return f"{self.kode_buku} | {self.judul} | {self.penulis} | Stok: {self._stok} | Lokasi: {self.get_lokasi_rak()}"


# 2. Class Peminjaman
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, durasi_hari=7):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_pinjam + timedelta(days=durasi_hari)
        self.status = "Dipinjam"
    
    def kembalikan(self, tanggal_pengembalian):
        self.status = "Dikembalikan"
        self.tanggal_kembali_aktual = tanggal_pengembalian
    
    def info_peminjaman(self):
        info = f"Kode Buku: {self.kode_buku} | Dipinjam: {self.tanggal_pinjam.strftime('%d-%m-%Y')} | "
        info += f"Kembali Sebelum: {self.tanggal_kembali.strftime('%d-%m-%Y')} | Status: {self.status}"
        return info


# 3. Class Anggota
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        # Public attributes
        self.id_anggota = id_anggota
        self.nama = nama
        
        # Protected attribute
        self._maks_pinjam = maks_pinjam
        
        # Private attribute
        self.__status_aktif = True
        
        # Aggregation: daftar peminjaman
        self.daftar_peminjaman: List[Peminjaman] = []
    
    # Getter status aktif
    def get_status_aktif(self):
        return self.__status_aktif
    
    # Setter status aktif
    def set_status_aktif(self, status):
        if not isinstance(status, bool):
            raise ValueError("Status harus boolean")
        self.__status_aktif = status
    
    # Pinjam buku
    def pinjam_buku(self, buku: Buku, tanggal_pinjam=None):
        if not self.get_status_aktif():
            raise ValueError(f"Anggota {self.nama} tidak aktif, tidak bisa meminjam")
        
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            raise ValueError(f"Anggota {self.nama} sudah mencapai batas peminjaman ({self._maks_pinjam} buku)")
        
        if buku._stok <= 0:
            raise ValueError(f"Buku '{buku.judul}' tidak tersedia")
        
        if tanggal_pinjam is None:
            tanggal_pinjam = datetime.now()
        
        # Kurangi stok buku
        buku.kurangi_stok(1)
        
        # Buat peminjaman baru
        peminjaman = Peminjaman(buku.kode_buku, tanggal_pinjam)
        self.daftar_peminjaman.append(peminjaman)
        
        print(f"{self.nama} meminjam '{buku.judul}'")
        return peminjaman
    
    # Kembalikan buku
    def kembalikan_buku(self, kode_buku, buku: Buku, tanggal_kembali=None):
        if tanggal_kembali is None:
            tanggal_kembali = datetime.now()
        
        # Cari peminjaman yang belum dikembalikan
        peminjaman_ditemukan = None
        for peminjaman in self.daftar_peminjaman:
            if peminjaman.kode_buku == kode_buku and peminjaman.status == "Dipinjam":
                peminjaman_ditemukan = peminjaman
                break
        
        if peminjaman_ditemukan is None:
            raise ValueError(f"Peminjaman dengan kode buku {kode_buku} tidak ditemukan atau sudah dikembalikan")
        
        # Kembalikan buku
        peminjaman_ditemukan.kembalikan(tanggal_kembali)
        buku.tambah_stok(1)
        
        print(f"{self.nama} mengembalikan '{buku.judul}'")
    
    def info_anggota(self):
        status = "Aktif" if self.get_status_aktif() else "Tidak Aktif"
        return f"{self.id_anggota} | {self.nama} | Status: {status} | Maks Pinjam: {self._maks_pinjam}"


# 4. Class Perpustakaan (Composition)
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku: List[Buku] = []
        self.daftar_anggota: List[Anggota] = []
    
    def tambah_buku(self, buku: Buku):
        self.daftar_buku.append(buku)
    
    def tambah_anggota(self, anggota: Anggota):
        self.daftar_anggota.append(anggota)
    
    def cari_buku(self, kode_buku):
        for buku in self.daftar_buku:
            if buku.kode_buku == kode_buku:
                return buku
        return None


# ============ DEMONSTRASI PROGRAM ============

if __name__ == "__main__":
    print("=" * 60)
    print("SISTEM MANAJEMEN PERPUSTAKAAN SEDERHANA")
    print("=" * 60)
    
    # 1. Buat Perpustakaan
    perpus = Perpustakaan("Perpustakaan Teknologi")
    
    # 2. Buat 3 Buku
    print("\n--- BUAT 3 BUKU ---")
    buku1 = Buku("BK001", "Pemrograman Python", "Guido van Rossum", stok=5, lokasi_rak="A1")
    buku2 = Buku("BK002", "Database SQL", "Blaha Michael", stok=3, lokasi_rak="A2")
    buku3 = Buku("BK003", "Web Development", "Jon Duckett", stok=4, lokasi_rak="B1")
    
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)
    perpus.tambah_buku(buku3)
    
    print("\n--- INFORMASI BUKU DAN STOKNYA ---")
    for buku in perpus.daftar_buku:
        print(f"  {buku.info_buku()}")
    
    # 3. Buat 2 Anggota
    print("\n--- BUAT 2 ANGGOTA ---")
    anggota1 = Anggota("A001", "Budi Santoso", maks_pinjam=3)
    anggota2 = Anggota("A002", "Siti Nurhaliza", maks_pinjam=2)
    
    perpus.tambah_anggota(anggota1)
    perpus.tambah_anggota(anggota2)
    
    print("\n--- INFORMASI ANGGOTA ---")
    for anggota in perpus.daftar_anggota:
        print(f"  {anggota.info_anggota()}")
    
    # 4. Anggota 1 pinjam 2 buku
    print("\n--- PROSES PEMINJAMAN ---")
    print("\nAnggota 1 meminjam 2 buku:")
    peminjaman1_1 = anggota1.pinjam_buku(buku1)
    peminjaman1_2 = anggota1.pinjam_buku(buku2)
    
    # 5. Anggota 2 pinjam 1 buku
    print("\nAnggota 2 meminjam 1 buku:")
    peminjaman2_1 = anggota2.pinjam_buku(buku3)
    
    # 6. Stok buku setelah peminjaman
    print("\n--- INFORMASI BUKU SETELAH PEMINJAMAN ---")
    for buku in perpus.daftar_buku:
        print(f"  {buku.info_buku()}")
    
    # 7. Tampilkan daftar peminjaman masing-masing anggota
    print("\n--- DAFTAR PEMINJAMAN MASING-MASING ANGGOTA ---")
    for anggota in perpus.daftar_anggota:
        print(f"\n{anggota.nama}:")
        if anggota.daftar_peminjaman:
            for peminjaman in anggota.daftar_peminjaman:
                print(f"  • {peminjaman.info_peminjaman()}")
        else:
            print("  (Tidak ada peminjaman)")
    
    # 8. Pengembalian buku
    print("\n--- PROSES PENGEMBALIAN BUKU ---")
    print("\nAnggota 1 mengembalikan buku:")
    anggota1.kembalikan_buku(buku1.kode_buku, buku1)
    
    print("\nAnggota 2 mengembalikan buku:")
    anggota2.kembalikan_buku(buku3.kode_buku, buku3)
    
    # 9. Stok buku setelah pengembalian
    print("\n--- INFORMASI BUKU SETELAH PENGEMBALIAN ---")
    for buku in perpus.daftar_buku:
        print(f"  {buku.info_buku()}")
    
    # 10. Tampilkan daftar peminjaman terbaru
    print("\n--- DAFTAR PEMINJAMAN TERBARU ---")
    for anggota in perpus.daftar_anggota:
        print(f"\n{anggota.nama}:")
        if anggota.daftar_peminjaman:
            for peminjaman in anggota.daftar_peminjaman:
                print(f"  • {peminjaman.info_peminjaman()}")
        else:
            print("  (Tidak ada peminjaman)")
    
    print("\n" + "=" * 60)
    print("PROGRAM SELESAI")
    print("=" * 60)
