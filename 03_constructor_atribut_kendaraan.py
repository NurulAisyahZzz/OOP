class Kendaraan:
    # Class attribute: dimiliki bersama oleh seluruh object
    bahan_bakar = "Bensin"

    def __init__(self, merk, warna, tahun):
        # Instance attributes: nilainya dapat berbeda pada setiap object
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk}, warna {self.warna}, tahun {self.tahun}"

# Membuat dua object
kendaraan1 = Kendaraan("Toyota", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda", "Putih", 2024)

# Mengakses instance attribute melalui object
print("Kendaraan 1:", kendaraan1.info_kendaraan())
print("Kendaraan 2:", kendaraan2.info_kendaraan())

# Mengakses class attribute melalui class dan object
print("Bahan bakar melalui class:", Kendaraan.bahan_bakar)
print("Bahan bakar melalui object:", kendaraan1.bahan_bakar)
