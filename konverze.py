import re


class BankovniUcet:
    """ Trida ukazuje simulaci bankovniho uctu """

    def __init__(self, cislo_uctu: str, mena: str):
        """
        Konstruktor prijima cislo uctu a menu, ve ktere je vedeny.

        :param cislo_uctu: Cislo uctu i kod banky ve formatu 5-10 cislic / 4 cislice
        :param mena: Mena uctu vyjadrena jako tri pismena, napr. EUR
        """
        if not re.match(r"^[0-9]{5,10}/[0-9]{4}$",cislo_uctu):
            raise Exception('Cislo uctu neodpovida formatu zapisu 000000000/0000.')

        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._cislo_uctu = cislo_uctu
        self._mena = mena
        self._zustatek = 0

    def __str__(self):
        return self._cislo_uctu + ": " + str(self._zustatek) + " " + str(self._mena)

    def __int__(self):
        return int(self._zustatek)

    def __float__(self):
        return float(self._zustatek)


try:
    muj_ucet = BankovniUcet("12341238/0100", "CZK")
    print(muj_ucet)
    ucet_alice = BankovniUcet("98526487/0500","EUR")
    print(ucet_alice)
    zustatek_alice = int(ucet_alice)
    print(zustatek_alice)
    zustatek_alice = float(ucet_alice)
    print(zustatek_alice)
except Exception as e:
    print(e)
