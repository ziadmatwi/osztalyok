import datetime

class Alkalmazott:
    def __init__(self,nev:str,szul_datum:int,fizetes:int,pozicio:str):
        self.nev=nev
        self.szul_datum=szul_datum
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.kor_beallit()

    def kor_beallit(self):
        today = datetime.date.today()
        year = today.year
        kor:int=year-self.szul_datum 
        self.kor=kor
    
    def __str__(self):
        return f"Alkalmazott neve:{self.nev}, Születési dátuma: {self.szul_datum} , Fizetése: {self.fizetes}, Pozíciója: {self.pozicio} " 
    
    def fizetesemeles(self,százalék:int):
        self.fizetes=int(self.fizetes*százalék)
