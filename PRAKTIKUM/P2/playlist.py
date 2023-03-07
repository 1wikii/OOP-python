
class lagu:
    
    def __init__(self,nama,penyanyi,tahun):
        self.__nama = nama
        self.__penyanyi = penyanyi
        self.__tahun = tahun
        
    def buat(self) -> list:
    	return [self.__nama,self.__penyanyi,self.__tahun]

class playlist:
	
	def __init__(self,list_lagu: list):
		self.saat_ini = 0
		self.list_lagu = list_lagu
		self.leng = len(self.list_lagu)

	def pertama(self):
		self.saat_ini = 0

		self.cetak(self.saat_ini)

	def terakhir(self):
		self.saat_ini = -1

		self.cetak(self.saat_ini)

	def putar(self):
		self.cetak(self.saat_ini)

	def selanjutnya(self):
		if self.saat_ini == self.leng:
			self.saat_ini = 0
		else:
			self.saat_ini += 1

		self.cetak(self.saat_ini)

	def sebelumnya(self):
		if self.saat_ini == 0:
			self.saat_ini = -1
		else:	
			self.saat_ini -= 1

		self.cetak(self.saat_ini)

	def set(self,idx: int):
		if idx > self.leng:
			print("None")
		else:
			self.saat_ini = idx-1

			self.cetak(self.saat_ini)

	def cetak(self,idx=" "):
		if idx == " ":
			for item in range(self.leng):
				print(str(item+1)+".",end=" ")
				print(self.list_lagu[item][0],end=", ")
				print(self.list_lagu[item][1],end=", ")
				print(self.list_lagu[item][2],end="\n")

		else:
			print(self.list_lagu[idx][0],end=", ")
			print(self.list_lagu[idx][1],end=", ")
			print(self.list_lagu[idx][2],end="\n\n")

def main():
	l_lagu = []
	
	# obj list lagu
	buat = lagu("DARIS","maju tak gentar","2023")
	l_lagu.append(buat.buat())
	buat = lagu("BUDI","Istriku seekor kartu","2025")
	l_lagu.append(buat.buat())
	buat = lagu("FARHAN","Mamahku surgaku","1999")
	l_lagu.append(buat.buat())
	buat = lagu("farhan","Kolor kecantol","1969")
	l_lagu.append(buat.buat())

	# obj playlist
	play = playlist(l_lagu)
	print(str(7*"*")+"Playlist music"+str(7*"*"),end="\n\n")
	play.cetak()
	print("\n")

	playing = True

	while playing:
		choice = input("Play (P) | First (F) | Last (L) | Next (N>) | Previous (<P) | Choose (C) | Stop (S) | : ")
		
		if choice == "P":
			print("\nNow Playing =>",end=" ")
			play.putar()
		elif choice == "F":
			print("\nNow Playing =>",end=" ")
			play.pertama()
		elif choice == "L":
			print("\nNow Playing =>",end=" ")
			play.terahir()
		elif choice == "N>":
			print("\nNow Playing =>",end=" ")
			play.selanjutnya()
		elif choice == "<P":
			print("\nNow Playing =>",end=" ")
			play.sebelumnya()
		elif choice == "C":
			no = int(input("Number of music : "))
			print("\nNow Playing =>",end=" ")
			play.set(no)
		elif choice == "S":
			playing  = False
		else:
			print("\n\tInput Eror !\t\n")

	print("\n"+str(7*"*")+"ArigataThanks"+str(7*"*"))

main()
