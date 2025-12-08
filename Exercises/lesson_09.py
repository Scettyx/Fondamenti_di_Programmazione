# esercizio1: data una lista di liste (righe) di uguale lunghezza,
# usa zip per trasporre la "tabella" (scambiare righe e colonne)
# e restituisci la nuova lista di liste.
def esercizio1(tabella: list[list[int]]) -> list[list[int]]:
    pass


print(esercizio1([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]))          # caso base
print(esercizio1([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8]]))            # caso estremo1 (più righe che colonne)
print(esercizio1([[10], [20], [30]]))  # caso estremo2 (una sola colonna)


# esercizio2: data una lista di interi, restituisci una nuova lista che:
# - contiene "positivo" se l’elemento è > 0
# - "negativo" se l’elemento è < 0
# - "zero" se è 0
# Usa una espressione condizionale (if ... else) dentro una list comprehension.
def esercizio2(valori: list[int]) -> list[str]:
    pass


print(esercizio2([1, -2, 0, 5]))       # caso base
print(esercizio2([]))                  # caso estremo1 (lista vuota)
print(esercizio2([0, 0, 0]))           # caso estremo2 (solo zeri)


# esercizio3: data una lista di dizionari studenti con chiave "nome" e "voto",
# implementa una funzione che:
# - ha una inner function come criterio per max (usa il voto)
# - restituisce lo studente con il voto massimo.
# Aggiungi annotazioni di tipo sensate (lista, dict, int, str, ecc.).
def esercizio3(studenti: list[dict[str, int | str]]) -> dict[str, int | str]:
    pass


print(esercizio3([{"nome": "Anna", "voto": 28},
                  {"nome": "Luca", "voto": 30},
                  {"nome": "Marta", "voto": 25}]))  # caso base

print(esercizio3([{"nome": "SoloUno", "voto": 18}]))  # caso estremo1 (un solo elemento)

print(esercizio3([{"nome": "A", "voto": 20},
                  {"nome": "B", "voto": 20},
                  {"nome": "C", "voto": 19}]))        # caso estremo2 (più max uguali)