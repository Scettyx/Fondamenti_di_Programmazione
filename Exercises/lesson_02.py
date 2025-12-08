# esercizio1: data una stringa 'testo', restituisci una nuova stringa
# che contiene SOLO il primo e l'ultimo carattere di 'testo' concatenati.
# Se la stringa è vuota o ha un solo carattere, restituisci 'testo' così com'è.
def esercizio1(testo):
    # TODO: usa len(testo) e indicizzazione/slicing per costruire il risultato
    # ricordati che le stringhe sono immutabili: crea una NUOVA stringa
    pass


# test esercizio1
print(esercizio1("Python"))     # caso base
print(esercizio1(""))           # caso estremo: stringa vuota
print(esercizio1("A"))          # caso estremo: un solo carattere


# esercizio2: data una stringa 'testo', restituisci una nuova stringa
# che contiene i caratteri in posizione PARI (0,2,4,...) seguiti
# dai caratteri in posizione DISPARI (1,3,5,...).
# Usa slicing con step e/o concatenazione.
def esercizio2(testo):
    # TODO: usa testo[::2] e testo[1::2] (o logica equivalente) e concatenali
    pass


# test esercizio2
print(esercizio2("abcdef"))     # caso base
print(esercizio2("a"))          # caso estremo: un solo carattere
print(esercizio2(""))           # caso estremo: stringa vuota


# esercizio3: leggi da input un numero intero (come stringa),
# converti in int e restituisci:
# - "PARI" se il numero è pari
# - "DISPARI" se il numero è dispari
# Se la conversione fallisce (ValueError), restituisci la stringa "ERRORE".
def esercizio3():
    # TODO: usa input(), int(), try/except ValueError e operatori %
    pass


# test esercizio3
print(esercizio3())  # caso base: inserisci un intero normale (es. 10)
print(esercizio3())  # caso estremo: inserisci 0
print(esercizio3())  # caso estremo: inserisci qualcosa NON convertibile (es. "ciao")