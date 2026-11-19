class ManajerInventori:
    def __init__(self):
        # Nama barang menjadi key dan jumlah stok menjadi value
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah <= 0:
            return "Jumlah penambahan harus lebih dari 0."

        self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
        return f"Berhasil menambahkan {jumlah} {nama_barang}. Stok sekarang: {self.inventori[nama_barang]}."

    def hapus_barang(self, nama_barang, jumlah):
        if jumlah <= 0:
            return "Jumlah pengurangan harus lebih dari 0."
        if nama_barang not in self.inventori:
            return f"{nama_barang} tidak ditemukan dalam inventori."
        if jumlah > self.inventori[nama_barang]:
            return f"Stok {nama_barang} tidak mencukupi."

        self.inventori[nama_barang] -= jumlah
        sisa = self.inventori[nama_barang]
        if sisa == 0:
            del self.inventori[nama_barang]
        return f"Berhasil mengurangi {jumlah} {nama_barang}. Sisa stok: {sisa}."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori masih kosong."

        hasil = ["Daftar Inventori:"]
        for nama_barang, jumlah in self.inventori.items():
            hasil.append(f"- {nama_barang}: {jumlah}")
        return "\n".join(hasil)

# Demonstrasi seluruh method
inventori = ManajerInventori()
print(inventori.tambah_barang("Buku", 10))
print(inventori.tambah_barang("Pulpen", 20))
print(inventori.hapus_barang("Buku", 3))
print(inventori.lihat_inventori())
