from deckbuild import *
from cardplayer import *

mazo = TrucoDeck()
mazo.shuffle_cards()

player = TrucoPlayer('Pepe')
player.hand.add_cards(mazo)








