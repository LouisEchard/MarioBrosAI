class State():
    import pygame
    class HashableRect(pygame.Rect):
        def __hash__(self):
            return hash(tuple(self))

    def EnvironmentCompressor(self, aGame):

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


        aCurrentContext = (tuple(myListOfBaddies), tuple(myListOfCoins), tuple(myListOfCanon), tuple(myListOfGrass), \
                           tuple(myListOfPlatforms), tuple(myListOfBricks), tuple(myListOfFlowers),
                           tuple(myListOfRoses),tuple(myListOfGMush))

        return aCurrentContext
        
        
    def updatingScore(self,aGame,aNewState):
        aGame.counterInLoop = aGame.counterInLoop + 1

        aGame.movementPoint = float(aGame.player.rect.x / 1) - float(aGame.oldPosition)
        aGame.score = aGame.score + aGame.movementPoint
        # self.reward.append(self.score)
        aGame.theQLearner.updateQValues(aGame.score,aNewState)
        goodTimeToSpreadScore = False

        if aGame.counterInLoop > 30:
            aGame.counterInLoop = 0
            aGame.QlearnSpread(sum(aGame.reward))
            aGame.theCumActions = []
            aGame.reward = []

        aGame.oldPosition = float(aGame.player.rect.x / 1)


