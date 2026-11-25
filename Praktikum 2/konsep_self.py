class Matakuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        if mhs not in self.mahasiswa:
            self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


if __name__ == "__main__":
    # 2 Mata Kuliah
    mk1 = Matakuliah("TI101", "Pemrograman Dasar")
    mk2 = Matakuliah("TI102", "Struktur Data")

    # 3 Mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    # Daftarkan ke masing-masing mata kuliah
    mk1.tambah_mahasiswa(m1)
    mk1.tambah_mahasiswa(m2)
    mk1.tambah_mahasiswa(m3)

    mk2.tambah_mahasiswa(m1)
    mk2.tambah_mahasiswa(m3)

    for mk in [mk1, mk2]:
        print(f"Mata Kuliah: {mk.kode} - {mk.nama}")
        print("Daftar Mahasiswa:", mk.daftar_mahasiswa())
        print("Jumlah Mahasiswa:", mk.jumlah_mahasiswa())
        print("-" * 40)

        