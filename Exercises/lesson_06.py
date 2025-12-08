# esercizio1
# Scrivi una funzione esercizio1() che:
# - chiede all'utente (con input) un intero tra 1 e 100
# - continua a richiederlo finché l'utente non inserisce un valore valido
#   (usa try/except per gestire errori di conversione)
# - restituisce l'intero valido letto
def esercizio1():
    pass

print("esercizio1 - caso_base:", esercizio1())        # prova normale
print("esercizio1 - caso_estremo1:", esercizio1())    # prova con input sbagliati prima di uno valido
print("esercizio1 - caso_estremo2:", esercizio1())    # prova con 1 o 100


# esercizio2
# Scrivi una funzione esercizio2(parole) che:
# - riceve una lista di stringhe 'parole'
# - restituisce una NUOVA lista ordinata secondo questi criteri:
#   1) per lunghezza crescente
#   2) a parità di lunghezza, ordine alfabetico ignorando maiuscole/minuscole
#   3) a parità di tutto il resto, mantieni l'ordine relativo originale (stabilità)
# Suggerimento: usa sorted con parametro key e magari enumerate.
def esercizio2(parole):
    pass

print("esercizio2 - caso_base:", esercizio2(["uno", "due", "tre", "quattro", "cinque", "sei", "sette"]))
print("esercizio2 - caso_estremo1:", esercizio2([]))
print("esercizio2 - caso_estremo2:", esercizio2(["Aa", "aA", "aa", "AA"]))


# esercizio3
# Scrivi una funzione esercizio3(*valori, minimo=None, massimo=None) che:
# - accetta un numero variabile di argomenti numerici (packing)
# - se minimo e/o massimo sono None, NON applica quel limite
# - restituisce una NUOVA lista con solo i valori compresi tra minimo e massimo (estremi inclusi)
#   es. esercizio3(1, 5, 10, minimo=3, massimo=8) -> [5]
# - gestisci il caso senza valori (ritorna lista vuota)
def esercizio3(*valori, minimo=None, massimo=None):
    pass

print("esercizio3 - caso_base:", esercizio3(1, 5, 10, minimo=3, massimo=8))
print("esercizio3 - caso_estremo1:", esercizio3())
print("esercizio3 - caso_estremo2:", esercizio3(-10, 0, 10, minimo=None, massimo=0))