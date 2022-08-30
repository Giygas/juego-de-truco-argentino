class TrucoTeam:

  def __init__(self, tn):
    self.__team = tn
    self.__players = []
    self.__total_puntos = 0
  
  @property
  def total_puntos(self):
    return self.__total_puntos
    
  @total_puntos.setter
  def total_puntos(self, amt):
    self.__total_puntos += amt
  
  @property
  def players(self):
    return self.__players
    
  @players.setter
  def players(self, player):
    self.__players.append(player)
    
  @property
  def team(self):
    return self.__team
  
tt = TrucoTeam(1)

print(tt.total_puntos)
print(len(tt.players))
print(tt.team)

tt.total_puntos = 15

print(tt.total_puntos)