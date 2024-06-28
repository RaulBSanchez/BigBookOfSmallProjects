"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():

	print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
	Pico           One digit is correct but in the wrong position.
	Fermi          One digit is correct and in the right position.
	Bagels         No digit is correct. 
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))
	
	while True:
		#this is the secret number the player needs to guess:
		secretNum = getSecretNum()
		print('I have thought of a number')
		print('  You have {} guesses to get it.'.format(MAX_GUESSES))

		numGuesses = 1
		while numGuesses <= MAX_GUESSES:
			guess = ''
			# keep looping until they enter a valid guess:
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Guess #{}: '.format(numGuesses))
				guess = input('> ')

			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1

			if guess == secretNum:
				break # they're correct so break out of the loop

			if numGuesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}'.format(secretNum))

		print('Do you wnat to play again? (yes or no)')
		if not input('> ').lower().startswith('y'):
			break
		print('Thanks for playing')

def getSecretNum():
	"""
	Returns a string made up of unique digits
	"""
	numbers = list('0123456789')
	random.shuffle(numbers)

	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum


def getClues(guess, secretNum):
	if guess == secretNum:
		return 'You got it'

	clues = []

	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			# a correct digit is in place
			clues.append('Fermi')
		elif guess[i] in secretNum:
			# a correct digit in the incorrect place
			clues.append('Pico')
	if len(clues) == 0:
		return 'Bagels'

	else:
		clues.sort()

		return ''.join(clues)






if __name__ == '__main__':
	main()





