class Zbozi:

    def __init__(self,nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi "+str(self.nazev)+" bylo vymazano z pameti")


try:
    z = Zbozi("mliko")
    moje = z
    del z
    del moje
    print("konec programu")
except Exception as e:
    print(e)
