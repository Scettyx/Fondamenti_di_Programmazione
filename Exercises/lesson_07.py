# esercizio1: scrivi una funzione che, data una lista di stringhe,
# restituisca una NUOVA lista ordinata per lunghezza crescente
# e, a parità di lunghezza, per ordine alfabetico case-insensitive.
# Usa una funzione anonima (lambda) come parametro key di sorted.

def esercizio1(lista_stringhe):
    pass


print(esercizio1(["cane", "Gatto", "a", "Casa", "AA"]))
print(esercizio1([]))
print(esercizio1(["x", "X", "xx", "XX", "xxx", "XXX"]))



# esercizio2: scrivi una funzione che, data una lista di interi,
# restituisca un DIZIONARIO in cui:
# - le chiavi sono SOLO i numeri pari della lista
# - i valori sono il quadrato del numero
# Usa una dict comprehension con condizione if.

def esercizio2(lista_interi):
    pass


print(esercizio2([1, 2, 3, 4, 5, 6]))
print(esercizio2([]))
print(esercizio2([0, -2, -3, 10, 11]))



# esercizio3: scrivi una funzione che, data una lista L di numeri
# e un intero k, restituisca la lista dei k massimi SENZA modificare L.
# - Controlla con assert che L non sia vuota e che 0 < k <= len(L).
# - Implementa una funzione interna estrai_massimo(lista) che rimuove
#   e restituisce il massimo da quella lista.
# - Usa una list comprehension per chiamare estrai_massimo k volte.

def esercizio3(L, k):
    pass


print(esercizio3([1, 5, 2, 89, 2, 23], 2))
print(esercizio3([10, 9, 8, 7], 4))
print(esercizio3([3], 1))