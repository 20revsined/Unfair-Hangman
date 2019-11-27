import random, sys

class GenerateWord():
	def __init__(self, number, word):
		self.number = number
		self.word = word

	def getWord():
		WordList = []
		WordList.append("pig")
		WordList.append("astroid")
		WordList.append("forest")
		WordList.append("sunny")
		WordList.append("canyon")
		WordList.append("cheese")
		WordList.append("tomato")
		WordList.append("royal")
		WordList.append("cats")
		WordList.append("dogs")
		WordList.append("mountain")
		WordList.append("waterfall")
		WordList.append("deal")
		WordList.append("shout")
		WordList.append("run")
		WordList.append("lacrosse")
		WordList.append("soccer")
		WordList.append("baseball")
		WordList.append("guitar")
		WordList.append("football")
		WordList.append("hockey")
		WordList.append("baseball")
		WordList.append("basketball")
		WordList.append("salon")
		WordList.append("salmon")
		WordList.append("fish")
		WordList.append("shark")
		WordList.append("squid")
		WordList.append("whale")
		WordList.append("shrimp")
		WordList.append("abcdefghijklmnopqrstuvwxyz")

		return WordList[random.randint(0, len(WordList) - 1)]

class Guess():
	global GenerateWord
	word = GenerateWord.getWord()
	listWord = list(word)

	x = 0
	z = 0

	string = ""

	def toString(string):
		z = ""
		NewString = ""
		for z in list(string):
			NewString += z
		return NewString

	def encode(string):
		x = 0
		EncodedString = ""

		while x < len(string):
			EncodedString += "*"
			x += 1
		return EncodedString

	CodedWord = encode(word)

	print(CodedWord)

	listCodedWord = list(CodedWord)

	#print(listCodedWord)

	print("Welcome to Unfair Hangman! You will guess letters and try guess the correct word. Good luck!")

	guess = 0
	GuessLimit = len(word) + 3
	number = 0

	while True:
		letter = str(input("Please enter a letter."))
		number = listWord.count(letter)

		if guess == GuessLimit and "*" in listCodedWord:
			print("Sorry, you were unable to guess the word. The word was " + word + ".")
			sys.exit(0)

		if number > 0:
			while z < len(listCodedWord):
				if letter == listWord[z]:
					listCodedWord[z] = letter
				z += 1
			print(toString(listCodedWord))
			#guess += 1
			z = 0

		else:
			print(toString(listCodedWord))
		
		guess += 1

		if listCodedWord == listWord and guess <= GuessLimit:
			print("Congratulations! You guessed the word!")
			sys.exit(0)

		if(guess % 4 == 0):
			word = ""
			word = GenerateWord.getWord()
			CodedWord = ""
			CodedWord = encode(word)
			#listCodedWord = ""
			listCodedWord = list(CodedWord)
			GuessLimit = len(word) + 3
			print("New Word!\n" + CodedWord)
