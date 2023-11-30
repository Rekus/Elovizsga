from abc import ABC, abstractmethod
from datetime import datetime
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def tulajdonsag(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, agytipus, dohanyzo):
        super().__init__(ar, szobaszam)
        self.agytipus = agytipus
        self.dohanyzo = dohanyzo

    def tulajdonsag(self):
        pass

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, agytipus, kilatas):
        super().__init__(ar, szobaszam)
        self.agytipus = agytipus
        self.kilatas = kilatas

    def tulajdonsag(self):
        pass

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    #def list_szobak(self):
    #    for szoba in self.szobak:
    #        szoba.tulajdonsag()

    def foglalasok(self, szobaszam, datum):
        foglalas = Foglalas()
        return foglalas

    #foglalasok = Foglalas(szobaszam, datum)
    #self.foglalasok.append(foglalasok)


    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print(f"Foglalés törölve!")
        else:
            print("Nincs ilyen foglalás.")

    def list_foglalasok(self):
        print(f"{self.nev} szálloda foglalásai:")

class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum


egyagyas = EgyagyasSzoba(5000, 102, "single", True)
ketagyas = KetagyasSzoba(8000, 110, "twin", False)

szalloda = Szalloda("Elmeny es SPA Resort")

foglalas_egyagyas = szalloda.foglalasok(egyagyas, (2023, 11, 30))
foglalas_ketagyas = szalloda.foglalasok(ketagyas, (2023, 12, 01))

szalloda.list_foglalasok()
szalloda.lemondas()
szalloda.list_foglalasok()

