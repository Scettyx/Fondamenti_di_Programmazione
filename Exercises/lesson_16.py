from typing import Sequence
import os

# esercizio1:
# Scrivi una funzione ricorsiva `fattoriale_ric(N: int) -> int` che:
# - per N == 1 ritorna 1 (caso base)
# - per N > 1 ritorna il prodotto di N per il fattoriale di N-1
# Usa SOLO una chiamata ricorsiva per volta (niente cicli for/while).
def esercizio1(N: int) -> int:
    # TODO: implementa la versione ricorsiva del fattoriale
    pass


print(esercizio1(1))   # caso base
print(esercizio1(5))   # caso "normale"
print(esercizio1(10))  # caso più grande


# esercizio2:
# Scrivi una funzione ricorsiva `palindroma_esercizio(seq: Sequence) -> bool` che:
# - ritorna True se `seq` è palindroma (uguale letta da sinistra e da destra)
# - usa il pattern: caso base (len(seq) < 2), controllo primi/ultimi, riduzione su sottosequenza interna
# Non usare cicli; puoi usare slicing oppure una funzione di supporto con indici.
def esercizio2(seq: Sequence) -> bool:
    # TODO: implementa il controllo palindromo in modo ricorsivo
    pass


print(esercizio2("aa"))                     # caso base minimo
print(esercizio2("amoRoma"))                # palindroma
print(esercizio2([1, 2, 3, 4, 3, 2, 1]))    # palindroma lista


# esercizio3:
# Scrivi una funzione ricorsiva `conta_py(directory: str) -> int` che:
# - conta quanti file che terminano con ".py" ci sono nella directory e nelle sottodirectory
# - usa os.listdir, os.path.isdir e os.path.join
# - per ogni sottodirectory fa una chiamata ricorsiva e aggiunge il risultato
# Non usare global; ritorna sempre il conteggio totale come intero.
def esercizio3(directory: str) -> int:
    # TODO: implementa il conteggio ricorsivo dei file .py
    pass


print(esercizio3("."))           # caso: directory corrente
print(esercizio3(".."))          # un livello sopra
print(esercizio3("/tmp"))        # directory che può avere molte sottodirectory