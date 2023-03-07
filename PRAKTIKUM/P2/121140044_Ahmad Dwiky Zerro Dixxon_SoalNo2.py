# A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 0	1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input('Masukkan kunci (key) : ')

def menu() -> str:
	print('\nVigenere Chiper :\n1. Enkripsi Plaintext\n2. Dekripsi Plaintext\n3. Ganti Kata Kunci\n4. Keluar')
	ch = input('Masukkan input : ')

	return ch

def vignere(text: str, iden) -> str:
	lp = len(text)
	lk = len(key)

	keyy = int(lp/lk)+1
	keyy = key*keyy
	keyy = list(keyy)

	for i in range(lp):						# membuat key dipisah juga dengan spasi
		if text[i] == ' ':
			for j in range(len(text),i,-1): # pergeseran key dari akhir ketika nambah spasi
				keyy[j] = keyy[j-1]
			keyy[i] = ' '

	res = ""
	for char in range(lp):
		if text[char] == ' ':		# jika spasi maka tidak ada perhitungan encrypt
			res += " "
		else:
			idxp = 0
			idxk = 0
			if iden == "en":
				al = alpha.lower()
			elif iden == "dec":
				al = alpha

			for c in range(len(alpha)):			# mencari nomor index dari char text dan char key
				if al[c] == text[char]:
					idxp = c 
				if alpha.lower()[c] == keyy[char]:
					idxk = c

			if iden == "en":
				enc = (idxp+idxk)%26	# rumus encrypt
			elif iden == "dec":
				enc = (idxp-idxk)%26	# rumus decrypt

			res += alpha[enc]	

	return res

def main():
	choices = menu()
	if choices == '1':
		print("Chipertext : "+vignere(input('Masukkan plaintext : '),"en"))
		main()
	elif choices == '2':
		print("Plaintext : "+vignere(input('Masukkan chipertext : '),"dec").lower())
		main()
	elif choices == '3':
		key = input('Masukkan kunci (key) : ')
		main()
	elif choices == '4':
		print('Berhasil keluar!')

main()