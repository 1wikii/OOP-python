
class operator:

	def tambah(self, a, b):
		return a+b

	def kurang(self, a, b):
		return a-b

	def kali(self, a, b):
		return a*b

	def bagi(self, a, b):
		return a/b


class tampilan:

	def tampil(self, result):
		print("Hasil Perhitungan adalah :",round(result,2))


class kalkulator(operator,tampilan):
	
	def hitung(self):
		n1 = int(input('Masukkan bilangan : '))
		op = input('Masukkan(+, -, *, atau /) : ')
		n2 = int(input('Masukkan bilangan : '))

		if op == "+":
			self.tampil(self.tambah(n1,n2))
		elif op == "-":
			self.tampil(self.kurang(n1,n2))
		elif op == "*":
			self.tampil(self.kali(n1,n2))
		elif op == "/":
			self.tampil(self.bagi(n1,n2))
		else:
			print("\nOperator Tidak Valid!\n")
			self.hitung()

user = kalkulator()
user.hitung()


		
		
		