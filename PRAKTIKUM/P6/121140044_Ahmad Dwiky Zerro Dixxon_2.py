#121140044~ahmad_dwiky

class produk:

	def __init__(self, harga):
		self.HargaProduk = harga

	def HitungHarga(self):
		pass


class makanan(produk):

	def __init__(self, harga, jumlah):
		super().__init__(harga)
		self.Jumlah = jumlah

	def HitungHarga(self):
		return self.HargaProduk*self.Jumlah


class minuman(produk):

	def __init__(self, harga, ukuran, jumlah):
		super().__init__(harga)
		self.Ukuran = ukuran
		self.Jumlah = jumlah

	def HitungHarga(self):
		return self.HargaProduk*self.Ukuran*self.Jumlah


class barang(produk):

	def __init__(self, harga, berat):
		super().__init__(harga)
		self.Berat = float(berat/10)

	def HitungHarga(self):
		return float(self.HargaProduk*self.Berat)


class keranjangBelanja:

	def __init__(self):
		self.Keranjang = []
		self.Loop = True

	def DaftarMakanan(self) -> int:
		makan = input('MAKANAN~\n1  Nasi Padang\n2  Ayam Geprek\n3  Nasi Goreng\n=> ')
		if makan == "1":
			return 2
		elif makan == "2":
			return 1
		else:
			return 1

	def DaftarMinuman(self) -> int:
		minum = input('MINUMAN~\n1  Mixue\n2  Pop Ice\n3  Es Teh\n=> ')
		if minum == "1":
			return 1.5
		elif minum == "2":
			return 0.5
		else:
			return 0.2

	def DaftarUkuran(self) -> int:
		minum = input('MINUMAN~\n1  Kecil\n2  Sedang\n3  Venti\n=> ')
		if minum == "3":
			return 3
		elif minum == "2":
			return 2
		else:
			return 1

	def DaftarBarang(self) -> int:
		barang = input('BARANG~\n1  Leptop Geming\n2  Kursi Geming\n3  Cewe Geming\n=> ')
		if barang == "1":
			return 1500
		elif barang == "2":
			return 600
		else:
			return 0

	def TambahProduk(self):
		
		while self.Loop:
			buy = input('TOKO MEGAwat JAYA\n1  Makanan\n2  Minuman\n3  Barang\n4  Bayar\n=> ')

			if buy == "1":
				self.Keranjang.append(makanan(self.DaftarMakanan(),int(input('Jumlah makanan yang dibeli : '))))
			elif buy == "2":
				self.Keranjang.append(minuman(self.DaftarMinuman(),self.DaftarUkuran(),
								int(input('Jumlah minuman yang dibeli : '))))
			elif buy == "3":
				self.Keranjang.append(barang(self.DaftarBarang(),int(input('Jumlah berat (1 - 100) KG : '))))

			elif buy == "4":
				self.Loop = False
				self.HitungTotalHarga()
			else:
				pass


	def HitungTotalHarga(self):
		
		Total = 0

		for objek in self.Keranjang:
			Total += objek.HitungHarga()

		print("\nTotal Pembayaran : ",round(float(Total),2),"US Dollar")


user = keranjangBelanja()
user.TambahProduk()