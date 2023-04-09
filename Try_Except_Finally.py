def Try_Else():
	try:
		print("Hello")
	except:
		print("Something went wrong")
	else:
		print("Nothing went wrong")		# ELSE ketika tidak ada EROR

def Bersarang():					# contoh NameEror variable not define
	a = 2							# contoh TypeEror datatype tidak sesuai
	b = "1"

	try:							
		print( a/b )
		print(c)
	except NameError as n:
		print(f"NameEror = {n}")

	except TypeError as t:
		try:
			print( a/int(b) )
		except:
			print(f"Type error {t}")
	except:
	 	print("TIDAK BISA BAGI NOL")
	finally:
		print("JALANNN!")

def RAISE():
	x = -2

	assert x > 0, f"X TIDAK VALID!"
	
	if x < 0:
		pass
		# raise AssertionError("ERORRRR")
		# #raise Exception("Tidak boleh kurang dari 0 !")

def RAISE_INT():
	num = "Name"

	if not type(num) is int:
		raise Exception("Tidak boleh selain integer !")

Try_Else()
RAISE()