import random as rd

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

		self.kecepatan = rd.randint(0,self.max_kecepatan)


	def tambah(self):
		if(self.kecepatan < self.max_kecepatan):
			self.kecepatan += 1

	def kurang(self):
		if(self.kecepatan > 0):
			self.kecepatan -= 1
		
	def cek(self):
	    print(f"Number of gear -> {self.roda_gigi_saat_ini}")
	    print(f"Max speed      -> {self.max_kecepatan}")
	    print(f"Speed          -> {self.kecepatan}")

def main():
    # objek
    play = sepeda()
    
    # objek.class
    play.pindah(2)
    play.tambah()
    # play.tambah()
    # play.tambah()
	
    play.cek()
	
main()

