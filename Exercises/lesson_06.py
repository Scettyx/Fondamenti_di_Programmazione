# esercizio1: scrivi una funzione che prende una lista di interi
# e RITORNA una NUOVA lista dove tutti i numeri negativi sono stati
# sostituiti con 0, senza modificare la lista originale (nessun effetto collaterale).
def esercizio1(lista_numeri):
    return [0 if n < 0 else n for n in lista_numeri]

print(esercizio1([1, -2, 3, -4, 0]))
print(esercizio1([]))
print(esercizio1([-1, -2, -3]))


# esercizio2: scrivi una funzione che prende una sequenza di parole (lista o tupla)
# e RITORNA una nuova lista di parole ordinate:
# 1) per lunghezza crescente
# 2) a parità di lunghezza, in ordine alfabetico ignorando maiuscole/minuscole.
def esercizio2(parole):
    return sorted(parole, key = lambda p: (len(p), p.lower()))

print(esercizio2(["Python", "c", "Java", "go", "Rust"]))
print(esercizio2([]))
print(esercizio2(["AA", "a", "Bb", "bB", "bb"]))


# esercizio3: scrivi una funzione che chiede all’utente da tastiera
# un numero tra 1 e 100 compresi, accettando anche input float (es. "3.5"),
# ripetendo la richiesta finché l’utente non inserisce un valore valido,
# e RITORNA l’intero corrispondente arrotondato per difetto (int(float(...))).
def esercizio3():
    while True:
        try:
            inp = input("Inserisci un numero tra 1 e 100 compresi: ")
            numero = float(inp)
            if 1 <= numero <= 100:
                return int(numero)
            else:
                print("Il numero deve essere compreso tra 1 e 100, riprova...")
        except ValueError:
            print("Input non valido, inserisci un NUMERO")

print(esercizio3())