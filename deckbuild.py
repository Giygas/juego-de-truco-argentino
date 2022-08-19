import random


################# CARD CLASSES
class Card:
  """
      Gaming card class.
      Initialises the class with all the possibles combinations of suit
      and rank, and assigns a value of 0 to each card, needs to be inherited 
      for the corresponding game
  """
  def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = 0

  def ranksuit(self):
      """Method for printing the rank and suit"""
      return f'{self.rank} of {self.suit}'
  
  def get_suit(self):
    return self.suit
  
  def get_rank(self):
    return self.rank
    
  def get_value(self):
    return self.value
  
  def set_suit(self, suit):
    self.suit = suit
  
  def set_rank(self, rank):
    self.suit = suit
    
  def set_value(self, value):
    self.suit = suit

class Bjcard(Card):
  """
    Gaming card class for Black Jack. The values are set for this game
    Inherits from class Card
  """
  
  VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
  
  def __init__(self, suit, rank):
    """ Initializes the values corresponding to the Black Jack game """
    super().__init__(suit, rank)
    self.set_value(VALUES[rank])
    

class TrucoCard(Card):
  """
    Gaming card class for Truco. The values are set for this game
    Inherits from class Card
  """
  
  ## Create values for each combination of cards
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
  
  def __init__(self, suit, rank):
    """ Initializes the values corresponding to the Truco game """
    super().__init__(suit, rank)
    # Take the value of the card from the VALUES constant
    value_index = rank + suit
    self.set_value(VALUES[value_index])

  def ranksuit(self):
    """ Method for printing the rank and suit """
    return f'{self.get_rank} de {self.get_suit}'

################# DECK CLASSES
class Deck:
  """
      Creates a deck, with methods to shuffle cards
      and deal one card to the player
      
      Normal Deck
      
      Methods:
      --------
      shuffle_cards : returns none
      deal_one      : returns the dealt card (Card) and removes it from the Deck
  """
  # Standard SUIT and RANKS 
  SUITS = ('Hearts','Diamonds','Spades','Clubs')
  RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
          'Ten', 'Jack', 'Queen', 'King', 'Ace')
  
  def __init__(self):
    """For each suit and rank, create a card object"""
            
    self.cards = []
    for suit in SUITS:
        for rank in RANKS:
            self.cards.append(Card(suit,rank))

  def shuffle_cards(self):
      """Imports random for shuffling the deck"""
      random.shuffle(self.cards)

  def deal_one(self):
      """Deals one to the player and removes it from the deck"""
      return self.cards.pop()


class TrucoDeck:
  """
      Creates a deck, with methods to shuffle cards
      and deal one card to the player
      
      Deck for playing Truco
      
      Methods:
      --------
      shuffle_cards : returns none
      deal_one      : returns the dealt card (Card) and removes it from the Deck
      restart_deck  : returns none
  """
  def __init__(self):
    
    SUITS = ('Espadas','Basto','Copas','Oro')
    RANKS = ('Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete',
              'Diez', 'Once', 'Doce')
              
    # Add all the cards to the Deck          
    super().__init__(self)
  
  def restart_deck(self):
    """ Restarts the deck with all the cards available for next round """
    super().__init__(self)
  
    
################# HAND CLASSES
class TrucoHand:
  """
    A card hand class to play truco
    #TODO better docs
  """
  
def __init__(self):
  """ Initialises the hand with an empty set of cards and a value of 0 """
  self.cards = [] 
  self.value = 0

def __str__(self, align=0):
  # TODO redo this, normally the player cannot see the opponent hand
  """
      Printing the cards in the hand and the total value
      If it's the player it aligns to the left, and right for the super AI
      
      Arguments:
                  0 (Default) : aligns the elements to the left
                  1           : aligns the elements to the right

  """
  output = ""
  if align == 0:
      for card in self.cards:
          output += card.ranksuit() + '\n'
      # output += f'\tTotal Hand: {self.value}' #TODO maybe reuse this code for printing envido
  else:
      for card in self.cards:
          output += f'{" ":>60}' + card.ranksuit() + '\n'
      # output += f'{" ":>50} {self.value} :Total Hand' #TODO same thing for envido
  return output

def has_flor():
  """
    Method for knowing if the player has flor
    Flor is when the player has 3 cards of the same suit
    
    Returns
    -------
    boolean : True or False depending if the payer has flor
  """
  if (self.cards[0].suit == self.cards[1].suit == self.cards[2].suit):
    return True
  else:
    return False
  
def total_envido(self):
  """ Method to see how much the player has in envido """
  pass
  #TODO calculate the envido total
  
  
def add_card(self, card):
  """
    Add a card to the player hand
    
    Arguments
    ---------
    TrucoCard  : a card to add to the player hand
  """
  self.cards.append(card)
  
def clear_hand(self):
  """ Method for clearing the player hand """
  while self.cards:
    self.cards.pop()
  del self.cards
  self.cards = []