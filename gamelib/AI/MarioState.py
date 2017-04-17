
class MarioState(object):
    MARIO_X = 9
    MARIO_Y = 9
    fields = ArrayList()

    #  0-small, 1-big, 2-fire.
    marioMode = Int("m", 2)

    #  0~8.
    marioDirection = Int("Dir", 8)
    marioX = 0
    marioY = 0
    stuck = Int("!!", 1)
    stuckCount = 0
    onGround = Int("g", 1)
    canJump = Int("j", 1)
    collisionsWithCreatures = Int("C", 1)
    lastCollisionsWithCreatures = 0
    enemies = [None]*LearningParams.NUM_OBSERVATION_LEVELS

    #  To keep track enemies killed in the observation window.
    enemiesCount = [None]*LearningParams.NUM_OBSERVATION_LEVELS
    totalEnemiesCount = 0
    lastTotalEnemiesCount = 0

    #  Whether enemies are killed in this frame.
    enemiesKilledByStomp = Int("ks", 1)
    enemiesKilledByFire = Int("kf", 1)
    killsByFire = 0
    killsByStomp = 0

    #  [4 bits] Whether obstacles are in front of Mario.
    #    | 3
    #    | 2 
    #  M | 1
    #    | 0
    obstacles = BitArray("o", 3)

    #  [2 bits] Whether there are gaps under or in front of Mario.
    #   M |
    #  ---|---
    #   0 | 1
    # BitArray gaps = new BitArray(2);
    # private Int win = new Int("W", 1);
    stateNumber = 0
    environment = Environment()
    scene = []
    dDistance = 0
    dElevation = 0
    lastElevation = 0
    lastDistance = 0

    def __init__(self):
        i = 0
        while i < LearningParams.NUM_OBSERVATION_LEVELS:
            #  Enemy directions: 0~7.
            self.enemies[i] = BitArray("e" + i, 8)
            i += 1

    def update(self, environment):
        self.environment = environment
        self.scene = environment.getMergedObservationZZ(1, 1)
        #  Update distance and elevation.
        distance = environment.getEvaluationInfo().distancePassedPhys
        self.dDistance = distance - self.lastDistance
        if Math.abs(self.dDistance) <= LearningParams.MIN_MOVE_DISTANCE:
            self.dDistance = 0
        self.lastDistance = distance
        elevation = Math.max(0, getDistanceToGround(self.MARIO_X - 1) - getDistanceToGround(self.MARIO_X))
        self.dElevation = Math.max(0, elevation - self.lastElevation)
        self.lastElevation = elevation
        #  *******************************************************************
        #  Update state params.
        self.marioMode.value = environment.getMarioMode()
        pos = environment.getMarioFloatPos()
        self.marioDirection.value = getDirection(pos[0] - self.marioX, pos[1] - self.marioY)
        self.marioX = pos[0]
        self.marioY = pos[1]
        if self.dDistance == 0:
            self.stuckCount += 1
        else:
            self.stuckCount = 0
            self.stuck.value = 0
        if self.stuckCount >= LearningParams.NUM_STUCK_FRAMES:
            self.stuck.value = 1
        self.collisionsWithCreatures.value = environment.getEvaluationInfo().collisionsWithCreatures - self.lastCollisionsWithCreatures
        self.lastCollisionsWithCreatures = environment.getEvaluationInfo().collisionsWithCreatures
        #  Fill can jump.
        # /*
        self.canJump.value = 1 if (not environment.isMarioOnGround() or environment.isMarioAbleToJump()) else 0
        # 
        self.onGround.value = 1 if environment.isMarioOnGround() else 0
        #  Fill enemy info.
        # /*
        maxSize = LearningParams.OBSERVATION_SIZES[len(enemies)]
        startX = self.MARIO_X - maxSize
        endX = self.MARIO_X + maxSize
        startY = self.MARIO_Y - maxSize - getMarioHeight() + 1
        endY = self.MARIO_Y + maxSize
        self.totalEnemiesCount = 0
        i = 0
        while len(enemiesCount):
            self.enemiesCount[i] = 0
            i += 1
        i = 0
        while len(enemies):
            self.enemies[i].reset()
            i += 1
        y = startY
        while y <= endY:
            while x <= endX:
                if self.scene[y][x] == Sprite.KIND_GOOMBA or self.scene[y][x] == Sprite.KIND_SPIKY:
                    if i < 0 or d == Direction.NONE:
                        continue 
                    self.enemies[i].value[d] = True
                    self.enemiesCount[i] += 1
                    self.totalEnemiesCount += 1
                x += 1
            y += 1
        self.enemiesKilledByStomp.value = environment.getKillsByStomp() - self.killsByStomp
        if self.totalEnemiesCount < self.lastTotalEnemiesCount:
            self.enemiesKilledByFire.value = environment.getKillsByFire() - self.killsByFire
        else:
            self.enemiesKilledByFire.value = 0
        self.lastTotalEnemiesCount = self.totalEnemiesCount
        self.killsByFire = environment.getKillsByFire()
        self.killsByStomp = environment.getKillsByStomp()
        self.obstacles.reset()
        y = 0
        while len(length):
            if isObstacle(self.MARIO_X + 1, self.MARIO_Y - y + 1):
                self.obstacles.value[y] = True
            y += 1
        self.computeStateNumber()
        Logger.println(2, self)

    def calculateReward(self):
        rewardScaler = 1
        i = 0
        while len(enemiesCount):
            if self.enemiesCount[i] > 0:
                rewardScaler = LearningParams.ENEMIES_AROUND_REWARD_SCALER[i]
                break
            i += 1
        reward = self.stuck.value * LearningParams.REWARD_PARAMS.stuck + rewardScaler * self.dDistance * LearningParams.REWARD_PARAMS.distance + rewardScaler * self.dElevation * LearningParams.REWARD_PARAMS.elevation + self.collisionsWithCreatures.value * LearningParams.REWARD_PARAMS.collision + self.enemiesKilledByFire.value * LearningParams.REWARD_PARAMS.killedByFire + self.enemiesKilledByStomp.value * LearningParams.REWARD_PARAMS.killedByStomp
        Logger.println(2, "D: " + self.dDistance)
        Logger.println(2, "H:" + self.dElevation)
        Logger.println(2, "Reward = " + reward)
        return reward

    def canJump(self):
        return self.environment.isMarioAbleToJump()

    def getStateNumber(self):
        return self.stateNumber

    def computeStateNumber(self):
        self.stateNumber = 0
        i = 0
        for field in fields:
            self.stateNumber += field.getInt() << i
            i += field.getNBits()
        if i >= Long.SIZE:
            System.err.println("State number too large!! = " + i + "bits!!")
            System.exit(1)

    def __str__(self):
        return Utils.join(self.fields, " | ")

    @classmethod
    def printStateNumber(cls, state):
        sb = StringBuilder("[]")
        return sb.__str__()

    def getMarioHeight(self):
        return 2 if self.marioMode.value > 0 else 1

    def getObservationLevel(self, x, y):
        i = 0
        while len(length):
            if Math.abs(x - self.MARIO_X) <= size and dy <= size:
                return i
            i += 1
        System.err.println("Bad observation level!! " + x + " " + y)
        return -1

    def getDistanceToGround(self, x):
        y = self.MARIO_Y + 1
        while len(scene):
            if isGround(x, y):
                return Math.min(3, y - self.MARIO_Y - 1)
            y += 1
        return -1

    def isObstacle(self, x, y):
        if self.scene[y][x]==GeneralizerLevelScene.BRICK:
            pass
        elif self.scene[y][x]==GeneralizerLevelScene.BORDER_CANNOT_PASS_THROUGH:
            pass
        elif self.scene[y][x]==GeneralizerLevelScene.FLOWER_POT_OR_CANNON:
            pass
        elif self.scene[y][x]==GeneralizerLevelScene.LADDER:
            return True
        return False

    def isGround(self, x, y):
        return self.isObstacle(x, y) or self.scene[y][x] == GeneralizerLevelScene.BORDER_HILL

    class Direction(object):
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        UP_RIGHT = 4
        DOWN_RIGHT = 5
        DOWN_LEFT = 6
        UP_LEFT = 7
        NONE = 8

    DIRECTION_THRESHOLD = 0.8

    def getDirection(self, dx, dy):
        if Math.abs(dx) < self.DIRECTION_THRESHOLD:
            dx = 0
        if Math.abs(dy) < self.DIRECTION_THRESHOLD:
            dy = 0
        if dx == 0 and dy > 0:
            return self.Direction.UP
        elif dx > 0 and dy > 0:
            return self.Direction.UP_RIGHT
        elif dx > 0 and dy == 0:
            return self.Direction.RIGHT
        elif dx > 0 and dy < 0:
            return self.Direction.DOWN_RIGHT
        elif dx == 0 and dy < 0:
            return self.Direction.DOWN
        elif dx < 0 and dy < 0:
            return self.Direction.DOWN_LEFT
        elif dx < 0 and dy == 0:
            return self.Direction.LEFT
        elif dx < 0 and dy > 0:
            return self.Direction.UP_LEFT
        return self.Direction.NONE

    class Field(object):
        name = str()

        def __init__(self, name):
            self.name = name
            self.fields.add(self)

        def __str__(self):
            return String.format("%s: %s", self.name, getValueToString())


    class BitArray(Field):
        value = []

        def __init__(self, name, n):
            super(BitArray, self).__init__(name)
            self.value = [None]*n

        def getNBits(self):
            return len(value)

        def getInt(self):
            decInt = 0
            i = 0
            while len(value):
                decInt <<= 1
                decInt += 1 if self.value[i] else 0
                i += 1
            return decInt

        def getValueToString(self):
            return Utils.printArray(self.value)

        def reset(self):
            i = 0
            while len(value):
                self.value[i] = False
                i += 1

    class Int(Field):
        value = int()
        max = int()

        def __init__(self, name, max):
            super(Int, self).__init__(name)
            self.max = max

        def getNBits(self):
            return int(Math.ceil(Math.log(self.max + 1) / Math.log(2)))

        def getInt(self):
            self.value = Math.max(0, Math.min(self.max, self.value))
            return self.value

        def getValueToString(self):
            return String.valueOf(self.value)

    @classmethod
    def main(cls, argv):
        state = MarioState()
        state.marioMode.value = 0
        state.canJump.value = 1
        state.onGround.value = 1
        state.stuck.value = 1
        state.obstacles.value[0] = True
        state.obstacles.value[1] = True
        state.obstacles.value[2] = False
        state.computeStateNumber()
        print state.getStateNumber()


if __name__ == '__main__':
    import sys
    MarioState.main(sys.argv)
