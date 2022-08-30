class TrucoPlayer:
  #TODO Player documentation
  def __init__(self, name):
    self.__name 
    self.__hand = TrucoHand()
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, nm):
    self.__name = nm
  
  @property
  def hand(self):
    return self.__hand
  
  @hand.setter
  def hand(self, hand):
    self.__hand = hand    
  
  
  def __str__(self):
    return 'Player: \t' + self.name