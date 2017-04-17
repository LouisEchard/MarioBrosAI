
class LearningTask(BasicTask, Task):
    EVALUATION_QUOTA = 100000
    currentEvaluation = 0
    uid = int()
    fileTimeStamp = "-uid-" + uid + "-" + GlobalOptions.getTimeStamp()
    fitnessEvaluations = 0

    def __init__(self, marioAIOptions):
        super(LearningTask, self).__init__(marioAIOptions)

    def reset(self, marioAIOptions):
        options = marioAIOptions
        environment.reset(marioAIOptions)

    def evaluate(self, agent):
        __currentEvaluation_0 = currentEvaluation
        currentEvaluation += 1
        if __currentEvaluation_0 > self.EVALUATION_QUOTA:
            return 0
        options.setAgent(agent)
        environment.reset(options)
        self.fitnessEvaluations += 1
        #  TODO : remove either or two currentEvaluation or fitnessEvaluations
        self.runSingleEpisode(1)
        return self.getEvaluationInfo().computeWeightedFitness()

    @classmethod
    def getEvaluationQuota(cls):
        return LearningTask.EVALUATION_QUOTA

    def dumpFitnessEvaluation(self, fitness, fileName):
        return
