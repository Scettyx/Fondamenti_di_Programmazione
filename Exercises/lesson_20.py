# esercizio1:
# Scrivi una funzione esercizio1(S, K) che, dati:
# - S: un insieme di interi
# - K: un intero >= 0
# RITORNA l'insieme di tutte le tuple di lunghezza K formate con elementi presi da S
# SENZA ripetere lo stesso elemento più di una volta nella stessa tupla.
# Usa una strategia RICORSIVA.
def esercizio1(S, K):
    pass


print(esercizio1({1, 2, 3}, 0))          # caso_base: K = 0
print(esercizio1(set(), 3))              # caso_estremo1: insieme vuoto, K > 0
print(esercizio1({1, 2, 3, 4}, 2))       # caso_estremo2: combinazioni di 2 su 4 elementi


# esercizio2:
# Scrivi una funzione esercizio2(lista) che, data una LISTA di interi,
# costruisce un albero di gioco in cui:
# - ogni mossa valida è la somma di due elementi consecutivi con lo stesso resto modulo 2
# - ad ogni mossa viene CREATO un nuovo nodo con la lista modificata
# La funzione deve:
# - costruire implicitamente l'albero partendo dalla lista iniziale
# - RESTITUIRE una TUPLA (min_prof, max_prof) dove:
#   min_prof = numero minimo di mosse per arrivare a una lista non più riducibile
#   max_prof = numero massimo di mosse per arrivare a una lista non più riducibile
# Usa una classe interna (o una classe a parte) per rappresentare i nodi.
def esercizio2(lista):
    pass


print(esercizio2([1, 13, 2, 7, 9, 2]))   # caso_base: esempio della lezione
print(esercizio2([1, 2, 3, 4, 5]))       # caso_estremo1: niente mosse possibili
print(esercizio2([2, 2, 2, 2]))          # caso_estremo2: molte mosse possibili


# esercizio3:
# Scrivi una funzione esercizio3(N, LM) che:
# - N è un intero >= 0 (resto da dare)
# - LM è una lista di interi POSITIVI, che contiene SEMPRE 1
# La funzione deve:
# - generare TUTTI i modi diversi di dare il resto N usando le monete in LM (monete illimitate)
# - RESTITUIRE una lista di liste, dove ogni lista interna è una combinazione di monete che somma N
# Vincoli:
# - usa una CLASSE per rappresentare una configurazione (N corrente, monete disponibili)
# - usa un METODO RICORSIVO per generare le soluzioni
# - NON includere "mosse" che non sottraggono nulla dal resto nella soluzione finale
def esercizio3(N, LM):
    pass


print(esercizio3(0, [1]))                # caso_base: resto 0, moneta minima
print(esercizio3(3, [2, 1]))             # caso_estremo1: devo usare per forza almeno una moneta da 1
print(esercizio3(5, [5, 2, 1]))          # caso_estremo2: più combinazioni possibili