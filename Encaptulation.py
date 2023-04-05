class item:

	def __init__(self,nama):
		self.__nama = nama

	def nama(self):
		return self.__nama


a = item("asu")

a.__nama = "kirig"
print(a.__nama)