
class MarioAIOptions():
    CmdLineOptionsMapString = {}
    optionsAsString = ""
#     marioInitialPos = Point()

    @overloaded
    def __init__(self, args):
        super(MarioAIOptions, self).__init__()
        self.setArgs(args)

    @__init__.register(object, str)
    def __init___0(self, args):
        super(MarioAIOptions, self).__init__()
        self.setArgs(args)

    @__init__.register(object)
    def __init___1(self):
        super(MarioAIOptions, self).__init__()
        self.setArgs("")

    @overloaded
    def setArgs(self, argString):
        if not "" == argString:
            self.setArgs(argString.trim().split("\\s+"))
        else:
            self.setArgs(str(None))

    def asString(self):
        return self.optionsAsString

    @setArgs.register(object, str)
    def setArgs_0(self, args):
        
        if args != None:
            for s in args:
                self.optionsAsString += s + " "
        self.setUpOptions(args)
        if isEcho():
            self.printOptions(False)
        GlobalOptions.receptiveFieldWidth = getReceptiveFieldWidth()
        GlobalOptions.receptiveFieldHeight = getReceptiveFieldHeight()
        if getMarioEgoPosCol() == 9 and GlobalOptions.receptiveFieldWidth != 19:
            GlobalOptions.marioEgoCol = GlobalOptions.receptiveFieldWidth / 2
        else:
            GlobalOptions.marioEgoCol = getMarioEgoPosCol()
        if getMarioEgoPosRow() == 9 and GlobalOptions.receptiveFieldHeight != 19:
            GlobalOptions.marioEgoRow = GlobalOptions.receptiveFieldHeight / 2
        else:
            GlobalOptions.marioEgoRow = getMarioEgoPosRow()
        GlobalOptions.VISUAL_COMPONENT_HEIGHT = getViewHeight()
        GlobalOptions.VISUAL_COMPONENT_WIDTH = getViewWidth()
        GlobalOptions.isShowReceptiveField = isReceptiveFieldVisualized()
        GlobalOptions.isGameplayStopped = isStopGamePlay()

    def getMarioGravity(self):
        return f(getParameterValue("-mgr"))

    def setMarioGravity(self, mgr):
        setParameterValue("-mgr", s(mgr))

    def getWind(self):
        return f(getParameterValue("-w"))

    def setWind(self, wind):
        setParameterValue("-w", s(wind))

    def getIce(self):
        return f(getParameterValue("-ice"))

    def setIce(self, ice):
        setParameterValue("-ice", s(ice))

    def getCreaturesGravity(self):
        return f(getParameterValue("-cgr"))

    def getViewWidth(self):
        return i(getParameterValue("-vw"))

    def setViewWidth(self, width):
        setParameterValue("-vw", s(width))

    def getViewHeight(self):
        return i(getParameterValue("-vh"))

    def setViewHeight(self, height):
        setParameterValue("-vh", s(height))

    def printOptions(self, singleLine):
        print "\n[MarioAI] : Options have been set to:"
        for el in optionsHashMap.entrySet():
            if singleLine:
                print el.getKey("," + " " + el.getValue() + " ")
            else:
                print el.getKey() + " " + el.getValue() + " "

    @classmethod
    def getOptionsByString(cls, argString):
        if cls.CmdLineOptionsMapString.get(argString) == None:
            cls.CmdLineOptionsMapString.put(argString, value)
            return value
        return cls.CmdLineOptionsMapString.get(argString)

    @classmethod
    def getDefaultOptions(cls):
        return cls.getOptionsByString("")

    def isToolsConfigurator(self):
        return b(getParameterValue("-tc"))

    def isGameViewer(self):
        return b(getParameterValue("-gv"))

    def setGameViewer(self, gv):
        setParameterValue("-gv", s(gv))

    def isGameViewerContinuousUpdates(self):
        return b(getParameterValue("-gvc"))

    def setGameViewerContinuousUpdates(self, gvc):
        setParameterValue("-gvc", s(gvc))

    def isEcho(self):
        return b(getParameterValue("-echo"))

    def setEcho(self, echo):
        setParameterValue("-echo", s(echo))

    def isStopGamePlay(self):
        return b(getParameterValue("-stop"))

    def setStopGamePlay(self, stop):
        setParameterValue("-stop", s(stop))

    def getJumpPower(self):
        return f(getParameterValue("-jp"))

    def setJumpPower(self, jp):
        setParameterValue("-jp", s(jp))

    def getReceptiveFieldWidth(self):
        ret = i(getParameterValue("-rfw"))

        return ret

    def setReceptiveFieldWidth(self, rfw):
        setParameterValue("-rfw", s(rfw))

    def getReceptiveFieldHeight(self):
        ret = i(getParameterValue("-rfh"))
        return ret

    def setReceptiveFieldHeight(self, rfh):
        setParameterValue("-rfh", s(rfh))

    def isReceptiveFieldVisualized(self):
        return b(getParameterValue("-srf"))

    def setReceptiveFieldVisualized(self, srf):
        setParameterValue("-srf", s(srf))

    def getMarioInitialPos(self):
        self.marioInitialPos.x = i(getParameterValue("-mix"))
        self.marioInitialPos.y = i(getParameterValue("-miy"))
        return self.marioInitialPos

    def reset(self):
        optionsHashMap.clear()

    def getMarioEgoPosRow(self):
        return i(getParameterValue("-mer"))

    def getMarioEgoPosCol(self):
        return i(getParameterValue("-mec"))

    def getExitX(self):
        return i(getParameterValue("-ex"))

    def getExitY(self):
        return i(getParameterValue("-ey"))

    def setExitX(self, x):
        setParameterValue("-ex", s(x))

    def setExitY(self, y):
        setParameterValue("-ey", s(y))
