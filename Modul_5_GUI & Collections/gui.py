import tkinter as tk
from tkinter import messagebox

class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi GUI Sederhana")
        self.root.geometry("300x250")  # Ukuran sedikit diperbesar agar proporsional

        # Label
        self.label = tk.Label(root, text="Selamat Datang di Aplikasi GUI", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entry (Input Teks)
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Masukkan nama Anda")

        # Tombol Sapa
        self.button = tk.Button(root, text="Sapa", command=self.tampilkan_sapa)
        self.button.pack(pady=10)

        # Tombol Keluar
        self.exit_button = tk.Button(root, text="Keluar", command=root.destroy)
        self.exit_button.pack(pady=10)

    def tampilkan_sapa(self):
        nama = self.entry.get()
        # Logika untuk mengecek apakah input sudah diisi/diubah dari default
        if nama and nama != "Masukkan nama Anda":
            messagebox.showinfo("Sapaan", f"Halo, {nama}!")
        else:
            messagebox.showwarning("Peringatan", "Masukkan nama terlebih dahulu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
