import Bottle
import Dvere

try:
    b = Bottle.Bottle(10, 3, True)

    print(b.printf())
    b.set_fullness(5)
    print(b.printf())
    print(b.get_fullness())
    b.set_fullness_empty()
    print(b.printf())
    b.set_fullness_ml(1800)
    print(b.printf())
    print(b.get_fullness_ml())
    b.open_close()
    b.open_close()
    b.set_fullness(0)
    print(b.printf())

    d = Dvere.Dvere(False, False)
    print(d.otevrit())

except Dvere.ZamceneDvereException as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Program nespadl a dobehl az do konce!")
