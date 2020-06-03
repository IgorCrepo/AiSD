

#kolejka (queue)

class Item:

    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None # ustawiamy element następny jako pusty
        self.poprzedni = None # ustawiamy element poprzedni jako pusty

class Kolejka:
    def __init__(self):
        self.head = None
        self.ostatni = None

    def push(self, wartosc):
        # jeżeli pusta
        if self.ostatni == None:
            self.head  = Item(wartosc)
            self.ostatni = self.head
        # jeżeli niepusta  
        else:
            self.ostatni.nastepny = Item(wartosc)
            self.ostatni.nastepny.poprzedni = self.ostatni
            self.ostatni = self.ostatni.nastepny
          
    # funkcja pop
    def pop(self):
        # jeżeli pusta
        if self.head == None:
            return None

        else:
            popowany = self.head.wartosc # ustalenie wartości popwanego elementu
            self.head = self.head.nastepny # ustalenie nowego heada
            if self.head == None:
                return None
            else:
                self.head.poprzedni = None # ustalenie elementu poprzedniego na brak
                return popowany # zwracanie elemntu przy użyciu funkcji pop

    # funkcja sprawdzająca czy stos jest pusty:
    def czyPusty(self):
        if self.head == None:
            return ("KOLEJKA JEST PUSTA")
        else:
            return ("KOLEJKA MA ELEMENTY")

    # funkcja pokazująca element na górze
    def pierwszy(self):

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
            print(element.wartosc , end= " ")
            element = element.nastepny

s = Kolejka()

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
print(s.pierwszy())
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

