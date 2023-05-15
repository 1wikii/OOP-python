
class buku:

	jumlah_buku = []
	bayar = 0
	diskon = 0

	def __init__(self, nama: str, pengarang: str, tahun_terbit: int, harga: int):
		self.nama = nama
		self.pengarang = pengarang
		self.terbit = tahun_terbit
		self.harga = harga

		buku.jumlah_buku.append(self)

	def __repr__(self):
		return f" {self.pengarang} => '{self.nama}' | Terbit : {self.terbit} | Rp. {self.harga} |""\n"

	def DISKON(self):
		self.harga = self.harga*buku.diskon
		buku.bayar += self.harga
		