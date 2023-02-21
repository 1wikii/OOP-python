import random

class sepeda:

	def __init__(self):
		self.roda_gigi_saat_ini = 1
		self.max_kecepatan = 2
		self.kecepatan = 0

	def pindah(self,roda_gigi):
		self.roda_gigi_saat_ini = roda_gigi

		if(roda_gigi == 1):
			self.max_kecepatan = 2
		elif(roda_gigi == 2):
			self.max_kecepatan = 4
		elif(roda_gigi == 3):
			self.max_kecepatan = 6
		elif(roda_gigi == 4):
			self.max_kecepatan = 8

		self.kecepatan = random.randint(1,self.max_kecepatan)

		print(self.roda_gigi_saat_ini)
		print(self.max_kecepatan)
		return self.kecepatan 

	def tambah(self):
		if(self.kecepatan < self.max_kecepatan):
			self.kecepatan += 1
		else:
			pass

		print(self.roda_gigi_saat_ini)
		print(self.max_kecepatan)
		return self.kecepatan 

	def kurang(self):
		if(self.kecepatan > 0):
			self.kecepatan -= 1
		else:
			pass

		print(self.roda_gigi_saat_ini)
		print(self.max_kecepatan)
		return self.kecepatan 

def main():
	play = sepeda()
	print(play.pindah(3))

main()
