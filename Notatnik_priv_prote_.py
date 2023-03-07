#*********
# klasa : Notatnik
# opis: klasa Notatnik przezentuje notatnik który wyswietla tytuł , tresc , id oraz licznik 
# pola :  __licznik - przyjmuje int i inkrementuje sie
#         id - przyjmuje int i inkrementuje sie
#         _tytul - przyjmuje String
#         _tresc - przyjmuje String
# autor: 3123123
#*********



class Notatnik:
    __licznik = 0

    def __init__(self,tytul,tresc):
        Notatnik.__licznik+=1
        self.id = Notatnik.__licznik
        self._tytul = tytul
        self._tresc = tresc
    
    def wypisz(self):
        print(f"\nTytuł: {self._tytul} tresc: {self._tresc}")
    def diagnostyczne(self):
        print(f"Tytuł: {self._tytul} ;tresc: {self._tresc};id: {self.id} ;licznik:{Notatnik.__licznik}")

#TESTY PONIŻEJ

N1= "Tytuł1"
T1="Tresc pierwszej notatki"

N2 = "Tytuł2"
T2 ="Tresc drugiej notatki"       

object1= Notatnik(N1,T1)
object1.wypisz()
object1.diagnostyczne()

object2 = Notatnik(N2,T2)
object2.wypisz()
object2.diagnostyczne()
