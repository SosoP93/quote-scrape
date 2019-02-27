from random import choice,shuffle

class Card:

	def __init__(self):
		self.suit = ["Hearts", "Diamonds",  "Clubs", "Spades"]
		self.value = list(("A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")))

	def __repr__(self):
		return f"{choice(self.value)} of {choice(self.suit)}"

class Deck:

	def __init__(self):
		self.cards = Card()
		lst = []
		for s in self.cards.suit:
			lst += [f"{v} of {s}" for v in self.cards.value]
		self.cards = lst	

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def _deal(self, num=1):
		cards_removed = []
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		elif num < self.count(): 
			while num:
				num -= 1
				# cards_removed.append(self.cards.pop())
				chosen_card = choice(self.cards)
				cards_removed.append(chosen_card)
				self.cards.remove(chosen_card)
			return cards_removed

		else:
			while self.count():
				# cards_removed.append(self.cards.pop())
				chosen_card = choice(self.cards)
				cards_removed.append(chosen_card)
				self.cards.remove(chosen_card)
			return cards_removed
			 	

	def count(self):
		return len(self.cards)

	def shuffle(self):
		if self.count() != 52:
			raise ValueError("Only full decks can be shuffled")	
		return shuffle(self.cards)

	def deal_card(self):
		card = self._deal()
		return card[0]

	def deal_hand(self, cards):
		hand = self._deal(cards)
		return hand







		


# first_deck = Deck()
# print(first_deck)
# first_deck.shuffle()
# # print(first_deck.deal_card())
# for i in first_deck.deal_hand(21): 
# 	print(i)
# print(first_deck)



