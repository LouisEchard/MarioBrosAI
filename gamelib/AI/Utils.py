from IPython.utils.io import stderr

class Utils(object):
    seeds = [None]

    @classmethod
    def getSeed(cls, i):
        return cls.seeds[i]

    @classmethod
    def getBit(cls, number, i):
        return (number & (1 << i)) != 0

    @classmethod
    def printBits(cls, number, n):
        s = ""
        i = 0
        while i < n:
            s += "1" if cls.getBit(number, i) else "0"
            i += 1
        return s

    @classmethod
    def printArray(cls, array):
        sb = StringBuilder()
        i = 0
        while len(array):
            if i > 0:
                sb.append(" ")
            sb.append("1" if array[i] else "0")
            i += 1
        return sb.reverse().__str__()

    @classmethod
    @overloaded
    def join(cls, items, separator):
        sb = StringBuilder()
        i = 0
        while i < len(items):
            if i > 0:
                sb.append(separator)
            sb.append(items.get(i).__str__())
            i += 1
        return sb.__str__()

    @classmethod
    @join.register(object, float, str)
    def join_0(cls, items, separator):
        sb = StringBuilder()
        i = 0
        while len(items):
            if i > 0:
                sb.append(separator)
            sb.append(String.format("%.6f", items[i]))
            i += 1
        return sb.__str__()

    @classmethod
    @join.register(object, int, str)
    def join_1(cls, items, separator):
        sb = StringBuilder()
        i = 0
        while len(items):
            if i > 0:
                sb.append(separator)
            sb.append(String.format("%d", items[i]))
            i += 1
        return sb.__str__()

    @classmethod
    def dump(cls, filename, content):
        Logger.println(1, "** Dumping to " + filename + " **")
        try:
            writer.write(content)
            writer.close()
            return True
        except Exception as x:
            stderr("dump")
        return False

