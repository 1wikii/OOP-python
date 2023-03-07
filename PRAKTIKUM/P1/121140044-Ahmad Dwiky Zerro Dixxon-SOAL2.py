
def check(temp: int) -> str:
	if temp >= 100:
		return "Gas"
	elif temp <= 0:
		return "Solid"
	else:
		return "Liquid"

def main():

	temp = int(input("Enter temperature (Celcius) : "))
	print(f"\nWater form on {temp} celcius is a " + check(temp))

main()