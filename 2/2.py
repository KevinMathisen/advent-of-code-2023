

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	ls = list(cont.strip().split("\n"))

	games = []
	for line in ls:
		game_parts = line.split(": ")[1].split("; ")

		game = []
		for game_part in game_parts:
			game_part_temp = []

			draws = game_part.split(", ")
			for draw in draws:
				amount, color = draw.split(" ")
				game_part_temp.append((int(amount), color))

			game.append(game_part_temp)

		games.append(game)

	return games

def checkIfPossible(game):
	for set in game:
		counts = {"red": 0, "green": 0, "blue": 0}

		for draw in set:
			counts[draw[1]] += draw[0]

		for color, count in counts.items():
			if count > requirements[color]:
				return False

	return True

# Task 1
def task1():
	
	sum = 0
	for i, game in enumerate(ls):
		if checkIfPossible(game):
			sum+= i+1

	return sum

def checkSmallestPossible(game):
	smallestPossibleValue = {"red": 0, "green": 0, "blue": 0}
	
	for set in game:
		counts = {"red": 0, "green": 0, "blue": 0}

		for draw in set:
			counts[draw[1]] += draw[0]

		for color, count in counts.items():
			if count > smallestPossibleValue[color]:
				smallestPossibleValue[color] = count

	power = 1
	for count in smallestPossibleValue.values():
		power *= count

	return power

# Task 2
def task2():
	
	sum = 0
	for game in ls:
		sum += checkSmallestPossible(game)
			
	return sum


requirements = {"red": 12, "green": 13, "blue": 14}

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

inputTxt = "y"
ls = setup((inputTxt == "y"), test)

print(task1())

print(task2())


