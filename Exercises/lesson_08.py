# ESERCIZIO 1
# Scrivi una funzione esercizio1(L, k) che:
# - prenda in input una lista di numeri L e un intero k
# - usi SOLO una versione NON distruttiva del calcolo dei k massimi (non modificare L)
# - controlli la validità degli argomenti usando raise (lista vuota, k <= 0, k > len(L))
# - usi almeno UNA assert per verificare una condizione interna "ovvia"
# - restituisca una lista con i k valori massimi (in ordine decrescente)
def esercizio1(L, k):
    pass


print(esercizio1([3, 10, 7, 10, 2], 2))      # caso base
print(esercizio1([5], 1))                    # caso estremo 1 (lista di un solo elemento)
print(esercizio1([1, 2, 3, 4, 5], 5))        # caso estremo 2 (k == len(L))


# ESERCIZIO 2
# Scrivi una funzione esercizio2(K, sequenza) che:
# - prenda in input un intero K e un iterabile di numeri (ad es. lista o range) chiamato "sequenza"
# - mantenga in memoria SOLO i K massimi visti finora, senza salvare tutta la sequenza
# - NON usi sorted sulla sequenza intera, ma aggiorni una struttura interna ad ogni elemento
# - mantenga i K massimi in ordine decrescente aggiornandoli con una strategia "lowmem"
# - restituisca la lista dei K massimi in ordine decrescente
# Suggerimento: puoi ispirarti all'idea di update_massimi / k_massimi_lowmem viste a lezione.
def esercizio2(K, sequenza):
    pass


print(esercizio2(3, [5, 1, 9, 2, 10, 4]))    # caso base
print(esercizio2(1, [7, 3, 8, 9]))           # caso estremo 1 (K=1)
print(esercizio2(3, range(10)))              # caso estremo 2 (iterabile range)


# ESERCIZIO 3
# Scrivi una funzione esercizio3(lista_ordinata, x) che:
# - prenda in input una lista di interi ORDINATA in modo DECRESCENTE (lista_ordinata) e un intero x
# - usi la RICERCA BINARIA per trovare la posizione in cui inserire x per mantenere l'ordine decrescente
# - NON usare metodi pronti come index o sort per trovare la posizione; implementa il ciclo while in stile lezione
# - restituisca l'indice in cui andrebbe inserito x
# Dopo aver calcolato l'indice, la funzione NON deve modificare la lista (niente insert dentro esercizio3)
def esercizio3(lista_ordinata, x):
    pass


print(esercizio3([100, 90, 80, 70, 60], 80))   # caso base (valore presente)
print(esercizio3([100, 90, 80, 70, 60], 75))   # caso estremo 1 (valore intermedio)
print(esercizio3([100, 90, 80, 70, 60], 110))  # caso estremo 2 (valore più grande di tutti)# ESERCIZIO 1
# Scrivi una funzione esercizio1(L, k) che:
# - prenda in input una lista di numeri L e un intero k
# - usi SOLO una versione NON distruttiva del calcolo dei k massimi (non modificare L)
# - controlli la validità degli argomenti usando raise (lista vuota, k <= 0, k > len(L))
# - usi almeno UNA assert per verificare una condizione interna "ovvia"
# - restituisca una lista con i k valori massimi (in ordine decrescente)
def esercizio1(L, k):
    pass


print(esercizio1([3, 10, 7, 10, 2], 2))      # caso base
print(esercizio1([5], 1))                    # caso estremo 1 (lista di un solo elemento)
print(esercizio1([1, 2, 3, 4, 5], 5))        # caso estremo 2 (k == len(L))


# ESERCIZIO 2
# Scrivi una funzione esercizio2(K, sequenza) che:
# - prenda in input un intero K e un iterabile di numeri (ad es. lista o range) chiamato "sequenza"
# - mantenga in memoria SOLO i K massimi visti finora, senza salvare tutta la sequenza
# - NON usi sorted sulla sequenza intera, ma aggiorni una struttura interna ad ogni elemento
# - mantenga i K massimi in ordine decrescente aggiornandoli con una strategia "lowmem"
# - restituisca la lista dei K massimi in ordine decrescente
# Suggerimento: puoi ispirarti all'idea di update_massimi / k_massimi_lowmem viste a lezione.
def esercizio2(K, sequenza):
    pass


print(esercizio2(3, [5, 1, 9, 2, 10, 4]))    # caso base
print(esercizio2(1, [7, 3, 8, 9]))           # caso estremo 1 (K=1)
print(esercizio2(3, range(10)))              # caso estremo 2 (iterabile range)


# ESERCIZIO 3
# Scrivi una funzione esercizio3(lista_ordinata, x) che:
# - prenda in input una lista di interi ORDINATA in modo DECRESCENTE (lista_ordinata) e un intero x
# - usi la RICERCA BINARIA per trovare la posizione in cui inserire x per mantenere l'ordine decrescente
# - NON usare metodi pronti come index o sort per trovare la posizione; implementa il ciclo while in stile lezione
# - restituisca l'indice in cui andrebbe inserito x
# Dopo aver calcolato l'indice, la funzione NON deve modificare la lista (niente insert dentro esercizio3)
def esercizio3(lista_ordinata, x):
    pass


print(esercizio3([100, 90, 80, 70, 60], 80))   # caso base (valore presente)
print(esercizio3([100, 90, 80, 70, 60], 75))   # caso estremo 1 (valore intermedio)
print(esercizio3([100, 90, 80, 70, 60], 110))  # caso estremo 2 (valore più grande di tutti)