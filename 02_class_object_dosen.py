class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}."

# Instansiasi dua object dosen
dosen1 = Dosen("Budi Santoso", "0123456789")
dosen2 = Dosen("Siti Aminah", "0987654321")

print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Basis Data"))
