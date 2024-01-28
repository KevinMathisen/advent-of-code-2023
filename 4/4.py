

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	ls = list(cont.strip().split("\n"))

	cards = []
	for line in ls:
		groups = line.split(": ")[1].split(" | ")

		winningNumsLine = groups[0].strip().split(' ')
		yourNumsLine = groups[1].strip().split(' ')

		cards.append([[int(num) for num in winningNumsLine if num != ""], [int(num) for num in yourNumsLine if num != ""] ])

	return cards

def calculateScoreCard(card):
	cardPoints = 0
	for yourNum in card[1]:
		for winningNum in card[0]:
			if yourNum == winningNum:
				if cardPoints == 0:
					cardPoints = 1
				else:
					cardPoints *= 2

	return cardPoints

# Task 1
def task1():
	sum = 0
	for card in ls:
		sum += calculateScoreCard(card)

	return sum

def calculateCopiesCard(card):
	cardPoints = 0
	for yourNum in card[1]:
		for winningNum in card[0]:
			if yourNum == winningNum:
				cardPoints += 1

	return cardPoints

# Task 2
def task2():
	
	for cardNum, card in enumerate(ls):		
		cardScore = calculateCopiesCard(card)

		for _ in range(cardCopies[cardNum]):
			for wins in range(cardNum+1, cardNum+cardScore+1):
				cardCopies[wins] += 1

	return sum(cardCopies)


test = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""




inputTxt = "y"
ls = setup((inputTxt == "y"), test)

cardCopies = []
for card in ls:
	cardCopies.append(1)

print(task1())

print(task2())


