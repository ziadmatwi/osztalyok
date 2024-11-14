from etel import Etel
from Alkalmazott import Alkalmazott
import fuggvenyek
import datetime
""" 2. Létrehozzuk a konkrét példányt a tervrajz alapján
"""

etel_lista=[]
etel_lista.append(Etel("Húsleves",1234))
etel_lista.append(Etel("Krumplis tészta",2345))
etel_lista.append(Etel("Rántotthús",2310))
etel_lista.append(Etel("Palacsinta",1310))


"""Írj egy metódust, amely megkapja a listát és kiírja az ételek neveit és árait"""
'fuggvenyek.etlap(etel_lista)'
"""a=fuggvenyek.legdragabb(etel_lista)
print(etel_lista[a].nev)

b=fuggvenyek.atlagar(etel_lista)
print(b)

print(etel_lista[0]) """

"""Hozz létre egy Alkalmaztott osztályt, amelyikben az alábbi infókat tudod tárolni 
egy cég dolgozóiról:
név
Szül_datum
fizetes
pozíció
kor

Készíts kor metódust, ami megmondja az adott ember korát.
Hozz létre legalább 5 embert, tedd bele őket listába
-mennyi az össz fizetés?
-Hány éves a legidősebb ember?
-Hány ember van "beosztott" pozícióban?
-kinek a legalacsonyabb a fizetése?

++ az osztálynak legyen egy fizetésemelés metódusa, amelyik a fizetést
megemeli a paraméterében megadott százelék értékkel.
A legkisebb fizetésű ember fizetését emeld meg.
"""

alkalmazott_lista=[]
alkalmazott_lista.append(Alkalmazott("Matwi Ziad",2002,250000,"Gyakornok"))
alkalmazott_lista.append(Alkalmazott("Rátkai József",1990,350000,"Junior Developer"))
alkalmazott_lista.append(Alkalmazott("Pénzes Adonisz",1995,600000,"Medior"))
alkalmazott_lista.append(Alkalmazott("Kanalas Vinettu",1978,950000,"Senior Manager"))
alkalmazott_lista.append(Alkalmazott("Monitor Márk",2010,1300000,"CEO"))

print(fuggvenyek.osszfizetes(alkalmazott_lista))
print(fuggvenyek.legidosebb(alkalmazott_lista))
print(fuggvenyek.gyakornokszam(alkalmazott_lista))
print(fuggvenyek.legalacsonyabb_fizetes(alkalmazott_lista))

alkalmazott_lista[fuggvenyek.legalacsonyabb_fizetes(alkalmazott_lista)].fizetesemeles(1.15) 
print(alkalmazott_lista[fuggvenyek.legalacsonyabb_fizetes(alkalmazott_lista)])







