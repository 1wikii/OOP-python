from kelas import coba


# nama = input("Nama : ")
# umur = input("Umur : ")

# #print(type(umur))

# obj = coba(nama,int(umur))

# print(obj.usia())


# def fak(num: int):

# 	assert num > 1 , f"{result} EROR!"
# 	result = 1
# 	for i in range(2, num+1):
# 		result *= i

# 	print(result)
	

# fak(2)

# def pow(num, power):

# 	if power <= 0:
# 		return 1

# 	else:
# 		return num * pow(num,power-1)

# print(pow(2,3))


def count(*args):
	for i in args:
		print(i)

count("satu","dua","tiga")


p = "aku"
print(enumerate(p, start=0))