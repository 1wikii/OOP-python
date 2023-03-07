
def prima(dct: dict,bil: int):
	
	if bil == 1 or bil == 0:
		dct["non"] = dct["non"] + 1
		return
	elif bil == 2:
		dct["prima"] = dct["prima"] + 1
		return
	else:
		for i in range(2,bil):
			if bil % i == 0:
				dct["non"] = dct["non"] + 1
				return

	dct["prima"] = dct["prima"] + 1
	return

def count(dct: dict) -> int:
	return dct["prima"]+dct["non"]

def precent(dct: dict) -> float:
	return round(dct["prima"]*100/count(dct),2)


# Main program
def main():
	nilai = {"prima": 0, "non": 0}

	for i in range(10):
		bil = int(input('Masukan bilangan : '))
		prima(nilai,bil)

	print("\nJumlah prima       : "+ str(nilai["prima"]))
	print("Jumlah bukan prima : "+ str(nilai["non"]))

	print("Presentase prima dari "+ str(count(nilai)) + " bilangan : " + str(precent(nilai)) + "%")

main()