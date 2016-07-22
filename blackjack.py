# BlackJack game - one player vs automated dealer
# The player can stand or hit and are able to pick betting amount
# Player's total amount of money should be tracked
# Alerts about losses, wins, busts, etc ...
import random
import sys

class Player(object):
	
	def __init__(self, name, score,money=100):
		self.name = name
		self.money = money
		self.score = score
	
	def add_money(self,amount):
		self.money += amount

	def take_money(self,amount):
		self.money -= amount

	def add_score(self,points):
		self.score += points

def draw(gamer):
	hand = random.randint(2,11)
# Each card should be assigned to its value
	if hand == 10:
		print(gamer.name + ' get J')
		J = gamer.add_score(10)
		print(gamer.name + ' score is ' + str(gamer.score))
	elif hand == 11:
		if (gamer.score + 11) <= 21:
			print(gamer.name + ' get A')				
			A = gamer.add_score(11)
			print(gamer.name + ' score is ' + str(gamer.score))
		elif (gamer.score + 11) > 21:
			print(gamer.name + ' get A')	
			A1 = gamer.add_score(1)
			print(gamer.name + ' score is ' + str(gamer.score))
	else:
		print(gamer.name + ' get ' + str(hand))
		gamer.add_score(hand)
		print(gamer.name + ' score is ' + str(gamer.score))
# Player class shows the amount of money player have and the score of player

sam = Player('You', 0, money=100)
dealer = Player('Dealer', 0, 0)
# Dealer get his card
draw(dealer)
# Player choose the amount for the bet.
bet = int(input("Your bet > "))
sam.take_money(bet)
print("You have " + str(sam.money) + " money")
# Player gets two cards
draw(sam)
draw(sam)
while sam.score < 21:
	# Player choose to stand or hit another card		
		hit = input("Want to draw a card? Y/N ")
		if hit.lower() == 'y':
			print("You have " + str(sam.money) + " money left")
			draw(sam)			
			if sam.score > 21:
				print("You got busted!")
		elif hit.lower() == 'n':
			print("Your score is " + str(sam.score))
			break
		else:
			print("Wrong command!")
			continue

def dealer_ai():
	while dealer.score < 17:
		draw(dealer)
	if dealer.score > 21:
		print("Dealer got busted. You won!")

# Player could win if he gets 21 or BJ with first two cards and dealer doesn't
if 21 >= sam.score > dealer.score or 21 > dealer.score == sam.score:
	dealer_ai()
	if sam.score == dealer.score <= 21:
		print("It's a tie!")
	elif 21 >= sam.score > dealer.score:
		print("Congratulations! You Won!")
	elif sam.score < dealer.score <= 21:
		print("You loose. Too bad.")

