# esercizio1:
# Scrivi una funzione che prende un numero intero e:
# - usa operatori di assegnamento potenziati (+=, -=, *=, ecc.)
# - restituisce una stringa che descrive passo passo come è cambiato il valore.
# Usa almeno 3 operatori diversi e integra un if/elif/else sul valore finale.


def esercizio1(n):
    pass


print(esercizio1(10))      # caso base: numero positivo medio
print(esercizio1(0))       # caso estremo1: zero
print(esercizio1(-5))      # caso estremo2: numero negativo


# esercizio2:
# Scrivi una funzione che prende una frase (stringa),
# la spezza in parole con split(), e poi:
# - usa assegnamento multiplo e/o match/case per riconoscere alcune strutture,
# - restituisce una descrizione testuale della frase (es: "soggetto-verbo-oggetto",
#   "frase sconosciuta", ecc.).
# Usa almeno un contenitore (lista/tupla/set/dict) nel ragionamento.


def esercizio2(frase):
    pass


print(esercizio2("Paperino ama Paperina"))    # caso base: frase ben formata
print(esercizio2("Topolino corre"))           # caso estremo1: frase più corta
print(esercizio2(""))                         # caso estremo2: stringa vuota


# esercizio3:
# Scrivi una funzione che simula un piccolo menu testuale:
# - prende un numero intero che rappresenta una scelta dell'utente,
# - usa cicli (for o while) e, se ti è comodo, range,
# - usa anche un dizionario o una lista per mappare scelte -> azioni,
# - restituisce una stringa che descrive cosa fa il programma
#   (es: "mostro la lista", "esci", "scelta non valida").
# Gestisci almeno un caso con break/continue in un ciclo.


def esercizio3(scelta):
    pass


print(esercizio3(1))       # caso base: scelta valida
print(esercizio3(99))      # caso estremo1: scelta non valida
print(esercizio3(-1))      # caso estremo2: scelta particolare (es: uscita forzata)