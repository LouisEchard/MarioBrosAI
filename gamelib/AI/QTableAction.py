
# 
#  * Q table implementation of the Mario learning agent.
#  * 
#  * @author lou.echard@gmail.com (Louis Echard)
#  
class QTableAction(Qtable):
    transitions = TransitionTable()

    def __init__(self, actionRange):
        super(ActionQtable, self).__init__(actionRange)
        self.transitions = TransitionTable(actionRange)

    def getBestAction(self, stateNumber):
        rewards = self.getActionsQValues(stateNumber)
        if rewards == None:
            print ("No rewards defined for this state")
            return 0
        else:
            while len(rewards):
                if maxRewards < rewards[i]:
                    maxRewards = rewards[i]
                    indexMaxRewards = i
                i += 1
            Logger.println(4, "Q values: " + Utils.join(rewards, ", "))
            Logger.println(4, "Best action: " + indexMaxRewards)
            return indexMaxRewards

    def updateQvalue(self, reward, currentStateNumber):
        """ generated source for method updateQvalue """
        self.transitions.addTransition(prevState, prevAction, currentStateNumber)
        #  Update Q values using the following update rule:
        # 
        #  Q(prevState, prevAction) =
        #      (1 - alpha) * Qprev + alpha * (reward + gamma * maxQ)
        # 
        #  where alpha = learningRate / # prevState/prevAction visited.
        prevQs = getActionsQValues(prevState)
        prevQ = prevQs[prevAction]
        bestAction = self.getBestAction(currentStateNumber)
        maxQ = getActionsQValues(currentStateNumber)[bestAction]
        alpha = learningRate / self.transitions.getCount(prevState, prevAction)

        newQ = (1 - alpha) * prevQ + alpha * (reward + gammaValue * maxQ)
        prevQs[prevAction] = newQ

    def getInitialQvalues(self, stateNumber):
        initialQvalues = [None]*actionRange
        i = 0
        while i < actionRange:
            #  Set as random float ranged (-.1, .1), check whether makes sense.
            initialQvalues[i] = float((randomGenerator.nextFloat() * 0.2 - 0.1))
            i += 1
        return initialQvalues

    def dumpQtable(self, logfile):
        Logger.println(1, "** Dumping Qtable to " + logfile + " **")
        try:
            writer.write("")
            for key in getTable().keySet():
                writer.append(printState(key) + "\n")
            writer.close()
        except IOException as x:
            print ("Failed to write qtable to: " + logfile)

    def printState(self, key):
        return String.format("%d:%s:%s", key, Utils.join(getTable().get(key), " "), Utils.join(self.transitions.getCounts(key), " "))

    def parseState(self, line):
        tokens = line.split(":")
        state = Long.valueOf(tokens[0])
        qvalueStrings = tokens[1].split(" ")
        countStrings = tokens[2].split(" ")
        qvalues = getActionsQValues(state)
        i = 0
        while i < actionRange:
            qvalues[i] = Float.valueOf(qvalueStrings[i])
            self.transitions.setCount(state, i, Integer.valueOf(countStrings[i]))
            i += 1

    def loadQtable(self, logfile):
        Logger.println(1, "** Loading Qtable from " + logfile + " **")
        try:
            while (line = reader.readLine()) != None:
                self.parseState(line)
            reader.close()
        except Exception as e:
            System.err.println("Failed to load qtable from: " + logfile)
