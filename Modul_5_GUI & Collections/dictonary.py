class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode 
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp {self.harga: ,}"

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