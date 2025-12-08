from typing import Callable

# Tipo semplificato per un pixel in scala di grigi
Pixel = int
Immagine = list[list[Pixel]]

FiltroXY = Callable[[int, int, Immagine, int, int], Pixel]


# Esercizio 1: filtro XY con "fade" verticale
# Richiesta:
#   Scrivi una funzione che, dato un filtro XY, crei una nuova immagine in cui
#   ogni pixel viene moltiplicato per un fattore compreso tra 0.5 (in basso)
#   e 1.0 (in alto). Il filtro deve usare la formula:
#       fattore = 1.0 - (y / (H - 1)) * 0.5
#   e restituire il nuovo valore arrotondato all'intero più vicino.
def esercizio1(img: Immagine) -> Immagine:
    pass


# Esercizio 2: classe Colore con somma e moltiplicazione
# Richiesta:
#   Definisci una classe Colore con attributi "privati" _R, _G, _B (float)
#   e i metodi:
#       - __init__(self, R, G, B)
#       - __add__(self, other) -> Colore   (somma canale per canale)
#       - __mul__(self, k) -> Colore       (moltiplicazione per costante)
#       - __repr__(self) -> str            (restituisce "Colore(R,G,B)")
#   I metodi devono controllare i tipi di input e sollevare errori sensati.
def esercizio2():
    pass


# Esercizio 3: classe Immagine con metodo di classe
# Richiesta:
#   Definisci una classe Immagine che abbia:
#       - __init__(self, W, H, sfondo) che crea una matrice W x H di sfondo
#       - un metodo di classe @classmethod load_nero(cls, W, H) che
#         costruisce e restituisce una Immagine tutta nera (sfondo = 0)
#       - un metodo area(self) che restituisce W*H
#   NON usare moduli esterni; rappresenta l'immagine come lista di liste di int.
def esercizio3():
    pass


# ==========================
#           TEST
# ==========================

# Test esercizio1
img_test1 = [
    [100, 100, 100],
    [100, 100, 100],
    [100, 100, 100],
]
print(esercizio1(img_test1))       # caso base

img_test2 = [[0]]                  # immagine 1x1 (estremo piccolo)
print(esercizio1(img_test2))       # caso estremo 1

img_test3 = [[200] * 10 for _ in range(20)]  # immagine 10x20 (estremo più grande)
print(esercizio1(img_test3))       # caso estremo 2


# Test esercizio2
print(esercizio2())                # caso base: crea almeno un oggetto Colore

# puoi decidere tu l'output esatto, ma deve mostrare qualcosa di significativo
print(esercizio2())                # caso estremo 1: usa valori diversi
print(esercizio2())                # caso estremo 2: prova un'operazione in più


# Test esercizio3
print(esercizio3())                # caso base: crea una Immagine e restituisci qualcosa da stampare

print(esercizio3())                # caso estremo 1: immagine più grande
print(esercizio3())                # caso estremo 2: usa il metodo area o load_nero in modo diverso