class State(object):

	def __init__(self, name):
		super(State, self).__init__()
		self.designation = name #the name of the state
		self.possibleTransitions = {} #contains a transition and the state it leads to
		self.isFinal = False
		self.isInitial = False
	
	def makeInitial(self):
		self.isInitial = True
	
	def makeFinal(self): 
		self.isFinal = True
	
	def setTransition(self, transition, destination): #to add a transition
		self.possibleTransitions[transition] = destination

class FSA(object):

	def __init__(self):
		super(FSA, self).__init__()
		self.states = [] #a list of all state objects of this FSA

	def addState(self, anotherState):
		self.states.append(anotherState)

	def getState(self, nameOfState):
		for state in self.states:
			if state.designation == nameOfState:
				return state

	def getAllStates(self):
		return self.states

	def size(self):
		print len(self.states)

	def getInitialState(self):
		for state in self.states:
			if state.isInitial:
				return state

	def getFinalStates(self):
		finalStates = []
		for state in self.states:
			if state.isFinal:
				finalStates.append(state)
		return finalStates
	
	def printAllStates(self):
		for state in self.states:
			print state.designation
			for key, value in state.possibleTransitions.iteritems():
				print key + "->" + value.designation

	def isAccepted(self, someString):
		currentState = self.getInitialState()
		path = [] #to store all states we go through
		path.append(currentState.designation)
		for i in someString:
			if i in currentState.possibleTransitions.keys():
				nextState = currentState.possibleTransitions[i]
				currentState = nextState
				path.append(currentState.designation)
			else:
				return "False", path
		if currentState in self.getFinalStates():
			return "True", path
		else:
			return "False", path