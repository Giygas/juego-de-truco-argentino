#TODO a round of Truco
class Round:
  #TODO who's mano
  #TODO clear all players hands at the end of the round
  #TODO track truco, retruco and vale cuatro
  #TODO documentation
  # A round consists of players, and how many rounds they have won
  # Make primera, segunda y tercera
  # Not possible to say Truco to a 4 in tercera
  # Players must be initialized before the round
  # Make teams of players (Maybe a second version)
  def __init__(self, teams, deck):
    self.__teams = teams
    self.__mano = None
    self.__primera = None
    self.__segunda = None
    self.__tercera = None
    self.__flor = False
    self.__puntos = 1 # Truco 2, Retruco 3, Vale cuatro 4
  
  @property
  def primera(self):
    return self.__primera
    
  @primera.setter
  def primera(self, team):
    self.__primera = team
    
  @property
  def segunda(self):
    return self.__segunda
    
  @segunda.setter
  def segunda(self, team):
    self.__segunda = team
  
  @property
  def tercera(self):
    return self.__tercera
    
  @tercera.setter
  def tercera(self, team):
    self.__tercera = team
  
  @property
  def flor(self):
    return self.__flor
  
  @flor.setter
  def flor(self, bool):
    self.__flor = bool
  
  @property
  def puntos(self):
    return self.__puntos
    
  @puntos.setter
  def puntos(self, p):
    self.__puntos = p
    
  
  def end_ronda(self):
    #TODO calculate who has won here
    
    
  
  #TODO calculate draw
  #When in first round, the game is won in the second round if there's not a draw in the second
  #When it's in the second round, the game is won at the third
  #When it's in the third round, the game is won by whoever has won the first hand
  #If all 3 rounds are draw, wins whoever is mano
  #TODO add the winning points to the team
  def parda(self):
    if 
  #TODO do the game flow