from random import random

class Player:
	def __init__(self, prob):
		# Create a player with this probability
		self.prob = prob
		self.score = 0

	def winsServe(self):
		# Returns true with probability self.prob
		return random() <= self.prob

	def incScore(self):
		# Add a point to this player's score
		self.score = self.score + 1

	def getScore(self):
		#Return this player's current score
		return self.score

