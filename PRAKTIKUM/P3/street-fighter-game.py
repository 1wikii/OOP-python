import random

class Fighter:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def is_alive(self):
        return self.health > 0
    
    def attack(self, opponent):
        damage_dealt = random.randint(1, self.damage)
        opponent.health -= damage_dealt
        print(f"{self.name} attacks {opponent.name} and deals {damage_dealt} damage.")
        if not opponent.is_alive():
            print(f"{opponent.name} is knocked out.")

class Player:
    def __init__(self, name, health, damage):
        self.fighter = Fighter(name, health, damage)
        self.is_blocking = False

    def block(self):
        self.is_blocking = True
        print(f"{self.fighter.name} is now blocking.")

    def attack(self, opponent):
        if self.is_blocking:
            print(f"{self.fighter.name} is blocking and can't attack.")
        else:
            self.fighter.attack(opponent.fighter)

    def reset_blocking(self):
        self.is_blocking = False

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print(f"Welcome to Street Fighter! {self.player1.fighter.name} vs {self.player2.fighter.name}.")
        while self.player1.fighter.is_alive() and self.player2.fighter.is_alive():
            self.player1.reset_blocking()
            self.player2.reset_blocking()

            print(f"\n{self.player1.fighter.name}: {self.player1.fighter.health} HP\n{self.player2.fighter.name}: {self.player2.fighter.health} HP\n")

            action1 = input(f"{self.player1.fighter.name}, what do you want to do? (attack/block): ")
            if action1.lower() == "block":
                self.player1.block()
            else:
                self.player1.attack(self.player2)

            action2 = input(f"{self.player2.fighter.name}, what do you want to do? (attack/block): ")
            if action2.lower() == "block":
                self.player2.block()
            else:
                self.player2.attack(self.player1)

        if self.player1.fighter.is_alive():
            print(f"{self.player1.fighter.name} wins!")
        else:
            print(f"{self.player2.fighter.name} wins!")

player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")
player1 = Player(player1_name, 100, 20)
player2 = Player(player2_name, 100, 20)
game = Game(player1, player2)
game.play()
