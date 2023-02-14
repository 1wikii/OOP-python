num = [1,2,3,4,5,6]

no = len(num)

for i in range(no):
	if (i+1) == no/2:
		print(num[i])
	else:
		print(num[i],end="")
