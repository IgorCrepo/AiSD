#stos (stack)

class Item:

    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None # ustawiamy element następny jako pusty
        self.poprzedni = None # ustawiamy element poprzedni jako pusty

class Stos:
    def __init__(self):
        self.head = None

    def push(self, wartosc):
        # jeżeli pusta
        if self.head is None:
            self.head = Item(wartosc)
        # jeżeli niepusta    
        else:
            nowy_Item = Item(wartosc) # nowy item to Item z podaną wartością
            self.head.poprzedni = nowy_Item # obecny head ustawia na element poprzedzający nowy item
            nowy_Item.nastepny = self.head # kolejny item od nowego to obecny self head
            nowy_Item.poprzedni = None # poprzednik nowego heada -> brak
            self.head = nowy_Item # ustawienie head na nowy item

    # funkcja pop
    def pop(self):
        # jeżeli pusta
        if self.head is None:
            return None
        else:
            popowany = self.head.wartosc # ustalenie wartości popwanego elementu
            self.head = self.head.nastepny # ustalenie nowego heada
            if self.head is None:
                return None
            else:
                self.head.poprzedni = None # ustalenie elementu poprzedniego na brak
                return popowany # zwracanie elemntu przy użyciu funkcji pop

    # funkcja sprawdzająca czy stos jest pusty:
    def czyPusty(self):
        if self.head == None:
            return ("STOS PUSTY")
        else:
            return ("STOS MA ELEMENTY")

    # funkcja pokazująca element na górze
    def gora(self):

        return self.head.wartosc

    # rozmiar stosu
    def rozmiar(self):

        element = self.head
        dlugosc = 0
        while element != None:
            dlugosc += 1
            element = element.nastepny
        return dlugosc
        
    def wyswietl(self):
        
        element = self.head
        while element != None:
            print(element.wartosc)
            element = element.nastepny

s = Stos()

s.push(1)
s.push(3)
s.push(7)
s.push(8)
s.push(9)
s.wyswietl()
s.pop()
print("")
s.wyswietl()
print("")
print(s.gora())
print("")
print(s.rozmiar())
print("")
print(s.czyPusty())
s.pop()
s.pop()
s.pop()
s.pop()
print("")
print(s.czyPusty())
s.pop()

