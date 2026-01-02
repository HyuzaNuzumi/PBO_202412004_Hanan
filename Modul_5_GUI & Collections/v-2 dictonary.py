class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode 
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp {self.harga: ,}"

class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f'{self.id_pelanggan} - {self.nama} - {self.email}'

status_pelanggan = {
    'X-01': Pelanggan('X-01', 'HyuzaNuzumi', 'linglegendstwo@gmail.com'),
    'X-02': Pelanggan('X-02', 'HyuzaNozumi', 'linglegendsone@gmail.com'),
    'X-03': Pelanggan('X-03', 'HikariYuzuko', 'linglegendstree@gmail.com'),
    'X-04': Pelanggan('X-04', 'HyuzaNuzumi', 'linglegendsfor@gmail.com')
}

# Mengakses dictinory of objects
print('=== Status Pelanggan ===')
for pelanggan in status_pelanggan.items():
    print(f"{pelanggan}")

    l
# Menambahkan
print('\n=== Tambahkan ===')
id_baru = input("Masukkan ID: ")
nama_baru = input('Masukkan Nama: ')
email_baru = input('Masukkan Email: ')

#Proses Penyimpanan
status_pelanggan[id_baru] = Pelanggan(id_baru, nama_baru, email_baru)
print('>>> Berhasil ditambahkan')


#mencari
print ('\n === Pencarian Pelanggan ===')
cari = input ('Masukkan ID Pelanggan yang dicari: ')

print (f"\nSedang mencari buku karya '{cari}'...")

#proses pencarian

hasil_pencarian = []

#Proses pencarian
for pelanggan in status_pelanggan:
    if cari.lower in pelanggan.id_pelanggan.lower():
        hasil_pencarian.append(pelanggan)

if not hasil_pencarian:
    print(f"ID Pelanggan Tidak ditemukan '{cari}'")
else:
    print(f'\nDitemukan {len(hasil_pencarian)} Pelanggan:')
    for hasil in hasil_pencarian:
        print(f'-{hasil.info()}')

# Delete

print("\n=== Menghapus ====")
id_hapus = input('Masukkan ID yang akan di hapus: ')

#Pengecekan
if id_hapus in status_pelanggan:
    del status_pelanggan[id_hapus]
    print(f'>>> Data dengan ID {id_hapus} Berhasil di hapus')
else:
    print(f'>>> ID tidak ditemukan!')

#Pembaruan
print('\n === Update ===')
for p in status_pelanggan.values():
    print(f"{p.id_pelanggan} | {p.nama} | {p.email}")

# Membuat dictinory of objects
katalog_produk = {
    "N-01": Produk('N-01', 'Laptop', 800000000),
    'N-02': Produk('N-02', 'Mouse', 150000000),
    'N-03': Produk('N-03', 'Keyboard', 40000000)
}

# Mengakses dictinory of objects
print('=== Katalog Produk ===')
for kode, produk in katalog_produk.items():
    print(f'{kode}: {produk.info()}')

# Mencari produk
cari_kode = 'N-02'
if cari_kode in katalog_produk:
    print(f'\nProduk ditemukan: {katalog_produk[cari_kode].info()}')