from csv import reader
from random import choice


class Game:

	def __init__(self, file):
		self.file = file


	def gather_quotes(self):
		with open(self.file, encoding = "utf-8") as file:
			csv_read = reader(file)
			return list(csv_read)

	def choose_quote(self):
		quotes = self.gather_quotes()
		quote = choice(quotes)
		return quote

	def display_question(self, quote):
		question = quote[1]
		print("Who is the author of the following quote?")
		print(question)

	def give_hint(self, quote, count):
		if count == 3:
			print(f"author was born {quote[-2]}")
		else:
			print(f"Author's first name begins with {quote[0][0]}")


	def check_answer(self, answer, quote):
		if answer.lower() == quote[0].lower():
			return True
		else:
			return False



play = Game("quotes.csv")
player_name = input("Please enter your name: ")
quote = play.choose_quote()

play.display_question(quote)
print("\n")
answer = input("Enter answer: ")

count = 3
while count > 0:
	if play.check_answer(answer, quote):
		print("You got it right!")
		break
	elif count == 1:
		print(f"You lose, the answer is {quote[0]}")
		break
	else:
		play.give_hint(quote, count)
		count -= 1
		answer = input("Enter answer: ")


another_round = input("Play again? (Y for yes, N for no) ")
if another_round.upper() == "Y":
	''' execute function to play game again'''
	print("restarting game.....beep.....boop")
else:
	print("Thank you for playing sucka")