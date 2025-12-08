# esercizio1:
# Scrivi una funzione che riceve una lista di interi e
# restituisce una nuova lista che contiene solo i numeri
# strettamente positivi, mantenendo l'ordine originale.
def esercizio1(lista_interi):
    pass


print(esercizio1([1, -2, 0, 5]))           # caso_base
print(esercizio1([]))                      # caso_estremo1 (lista vuota)
print(esercizio1([-1, -2, -3]))            # caso_estremo2 (nessun positivo)


# esercizio2:
# Scrivi una funzione che riceve una stringa di testo e
# restituisce un dizionario che mappa ogni parola (in minuscolo,
# senza punteggiatura semplice ,.!?;:) al numero di occorrenze.
def esercizio2(testo):
    pass


print(esercizio2("Ciao, ciao! come va?"))  # caso_base
print(esercizio2(""))                      # caso_estremo1 (stringa vuota)
print(esercizio2("Python, python PYTHON")) # caso_estremo2 (maius/minus)


# esercizio3:
# Scrivi una funzione che riceve un elenco di studenti sotto forma di
# lista di dizionari, ad esempio:
# [{"nome": "Ana", "voti": [30, 28]}, {"nome": "Luca", "voti": [18, 25, 30]}]
# e restituisce un DIZIONARIO che mappa il nome alla media dei voti.
# Se la lista dei voti è vuota, la media deve essere 0.
def esercizio3(lista_studenti):
    pass


print(esercizio3([{"nome": "Ana", "voti": [30, 28]}]))  # caso_base
print(esercizio3([]))                                   # caso_estremo1 (nessuno studente)
print(esercizio3([{"nome": "Luca", "voti": []}]))       # caso_estremo2 (nessun voto)