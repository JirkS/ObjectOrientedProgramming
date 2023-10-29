class Zivnostnik:
    """ Trida reprezentuje zivnostnika """

    @staticmethod
    def factory_from_obchodni_nazev(obchodni_nazev: str):
        """
        Staticka metoda vytvorit zivnostnika z obchodniho nazvu

        :param obchodni_nazev: Napriklad Jan Novak
        :return: Novy objekt tridy Zinvostnik
        """
        data = obchodni_nazev.split(' ')

        if len(data) != 2:
            raise Exception("Nelze parsovat obchodni nazev")

        return Zivnostnik(data[0], data[1])

    def __init__(self, jmeno: str, prijmeni: str):
        """
        Konstruktor nastavi jmeno a prijimeni
        :param jmeno: Jmeno zivnostnika
        :param prijmeni: Prijimeni zivnostnika
        """
        if len(jmeno) < 1 or len(prijmeni) < 0:
            raise Exception("Jmeno a prijimani musi byt definovnao")

        self.jmeno = jmeno
        self.prijmeni = prijmeni


class Firma:
    """ Třída reprezentuje firmu"""

    @staticmethod
    def factory_from_obchodni_nazev(obchodni_nazev: str):
        data = obchodni_nazev.split(', ')

        if len(data) != 2:
            raise Exception("Nelze parsovat obchodni nazev")

        return Firma(data[0], data[1])

    def __init__(self, nazev, pravni_forma):
        """
        Vytvoří instanci firmy
        :param nazev: Název například Maso a uzeniny od Pavlíka
        :param pravni_forma: Právní forma, například s.r.o, nebo a.s. apod.
        """
        self.jmeno = nazev
        self.pravni_forma = pravni_forma


try:
    sporka = Firma.factory_from_obchodni_nazev("Česká spořitelna, a.s.")
    print(sporka.pravni_forma)  # ma vypsat "a.s."
    pepa = Zivnostnik.factory_from_obchodni_nazev("Josef Novák")
    print(pepa.prijmeni)
except Exception as e:
    print(e)
