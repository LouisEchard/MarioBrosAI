 
class LearningParams(object):
    DEBUG = 0

    # 
    #    * Total number of iterations to train for each configuration (mode/seed).
    #    
    NUM_TRAINING_ITERATIONS = 800

    # 
    #    * Number of Mario modes to train.
    #    
    NUM_MODES_TO_TRAIN = 3

    # 
    #    * Whether we should use a different random seed for training.
    #    
    NUM_SEEDS_TO_TRAIN = 1

    # 
    #    * Number of evaluation iterations to run.
    #    
    NUM_EVAL_ITERATIONS = 10

    # 
    #    * Whether we should use a different random seed for evaluation.
    #    
    EVAL_SEED = -1

    # 
    #    * Exploration chance during evaluation.
    #    
    EVAL_EXPLORATION_CHANCE = 0.01

    #  E-GREEDY Q-LEARNING SPECIFIC VARIABLES
    # 
    #    * For e-greedy Q-learning, when taking an action a random number is checked
    #    * against the explorationChance variable: if the number is below the
    #    * explorationChance, then exploration takes place picking an action at
    #    * random. Note that the explorationChance is not a final because it is
    #    * customary that the exploration chance changes as the training goes on.
    #    
    EXPLORATION_CHANCE = 0.3

    # 
    #    * The discount factor is saved as the gammaValue variable. The discount
    #    * factor determines the importance of future rewards. If the gammaValue is 0
    #    * then the AI will only consider immediate rewards, while with a gammaValue
    #    * near 1 (but below 1) the AI will try to maximize the long-term reward even
    #    * if it is many moves away.
    #    
    GAMMA_VALUE = 0.6

    # public static final float GAMMA_VALUE = 0.2f;
    # 
    #    * The learningRate determines how new information affects accumulated
    #    * information from previous instances. If the learningRate is 1, then the new
    #    * information completely overrides any previous information. Note that the
    #    * learningRate is not a final because it is customary that the exploration
    #    * chance changes as the training goes on.
    #    * 
    #    * The actual learning rate will decrease as the number of times the given
    #    * state and action are visited increase.
    #    
    LEARNING_RATE = 0.8

    #  Reward/state related params.
    # 
    #    * The minimum distance Mario must travel in a frame to receive distance
    #    * reward, and to indicate that Mario is moving instead of being stuck.
    #    
    MIN_MOVE_DISTANCE = 2

    # 
    #    * Mario will change to the stuck state if he has been stuck for
    #    * NUM_STUCK_FRAMES number of frames.
    #    
    NUM_STUCK_FRAMES = 25

    # 
    #    * Number of observation levels (window sizes).
    #    
    NUM_OBSERVATION_LEVELS = 3

    # 
    #    * Window size of each observation level.
    #    
    OBSERVATION_SIZES = [1, 3, 5]

    # 
    #    * Scalers to apply to distance/elevation rewards when enemies are present
    #    * in the corresponding observation level.
    #    
    ENEMIES_AROUND_REWARD_SCALER = [0, 0, 0.15]

    class REWARD_PARAMS(object):
        distance = 2
        elevation = 8
        collision = -800
        killedByFire = 60
        killedByStomp = 60
        stuck = -20

        #  Params below are not used.
        win = 0
        mode = 0
        coins = 0
        flowerFire = 0
        kills = 0
        killedByShell = 0
        mushroom = 0
        timeLeft = 0
        hiddenBlock = 0
        greenMushroom = 0
        stomp = 0

    #  Logging related params.
    # 
    #    * Whether we should dump intermediate Q table values.
    #    
    DUMP_INTERMEDIATE_QTABLE = False

    # 
    #    * Whether we should load the final Q table trained from last time.
    #    
    LOAD_QTABLE = False

    # 
    #    * The format of intermediate Q table dump filenames.
    #    
    QTABLE_NAME_FORMAT = "qt.%d.txt"

    # 
    #    * The filename of the final Q table dump.
    #    
    FINAL_QTABLE_NAME = "qt.final.txt"

    # 
    #    * The filename of scores dump.
    #    
    SCORES_NAME = "scores.txt"
