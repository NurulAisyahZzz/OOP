class Buku:
    def __init__(self, kode_buku: str, judul: str, penulis: str, stok: int, lokasi_rak: str):
        self.kode_buku = kode_buku      # public
        self.judul = judul              # public
        self.penulis = penulis          # public
        self._stok = stok               # protected
        self.__lokasi_rak = lokasi_rak  # private

    # Getter & Setter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, rak_baru: str):
        if not rak_baru:
            raise ValueError("Lokasi rak tidak boleh kosong.")
        self.__lokasi_rak = rak_baru

    def tambah_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah penambahan stok harus lebih dari 0.")
        self._stok += jumlah

    def kurangi_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0.")
        if jumlah > self._stok:
            raise ValueError(f"Stok buku '{self.judul}' tidak mencukupi.")
        self._stok -= jumlah

    def info_buku(self):
        return (
            f"[{self.kode_buku}] {self.judul} - {self.penulis} | "
            f"Stok: {self._stok} | Rak: {self.get_lokasi_rak()}"
        )


class Peminjaman:
    def __init__(self, buku: Buku, tanggal_pinjam: str, tanggal_kembali: str = "-", status: str = "Dipinjam"):
        self.buku = buku                        # association dengan Buku
        self.kode_buku = buku.kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return (
            f"Kode Buku: {self.kode_buku} ({self.buku.judul}) | "
            f"Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | "
            f"Status: {self.status}"
        )


class Anggota:
    def __init__(self, id_anggota: str, nama: str, maks_pinjam: int = 3, status_aktif: bool = True):
        self.id_anggota = id_anggota        # public
        self.nama = nama                    # public
        self._maks_pinjam = maks_pinjam     # protected
        self.__status_aktif = status_aktif  # private
        self.daftar_peminjaman = []         # aggregation: objek Peminjaman disimpan di list

    # Getter & Setter status aktif
    def get_status(self):
        return "Aktif" if self.__status_aktif else "Non-Aktif"

    def set_status(self, aktif: bool):
        self.__status_aktif = bool(aktif)

    def _jumlah_sedang_dipinjam(self):
        return sum(1 for p in self.daftar_peminjaman if p.status == "Dipinjam")

    def pinjam_buku(self, buku: Buku, tanggal_pinjam: str):
        if not self.__status_aktif:
            print(f"Gagal: Anggota {self.nama} berstatus Non-Aktif.")
            return None
        if self._jumlah_sedang_dipinjam() >= self._maks_pinjam:
            print(f"Gagal: Anggota {self.nama} sudah mencapai batas maksimal pinjam.")
            return None

        buku.kurangi_stok(1)
        pinjam = Peminjaman(buku=buku, tanggal_pinjam=tanggal_pinjam, status="Dipinjam")
        self.daftar_peminjaman.append(pinjam)
        return pinjam

    def kembalikan_buku(self, kode_buku: str, tanggal_kembali: str):
        for p in self.daftar_peminjaman:
            if p.kode_buku == kode_buku and p.status == "Dipinjam":
                p.status = "Dikembalikan"
                p.tanggal_kembali = tanggal_kembali
                p.buku.tambah_stok(1)
                return True
        print(f"Data peminjaman aktif untuk kode {kode_buku} pada {self.nama} tidak ditemukan.")
        return False

    def info_anggota(self):
        return (
            f"ID: {self.id_anggota} | Nama: {self.nama} | "
            f"Maks Pinjam: {self._maks_pinjam} | Status: {self.get_status()} | "
            f"Total Riwayat Pinjam: {len(self.daftar_peminjaman)}"
        )


# Relasi composition: Buku dibuat dan dikelola oleh Perpustakaan
class Perpustakaan:
    def __init__(self, nama: str):
        self.nama = nama
        self._koleksi_buku = []

    def tambah_buku(self, kode_buku: str, judul: str, penulis: str, stok: int, lokasi_rak: str):
        buku = Buku(kode_buku, judul, penulis, stok, lokasi_rak)
        self._koleksi_buku.append(buku)
        return buku

    def get_daftar_buku(self):
        return self._koleksi_buku


if __name__ == "__main__":
    perpus = Perpustakaan("Perpustakaan STITEK")

    # d.1. Buat 3 buku (composition melalui Perpustakaan)
    b1 = perpus.tambah_buku("BK01", "Pemrograman Python", "Guido", 4, "Rak A1")
    b2 = perpus.tambah_buku("BK02", "Struktur Data & Algoritma", "Rinaldi", 3, "Rak A2")
    b3 = perpus.tambah_buku("BK03", "Basis Data Lanjut", "Rosa", 2, "Rak B1")

    # d.2. Buat 2 anggota
    agt1 = Anggota("AGT01", "Dina", maks_pinjam=3, status_aktif=True)
    agt2 = Anggota("AGT02", "Raka", maks_pinjam=2, status_aktif=True)

    # d.3. Anggota 1 pinjam 2 buku
    agt1.pinjam_buku(b1, "2026-11-20")
    agt1.pinjam_buku(b2, "2026-11-20")

    # d.4. Anggota 2 pinjam 1 buku
    agt2.pinjam_buku(b3, "2026-11-21")

    # d.5. Pengembalian buku (contoh Anggota 1 mengembalikan BK01)
    agt1.kembalikan_buku("BK01", "2026-11-25")

    # e.1. Demonstrasi: Informasi buku dan stoknya
    print("=== INFORMASI BUKU & STOK ===")
    for b in perpus.get_daftar_buku():
        print(b.info_buku())

    # e.2. Demonstrasi: Informasi anggota
    print("\n=== INFORMASI ANGGOTA ===")
    for a in [agt1, agt2]:
        print(a.info_anggota())

    # e.3. Demonstrasi: Daftar peminjaman masing-masing anggota
    print("\n=== DAFTAR PEMINJAMAN ANGGOTA ===")
    for a in [agt1, agt2]:
        print(f"Anggota: {a.nama} ({a.id_anggota})")
        if not a.daftar_peminjaman:
            print("  - Belum ada peminjaman")
        else:
            for p in a.daftar_peminjaman:
                print("  -", p.info_peminjaman())

                