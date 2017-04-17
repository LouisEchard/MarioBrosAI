
class TransitionTable(object):
    class ActionData(object):
        actionCount = 0
        transitions = Hashtable()

        def getActionCount(self):
            return self.actionCount

        def setActionCount(self, count):
            self.actionCount = count

        def addTransition(self, toState):
            self.actionCount += 1
            if not self.transitions.containsKey(toState):
                self.transitions.put(toState, 0)
            self.transitions.put(toState, self.transitions.get(toState) + 1)

    stateCounter = Hashtable()
    actionRange = int()

    def __init__(self, actionRange):
        self.actionRange = actionRange

    def getState(self, state):
        actionData = self.stateCounter.get(state)
        if actionData == None:
            actionData = [None]*actionRange
            while i < self.actionRange:
                actionData[i] = self.ActionData()
                i += 1
            self.stateCounter.put(state, actionData)
        return actionData

    def getActionData(self, fromState, action):
        return self.getState(fromState)[action]

    def addTransition(self, fromState, action, toState):
        self.getActionData(fromState, action).addTransition(toState)

    def getCount(self, fromState, action):
        return self.getActionData(fromState, action).getActionCount()

    def getCounts(self, state):
        counts = [None]*actionRange
        i = 0
        while i < self.actionRange:
            counts[i] = self.getActionData(state, i).getActionCount()
            i += 1
        return counts

    def setCount(self, fromState, action, count):
        self.getActionData(fromState, action).setActionCount(count)
