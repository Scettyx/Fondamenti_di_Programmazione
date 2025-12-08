from typing import Callable
from copy import deepcopy

Colore = tuple[int, int, int]
Immagine = list[list[Colore]]
Filtro = Callable[[Colore], Colore]


def bound(x: int | float, minimo: int = 0, massimo: int = 255) -> int:
    """Arrotonda x e lo limita nell'intervallo [minimo, massimo]."""
    intero = round(x)
    return min(max(intero, minimo), massimo)


# esercizio1: scrivi una funzione che applica un filtro di luminosità (fattore k)
# a TUTTA l'immagine, SENZA modificare l'immagine originale.
# Usa le annotazioni di tipo viste a lezione (Colore, Immagine, Filtro) e la funzione bound.
# Il filtro deve moltiplicare ogni canale R,G,B per k e poi usare bound per tenerlo in [0..255].
def esercizio1(img: Immagine, k: float) -> Immagine:
    # TODO: da implementare
    pass


print(esercizio1([[(100, 100, 100)]], 1.5))        # caso base
print(esercizio1([[(0, 0, 0)]], 10.0))             # caso estremo1 (immagine molto scura)
print(esercizio1([[(255, 255, 255)]], 0.0))        # caso estremo2 (immagine tutta bianca)


# esercizio2: scrivi una funzione che CREA una copia profonda dell'immagine
# usando SOLO list comprehension (niente deepcopy).
# La funzione deve restituire una nuova immagine tale che modificare la copia
# NON modifichi l'originale.
def esercizio2(img: Immagine) -> Immagine:
    # TODO: da implementare
    pass


img_test2: Immagine = [[(1, 2, 3), (4, 5, 6)]]
copia2 = esercizio2(img_test2)                     # caso base
print(img_test2, copia2)
img_test2_estremo1: Immagine = []                  # caso estremo1 (immagine vuota)
print(esercizio2(img_test2_estremo1))
img_test2_estremo2: Immagine = [[(0, 0, 0)] * 5]   # caso estremo2 (una sola riga larga)
print(esercizio2(img_test2_estremo2))


# esercizio3: definisci un tipo alias FiltroXY che rappresenta una funzione
# che prende (x, y, img, larghezza, altezza) e restituisce un Colore.
# Poi implementa una funzione che applica un filtroXY all'immagine
# e un filtroXY specifico che crea un bordo nero di spessore 'spessore'
# intorno all'immagine (tutti i pixel nel bordo diventano neri).
def esercizio3(img: Immagine, spessore: int) -> Immagine:
    # TODO: da implementare
    pass


img_base3: Immagine = [[(255, 255, 255)] * 4 for _ in range(4)]  # 4x4 bianca
print(esercizio3(img_base3, 1))                # caso base: bordo di 1 pixel
print(esercizio3(img_base3, 0))                # caso estremo1: bordo di spessore 0 (nessun bordo)
print(esercizio3(img_base3, 2))                # caso estremo2: bordo spesso 2 (quasi tutta bordo)