import random


################# CARD CLASSES #################
class Card:
  #TODO refactor this
  """
      Gaming card class.
      Initialises the class with all the possibles combinations of suit
      and rank, and a card value for the game
  """
  #TODO Card docs with arguments
  def __init__(self, suit, rank, value):
        self.__suit = suit
        self.__rank = rank
        self.__value = value

  def ranksuit(self):
      """Method for printing the rank and suit"""
      return f'{self.rank} of {self.suit}'
  
  @property
  def suit(self):
    return self.__suit
  
  @property
  def rank(self):
    return self.__rank
  
  @property  
  def value(self):
    return self.__value
  
  @suit.setter
  def suit(self, suit):
    self.__suit = suit
  
  @rank.setter
  def rank(self, rank):
    self.__rank = rank
  
  @value.setter
  def value(self, value):
    self.__value = value

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
  
  def __init__(self, suit, rank, value):
    """ Initializes the values corresponding to the Truco game """
    #TODO TrucoCard docs
    super().__init__(suit, rank, value)
  
  ##Redefine the ranksuit method to be in spanish  
  def ranksuit(self):
    """ Method for printing the rank and suit in spanish"""
    return f'{self.rank} de {self.suit}'
  
  @property
  def n_rank(self):
    """
      Method for returning an integer with the numerical value of the rank
      
      Returns
      -------
        int : the numerical value of the rank
    """
    
    # All ranks to numbers
    ranks_numbers = ['', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete'
                    , '', '', 'Diez', 'Once', 'Doce']
    num_value = ranks_numbers.index(self.rank)
    return num_value
    
    
################# DECK CLASSES #################
class Deck:
  """
      Creates a deck, with methods to shuffle cards
      and deal one card to the player
      
      Normal Deck
      
      Methods:
      --------
      shuffle_cards : returns none
      deal_one      : returns the dealt card (Card) and removes it from the Deck
      restart_deck  : returns none
      add_card      : returns none
  """
  # Standard SUIT and RANKS 
  SUITS = ('Hearts','Diamonds','Spades','Clubs')
  RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
          'Ten', 'Jack', 'Queen', 'King', 'Ace')
  
  def __init__(self):
    """For each suit and rank, create a card object"""
    self.__cards = []
    for suit in SUITS:
        for rank in RANKS:
            self.add_card(Card(suit,rank))
            
  @property
  def cards(self):
    return self.__cards

  def shuffle_cards(self):
    """Imports random for shuffling the deck"""
    random.shuffle(self.cards)

  def deal_one(self):
    """Deals one to the player and removes it from the deck"""
    return self.cards.pop()
  
  # Here I have the option of Restarting the full deck with this method,
  # or add the cards used in the players hands with the add_card method in
  # the parent class. I'm not very well versed in efficiency (yet) and 
  # I don't know which one will be better and the end
  # I think that memory is more expensive that cpu power, so I'll go with 
  # readding the cards in the player hands and not redoing the whole deck
  # every hand waiting for the garbage collector to eventually collect
  # the extra deck used 
  def restart_deck(self):
    """ Restarts the deck with all the cards available for next round """
    self.__init__(self)
    
  def add_card(self, card):
    """
      Add a card to the deck
      Arguments
      ---------
      card  : the card(Card) to be added to the Deck
    """
    self.cards.append(card)


class TrucoDeck(Deck):
  """
      Creates a deck, with methods to shuffle cards
      and deal one card to the player
      
      Deck for playing Truco
      
      Methods:
      --------
      shuffle_cards : returns none
      deal_one      : returns the dealt card (Card) and removes it from the Deck
  """
            
  # Add all the cards to the Deck
  def __init__(self):
    """For each suit and rank, create a card object with Truco values"""
    
    SUITS = ('Espadas','Basto','Copas','Oro')
    RANKS = ('Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete',
              'Diez', 'Once', 'Doce')
    VALUES = {}
    VALUES['UnoEspadas']    = 1
    VALUES['UnoBasto']      = 2
    VALUES['SieteEspadas']  = 3
    VALUES['SieteOro']      = 4
    VALUES['TresEspadas']   = 5
    VALUES['TresBasto']     = 5
    VALUES['TresOro']       = 5
    VALUES['TresCopas']     = 5
    VALUES['DosEspadas']    = 6
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
    
    # Take the value of the card from the VALUES constant
    
    self.__cards = []
    for suit in SUITS:
        for rank in RANKS:
          value_index = str(rank) + str(suit)
          self.add_card(TrucoCard(suit, rank, VALUES[value_index]))
  
  @property
  def cards(self):
    return self.__cards   



################# HAND CLASSES #################
class TrucoHand:
  """
    A card hand class to play truco
    #TODO better docs
  """
  
  def __init__(self):
    """ Initialises the hand with an empty set of cards and a value of 0 """
    self.__cards = [] 
    self.__puntos = 0

  @property
  def cards(self):
    """ Returns the card list """
    return self.__cards

  def add_card(self, card):
    """
      Adds one card to the hand
      
      Arguments
      ---------
      (Card)  : Card to be added to the hand
    """ 
    self.cards.append(card)

  @property
  def puntos(self):
    return self.__puntos

  @puntos.setter  
  def puntos(self, n):
    self.__puntos = n

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

  @property
  def has_flor(self):
    """
      Method for knowing if the player has flor
      Flor is when the player has 3 cards of the same suit
      
      Returns
      -------
      boolean : True or False depending if the payer has flor
    """
    if (self.cards[0].suit == \
        self.cards[1].suit == \
        self.cards[2].suit):
      return True
    else:
      return False
    
  def calculate_puntos(self):
    """ Method to calculate how much the player has in envido or flor """
    equal_suits = []
    # If the player has flor, add all 3 cards in the count
    if self.has_flor:
      equal_suits.append(self.cards[0])
      equal_suits.append(self.cards[1])
      equal_suits.append(self.cards[2])
    elif self.cards[0].suit == self.cards[1].suit:
      equal_suits.append(self.cards[0])
      equal_suits.append(self.cards[1])
    elif self.cards[0].suit == self.cards[2].suit:
      equal_suits.append(self.cards[0])
      equal_suits.append(self.cards[2])
    elif self.cards[1].suit == self.cards[2].suit:
      equal_suits.append(self.cards[1])
      equal_suits.append(self.cards[2])
    
    # The ranks that have no value in envido or flor
    zero_ranks = (10, 11, 12)
    
    tanto = 0
    #TODO make ranks Letters to numbers
    # If there are no cards of the same suit, pick the highest card
    if not equal_suits:
      highest = 0
      for c in self.cards:
        if c.n_rank not in zero_ranks:
          if c.n_rank > highest:
            highest = c.n_rank
      self.puntos = tanto
    else:
      tanto += 20
      for c in equal_suits:
        if c.n_rank not in zero_ranks:
          tanto += c.n_rank
      self.puntos = tanto


  def add_cards(self, deck):
    """
      Add 3 cards to the player hand
      Calculates the total envido or flor points at the same time
      
      Arguments
      ---------
      Deck  : the deck from which the cards are taken
    """
    self.add_card(deck.deal_one())
    self.add_card(deck.deal_one())
    self.add_card(deck.deal_one())
    
    self.calculate_puntos()
    
  def end_hand(self, deck):
    """
      Clears the player hand and adds the cards to the deck 
      Arguments
      ---------
      deck  : the deck(TrucoDeck) to put the player cards in
    """
    while self.cards:
      deck.add_card(self.cards.pop())
    del self.cards
    self.cards = []
    self.puntos = 0