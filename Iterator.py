parta = ["Karel", "Petra", "Mirka"]
iterator_party = iter(parta)
try:
    for jmeno in parta:
        print(jmeno)
    print()
    print(next(iterator_party))
    print(next(iterator_party))
    print(next(iterator_party))
    print(next(iterator_party))  # Tohle vyhodi vyjimku StopIteration error protoze dalsi uz nema
except StopIteration as si:
    print(si)
