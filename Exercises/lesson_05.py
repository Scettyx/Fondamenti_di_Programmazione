# esercizio1: scrivi una funzione che riceve una lista di numeri interi
# e ritorna una tupla (media, minimo, massimo).
# Se la lista è vuota, ritorna (0.0, None, None).
def esercizio1(numeri):
    # TODO: implementa qui usando somma, len, min, max e return multiplo
    pass


# Test per esercizio1
print(esercizio1([1, 2, 3, 4]))       # caso base
print(esercizio1([]))                 # caso estremo1: lista vuota
print(esercizio1([-5, 0, 10, 7]))     # caso estremo2: numeri negativi e positivi


# esercizio2: scrivi una funzione che dato un intero N >= 1
# costruisce la stringa "123456789101112..." fino ad avere almeno N cifre
# e ritorna la cifra (come carattere) che sta in posizione N (contando da 1).
def esercizio2(N):
    # TODO: implementa usando un while o for, concatenazione di stringhe e indicizzazione
    pass


# Test per esercizio2
print(esercizio2(1))      # caso base: deve dare '1'
print(esercizio2(10))     # caso estremo1: controlla con carta/penna
print(esercizio2(200))    # caso estremo2: il valore è quello del testo della lezione


# esercizio3: scrivi una funzione che dato un intero N >= 1
# trova la cifra in posizione N nella sequenza "123456789101112..."
# SENZA costruire la stringa completa, ma:
#  - usando una funzione di supporto num_cifre(x) (definiscila tu)
#  - scorrendo i numeri da 1 in poi come nell'approccio "cercasenzastringhe".
def esercizio3(N):
    # TODO:
    # 1) definisci dentro (o fuori) una funzione num_cifre(x)
    # 2) scorri i numeri da 1 in avanti, sottraendo num_cifre(i) finché serve
    # 3) quando trovi il numero giusto, estrai la cifra corrispondente
    pass


# Test per esercizio3
print(esercizio3(1))      # caso base: deve dare '1'
print(esercizio3(10))     # caso estremo1: confronta con esercizio2(10)
print(esercizio3(200))    # caso estremo2: controlla con carta/penna o esercizio2(200)