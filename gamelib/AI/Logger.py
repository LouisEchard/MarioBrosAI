
class Logger(object):
    @classmethod
    @overloaded
    def println(cls, level, message):
        Logger.print_(level, message + "\n")

    @classmethod
    @println.register(object, int, object)
    def println_0(cls, level, message):
        Logger.println(level, message.__str__())

    @classmethod
    @println.register(object, int, int)
    def println_1(cls, level, number):
        Logger.println(level, String.valueOf(number))

    @classmethod
    @println.register(object, int, str, A)
    def println_2(cls, level, format, *values):
        Logger.println(level, String.format(format, values))

    @classmethod
    def print_(cls, level, message):
        if level <= LearningParams.DEBUG:
            print message,
