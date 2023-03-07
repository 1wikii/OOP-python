
def check(M,r,c):
	if len(M) != r or len(M[0]) != c:
		return False
	
	return True

def mat_in(M , row , num_row):
	temp = []
	M.append(temp)

	for chr in row:
		if chr != ' ':
			M[num_row].append(int(chr))

def transpose(M: list, r, c) -> list:

	tran = [[0 for i in range(r)] for j in range(c)]

	for i in range(r):
		for j in range(c):
			tran[j][i] = M[i][j]

	return tran

# MAIN PROGRAM
def main():
	main = []

	inp = input()
	row = int(inp[0])
	col = int(inp[2])

	if row > 0 and row <= 10 or col > 0 and col <= 10:
		for i in range(row):
			mat_in(main,input(),i)

		if check(main,row,col):
			main = transpose(main,row,col)
			for row in main:
				for col in row:
					print(int(col),end=" ")
				print()
		else:
			print("-1")
	else:
		print("-1")
main()