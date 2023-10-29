class Zbozi:
    def __new__(cls, nazev: str, cena: int):
        if (not isinstance(cena, int) and not isinstance(cena, float)) or cena < 0:
            raise ValueError("Promenna \"cena\" nemuze byt zaporna a musi byt typu int nebo float!")
        elif not isinstance(nazev, str) or len(nazev) == 0:
            raise ValueError("Promenna \"nazev\" nesmi byt prazdna!")
        else:
            instance = super().__new__(cls)
        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def printf(self):
        return self.nazev + " stoji " + str(self.cena) + "Kc"


try:
    a = Zbozi("Rohlik", 58)
    print(a.printf())
    b = Zbozi("Hackers item", 10)
    print(b.printf())
except Exception as e:
    print(e)
