class coba:

	note = 10

	def __init__(self, nama: str, umur: int):
		
		assert umur >= 10, f"{umur} not enough!"

		self.nama = nama 
		self.umur = umur

	def usia(self):
		if self.umur > 20:
			return "dewasa !"
		elif self.umur > 40:
			return "tua !"
		elif self.umur < 10:
			return "anak-anak !"
		elif self.umur >= 10:
			return "remaja !"
		else:
			return "unknown !!!"