import random

class question:

	word = ["daris","abang","ganteng"]
	number = 0
	def __init__(self,name:str,health:int):
		self.name = name 
		self.health = health

	def start(self):

		while question.number < len(question.word) and self.health > 0:

			loop = False
			while not loop and self.health > 0:
				print(f"Player : {self.name}",end=f"   Health : {self.health}\n")
				number = question.number
				word_raw = question.word[number]
				word_question = ""
				for ch in word_raw:
					r = random.randint(0,len(word_raw)-1)
					word_question += word_raw[r]
					word_raw = word_raw.replace(word_raw[r],"",1)

				print("\nRangkai huruf dibawah :")
				print("   ",end="")
				for i in word_question:
					print(i,end=" ")
				answer = input("\n\n=> ")

				if self.check(answer):
					print("\nJawaban Benar!")
					loop = True
					input()
				else:
					print("\nJawaban Salah!")
					self.health -= 1
					input()

			question.number += 1

		print(f"Player : {self.name}",end=f"   Health : {self.health}\n")
		if self.health <= 0:
			print("\tGame Over !!!\n\n")
		else:
			print("Selamat anda menang!")

	def check(self,answer=""):

		if answer == question.word[question.number]:
			return True
		else:
			return False

def main():
	health  = 3
	name = input("enter your name : ")
	play = question(name,health)

	play.start()

main()