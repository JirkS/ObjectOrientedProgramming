class Auto:
    """ Trida auto reprezentuje auto pro simulaci realneho vozidlo pro cviceni PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l : float, spotreba_na_100_km_l: float):
        """
        Konstruktor nastavi objem nadrze a spotrebu dle parametru a nastavi prazdnou nadrz.

        :param objem_nadrze_l: Objem nadrze v litrech
        :param spotreba_na_100_km_l: Spotreba na 100km v litrech
        """

        if objem_nadrze_l < 0:
            raise Exception("Nadrz musi mit kladny objem")
        if spotreba_na_100_km_l < 0:
            raise Exception("Spotreba nesmi byt zaporna")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0
        self._najete_km = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrati aktualni stav nadrze
        :return: Zbyle palivo v nadrzi v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def natankuj(self, objem_l: float ) -> None:
        if objem_l < 0:
            raise Exception("Nelze odcerpat palivo pomoci metody natankovat")

        if(self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l:
            raise Exception("Nelze nacerpat vice nez je kapacita nadrze")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km : float ) -> None:
        if pocet_km < 0:
            raise Exception("Couvani je take jizda, smer neresime")

        spotreba_paliva_l = pocet_km/100.0 * self.spotreba_na_100_km_l
        self._najete_km += pocet_km

        if self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l:
            raise Exception("Na jizdu neni dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l

    def aktualni_stav_najetych_km(self) -> float:
        """
        Metoda vrati aktualni najete km
        :return: najete km
        """
        return self._najete_km


try:
    a = Auto(30, 12.5)
    print(a.aktualni_stav_nadrze())
    a.natankuj(22.5)
    print(a.aktualni_stav_nadrze())
    a.popojed(20)
    print(a.aktualni_stav_nadrze())
    print(a.aktualni_stav_najetych_km())
except Exception as e:
    print(e)
