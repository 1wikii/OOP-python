import random as rdm

class Base_Hero:
	def __init__(self, name, health, attack, defense, mana):
		self.__name = name
		self.__health = health
		self.__attack = attack
		self.__defense = defense
		self.__mana = mana

	def is_alive(self):
		return self.__health > 0

	def is_defense(self):
		return self.__defense > 0


	# GETTER n SETTER
	def name(self):
		return self.__name

	def health(self):
		return self.__health 

	def set_health(self, value):
		self.__health = value

	def attack(self):
		return self.__attack

	def set_attack(self, value):
		self.__attack = value

	def defense(self):
		return self.__defense 

	def set_defense(self, value):
		self.__defense = value

	def mana(self):
		return self.__mana 

	def set_mana(self, value):
		self.__mana = value

class Hero(Base_Hero):
	def __init__(self, name, health, attack, defense, mana):
		super().__init__(name,health,attack,defense,mana)


	def skill(self, skill_name, hero) -> int:
		skill_list = {"earth": 50,"fire": 60,"thunder": 70,"wind": 30,"water": 20}

		if hero.mana() >= 50:
			for i in skill_list:
				if i == skill_name.lower():
					mana_left = hero.mana() - 50
					hero.set_mana(mana_left)
					return skill_list[i]
		else:
			print("Not enough mana!")		
		return 0

	def receive_attack(self, damage, skill=0):
		damage += skill
		if self.is_defense():
			defen = self.defense() - damage
			if defen > 0:
				self.set_defense(defen)
			else:
				self.set_defense(0)
				H = self.health() + defen
				self.set_health(H)
		else:
			H = self.health() - damage
			self.set_health(H)


aldous = Hero("Aldous", 100, 40 ,30 ,100)
tigreal = Hero("Tigreal", 150, 20 ,50 ,100)
moskov = Hero("Moskov", 80, 60 ,30 ,120)

monster = Hero("Monster", 200, 60, 50, 0)


while aldous.is_alive() and tigreal.is_alive() and moskov.is_alive() and monster.is_alive():

	# GAME BAR
	print(aldous.name(), "|", aldous.health(), "|", "|",aldous.defense(),"|")
	print(tigreal.name(), "|", tigreal.health(), "|", "|",tigreal.defense(),"|")
	print(moskov.name(), "|", moskov.health(), "|", "|",moskov.defense(),"|\n")
	print(monster.name(), "|", monster.health(), "|", "|",monster.defense(),"|")

	chH = input("\n*****HERO*****\n1. Aldous\n2. Tigreal\n3. Moskov\nPilih Hero :")
	chS = input("\n~Basic\n~Fire\n~Earth\n~Water\n~Thunder\n~Wind\nPilih Skill :")

	if chH == "1":
		monster.receive_attack(damage=aldous.attack() , skill=aldous.skill(chS, aldous))
		aldous.receive_attack(damage=monster.attack())
	elif chH == "2":
		monster.receive_attack(damage=tigreal.attack() , skill=tigreal.skill(chS, tigreal))
		tigreal.receive_attack(damage=monster.attack())
	elif chH == "3":
		monster.receive_attack(damage=moskov.attack() , skill=moskov.skill(chS, moskov))
		moskov.receive_attack(damage=monster.attack())
	else:
		print("Hero's not exist!")

if monster.is_alive():
	print("MONSTER WIN, THE HERO's CANNOT PROTECT THE WORLD !!!")
else:
	print("MONSTER DEFEATED, THE HERO's SUCCEED PROTECT THE WORLD.")
