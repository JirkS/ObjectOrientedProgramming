class Bottle:

    def __init__(self, c, f, o):
        self.open = None
        self.check_open(o)
        self.capacity = None
        self.check_capacity(c)
        self.fullness = None
        self.set_fullness(f)

    def check_open(self, o):
        if type(o) == bool:
            self.open = o
        else:
            raise Exception("Promenna \"open\" muze byt pouze but True nebo False typu boolean!")

    def check_capacity(self, c):
        """
        Checking validation of variable capacity
        :param c:
        :return: True/False by if is the num int and positive
        """
        if (isinstance(f, int) or isinstance(f, float)) and c >= 0:
            self.capacity = c
        else:
            raise Exception("Promenna \"capacity\" musi byt kladne cislo!")

    def check_fullness(self, f):
        """
        Checking validation of variable fullness
        :param f:
        :return: True/False by if is the num int and positive
        """
        if (isinstance(f, int) or isinstance(f, float)) and f >= 0:
            return True
        else:
            raise Exception("Promenna \"fullness\" musi byt kladne cislo!")
            return False

    def set_fullness(self, f):
        """
        Setting fullness
        :param f: number to set into fullness
        """
        if self.open:
            if f < self.capacity and self.check_fullness(f):
                self.fullness = f
            else:
                raise Exception("Tolik tekutiny se do lahve nevejde!")
        else:
            raise Exception("Lahev je zavrena!")

    def get_fullness(self):
        return "naplnena: " + str(self.fullness) + " [l]"

    def set_fullness_empty(self):
        """
        Set empty volume to bottle
        :param fullness
        """
        if self.open:
            self.fullness = 0
        else:
            raise Exception("Lahev je zavrena!")

    def set_fullness_ml(self, num):
        """
        Set volume to bottle in ml
        :param num: number of new volume
        """
        self.set_fullness(num/1000)

    def get_fullness_ml(self):
        """
        Return value of fullness of bottle
        :return: value of fullness of bottle
        """
        return "naplnena: " + str(self.fullness * 10**3) + " [ml]"

    def open_close(self):
        """
        When bottle is close, method will open it, when bootle is open, method will close it
        """
        if self.open:
            self.open = False
        else:
            self.open = True

    def printf(self):
        """
        :return: pekny, prehledny vypis se vsemi informacemi
        """
        return "Lahev - kapacita: " + str(self.capacity) + " [l], naplnena: " + str(self.fullness) + " [l], otavrena: " + str(self.open)

