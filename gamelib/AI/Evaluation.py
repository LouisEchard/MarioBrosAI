
class Evaluation(object):
    class Mode:
        DEBUG = u'DEBUG'
        DEMO = u'DEMO'
        EVAL = u'EVAL'

        @classmethod
        def getMode(cls, mode):
            for m in Mode.values():
                if m.name().lower() == mode.lower():
                    return m
            return cls.Mode.DEMO

    class EvaluationData(object):
        averageScore = 0
        wins = 0
        averageKills = 0
        averageDistance = 0
        averageTimeSpent = 0

        def __str__(self):
            return String.format("%f %f %f %f %f", self.averageScore, self.wins, self.averageKills, self.averageDistance, self.averageTimeSpent)

        def computeFinalEvalInfo(self):
            self.averageScore /= LearningParams.NUM_EVAL_ITERATIONS
            self.wins /= LearningParams.NUM_EVAL_ITERATIONS
            self.averageKills /= LearningParams.NUM_EVAL_ITERATIONS
            self.averageDistance /= LearningParams.NUM_EVAL_ITERATIONS
            self.averageTimeSpent /= LearningParams.NUM_EVAL_ITERATIONS

        def accumulateEvalInfo(self, evaluationInfo):
            self.averageScore += evaluationInfo.computeWeightedFitness()
            self.wins += 1 if evaluationInfo.marioStatus == Mario.STATUS_WIN else 0
            self.averageKills += 1.0 * evaluationInfo.killsTotal / evaluationInfo.totalNumberOfCreatures
            self.averageDistance += 1.0 * evaluationInfo.distancePassedCells / evaluationInfo.levelLength
            self.averageTimeSpent += evaluationInfo.timeSpent

    mode = Mode()
    marioAIOptions = MarioAIOptions()
    agent = MarioRLAgent()
    evaluationResults = ArrayList()

    def __init__(self, mode):
        self.mode = mode
        self.agent = MarioRLAgent()
        self.marioAIOptions = MarioAIOptions()
        self.marioAIOptions.setAgent(self.agent)
        self.marioAIOptions.setVisualization(True)
        self.marioAIOptions.setFPS(240)

        self.agent.setOptions(self.marioAIOptions)
        self.agent.setLearningTask(LearningTask(self.marioAIOptions))

    def evaluate(self, aNumRound):
        if self.mode == self.Mode.DEBUG:
            self.marioAIOptions.setVisualization(True)
            LearningParams.DEBUG = 2
        self.agent.learn()
        if self.mode == self.Mode.DEMO:
            self.marioAIOptions.setVisualization(True)
        if aNumRound > 2000:
            self.marioAIOptions.setVisualization(True)
        basicTask = BasicTask(self.marioAIOptions)
        Logger.println(0, "*************************************************")
        Logger.println(0, "*                                               *")
        Logger.println(0, "*              Starting Evaluation              *")
        Logger.println(0, "*                                               *")
        Logger.println(0, "*************************************************")
        print "Task = " + basicTask
        print "Agent = " + self.agent
        results = self.EvaluationData()
        self.evaluationResults.add(results)
        i = 0
        while i < LearningParams.NUM_EVAL_ITERATIONS:

            self.marioAIOptions.setLevelRandSeed(Math.round(date.getTime() % 1000))
            #  Make evaluation on the same episode once.
            while not basicTask.runSingleEpisode(1):
                System.err.println("MarioAI: out of computational time per action?")
                failedCount += 1
                if failedCount >= 3:
                    System.err.println("Exiting.. =(")
                    System.exit(0)
            results.accumulateEvalInfo(evaluationInfo)
            print evaluationInfo.__str__()
            i += 1
        results.computeFinalEvalInfo()
        return results.averageScore

    def dumpResult(self):
        Utils.dump("eval.txt", Utils.join(self.evaluationResults, "\n"))

    @classmethod
    def getParam(cls, args, name):
        i = 0
        while len(args):
            if s.startsWith("-") and s.substring(1) == name:
                if len(args):
                    if not v.startsWith("-"):
                        return v
                return ""
            i += 1
        return None

    @classmethod
    def isNullOrEmpty(cls, v):
        return v == None or v.isEmpty()

    @classmethod
    def getIntParam(cls, args, name, defaultValue):
        v = cls.getParam(args, name)
        return defaultValue if cls.isNullOrEmpty(v) else Integer.valueOf(v)

    @classmethod
    def getBooleanParam(cls, args, name):
        v = cls.getParam(args, name)
        return v != None

    @classmethod
    def main(cls, args):
        mode = cls.Mode.getMode(cls.getParam(args, "m"))
        numRounds = cls.getIntParam(args, "n", 1)
        LearningParams.NUM_MODES_TO_TRAIN = cls.getIntParam(args, "nm", LearningParams.NUM_MODES_TO_TRAIN)
        LearningParams.NUM_SEEDS_TO_TRAIN = cls.getIntParam(args, "ns", LearningParams.NUM_SEEDS_TO_TRAIN)
        LearningParams.NUM_TRAINING_ITERATIONS = cls.getIntParam(args, "i", LearningParams.NUM_TRAINING_ITERATIONS)
        LearningParams.NUM_EVAL_ITERATIONS = cls.getIntParam(args, "ei", LearningParams.NUM_EVAL_ITERATIONS)
        LearningParams.EVAL_SEED = cls.getIntParam(args, "es", LearningParams.EVAL_SEED)
        LearningParams.LOAD_QTABLE = cls.getBooleanParam(args, "l")
        eval = Evaluation(mode)
        i = 0
        while i < numRounds:
            print "~ Round " + i + " ~"
            print "Final Score = " + finalScore + "\n"
            i += 1
        eval.dumpResult()
        System.exit(0)


if __name__ == '__main__':
    import sys
    Evaluation.main(sys.argv)
