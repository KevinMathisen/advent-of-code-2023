import re

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	ls = list(cont.strip().split("\n"))

	gNumbers = []
	gSymbols = []
	gGears = []
	for line in ls:
		numbers = re.finditer(r'\d+', line)
		symbols = re.finditer(r'[!@#$%^&*()\-_=+{}\[\]|;:\'",<>/?]', line)

		numbersLine = []
		symbolsLine = []
		gearsLine = []
		for number in numbers:
			numbersLine.append([int(number.group()), number.start(), number.end()-1])
		for symbol in symbols:
			symbolsLine.append(symbol.start())
			if symbol.group() == '*':
				gearsLine.append(symbol.start())

		gNumbers.append(numbersLine)
		gSymbols.append(symbolsLine)
		gGears.append(gearsLine)


	return gNumbers, gSymbols, gGears


def checkIfRowAdjacent(symbols, number):
	for symbol in symbols:
		if symbol >= number[1]-1 and symbol <= number[2]+1:
			return True
	return False

def checkIfNumHasAdjacentSym(lineNum, number):
	if checkIfRowAdjacent(gSymbols[lineNum], number):
		return True
	if lineNum > 0:
		if checkIfRowAdjacent(gSymbols[lineNum-1], number):
			return True
	if lineNum < len(gNums)-1:
		if checkIfRowAdjacent(gSymbols[lineNum+1], number):
			return True		

	return False

# Task 1
def task1():
	sum = 0
	for index, line in enumerate(gNums):
		for number in line:
			if checkIfNumHasAdjacentSym(index, number):
				sum += number[0]
	return sum

def checkIfRowAdjacentGear(numbers, gear):
	adjacent = []
	for number in numbers:
		if gear >= number[1]-1 and gear <= number[2]+1:
			adjacent.append(number[0])
	return adjacent

def checkIfGearHasTwoAdjacentNum(lineNum, gear):
	adjacent = []

	adjacent += checkIfRowAdjacentGear(gNums[lineNum], gear)
	if lineNum > 0:
		adjacent += checkIfRowAdjacentGear(gNums[lineNum-1], gear)
	if lineNum < len(gNums)-1:
		adjacent += checkIfRowAdjacentGear(gNums[lineNum+1], gear)

	if len(adjacent) == 2:
		return adjacent[0]*adjacent[1]
	
	return -1

# Task 2
def task2():
	
	sum = 0
	for index, line in enumerate(gGears):
		for gear in line: 
			ratio = checkIfGearHasTwoAdjacentNum(index, gear)
			if ratio != -1:
				sum += ratio

	return sum

test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

inputTxt = True
gNums, gSymbols, gGears = setup(inputTxt, test)

print(task1())

print(task2())


