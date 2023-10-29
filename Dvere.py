class Dvere:

    def __init__(self, o, z):
        self.otevreno = None
        self.check_otevreno(o)
        self.zamceno = None
        self.check_zamceno(z)

    def check_otevreno(self, o):
        if type(o) == bool:
            self.otevreno = o
        else:
            raise Exception("Promenna \"otevreno\" muze byt pouze but True nebo False typu boolean!")

    def check_zamceno(self, z):
        if type(z) == bool:
            self.zamceno = z
        else:
            raise Exception("Promenna \"zamceno\" muze byt pouze but True nebo False typu boolean!")

    def otevrit(self):
        """
        Metoda pro otevreni dveri
        :return: prosel/neprosel
        """
        if not self.zamceno:
            if not self.otevreno:
                self.otevreno = True
            return self.projit()
        else:
            raise ZamceneDvereException("Dvere jsou zamcene, nelze otevrit a projit!")

    def zavrit(self):
        """
        Metoda pro zavreni dveri za sebou po projiti otevrenymi dvermi
        """
        if self.otevreno:
            self.otevreno = False

    def projit(self):
        """
        Metoda pro projiti otevrenych dveri
        :return: prosel/neprosel
        """
        if self.otevreno:
            self.zavrit()
            return "prosel"
        else:
            return "neprosel"

    def odemknout(self):
        """
        Metoda pro odemknuti dveri
        :return:
        """
        if self.zamceno:
            self.zamceno = False
        else:
            self.zamknout()

    def zamknout(self):
        """
        Metoda pro zamknuti dveri
        """
        if self.zamceno:
            self.zamceno = True

class ZamceneDvereException(Exception):
    pass
