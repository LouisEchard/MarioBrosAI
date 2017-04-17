
class MarioAction:
    TOTAL_ACTIONS = 12
    actionNumber = int()
    action = []

    def __init__(self, actionNumber, *keys):
        self.actionNumber = actionNumber
        self.action = [None]*6
        for key in keys:
            self.action[key] = True

    def getActionNumber(self):
        return self.actionNumber

    @overloaded
    def getAction(self):
        return self.action

    @classmethod
    @getAction.register(object, int)
    def getAction_0(cls, actionNumber):
        return MarioAction.values()[actionNumber].getAction()

MarioAction.DO_NOTHING = MarioAction(0)

MarioAction.LEFT = MarioAction(1, Mario.KEY_LEFT)

MarioAction.RIGHT = MarioAction(2, Mario.KEY_RIGHT)

MarioAction.JUMP = MarioAction(3, Mario.KEY_JUMP)

MarioAction.FIRE = MarioAction(4, Mario.KEY_SPEED)

MarioAction.LEFT_JUMP = MarioAction(5, Mario.KEY_LEFT, Mario.KEY_JUMP)

MarioAction.RIGHT_JUMP = MarioAction(6, Mario.KEY_RIGHT, Mario.KEY_JUMP)

MarioAction.LEFT_FIRE = MarioAction(7, Mario.KEY_LEFT, Mario.KEY_SPEED)

MarioAction.RIGHT_FIRE = MarioAction(8, Mario.KEY_RIGHT, Mario.KEY_SPEED)

MarioAction.JUMP_FIRE = MarioAction(9, Mario.KEY_JUMP, Mario.KEY_SPEED)

MarioAction.LEFT_JUMP_FIRE = MarioAction(10, Mario.KEY_LEFT, Mario.KEY_JUMP, Mario.KEY_SPEED)

MarioAction.RIGHT_JUMP_FIRE = MarioAction(11, Mario.KEY_RIGHT, Mario.KEY_JUMP, Mario.KEY_SPEED)
