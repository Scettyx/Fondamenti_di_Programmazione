# esercizio1: scrivi una funzione che, dato un intero n e una funzione unaria f (es. quadrato, cubo),
#             applichi f a TUTTI i numeri da 1 a n usando map e restituisca la lista dei risultati.
def esercizio1(n, f):
    return list(map(f, range(1, n + 1)))

print(esercizio1(5, lambda x: x))          # caso base
print(esercizio1(0, lambda x: x * 2))      # caso estremo 1
print(esercizio1(5, lambda x: x ** 2))     # caso estremo 2


# esercizio2: scrivi una funzione che, data una lista di interi, restituisca True
#             se TUTTI i numeri sono pari e POSITIVI, usando filter/all oppure map/all.
def esercizio2(lista):
    return all(map(lambda n: n > 0 and n % 2 == 0, lista))

print(esercizio2([2, 4, 6]))               # caso base
print(esercizio2([]))                      # caso estremo 1
print(esercizio2([2, -4, 6, 7]))           # caso estremo 2


# esercizio3: scrivi una funzione che legga da un file di testo (filename) TUTTE le righe,
#             tenga solo quelle NON vuote usando filter, e restituisca il numero di righe non vuote.
#             Usa with per aprire il file e qualsiasi modalità di lettura (read/readlines/for riga in file).
def esercizio3(filename):
    with open(filename, mode="r", encoding="utf8") as f:
        testo = f.readlines()
        buone = list(filter(lambda riga: riga.strip() != "", testo))
        return len(buone)

print(esercizio3("righe_esempio.txt"))     # caso base (crea tu il file prima di testare)
print(esercizio3("vuoto.txt"))             # caso estremo 1 (file vuoto)
print(esercizio3("righe_miste.txt"))       # caso estremo 2 (righe vuote + non vuote))