

def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	fields = list(cont.strip().split("\n\n"))

	seeds = [int(seed) for seed in fields[0].split(": ")[1].split(" ")]

	maps = []
	for field in fields:
		if field == fields[0]:
			continue

		lines = field.split(":\n")[1].split("\n") 
		rules = []
		for line in lines:
			rules.append([int(number) for number in line.split(" ")])

		maps.append(rules)

	return seeds, maps

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

def getPossibleSeedsFromLocationRule(locationRule):
	desiredOutValues = [[locationRule[0], locationRule[0]+locationRule[2]-1]]
	
	# convert step by step for each mapping (except location)
	for rules in reversed(maps):
		if rules == maps[-1]:
			continue

		desiredOutValues = convertToNewDesiredFromStep(desiredOutValues, rules)
		
	return desiredOutValues
		 
def convertToNewDesiredFromStep(oldDesired, rules):
	foundDesiredOutValues = []
	newDesiredOutValues = []
	# go trough each rule, to find if any of their output overlaps with the desired output
	# IF so, save the valid range to mapOutValues
	# for any part of the desired output, if no overlap with rules, these parts desired output will be the same
	for rule in rules:
		# Go trough all desired ranges
		for outValue in oldDesired:
			# Calculate the overlap if there is any
			startOverlap = max(outValue[0], rule[0])
			endOverlap = min(outValue[1], rule[0]+rule[2]-1)
			if startOverlap <= endOverlap:
				# Calculate the new desired values for the next stage
				# Also, save the overlap we found from the current
				startOut = startOverlap - rule[0] + rule[1]
				endOut = endOverlap - rule[0] + rule[1]
				newDesiredOutValues.append([startOut, endOut])
				foundDesiredOutValues.append([startOverlap, endOverlap])

	# Remove where we have found valid ranges from the desired range, but keep where we did not found anything
	# Then merge these ranges to find the true desiredValues 
	oldDesiredWithoutOverlap = removeOverlap(oldDesired, foundDesiredOutValues)
	newDesiredOutValues = newDesiredOutValues + oldDesiredWithoutOverlap

	return sorted(newDesiredOutValues, key=lambda range: range[0])

def removeOverlap(original, toRemove):
	newRange = original[:]
	for rangeRemove in toRemove:
		newTempRange = []
		for orgRange in newRange:

			startOverlap = max(orgRange[0], rangeRemove[0])
			endOverlap = min(orgRange[1], rangeRemove[1])

			# No overlap
			if startOverlap > endOverlap:
				newTempRange.append(orgRange)
				continue

			# If total overlap
			if startOverlap <= orgRange[0] and endOverlap >= orgRange[1]:
				continue
			# partial overlaps
			elif startOverlap > orgRange[0] and endOverlap >= orgRange[1]:
				newTempRange.append([orgRange[0], startOverlap-1])
			elif startOverlap <= orgRange[0] and endOverlap < orgRange[1]:
				newTempRange.append([endOverlap+1, orgRange[1]])
			elif startOverlap > orgRange[0] and endOverlap < orgRange[1]:
				newTempRange.append([orgRange[0], startOverlap-1])
				newTempRange.append([endOverlap+1, orgRange[1]])
			
		newRange = newTempRange[:]

	return newRange

# Task 2
def task2():
	
	#print(getPossibleSeedsFromLocationRule([1, 1, 55]))
	for locationOut in sorted(maps[-1], key=lambda rules: rules[0]):
		seedRanges = getPossibleSeedsFromLocationRule(locationOut)

		

	return seedRanges


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

inputTxt = "n"
seeds, maps = setup((inputTxt == "y"), test)

#print(removeOverlap([[10, 20], [30, 35]], [[11, 11], [25, 30]]))
#print(calLocationFromSeed(91))

print(task1())

print(task2())


