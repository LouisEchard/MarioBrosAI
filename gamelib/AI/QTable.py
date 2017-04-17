
class Qtable(object):
 
    # 
    #    * for creating random numbers
    #    
    randomGenerator = Random()

    # 
    #    * the table variable stores the Q-table, where the state is saved as the
    #    * state number of each MarioState. Each state has an array of Q values for
    #    * all the actions available for that state.
    #    
    table = Hashtable()

    # 
    #    * the actionRange variable determines the number of actions available at any
    #    * map state, and therefore the number of Q values in each entry of the
    #    * Q-table.
    #    
    actionRange = int()

    #  E-GREEDY Q-LEARNING SPECIFIC VARIABLES
    # 
    #    * for e-greedy Q-learning, when taking an action a random number is checked
    #    * against the explorationChance variable: if the number is below the
    #    * explorationChance, then exploration takes place picking an action at
    #    * random. Note that the explorationChance is not a final because it is
    #    * customary that the exploration chance changes as the training goes on.
    #    
    explorationChance = LearningParams.EXPLORATION_CHANCE

    # 
    #    * the discount factor is saved as the gammaValue variable. The discount
    #    * factor determines the importance of future rewards. If the gammaValue is 0
    #    * then the AI will only consider immediate rewards, while with a gammaValue
    #    * near 1 (but below 1) the AI will try to maximize the long-term reward even
    #    * if it is many moves away.
    #    
    gammaValue = LearningParams.GAMMA_VALUE

    # 
    #    * the learningRate determines how new information affects accumulated
    #    * information from previous instances. If the learningRate is 1, then the new
    #    * information completely overrides any previous information. Note that the
    #    * learningRate is not a final because it is customary that the exploration
    #    * chance changes as the training goes on.
    #    
    learningRate = LearningParams.LEARNING_RATE

    #  PREVIOUS STATE AND ACTION VARIABLES
    # 
    #    * Since in Q-learning the updates to the Q values are made ONE STEP LATE, the
    #    * state of the world when the action resulting in the reward was made must be
    #    * stored.
    #    
    prevState = long()

    # 
    #    * Since in Q-learning the updates to the Q values are made ONE STEP LATE, the
    #    * index of the action which resulted in the reward must be stored.
    #    
    prevAction = int()

    # 
    #    * Q table constructor, initiates variables.
    #    * 
    #    * @param actionRange The number of actions available at any state.
    #    
    def __init__(self, actionRange):
        self.randomGenerator = Random()
        self.table = Hashtable()
        self.actionRange = actionRange

    # 
    #    * For this example, the getNextAction function uses an e-greedy approach,
    #    * having exploration happen if the exploration chance is rolled.
    #    * 
    #    * @param the
    #    *          current map (state)
    #    * @return the action to be taken by the calling progam
    #    
    def getNextAction(self, stateNumber):
        self.prevState = stateNumber
        if self.randomGenerator.nextFloat() < self.explorationChance:
            self.prevAction = explore()
        else:
            self.prevAction = getBestAction(stateNumber)
        return self.prevAction

    # 
    #    * The getBestAction function uses a greedy approach for finding the best
    #    * action to take. Note that if all Q values for the current state are equal
    #    * (such as all 0 if the state has never been visited before), then
    #    * getBestAction will always choose the same action. If such an action is
    #    * invalid, this may lead to a deadlock as the map state never changes: for
    #    * situations like these, exploration can get the algorithm out of this
    #    * deadlock.
    #    * 
    #    * @param the
    #    *          current map (state)
    #    * @return the action with the highest Q value
    #    
#     def getBestAction(self, stateNumber):

    # 
    #    * The explore function is called for e-greedy algorithms. It can choose an
    #    * action at random from all available, or can put more weight towards actions
    #    * that have not been taken as often as the others (most unknown).
    #    * 
    #    * @return index of action to take
    #    
    def explore(self):
        return self.randomGenerator.nextInt(self.actionRange)

    # 
    #    * The updateQvalue is the heart of the Q-learning algorithm. Based on the
    #    * reward gained by taking the action prevAction while being in the state
    #    * prevState, the updateQvalue must update the Q value of that {prevState,
    #    * prevAction} entry in the Q table. In order to do that, the Q value of the
    #    * best action of the current state must also be calculated.
    #    * 
    #    * @param reward The reward at the current state.
    #    * @param currentStateNumber The current state number.
    #    
#     def updateQvalue(self, reward, currentStateNumber):

    # 
    #    * The getActionsQValues function returns an array of Q values for all the
    #    * actions available at given state. Note that if the current state does not
    #    * already exist in the Q table (never visited before), then it is initiated
    #    * with Q values of 0 for all of the available actions.
    #    * 
    #    * @param the current state
    #    * @return an array of Q values for all the actions available at given state.
    #    
    def getActionsQValues(self, stateNumber):
        if not self.table.containsKey(stateNumber):
            self.table.put(stateNumber, initialQvalues)
            return initialQvalues
        return self.table.get(stateNumber)

#     def getInitialQvalues(self, stateNumber):

    def getTable(self):
        return self.table
