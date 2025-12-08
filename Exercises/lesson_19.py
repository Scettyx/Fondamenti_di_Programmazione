# esercizio1: data una lista di numeri interi, costruisci a mano un albero N-ario
# (classe NodoNario) con il primo numero come radice e gli altri come figli diretti.
# Scrivi la funzione in modo che restituisca l'altezza dell'albero costruito.
def esercizio1(numeri: list[int]) -> int:
    # TODO: implementa qui usando una classe NodoNario interna o esterna
    # 1) se la lista è vuota, decidi che altezza restituire (ad esempio 0)
    # 2) crea la radice con il primo elemento
    # 3) aggiungi gli altri come figli
    # 4) calcola e restituisci l'altezza dell'albero
    raise NotImplementedError

print(esercizio1([1, 2, 3]))          # caso base
print(esercizio1([]))                 # caso estremo: lista vuota
print(esercizio1([5, 10, -3, 7, 9]))  # caso estremo: più elementi


# esercizio2: data una struttura di NodoNario che rappresenta valori interi,
# scrivi una funzione che, dato un nodo radice, restituisca una tupla
# (valore_massimo, profondita_del_massimo) usando una visita ricorsiva.
def esercizio2(radice) -> tuple[int, int]:
    # TODO:
    # 1) gestisci il caso radice None
    # 2) esplora ricorsivamente i figli
    # 3) confronta i valori e tieni traccia del livello (partendo da 0)
    # 4) restituisci la coppia (valore_massimo, livello)
    raise NotImplementedError

# Per test: dovrai prima costruire a mano un albero NodoNario e passarlo alla funzione
print(esercizio2(None))  # caso base: albero vuoto
print(esercizio2(None))  # caso estremo: ancora None (puoi cambiare dopo i test)
print(esercizio2(None))  # caso estremo: sostituisci poi con un albero reale


# esercizio3: definisci una classe NodoBinario e una funzione diametro_binario(radice)
# che calcola il diametro di un albero binario in termini di numero di nodi del percorso
# più lungo. Usa una strategia simile a quella vista: prima calcola le altezze, poi i
# percorsi, poi il diametro.
def esercizio3(radice) -> int:
    # TODO:
    # 1) definisci (fuori o dentro) la classe NodoBinario con _value, _sx, _dx
    # 2) scrivi una funzione che aggiunge _altezza ricorsivamente
    # 3) scrivi una funzione che aggiunge _percorso a ogni nodo
    # 4) scrivi la funzione diametro che restituisce il valore massimo
    raise NotImplementedError

print(esercizio3(None))  # caso base: albero vuoto
print(esercizio3(None))  # caso estremo1: ancora None (poi userai un albero sbilanciato)
print(esercizio3(None))  # caso estremo2: poi userai un albero più complesso