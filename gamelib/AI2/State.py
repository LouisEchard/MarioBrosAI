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
        myPlayerRect = aGame.player.rect

        for b in aGame.baddies:
            if b.rect.colliderect(aGame.camera.rect):
                myListOfBaddies.append(self.HashableRect(b.rect))

        for c in aGame.coins:
            if aGame.camera.rect.colliderect(c.rect):
                myListOfCoins.append(self.HashableRect(c.rect))

        for g in aGame.grasss:
            g.update()
            if aGame.camera.rect.colliderect(g.rect):
                myListOfGrass.append(self.HashableRect(g.rect))

        for b in aGame.cannons:
            b.update()
            if aGame.camera.rect.colliderect(b.rect):
                myListOfCanon.append(self.HashableRect(b.rect))

        for p in aGame.platforms:
            p.update()
            if aGame.camera.rect.colliderect(p.rect):
                #             aGame.player.collide(aGame.springs)
                #             aGame.player.collide(aGame.platforms)
                myListOfPlatforms.append(self.HashableRect(p.rect))

        for b in aGame.bricks:
            b.update()
            if aGame.camera.rect.colliderect(b.rect):
                #             aGame.player.collide(aGame.springs)
                #             aGame.player.collide(aGame.platforms)
                myListOfBricks.append(self.HashableRect(b.rect))

        aCurrentContext = (tuple(myListOfBaddies), tuple(myListOfCoins), tuple(myListOfCanon), tuple(myListOfGrass), \
                           tuple(myListOfPlatforms), tuple(myListOfBricks), tuple(myPlayerRect))

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


