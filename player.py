import math
import random
class player:
    def __init__(self,letter):
        self.__letter = letter
    # def get_move(self,game):
    #     pass
class Random_computer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        move=random.choice(game)
        return move
class Human_player(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self):
        move=int(input('type the move(0-9) '))
        return move