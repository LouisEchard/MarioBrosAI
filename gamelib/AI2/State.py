class State():
    import pygame

    myFListOfBaddies = []
    myFListOfCoins = []
    myFListOfCanon = []
    myFListOfGrass = []
    myFListOfPlatforms = []
    myFListOfBricks = []
    myFListOfFlowers = []
    myFListOfGMush = []
    myFListOfRoses = []

    myFListOfMovPlat = []
    myFListOfMovPlat2 = []
    myFPlayerRect = []
    counter=0

    class HashableRect(pygame.Rect):
        def __hash__(self):
            return hash(tuple(self))

    def EnvironmentCompressor(self, aGame):

        import StateConvertor as convertor

        myListOfBaddies = []
        myListOfCoins = []
        myListOfCanon = []
        myListOfGrass = []
        myListOfPlatforms = []
        myListOfBricks = []
        myListOfFlowers = []
        myListOfGMush = []
        myListOfRoses = []
        myPlayerRect = aGame.player.rect
        myListOfMovPlat=[]
        myListOfMovPlat2=[]
        myListOfFireBrows=[]
        myListOfBosses=[]
        myListOfShots=[]
        myListOfBomb=[]

        for b in aGame.baddies:
            if b.rect.colliderect(aGame.camera.rect):
                myListOfBaddies.append(self.HashableRect(b.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for c in aGame.coins:
            if aGame.camera.rect.colliderect(c.rect):
                myListOfCoins.append(self.HashableRect(c.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for g in aGame.grasss:
            g.update()
            if aGame.camera.rect.colliderect(g.rect):
                myListOfGrass.append(self.HashableRect(g.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for b in aGame.cannons:
            b.update()
            if aGame.camera.rect.colliderect(b.rect):
                myListOfCanon.append(self.HashableRect(b.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for p in aGame.platforms:
            p.update()
            if aGame.camera.rect.colliderect(p.rect):
                #             aGame.player.collide(aGame.springs)
                #             aGame.player.collide(aGame.platforms)
                myListOfPlatforms.append(self.HashableRect(p.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for b in aGame.bricks:
            b.update()
            if aGame.camera.rect.colliderect(b.rect):
                #             aGame.player.collide(aGame.springs)
                #             aGame.player.collide(aGame.platforms)
                myListOfBricks.append(self.HashableRect(b.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for b in aGame.flowers:
            if aGame.camera.rect.colliderect(b.rect):
                myListOfFlowers.append(self.HashableRect(b.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for r in aGame.roses:
            if aGame.camera.rect.colliderect(r.rect):
                myListOfRoses.append(self.HashableRect(r.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for m in aGame.mushroomgreens:
            if aGame.camera.rect.colliderect(m.rect):
                myListOfGMush.append(self.HashableRect(m.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for p in aGame.movingplatformtwos:
            if aGame.camera.rect.colliderect(p.rect):
                myListOfMovPlat2.append(self.HashableRect(p.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for p in aGame.movingplatforms:
            if aGame.camera.rect.colliderect(p.rect):
                myListOfMovPlat.append(self.HashableRect(p.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for b in aGame.bombs:
            if aGame.camera.rect.colliderect(b.rect):
                myListOfBomb.append(self.HashableRect(b.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for s in aGame.shots:
            if aGame.camera.rect.colliderect(s.rect):
                myListOfShots.append(self.HashableRect(s.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for b in aGame.bosses:
            if aGame.camera.rect.colliderect(m.rect):
                myListOfBosses.append(self.HashableRect(p.rect.move(-myPlayerRect.x, -myPlayerRect.y)))

        for f in aGame.firebowsers:
            if aGame.camera.rect.colliderect(f.rect):
                myListOfFireBrows.append(self.HashableRect(f.rect.move(-myPlayerRect.x, -myPlayerRect.y)))


        myTempCurrentContext = (tuple(myListOfBaddies), tuple(myListOfCoins), tuple(myListOfCanon), tuple(myListOfGrass), \
                           tuple(myListOfPlatforms), tuple(myListOfBricks), tuple(myListOfFlowers),
                           tuple(myListOfRoses),tuple(myListOfGMush),
                           tuple(myListOfMovPlat), tuple(myListOfMovPlat2),
                           tuple(myListOfBomb), tuple(myListOfFireBrows),
                           tuple(myListOfBosses),tuple(myListOfShots),
                           # tuple([self.HashableRect(myPlayerRect)]),
                           tuple(self.myFListOfBaddies),tuple(self.myFListOfFlowers),
                           tuple(self.myFListOfGMush),
                           tuple(self.myFListOfMovPlat), tuple(self.myFListOfMovPlat2)
                           )
        myCurrentContext=convertor.compressStateToNumberHash(myTempCurrentContext)

        if self.counter>1:
            self.counter=0
            self.myFListOfBaddies = myListOfBaddies

            self.myFListOfFlowers = myListOfFlowers
            self.myFListOfGMush = myListOfGMush
            self.myFPlayerRect = myPlayerRect
            self.myFListOfMovPlat=myListOfMovPlat
            self.myFListOfMovPlat2=myListOfMovPlat2
        self.counter +=1

        return myCurrentContext
        
        
    def updatingScore(self,aGame,aNewState):
        aGame.counterInLoop = aGame.counterInLoop + 1

        aGame.movementPoint = float(aGame.player.rect.x / 1) - float(aGame.oldPosition)
        aGame.score = aGame.score + 0.3*aGame.movementPoint
        # self.reward.append(self.score)
        aGame.theQLearner.updateQValues(aGame.score-aGame.oldScore,aNewState)
        goodTimeToSpreadScore = False

        # if aGame.counterInLoop > 30:
        #     aGame.counterInLoop = 0
        #     aGame.QlearnSpread(sum(aGame.reward))
        #     aGame.theCumActions = []
        #     aGame.reward = []
        aGame.oldScore=aGame.score
        aGame.oldPosition = float(aGame.player.rect.x / 1)


