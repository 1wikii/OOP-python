import random

class Game:
    def __init__(self, player):
        self.player = player
        self.random_number = random.randint(1, 100)
        self.player_guesses = []

    def play(self):
        print(f"Welcome {self.player.name}! Let's play a game of Guess the Number.")
        while True:
            guess = self.player.guess()
            self.player_guesses.append(guess)
            if guess == self.random_number:
                print(f"Congratulations {self.player.name}, you have won the game in {len(self.player_guesses)} attempts.")
                break
            elif guess < self.random_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

class Player:
    def __init__(self, name):
        self.name = name

    def guess(self):
        guess = int(input(f"{self.name}, please enter your guess: "))
        return guess

player = Player(input("Enter your name: "))
game = Game(player)
game.play()
