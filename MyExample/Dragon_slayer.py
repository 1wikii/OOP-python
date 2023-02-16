
class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def is_alive(self):
        return self.health > 0

    def is_low(self):
        return self.health <= 30 
    
    def attack(self, dragon):
        dragon.health -= self.damage
        if dragon.health < 0:
            dragon.health = 0
            print(f"{self.name}     || {self.health}\n{dragon.name} || {dragon.health}\n")
        else:
            print(f"{self.name}     || {self.health}\n{dragon.name} || {dragon.health}\n")
        
        if not dragon.is_alive():
                print(f"The dragon {dragon.name} is defeated.")

    def attk_plus(self,dmg):
        self.damage += dmg

class Dragon (Player):
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def is_alive(self):
        return self.health > 0
    
    def attack(self, player):
        player.health -= self.damage

        if player.health < 0 :
            player.health = 0
            print(f"{self.name} || {self.health}\n{player.name}     || {player.health}\n")
        else:
            print(f"{self.name} || {self.health}\n{player.name}     || {player.health}\n")
        
        if not player.is_alive():
            print("Defeated")

def game_start():

    play, health = True, 100 
    player_name = input("Enter your name : ")

    dragon = Dragon("Red Boar", health, 10)
    player = Player(player_name, health, 10)

    while play:
        play = False

        while dragon.is_alive() and player.is_alive():
            
            dragon.attack(player)
            player.attack(dragon)
            
            if player.is_low():
                player.attk_plus(30)


print("Welcome to Dragom Slayer\n------------------------")
game_start()
