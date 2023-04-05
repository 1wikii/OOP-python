# *SISTEMATIS GAME*
# mempunyai skill random
# setelah memakai skill berikutnya player tersilence, batas pengunaan skill 1x
# magic power tidak peduli armor, langsung ke health dmg 3x dari basic
# phisic menghancurkan armor dmg 3x dari basic
# ketika basic attack didefense , dmg masuk = 15
# ketika skill attack didefense , dmg masuk = 50

import random as rdm

l_skill = ["m","p","p","m"]  # m = magic dmg
					  		 # p = phisic dmg
class robot:

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.__skill = ""
		self.skill_silence = ""
		self.skill_count = 1
		self.__armor = 30
		self.basic_dmg = 20

	def skill(self):
		return self.__skill

	def armor(self):
		return self.__armor

	def set_armor(self, num):
		self.__armor = num

	def skill_rand(self):
		Rskill = rdm.randint(0,3)
		self.__skill = l_skill[Rskill]		# Random skill untuk player

	def alive(self) -> bool:
		return self.health > 0

	def skill_availability(self) -> bool:
		return self.skill_count > 0

	# method ketika health lebih maka pindah ke armor
	def OverH(self):
		if self.health > 100:
			overH = self.health - 100
			self.health -= overH
			if self.__armor < 0:
				self.__armor = 0
			self.__armor += overH 

	def ATTACK(self, opponent, attk_type):

		# Basic Attack
		if attk_type == 1:
			if opponent.armor() > 0:
				arm = opponent.armor() - self.basic_dmg
				opponent.set_armor(arm)
				if opponent.armor() < 0:
					opponent.health += opponent.armor()
					opponent.set_armor(0)
			else:
				opponent.health -= self.basic_dmg

		# Skill attack
		elif attk_type == 3:

			if self.skill_count > 0 and self.__skill == "m":
				opponent.health -= (self.basic_dmg*3)

			elif self.skill_count > 0 and self.__skill == "p":

				if opponent.armor() > 0:
					arm = opponent.armor() - (self.basic_dmg*3)
					opponent.set_armor(arm)
					if opponent.armor() < 0:
						opponent.health += opponent.armor()
						opponent.set_armor(0)
				else:
					opponent.health -= (self.basic_dmg*3)

			self.skill_count = 0
			self.SILENCE() # awto silence stelah guna skill

	# method DEFENSE
	def DEFENSE(self, attk_type, opponent):		# Sistematis defense adalah menambah hp atau armor
			if attk_type == 1:					# setelah di attack dgn jumlah tertentu sesuai basic/skill attk
				if self.__armor > 0:
					self.__armor += 5
				else:
					self.health += 5
					self.OverH()

			elif attk_type == 3:
				
				if opponent.skill() == "m":
					self.health += 15
					self.OverH()

				else:
					if self.__armor > 0:
						self.__armor += 15
					else:
						self.health += 15
						self.OverH()

	def SILENCE(self, n=""):			# parameter agar bisa dipakai untuk silence dan non-silence
		if n == "non":
			self.skill_silence = ""
		else:
			self.skill_silence = "silenced"

	def SUREN(self):
		self.health = 0

class game:

	def __init__(self, player1_name, player2_name):
		self.p1 = robot(player1_name)			# mengisikan objek disini agar mudah memanipulasi
		self.p2 = robot(player2_name)			# attribut di class lain

	# method MENU
	def ch_print(self, player):
		if player.skill_silence == "silenced":
			print(f"{player.name} SILENCED")
			return False
		elif player.skill_availability():
			print("0  SURRENDER\n1  BASIC ATTACK\n2  DEFENSE\n3  SKILL ATTACK")
			return True
		else:
			print("0  SURRENDER\n1  BASIC ATTACK\n2  DEFENSE")
			return True

	# method MULAI
	def start(self):
		self.p1.skill_rand()
		self.p2.skill_rand()

		while self.p1.alive() and self.p2.alive():

			# GAME BAR
			print(f"\n{self.p1.name}   |{self.p1.health}||{self.p1.armor()}|   VS   |{self.p2.armor()}||{self.p2.health}|   {self.p2.name}\n")
			
			if self.ch_print(self.p1):
				act_p1 = input(f'{self.p1.name}, Select your action : ')
				if act_p1 == "0":
					self.p1.SUREN()			# Suren disini agar langsung keluar program
					break
			print()
			if self.ch_print(self.p2):		
				act_p2 = input(f'{self.p2.name}, Select your action : ')
				if act_p2 == "0":
					self.p2.SUREN()			# Suren disini agar langsung keluar program
					break

			if self.p1.skill_silence == "silenced":
				act_p1 = "9"
				self.p1.SILENCE("non")
			if self.p2.skill_silence == "silenced":
				act_p2 = "9"
				self.p2.SILENCE("non")

			if act_p1 == "1":
				self.p1.ATTACK(self.p2, 1)
			elif act_p1 == "3":
				self.p1.ATTACK(self.p2, 3)

			if act_p2 == "1":
				self.p2.ATTACK(self.p1, 1)
			elif act_p2 == "3":
				self.p2.ATTACK(self.p1, 3)

			if act_p2 == "2":
				self.p2.DEFENSE(int(act_p1),self.p1)	# defense disini karena harus setelah attk
			if act_p1 == "2":
				self.p1.DEFENSE(int(act_p2),self.p2)

		if self.p1.alive():
			print("The winner is",self.p1.name)
		elif self.p2.alive():
			print("The winner is",self.p2.name)
		else:
			print("The fight end with draw!")


# Identitas robot
play = game(input('Nama robot player ke 1 : '), input('Nama robot player ke 2 : '))

# Tournament dimulai
play.start()