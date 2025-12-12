# esercizio1: dato un numero intero n,
# restituisci una stringa che descrive se n è negativo, zero o positivo,
# e se è pari o dispari (usa if/elif/else e operatori di assegnamento potenziato dove utile).
def esercizio1(n: int) -> str:
    if n == 0:
        return "zero"
    segno = "positivo" if n > 0 else "negativo"
    tipo = "pari" if n % 2 == 0 else "dispari"
    return f"{segno} {tipo}"

print(esercizio1(0))       # caso_base
print(esercizio1(7))       # caso_estremo1
print(esercizio1(-8))      # caso_estremo2)


# esercizio2: data una frase (stringa),
# usa split e assegnamenti multipli per estrarre nome e cognome dal formato "Nome Cognome",
# e restituisci un dizionario con chiavi 'nome', 'cognome', 'iniziale',
# dove 'iniziale' contiene la prima lettera del cognome.
def esercizio2(frase: str) -> dict:
    nome, cognome = frase.split()
    return {"nome": nome, "cognome": cognome, "iniziale": cognome[0]}

print(esercizio2("Mario Rossi"))        # caso_base
print(esercizio2("Anna Bianchi"))       # caso_estremo1
print(esercizio2("Luigi Verdi"))        # caso_estremo2


# esercizio3: data una lista di numeri interi,
# usa un ciclo for e/o while, insieme a range, per costruire un dizionario
# che mappa ogni numero alla stringa "pari" o "dispari",
# ma si deve fermare (break) quando incontra il numero 0.
def esercizio3(lista_numeri: list[int]) -> dict:
    d = {}
    for n in lista_numeri:
        if n == 0:
            break
        d[n] = "pari" if n % 2 == 0 else "dispari"
    return d

print(esercizio3([1, 2, 3, 0, 4, 5]))        # caso_base
print(esercizio3([0, 1, 2, 3]))              # caso_estremo1
print(esercizio3([7, 9, 11]))                # caso_estremo2