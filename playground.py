import deckbuild


class DumbClass:
    def __init__(self, p):
        self._ciao = p

    @property
    def ciao(self):
        return self._ciao

    @ciao.setter
    def ciao(self, v):
        self._ciao = v
        
        
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
  def __init__(self):
    self.mano = None
    self.primera = None
    self.segunda = None
    self.tercera = None
    self.flor = False
    self.puntos = 1 # Truco 2, Retruco 3, Vale cuatro 4
  
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
    pass
    
  
  #TODO calculate draw
  #When in first round, the game is won in the second round if there's not a draw in the second
  #When it's in the second round, the game is won at the third
  #When it's in the third round, the game is won by whoever has won the first hand
  #If all 3 rounds are draw, wins whoever is mano
  #TODO add the winning points to the team
  def parda(self):
    pass
  #TODO do the game flow

VALUES = {}
VALUES['UnoEspadas']    = 1
VALUES['UnoBasto']      = 2
VALUES['SieteEspadas']  = 3
VALUES['SieteOro']      = 4
VALUES['TresEspadas']   = 5
VALUES['TresBasto']     = 5
VALUES['TresOro']       = 5
VALUES['TresCopas']     = 5
VALUES['DosEspada']     = 6
VALUES['DosBasto']      = 6
VALUES['DosOro']        = 6
VALUES['DosCopas']      = 6
VALUES['UnoOro']        = 7
VALUES['UnoCopas']      = 7
VALUES['DoceEspadas']   = 8
VALUES['DoceBasto']     = 8
VALUES['DoceOro']       = 8
VALUES['DoceCopas']     = 8
VALUES['OnceEspadas']   = 9
VALUES['OnceBasto']     = 9
VALUES['OnceOro']       = 9
VALUES['OnceCopas']     = 9
VALUES['DiezEspadas']   = 10
VALUES['DiezBasto']     = 10
VALUES['DiezOro']       = 10
VALUES['DiezCopas']     = 10
VALUES['SieteCopas']    = 11
VALUES['SieteBasto']    = 11
VALUES['SeisEspadas']   = 12
VALUES['SeisBasto']     = 12
VALUES['SeisOro']       = 12
VALUES['SeisCopas']     = 12
VALUES['CincoEspadas']  = 13
VALUES['CincoBasto']    = 13
VALUES['CincoOro']      = 13
VALUES['CincoCopas']    = 13
VALUES['CuatroEspadas'] = 14
VALUES['CuatroBasto']   = 14
VALUES['CuatroOro']     = 14
VALUES['CuatroCopas']   = 14

rank = 'Doce'
suit = 'Oro'

value_index = rank + suit

print(VALUES[value_index])

ronda = Round()
print(ronda.puntos)

ronda.puntos = 15

print(ronda.puntos)
print(ronda.flor)

dumb = DumbClass(10)




