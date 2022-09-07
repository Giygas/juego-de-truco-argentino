import os
from time import sleep
from deckbuild import *


def clrscr():
  if (os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')
    
#TODO class TrucoGame
#TODO TrucoGame counts the total points for falta envido
# Truco points counted per round
# This class creates the teams (team 1 and team 2)
# This class should manage who's mano
# The player that wins plays first the second hand
# And there the round continue

# Maybe create a list of players and his turns, then continue from the player that won
# Team mano keeps counting if all the players have a draw

# team 1 player 1 plays
# ask for input
# # show possibilities, cantar truco, envido o flor
# # last round check for 4 in the other team
# team 2 player 1 plays
# team 1 player 2 plays
# team 2 player 2 plays
class TrucoGame():
  
  def __init__(self):
    self.__teams = []
    self.__players = 0
    self.__hplayers = 0
    self.__bots = 0
    self.__deck = TrucoDeck()
  
  @property
  def teams(self):
    return self.__teams
    
  @property
  def players(self):
    return self.__players
    
  @players.setter
  def players(self, num):
    self.__players = num
  
  @property
  def hplayers(self):
    return self.__hplayers
    
  @hplayers.setter
  def hplayers(self, num):
    self.__hplayers = num
  
  @property
  def bots(self):
    return self.__bots
    
  @bots.setter
  def bots(self, num):
    self.__bots = num
    
  def game_status():
    #TODO clears the screen and prints the actual game status
    clrscr()
    if self.players != 0:
      pass
  def ask_players():
    max_players = 6
    no_pair = (1, 3, 5)
    try:
      players_num = int(input("Ingrese el numero de jugadores (Máximo 6): "))
      if players_num > max_players:
        print("Lo siento, el máximo de jugadores es 6")
        time.sleep(2)
      elif players_num in no_pair:
        print("Lo siento, no es posible jugar con un número impar de jugadores")
        time.sleep(2)
      else:
        self.players = players_num
    except TypeError:
      print("Lo siento, tiene que ingresar un entero")
      time.sleep(2)
      
game = TrucoGame()
#TRUCOGAME should initialize the deck and teams
while game.players == 0:
  game.ask_players()

game.players = 2 #number of players
game.bots = 1 #number of players that are bots
game.human_players() # Request name for the human players (for each player that are not a bot)
game.split_teams()  # Request how the teams are going to be (mostly if the human players are playing together or with a bot)
                  # In this method the trucoteam will be created
game.play_round() # Start a truco round. At the end it should restart the deck and 