
filePath = "/home/ldrahce/git/MarioBros-AI/gamelib/AI2/QStatesAndValues.txt"

from actionSelector import validDecisions as VD
from pygame.rect import Rect
import pygame

class HashableRect(pygame.Rect):
    def __hash__(self):
        return hash(tuple(self))

def save(dict):
    file = open(filePath, 'w')
    for obj in dict.keys():
        save = True
        myString = ""
        file.write('\n')

        for length in obj[0]:
            myString = myString + str(length)+":"

        myString = myString + ";"

        for rect in obj[1]:
            if(isinstance(rect,int)):
                hehe="stop"
            for dim in rect:
                myString = myString + str(dim)+":"
            myString = myString+";"


        # for key in obj:
        #     if(key==()):
        #         myString = myString+"empty;"
        #     elif(key==""):
        #         myString=myString
        #     else:
        #         if not isinstance(key[0], int):
        #             myRect = key[0]
        #         else:
        #             myRect = key
        #         myString=myString+str(myRect.left)+":"+str(myRect.top)+":"+str(myRect.width)+":"+str(myRect.height)+";"

        if save and obj!=():
            file.write(myString+" ,Results ")
            for enum in VD:
                # if len(dict[obj])<5:
                #     stop=True
                file.write(str(dict[obj][enum.value])+':')


def load(dict):
    # def __hash__(self):
    #     return hash(tuple(self))
    myLastTuple=()
    first=True
    myArrayOfResults=[]
    with open(filePath) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            if(line!=""):
                myResults=line.split(" ,Results ")
                mySplitResults=myResults[1].split(":")
                mySplitResults.remove("")
                myContexts=myResults[0].split(";")

                myTuple=()
                myTupleOfLen=()
                myArrayOfLenghts=[]
                myFirst=True
                for stri in myContexts:
                    if(myFirst):
                        myArrayOfLenghts=stri.split(":")
                        myArrayOfLenghts.remove("")
                        myFirst=False
                        for length in myArrayOfLenghts:
                            if isinstance(int(length), int):
                                myTupleOfLen= myTupleOfLen+(int(length),)
                    else:
                        myArrayOfRectDim=stri.split(":")
                        myArrayOfRectDim.remove("")
                        # for length in myArrayOfLenghts:
                        #     myCategoryCounter=length
                        #     while myCategoryCounter>0:
                        #         myCounterOfDim
                        #         myCategoryCounter=myCategoryCounter-1
                        myTempTuple=()
                        for val in myArrayOfRectDim:
                            if(isinstance(int(val), int)):
                                myTempTuple = myTempTuple + (int(val),)
                            else:
                                doSave=False
                        if(myTempTuple!=()):
                            myTuple=myTuple+(myTempTuple,)

                    # myFirst=False
                # if(myTuple!=myLastTuple):
                myFinalTuple=(tuple((myTupleOfLen,)))+(tuple((myTuple,)))
                dict[myFinalTuple] = map(float,mySplitResults)

    return dict


