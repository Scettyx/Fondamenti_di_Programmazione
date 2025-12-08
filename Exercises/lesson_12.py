# esercizio1: scrivi una funzione che, dato il nome di una cartella,
# stampa tutti i file (non le directory) che si trovano direttamente al suo interno,
# mostrando per ciascuno: nome del file e dimensione in byte (usando os.path e os.stat).

import os

def esercizio1(cartella: str) -> None:
    pass

print(esercizio1("."))          # caso base: cartella corrente
print(esercizio1(".."))         # caso estremo1: cartella padre
print(esercizio1("cartella_inesistente"))  # caso estremo2: cartella che non esiste


# esercizio2: scrivi una funzione che crea un'immagine (Picture) di larghezza e altezza date,
# con sfondo nero, e disegna un rettangolo vuoto rosso centrato,
# usando una tua funzione draw_pixel e, se vuoi, draw_line.

Pixel = tuple[int, int, int]
Row = list[Pixel]
Picture = list[Row]

def esercizio2(larghezza: int, altezza: int) -> Picture:
    pass

print(esercizio2(10, 6))        # caso base
print(esercizio2(3, 3))         # caso estremo1: immagine piccola
print(esercizio2(0, 0))         # caso estremo2: immagine vuota (gestire bene)


# esercizio3: scrivi una funzione che, dato un elenco di cifre tutte diverse (lunghezza 6),
# restituisce una lista con tutte le permutazioni possibili (come liste di interi),
# implementando tu stesso l’algoritmo (NON usare itertools.permutations).

def esercizio3(cifre: list[int]) -> list[list[int]]:
    pass

print(esercizio3([1, 2, 3, 4, 5, 6]))  # caso base: 6 cifre consecutive
print(esercizio3([9, 0, 2, 7, 4, 8]))  # caso estremo1: include 0 e cifre sparse
print(esercizio3([1, 1, 2, 3, 4, 5]))  # caso estremo2: cifre non tutte diverse, da gestire