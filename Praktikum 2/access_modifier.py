class Mahasiswa:
    def __init__(self, nim, nama, semester=1, ipk=0.0):
        self.nim = nim               # public
        self.nama = nama             # public
        self._semester = semester    # protected
        self.__ipk = ipk             # private

    # Getter & Setter untuk _semester (protected)
    def get_semester(self):
        return self._semester

    def set_semester(self, semester_baru):
        self._semester = semester_baru

    # Getter & Setter untuk __ipk (private)
    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, ipk_baru):
        self.__ipk = ipk_baru


if __name__ == "__main__":
    # Buat 2 objek Mahasiswa
    mhs1 = Mahasiswa("23001", "Budi", 2, 3.45)
    mhs2 = Mahasiswa("23002", "Siti", 4, 3.80)

    print("=== Data Awal ===")
    for m in [mhs1, mhs2]:
        print(f"NIM: {m.nim} | Nama: {m.nama} | Semester: {m.get_semester()} | IPK: {m.get_ipk()}")

    # Ganti semester dan IPK (bebas sesuai instruksi latihan c)
    mhs1.set_semester(6)
    mhs1.set_ipk(3.92)

    mhs2.set_semester(8)
    mhs2.set_ipk(2.75)

    print("\n=== Setelah Diubah ===")
    for m in [mhs1, mhs2]:
        print(f"NIM: {m.nim} | Nama: {m.nama} | Semester: {m.get_semester()} | IPK: {m.get_ipk()}")

        