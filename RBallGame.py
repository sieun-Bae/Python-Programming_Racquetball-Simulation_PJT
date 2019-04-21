class RBallGame:
	# A RBallGame represents a game in progress. A game has two players
	# and keeps track of which one is currently serving.

	def __init__(self, probA, probB):
		#Create a new game having players with the given probs.
		self.playerA = Player(probA)
		self.playerB = Player(probB)
		self.server = self.playerA # Player A always serves first

	def play(self):
		# Play the game to completion
		while not self.isOver():
			if self.server.winsServe():
				self.server.incScore()
			else:
				self.changeServer()

	def getScores(self):
		# Returns the current scores of player A and player B

		return self.playerA.getScore(), self.playerB.getScore()

	def isOver(self):
		# Returns game is finished (i.e. one of the players has won).

		a, b = self.getScores()
		return a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and b == 0)

	def changeServer(self):
		# Switch which player is serving
		
		if self.server == self.playerA:
			self.server = self.playerB
			
		else:
			self.server = self.playerA