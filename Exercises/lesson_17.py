# esercizio1:
# Scrivi una funzione ricorsiva memoizzata fibonacci_mio(N) che:
# - usa un dizionario di cache passato come parametro (con default sicuro None)
# - calcola l'N-esimo numero di Fibonacci in modo efficiente (simile a fib_memo della lezione)
# - deve gestire correttamente N = 0 e N = 1 (casi base) e N grandi (es. 30, 40)
def esercizio1(N, cache=None):
    pass


print(esercizio1(0))    # caso base: Fibonacci di 0
print(esercizio1(1))    # caso base: Fibonacci di 1
print(esercizio1(10))   # caso estremo: controlla che sia coerente (es. 55)


# esercizio2:
# Scrivi una classe NodoNarioMio e un metodo altezza_mia(self) che:
# - rappresenta un albero N-ario con attributi: _value (valore) e _sons (lista di figli)
# - NON usa una lista di default mutabile nel costruttore (__init__), ma il pattern con None
# - altezza_mia() deve calcolare l'altezza del nodo come nella lezione (1 + max altezze figli, default=1)
# Suggerimento: puoi aggiungere un costruttore e poi testare altezza_mia su un piccolo albero.
class NodoNarioMio:
    pass


# Costruisci qui sotto un piccolo albero per test:
# ad esempio un nodo radice con due figli, uno dei quali ha a sua volta un figlio.
def esercizio2():
    pass


print(esercizio2())      # caso base: albero piccolo
print(esercizio2())      # ripeti per verificare che NON ci siano effetti collaterali
print(esercizio2())      # prova a variare l'albero (es. cambia i valori dentro la funzione)


# esercizio3:
# Scrivi una funzione merge_sort_mio(L) che:
# - ordina una lista di numeri interi usando la strategia MergeSort vista a lezione
# - usa una funzione interna merge_mio(L1, L2) per fondere due liste ordinate
# - come caso base deve trattare liste di lunghezza < 2
# - NON usare sort() o sorted(), ma solo ricorsione e merge
def esercizio3(L):
    pass


print(esercizio3([]))                 # caso base: lista vuota
print(esercizio3([1]))                # caso base: lista con un solo elemento
print(esercizio3([5, 2, 9, 1, 0]))    # caso estremo: lista non ordinata