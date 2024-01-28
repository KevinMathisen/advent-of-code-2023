

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	ls = list(cont.split("\n"))
	ls.remove("")

	return ls



# Task 1
def task1():
	sum = 0

	for line in ls:
		firstNum = ''
		lastNum = ''
		for char in line:
			if char.isdigit():
				if (firstNum == ''):
					firstNum = char

				lastNum = char

		sum += int(firstNum+lastNum)
		
	return sum

def getDigitLine(line):

	tempChar = ""
	firstNum = ""
	lastNum = ""
	lastPos = -1
	lenOldString = 0

	for i, char in enumerate(line):
		tempChar += char

		for key, value in nums.items():
			pos = tempChar.find(key)
			if pos != -1:
				firstNum = value
				break
		
		if firstNum:
			break

		if char.isdigit():
			firstNum = char
			break
	
	tempChar = ""
	for i, char in enumerate(line[::-1]):
		tempChar += char

		for key, value in nums.items():
			pos = tempChar.find(key[::-1])
			if pos != -1:
				lastNum = value
				break

		if lastNum:
			break

		if char.isdigit():
			lastNum = char
			break

		

	returnval = int(firstNum+lastNum)
	#print(str(line) + " gives: "+str(returnval))
	return returnval

#def convertLine(line):



# Task 2
def task2():
	sum = 0

	for line in ls:
		
		sum += getDigitLine(line)
		
	return sum

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

a = "i"
ls = setup((a == "i"), test)

#print(task1())

print(task2())


