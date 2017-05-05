import pygame



def compressStateToNumberHash(aState):
    # hash=13;
    lengthPerDimension=()
    dimRect=()
    listOfRect=()
    # for object in aState:
    #     if(isinstance(object[0],pygame.rect)):
    #         for rect in object:
    #             hash=7*rect+1

    if(aState==()):
        return
    len(aState)
    for intI in range(0,len(aState)):
        lengthPerDimension=lengthPerDimension+(len(aState[intI]),)

    for intJ in range(0,len(aState)):
        for rect in aState[intJ]:
            for dim in rect:
                dimRect=dimRect+(dim,)
            listOfRect=listOfRect+(dimRect,)
            dimRect=()

    return (tuple(lengthPerDimension),)+(listOfRect,)



# def reverseCompression(aHash):
#     (aHash-1) /7