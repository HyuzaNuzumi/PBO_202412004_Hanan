from typing import List
from datetime import datetime, timedelta

#class Buku
class Buku:
    # attribut
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak ):
        #Public
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku

        # protected
        self._stok = stok

        # privasi
        self.__lokasi_rak = lokasi_rak
        
        # getter
        @property
        def lokasi_rak(self):
            return self.__lokasi_rak
        
        # setter
        @lokasi_rak.setter
        def lokasi_rak(self, lokasi):
            if not lokasi:
                raise ValueError("Jumlah rak tidak boleh kosong")
            self.__lokasi_rak = lokasi
        
        # tambah stok
        def tambah_stok(self, jumlah):
            if jumlah < 0:
                raise ValueError("Jumlah stok tidak boleh negatif")
            self._stok += jumlah
            print(f"Stok {self.judul} ditambah {jumlah}. Stok sekarang: {self._stok}")
        
        # kurangi stok
        def kurangi_stok(self, jumlah):
            if jumlah < 0:
                raise ValueError("Jumlah stok tidak boleh negatif")
            if jumlah > self._stok:
                raise ValueError(f"Stok tidak mencukupi. Stok tersedia: {self._stok}")
            self._stok -= jumlah
            print(f"Stok {self.judul} dikurangi {jumlah}. Stok sekarang: {self._stok}")

        # info buku
        def info_buku(self):
            return f"{self.kode_buku} | {self.judul} | {self.penulis} | Stok: {self._stok} | Lokasi: {lokasi_rak()}"
            

#class Anggota
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam, status_aktif, daftar_peminjaman):
        #Public
        self.id_anggota = id_anggota
        self.nama = nama

        #protected
        self._maks_pinjaman = maks_pinjam

        #private
        self.__status_aktif = status_aktif

        #aggregation
        self.daftar_peminjaman = List[Peminjam] = []

    # getter status
    @property
    def status(self):
        return self.status
    
    # setter
    @status.setter
    def status(self, status):
        if not isinstance(status, bool):
            raise ValueError("Status harus boolean")
        self.__status_aktif = status

    # peminjaman buku
    # relasi antar class anggota dan peminjam
    def pinjam_buku(self, buku:Buku, tanggal_pinjam = None): 
        # Cek status
        if not self.status():
            raise ValueError(f"Anggota {self.nama} tidak aktif, tidak bisa meminjam")
        
        # Cek Kouta
        if len(self.daftar_peminjaman) >= self._maks_pinjaman:
            raise ValueError(f"Anggota {self.nama} sudah mencapai batas peminjaman ({self._})Buku")
        
        # Cek tanggal pinjam
        if tanggal_pinjam is None:
            tanggal_pinjam = datetime.now()
        
        # Cek Stok
        if buku._stok <= 0:
            raise ValueError(f"Buku '{buku.judul}' tidak tersedia")
        
        # Kurangi Stok
        buku._stok(1)

        # Buat Peminjaman baru
        peminjaman = Peminjam(buku.kode_buku, tanggal_pinjam)
        self.daftar_peminjaman.append(peminjaman)

        print(f"{self.nama} meminjam '{buku.judul}'")
        return peminjaman
        
#class Peminjam
class Peminjam:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali, status):
        self.kode_buku=kode_buku
        self.tanggal_pinjam=tanggal_pinjam
        self.tanggal_kembali=tanggal_kembali
        self.status=status


    def kembalikan(self, tanggal_pengembalian):
        self.status = "Dikembalikan"
        self.tanggal_kembali_aktual = tanggal_pengembalian
    
    def info_peminjaman(self):
        info = f"Kode Buku: {self.kode_buku} | Dipinjam: {self.tanggal_pinjam.strftime('%d-%m-%Y')} | "
        info += f"Kembalikan Sebelum: {self.tanggal_kembali.strftime('%d-%m-%Y')} | Status: {self.status}"
        return info
    

# Go Program

if __name__== "__main__":
    print("=" * 45)
    print("PROGRAM OOP PERPUSTAKAAN SEDERHANA")