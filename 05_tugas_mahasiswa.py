class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return (
            f"Halo, nama saya {self.nama}, NIM {self.nim}, "
            f"dari jurusan {self.jurusan}. "
            f"Saya mahasiswa {Mahasiswa.universitas}."
        )

    def update_ipk(self, ipk_baru):
        if not 0.0 <= ipk_baru <= 4.0:
            return "IPK harus berada pada rentang 0.0 sampai 4.0."

        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk:.2f}."

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            # Modul tidak menentukan predikat untuk IPK di bawah 2.0.
            return "Belum memenuhi batas kelulusan"


# Instansiasi tiga object mahasiswa dengan data berbeda
mhs1 = Mahasiswa("Andi Pratama", "TI001", "Teknik Informatika", 3.70)
mhs2 = Mahasiswa("Siti Rahma", "TI002", "Teknik Informatika", 3.20)
mhs3 = Mahasiswa("Dewi Lestari", "TI003", "Sistem Informasi", 2.40)

daftar_mahasiswa = [mhs1, mhs2, mhs3]

# Demonstrasi semua method
for mahasiswa in daftar_mahasiswa:
    print(mahasiswa.perkenalan_diri())
    print(f"IPK: {mahasiswa.ipk:.2f}")
    print(f"Predikat: {mahasiswa.predikat_kelulusan()}")
    print("-" * 50)

# Demonstrasi update_ipk()
print(mhs3.update_ipk(2.80))
print(f"Predikat terbaru {mhs3.nama}: {mhs3.predikat_kelulusan()}")
