class Zbozi:
    def __init__(self):
        self._vaha = 0

    @property
    def vaha(self):
        return self._vaha

    @vaha.setter
    def vaha(self,x):
        if x < 0:
            raise Exception("Zaporna vaha nesmi existovat")

        self._vaha = x


class Obdelnik:
    def __init__(self):
        self._a = 0
        self._b = 0

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, x):
        if x < 0:
            raise Exception("Zaporna strana nesmi existovat")
        self._a = x

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, y):
        if y < 0:
            raise Exception("Zaporna strana nesmi existovat")
        self._b = y


try:
    rohlik = Zbozi()
    rohlik.vaha = 10
    print(rohlik.vaha)
    obdelnik = Obdelnik()
    obdelnik.a = 30
    obdelnik.b = 29
    print(str(obdelnik.a) + ", " + str(obdelnik.b))
except Exception as e:
    print(e)
