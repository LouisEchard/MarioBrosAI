 
class MarioRLAgent():
    
    import MarioAIOptions
    import LearningTask
    import MarioState
    import QTableAction
    name = str()

    #  Training options, task and quota.
    options = MarioAIOptions()
    learningTask = LearningTask()

    #  Fields for the Mario Agent
    currentState = MarioState()

    #  Associated Qtable for the agent. Used for RL training.
    actionTable = QTableAction()

    class Phase:
        INIT = u'INIT'
        LEARN = u'LEARN'
        EVAL = u'EVAL'

    currentPhase = Phase.INIT
    learningTrial = 0
    scores = ArrayList(LearningParams.NUM_TRAINING_ITERATIONS)

    def __init__(self):
        super(MarioRLAgent, self).__init__()
        setName(" Mario ")
        self.currentState = MarioState()
        self.actionTable = ActionQtable(MarioAction.TOTAL_ACTIONS)
        if LearningParams.LOAD_QTABLE:
            self.actionTable.loadQtable(LearningParams.FINAL_QTABLE_NAME)
        Logger.println(0, "*************************************************")
        Logger.println(0, "*                                               *")
        Logger.println(0, "*                Super Mario                    *")
        Logger.println(0, "*                 Agent created!                *")
        Logger.println(0, "*                                               *")
        Logger.println(0, "*************************************************")

    def getAction(self):
        actionNumber = self.actionTable.getNextAction(self.currentState.getStateNumber())
        Logger.println(2, "Next action: " + actionNumber + "\n")
        return MarioAction.getAction(actionNumber)

    # 
    def integrateObservation(self, environment):
        #  Update the current state.
        self.currentState.update(environment)
        if self.currentPhase == self.Phase.INIT and environment.isMarioOnGround():
            #  Start learning after Mario lands on the ground.
            Logger.println(1, "============== Learning Phase =============")
            self.currentPhase = self.Phase.LEARN
        elif self.currentPhase == self.Phase.LEARN:
            #  Update the Qvalue entry in the Qtable.
            self.actionTable.updateQvalue(self.currentState.calculateReward(), self.currentState.getStateNumber())

    def learnOnce(self):
        Logger.println(1, "================================================")
        Logger.println(0, "Trial: %d", self.learningTrial)
        init()
        self.learningTask.runSingleEpisode(1)
        evaluationInfo = self.learningTask.getEnvironment().getEvaluationInfo()
        score = evaluationInfo.computeWeightedFitness()
        Logger.println(1, "Intermediate SCORE = " + score)
        Logger.println(1, evaluationInfo.toStringSingleLine())
        self.scores.add(score)
        #  Dump the info of the most visited states into file.
        if LearningParams.DUMP_INTERMEDIATE_QTABLE:
            self.actionTable.dumpQtable(String.format(LearningParams.QTABLE_NAME_FORMAT, self.learningTrial))
        self.learningTrial += 1

    def learn(self):
        m = 0
        while m < LearningParams.NUM_MODES_TO_TRAIN:
            self.options.setMarioMode(m)
            while j < LearningParams.NUM_SEEDS_TO_TRAIN:
                if j > 0:
                    self.options.setLevelRandSeed(Utils.getSeed(j - 1))
                while i < LearningParams.NUM_TRAINING_ITERATIONS:
                    self.learnOnce()
                    i += 1
                j += 1
            m += 1
        setUpForEval()

    def init(self):
        Logger.println(1, "=================== Init =================")
        self.currentPhase = self.Phase.INIT
        self.actionTable.explorationChance = LearningParams.EXPLORATION_CHANCE

    def reset(self):
        Logger.println(1, "================== Reset =================")
        self.currentState = MarioState()

    def setUpForEval(self):
        Logger.println(1, "============= Dumping Results ============")
        #  Dump final Qtable.
        self.actionTable.dumpQtable(LearningParams.FINAL_QTABLE_NAME)
        #  Dump training scores.
        dumpScores(LearningParams.SCORES_NAME)
        #  Entering EVAL phase.
        Logger.println(1, "================ Eval Phase ==============")
        self.currentPhase = self.Phase.EVAL
        #  Set exploration chance for evaluations.
        self.actionTable.explorationChance = LearningParams.EVAL_EXPLORATION_CHANCE

    def dumpScores(self, logfile):
        Utils.dump(logfile, Utils.join(self.scores, "\n"))

    def setOptions(self, options):
        self.options = options

    # 
    #    *  Gives access to the evaluator through learningTask.evaluate(Agent).
    #    
    def setLearningTask(self, learningTask):
        self.learningTask = learningTask


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name



