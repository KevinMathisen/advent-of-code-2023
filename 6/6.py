import re

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	ls = list(cont.strip().split("\n"))
	time = [int(match) for match in re.findall(r'\d+', ls[0].split(": ")[1])]
	distance = [int(match) for match in re.findall(r'\d+', ls[1].split(": ")[1])]
	time2 = int(''.join(map(str, time)))
	distance2 = int(''.join(map(str, distance)))

	return time, distance, time2, distance2

def findAmountOfSolutionsToRace(time, distance):
	amountOfSolutions = 0
	for holdtime in range(1, time):
		if holdtime % 100000 == 0:
			print(str(holdtime) + "of this completed: " + str(time) + "Percentage completed "+str(holdtime/time*100))
		if holdtime*(time-holdtime) > distance:
			amountOfSolutions += 1
	return amountOfSolutions

# Task 1
def task1():

	ways = 1
	for raceNum in range(0, len(time)):
		amountOfSolutions = findAmountOfSolutionsToRace(time[raceNum], distance[raceNum])
		ways *= amountOfSolutions
	return ways


# Task 2
def task2():
	
	amountOfSolutions = findAmountOfSolutionsToRace(time2, distance2)

	return amountOfSolutions

test = """Time:      7  15   30
Distance:  9  40  200
"""

inputTxt = "y"
time, distance, time2, distance2 = setup((inputTxt == "y"), test)


print(task1())

print(task2())


