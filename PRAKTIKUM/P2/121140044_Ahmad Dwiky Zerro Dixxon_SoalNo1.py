
class buku:
	
	def __init__(self):
		self._List = []

	def menu(self) -> str:
		print('\nToko buku serba (Ada)\n1. Tambah Data Buku\n2. Lihat List Buku')
		print('3. Modifikasi Buku Lama\n4. Hapus Buku Lama\n5. Keluar')
		ch = input('Masukkan nomor input : ')

		return ch

	def start(self) -> int:
		ch = int(input('Masukkan jumlah buku mula-mula : '))

		self.add(ch)

	def add(self, amount=1, modif="x"):
		for book in range(amount):
			title = input('Masukkan nama buku : ')
			genre = input('Masukkan genre buku : ')
			author = input('Masukkan nama pengarang : ')
			year = input('Masukkan tahun terbit : ')

			if modif == 'x':
				self._List.append([title,genre,author,year])
			else:
				self._List[modif] = [title,genre,author,year]
				print('Data buku berhasil dimodifikasi\n')
				break

			print('Data buku berhasil ditambahkan\n')

	def printout(self, iden=0):

		if iden == 0:
			for book in self._List:
				print(book[0]+"  "+book[1]+"  "+book[2]+"  "+book[3])
		else:
			print(f"nama : {iden[0]}   genre : {iden[1]}   pengarang : {iden[2]}   tahun terbit : {iden[3]}")


	def modif(self):
		title = input('Masukkan nama buku yang akan diubah : ')
		print('\nData buku yang akan diedit :')

		for i in range(len(self._List)):
			if self._List[i][0] == title:
				self.printout(self._List[i])
				self.add(modif=i)

				break

	def delete(self):
		title = input('Masukkan nama buku yang akan dihapus : ')
		print('\nData buku yang akan dihapus :')

		for i in range(len(self._List)):
			if self._List[i][0] == title:
				self.printout(self._List[i])
				if i == (len(self._List)-1):
					self._List.pop(-1)
					print('Data buku berhasil dihapus\n')
					break
				else:
					for idx in range(i,len(self._List)-1):
						self._List[idx] = self._List[idx+1]

					self._List.pop(-1)
					print('Data buku berhasil dihapus\n')
					break

def main():

	user = buku()
	user.start()

	while True:
		ch = user.menu()

		if ch == '1':
			user.add()
		elif ch == '2':
			user.printout()
		elif ch == '3':
			user.modif()
		elif ch == '4':
			user.delete()
		elif ch == '5':
			print('Berhasil keluar program!')
			break
		else:
			print('Eror input!')
			pass

main()
	
