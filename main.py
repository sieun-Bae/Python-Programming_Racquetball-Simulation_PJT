from Player import Player
from RBallGame import RBallGame
from SimStats import SimStats



def printIntro():
	print("This program simulates games of racquetball between two")
	print('players called "A" and "B". The ability of each player is')
	print("the player wins the point when serving. Player A always")
	print("has the first serve.\n")

def getInputs():
	#returns the three simulation parameters
	a = float(input("What is the prob. player A wins a serve? "))
	b = float(input("What is the prob. player B wins a serve? "))
	n = int(input("How many games to simulate? "))
	return a, b, n

def main():
	printIntro()

	probA, probB, n = getInputs()

	# Play the games
	stats = SimStats()
	for i in range(n):
		theGame = RBallGame(probA, probB)
		theGame.play()
		stats.update(theGame)

	# Print the results
	stats.printReport()

if __name__ == "__main__":
	main()