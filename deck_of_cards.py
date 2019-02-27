from random import choice,shuffle

class Card:

	def __init__(self, suit, value):
		# self.suit = ["Hearts", "Diamonds",  "Clubs", "Spades"]
		# self.value = list(("A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")))
		self.suit = suit
		self.value = value

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:

	def __init__(self):
		suits = ["Hearts", "Diamonds",  "Clubs", "Spades"]
		values = list(("A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")))
		self.cards = [Card(suit, value) for suit in suits for value in values]	
		

	def __repr__(self):
		return "Deck of {} cards".format(self.count())

	def _deal(self, num):
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		count = self.count()
		actual = min([num,count])
		removed = self.cards[:actual]
		self.cards = self.cards[actual:]
		return removed

	def count(self):
		return len(self.cards)

	def shuffle(self):
		if self.count() != 52:
			raise ValueError("Only full decks can be shuffled")	
		return shuffle(self.cards)

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, cards):
		hand = self._deal(cards)
		return hand







		


first_deck = Deck()
first_deck.shuffle()
print(first_deck.cards)
# print(first_deck)
print(first_deck.deal_card())
# first_deck.shuffle()
print(first_deck.deal_hand(5))
print(first_deck.deal_hand(50))
print(first_deck.deal_hand(2))




