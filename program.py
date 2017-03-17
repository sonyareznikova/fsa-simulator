from fsa import *

#function to deal with some of the typical patterns in the input file
def getRidOfBracketsAndCommas(someString):
	someStringNoBrackets = someString[1:len(someString)-2]
	someStringNoCommas = someStringNoBrackets.split(",")
	return someStringNoCommas

f = open('input.txt') #file to read from

f1 = open('output.txt', 'w') #file for writing
f1.write('Sofia Reznikova\n')

numberOfTestCases = f.readline()
for i in range(1, int(numberOfTestCases) + 1): 
	thisFSA = FSA()
	allStates = getRidOfBracketsAndCommas(f.readline())
	#adding states to the FSA
	for j in allStates:
		newState = State(j)
		thisFSA.addState(newState)

	alphabet = f.readline()
	#setting the initial state
	initialState = f.readline()
	for state in thisFSA.getAllStates():
		if state.designation == initialState[0:len(initialState)-1]:
			state.makeInitial()

	#setting final states
	finalStates = getRidOfBracketsAndCommas(f.readline())
	for someFinalStateName in finalStates:
		for potentialFinalState in thisFSA.getAllStates():
			if someFinalStateName == potentialFinalState.designation:
				potentialFinalState.makeFinal()
				 
	#dealing with transitions
	allPaths = getRidOfBracketsAndCommas(f.readline())
	#going through all possible transitions 
	for path in allPaths:
		#parsing possible transitions and adding them
		parsedNoArrow = path.split(")->")
		parsedNoParens = parsedNoArrow[0].split("(")
		parsedNoArrow.pop(0)
		fullyParsed = parsedNoParens + parsedNoArrow #list of the form [startState, transition, endState]
		startState = fullyParsed[0]
		transition = fullyParsed[1]
		endState = fullyParsed[2]
		for state in thisFSA.getAllStates():
			if state.designation == startState: #if there's such a state in our FSA
				destination = thisFSA.getState(endState) #get a state with the endState designation
				state.setTransition(transition, destination) #set the transition

	#dealing with input strings
	numberOfInputStrings = f.readline()
	
	#testing and outputting
	f1.write(str(i) + '\n') #writing the number of the current test case into the output
	for k in range(0, int(numberOfInputStrings)):
		currentTestString = f.readline()
		output = thisFSA.isAccepted(currentTestString[0:len(currentTestString)-1]) #testing the string
		f1.write(output[0] + ",")
		for m in range(0, len(output[1])):
			if m == len(output[1]) - 1:
				f1.write(output[1][m])
			else:
				f1.write(output[1][m] + "->")
		f1.write("\n")