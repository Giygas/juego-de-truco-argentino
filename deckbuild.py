import random

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
  

class Bjcard(Card):
  """
    Gaming card class. The values are set for the BlackJack game
    Inherits from class Card
  """
  
  VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
  
  def __init__(self, suit, rank):
    """ Initializes the values corresponding to the Black Jack game """
    super().__init__(suit, rank)
    self.value = VALUES[rank]
    


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


class Dtruco:
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
  
  