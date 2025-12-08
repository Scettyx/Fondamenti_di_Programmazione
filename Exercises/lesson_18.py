# esercizio1: Implementa una funzione merge_sort_lista(L)
# che ordina una lista di numeri usando l'algoritmo MergeSort.
# NON puoi usare list.sort() o sorted().
# Suggerimento: definisci eventualmente una funzione interna merge(L1, L2)
# e usa la logica "caso base + caso ricorsivo" vista a lezione.
def esercizio1(L):
    pass


print(esercizio1([3, 1, 2, 5]))          # caso base: pochi elementi disordinati
print(esercizio1([]))                     # caso estremo1: lista vuota
print(esercizio1([7, 7, 7, 7, 7, 7]))     # caso estremo2: tutti elementi uguali


# esercizio2: Definisci una classe NodoBinario con attributi _value, _sx, _dx
# e un metodo altezza(self) che calcola l'altezza del sottoalbero radicato nel nodo.
# Poi fai in modo che esercizio2 costruisca un piccolo albero binario di test
# (ad es. con 3-5 nodi) e ritorni la sua altezza.
def esercizio2():
    pass


print(esercizio2())   # caso base: albero piccolino fisso dentro la funzione
print(esercizio2())   # caso estremo1: verifica che il risultato sia stabile a chiamate ripetute
print(esercizio2())   # caso estremo2: puoi modificare la funzione per costruire un albero più profondo


# esercizio3: Definisci una classe NodoNario con attributi _value e _sons (lista di figli),
# attento a NON usare una lista mutabile come valore di default.
# Implementa un metodo massimo(self) che ritorna il massimo valore nell'albero,
# e un metodo altezza(self) che ritorna l'altezza del nodo.
# La funzione esercizio3 deve creare un piccolo albero N-ario di test
# e ritornare una tupla (altezza, massimo).
def esercizio3():
    pass


print(esercizio3())   # caso base: albero N-ario di pochi nodi
print(esercizio3())   # caso estremo1: controlla che non ci siano effetti collaterali tra chiamate
print(esercizio3())   # caso estremo2: modifica l'albero per renderlo più profondo o con valori diversi