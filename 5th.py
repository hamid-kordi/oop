class Demo:

    def __init__(self):

        self.a = 1

        self._b = 2

        self.__c = 3

    def _display(self, inp):
        self.__c = 5 * inp
        return self.__c

    def incr(self, inv):
        self._display(inv)


obj = Demo()


print(obj._display(5))
