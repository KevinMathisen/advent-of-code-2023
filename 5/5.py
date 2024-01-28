

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	fields = list(cont.strip().split("\n\n"))

	seeds = [int(seed) for seed in fields[0].split(": ")[1].split(" ")]
	seeds2 = [[seeds[i], seeds[i]+seeds[i+1]] for i in range(0, len(seeds), 2)]

	maps = []
	for field in fields:
		if field == fields[0]:
			continue

		lines = field.split(":\n")[1].split("\n") 
		rules = []
		for line in lines:
			rules.append([int(number) for number in line.split(" ")])

		maps.append(rules)

	return seeds, seeds2, maps

def calLocationFromSeed(seed):
	newValue = seed
	#print("\n\ncalculating seed "+str(seed))
	for map in maps:
		newValue = convertNumToOutput(newValue, map)
		#print("\tConverted to "+str(newValue))
	return newValue

def convertNumToOutput(source, rules):
	for rule in rules:
		if source >= rule[1] and source < rule[1] + rule[2]:
			return source - rule[1] + rule[0]
	return source

# Task 1
def task1():
	smallestLocationNum = 100000000000
	for seed in seeds:
		locationNum = calLocationFromSeed(seed)
		if locationNum < smallestLocationNum:
			smallestLocationNum = locationNum

	return smallestLocationNum

def getStartFromEnd(endValue):
	newValue = endValue

	for map in reversed(maps):
		newValue = convertNumToOutputReversed(newValue, map)
	
	return newValue

def convertNumToOutputReversed(dest, rules):
	for rule in rules:
		if dest >= rule[0] and dest < rule[0] + rule[2]:
			return dest - rule[0] + rule[1]
	return dest

# Task 2
def task2():

	max = 0
	for locationValues in maps[-1]:
		if locationValues[0]+locationValues[2] > max:
			max = locationValues[0]+locationValues[2]

	print("Calculating startingpositions from 0 to " + str(max))

	for endValue in range(int(max/40), max):
		if endValue % 100000 == 0:
			print(str(endValue/max*1000))

		startValue = getStartFromEnd(endValue)

		for seedRange in seeds2:
			if startValue >= seedRange[0] and startValue <= seedRange[1]:
				return endValue

	return -1


test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

inputTxt = "y"
seeds, seeds2, maps = setup((inputTxt == "y"), test)

#print(removeOverlap([[10, 20], [30, 35]], [[11, 11], [25, 30]]))
#print(calLocationFromSeed(91))

print(task1())

print(task2())


