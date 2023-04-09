import sys


file = open("Try_latihan.txt", "r")


try:
	print(file.read())
except NameError:
	print("FILE TIDAK DITEMUKAN!")
else:
	assert sys.getsizeof(file) < 102, f"FILE terlalu besar, maksimal ukuran adalah 1024, file anda berukuran: {sys.getsizeof(file)} Byte !!!"
	print("File sudah Dibaca")		