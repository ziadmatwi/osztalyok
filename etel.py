class Etel:
    def __init__(self,nev:str,ar:int=1000):
        """Konstruktor feladata, hogy létrehozza a konkrét példányt, a konkrét adatokkal
        a tervrajzból, és beállítsa az adattagokat - objektum tulajdonságok értékei
        """
        self.nev=nev
        self.ar=ar
        self.allapot="készül"

    def keszul(self):
        self.allapot="kész"

    def __str__(self):
        return f"Étel neve:{self.nev}, Ár: {self.ar} Ft, Állapot: {self.allapot} " 

