def etlap(lista):
    for i in range (0,len(lista),1):
        print(f"** {lista[i].nev} {lista[i].ar} **")

"""Írj metódust amely kiírja az ételek átlagárát"""
def atlagar(lista):
    osszeg:int=0
    for i in range(0,len(lista),1):
        osszeg+=lista[i].ar

    osszeg=osszeg/len(lista)
    return osszeg


"""Írj metódust, ami megmondja a legdrágább étel nevét"""
    
def legdragabb(lista):
    max_index=0
    for i in range (0,len(lista)):
        if lista[i].ar > lista[max_index].ar:
            max_index=i
    return max_index

def osszfizetes(lista):
    osszfizetes:int=0
    for i in range(0,len(lista)):
        osszfizetes += lista[i].fizetes
    return osszfizetes

def legidosebb(lista):
    max_index=0
    for i in range (0,len(lista)):
        if lista[i].kor > lista[max_index].kor:
            max_index=i
    return max_index

def gyakornokszam(lista):
    gyakornokszam:int=0
    for i in range(0,len(lista)):
        if lista[i].pozicio == "Gyakornok":
            gyakornokszam+=1
    return gyakornokszam

def legalacsonyabb_fizetes(lista):
    min_index=0
    for i in range (0,len(lista)):
        if lista[i].fizetes < lista[min_index].fizetes:
            min_index=i
    return min_index


        