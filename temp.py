def setup(inputTxt, test):
	if inputTxt:
		input = open("input.txt")
		cont = input.read()
	else:
		
		cont = test

	ls = list(cont.strip().split("\n"))

	return ls



# Task 1
def task1():
	pass


# Task 2
def task2():
	
	pass

test = """
"""

inputTxt = "y"
ls = setup((inputTxt == "y"), test)

print(task1())

print(task2())


