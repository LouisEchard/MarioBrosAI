import pygame

from enum import Enum
from bokeh.util.session_id import random
from pygame.constants import K_LEFT, K_RIGHT, K_z
from State import State
import numpy as np

counter=0

class HashableRect(pygame.Rect):
    def __hash__(self):
        return hash(tuple(self))


class validDecisions(Enum):
    DO_NOTHING = 0

    LEFT = 1

    RIGHT = 2

    JUMP = 3

    LEFT_JUMP = 4

    RIGHT_JUMP = 5



actionNumber = int()


def __init__(self, actionNumber, *keys):
    self.actionNumber = actionNumber
    self.action = [None] * 6
    for key in keys:
        self.action[key] = True


def getActionNumber(self):
    return self.actionNumber


def getAction(self):
    return self.action


def MarioAction(anEnum, aKey):
    if (anEnum == validDecisions.DO_NOTHING):
        return aKey
    elif anEnum == validDecisions.JUMP:
        aKey[K_z] = True
    elif (anEnum == validDecisions.LEFT):
        aKey[K_LEFT] = True
    elif (anEnum == validDecisions.RIGHT):
        aKey[K_RIGHT] = True
    elif (anEnum == validDecisions.LEFT_JUMP):
        aKey[K_z] = True
        aKey[K_LEFT] = True
    elif (anEnum == validDecisions.RIGHT_JUMP):
        aKey[K_z] = True
        aKey[K_RIGHT] = True

    return aKey

def inverseMarioAction(aKey):
    myEnum=validDecisions.DO_NOTHING
    if(aKey[K_z] == True and aKey[K_LEFT] == True):
        myEnum=validDecisions.LEFT_JUMP
    elif(aKey[K_z] == True and aKey[K_RIGHT] == True):
        myEnum = validDecisions.RIGHT_JUMP
    elif(aKey[K_LEFT] == True):
        myEnum=validDecisions.LEFT
    elif(aKey[K_RIGHT]==True):
        myEnum=validDecisions.RIGHT
    elif(aKey[K_z]==True):
        myEnum=validDecisions.JUMP

    return myEnum



#     @classmethod
#     @getAction.register(object, int)
def getAction_0(aGame, aKey, aRandom=False, aPres=False):
    myKey = [False] * 1000
    aGame.score=aGame.score-1

    myCurrentContext = State().EnvironmentCompressor(aGame)


    State().updatingScore(aGame, myCurrentContext)

    if aRandom or random.random() < 0.10:#np.exp(-0.20*aGame.counterInLoop):
        myEnum = random.choice(list(validDecisions))  # [TOTAL_ACTIONS*random.random]
    elif random.random()<0.1:
        myEnum=validDecisions.DO_NOTHING
    elif(aPres):
        myEnum=inverseMarioAction(aKey)
    else:
        #         theBest=random.choice(list(validDecisions))
        #         theBestValue=-1000
        #         for context in aGame.theDecisionMaker:
        #             if(context[0]==myListOfBaddies and context[1]==myListOfCoins and context[3]==myListOfCanon and context[4]==myListOfGrass and \
        #                context[5]==myListOfPlatforms and context[6]==myListOfBricks and context[7]==myPlayerRect):
        #                 if(aGame.theDecisionMaker.get(context)>theBestValue):
        #                     theBest=context[2]
        #                     theBestValue=aGame.theDecisionMaker.get(context)
        theBest = aGame.theQLearner.getBestAction(aGame, myCurrentContext)


        myEnum = theBest  # list(validDecisions)[actionNumber]

    # saveDecision(aCurrentContext, aGame)

    aGame.theQLearner.setPreviousState(myCurrentContext)
    aGame.theQLearner.setPreviousAction(myEnum)
    return MarioAction(myEnum, myKey)


def saveDecision(anEnum, aGame):
    aGame.theCumActions.append(anEnum)


def getDecision(randomly=False):
    Nothing = 0
