import json
import yaml
import requests
from typing import Dict, List, Tuple


# ESERCIZIO 1
# Scrivi una funzione che, dato il nome di un file di testo,
# legge il contenuto, lo porta in minuscolo, sostituisce tutti i caratteri NON alfabetici con spazi
# usando str.maketrans/str.translate, e restituisce la lista di parole.
# NON usare split direttamente sul file: prima leggi tutto il testo, poi pulisci, poi fai split().
def esercizio1(nome_file: str, encoding: str = "utf-8") -> List[str]:
    # TODO: implementa i passi descritti nel commento sopra
    pass


print(esercizio1("testo_piccolo.txt")[:10])          # caso base: file di poche righe
print(len(esercizio1("alice.txt")))                  # caso estremo 1: file lungo (libro)
print(esercizio1("vuoto.txt"))                       # caso estremo 2: file vuoto -> lista vuota attesa


# ESERCIZIO 2
# Scrivi una funzione che, dato il nome di un file JSON contenente una lista di contatti
# (ogni contatto è un dizionario con chiavi "nome" e "telefono"),
# carica il file, costruisce un dizionario nome -> numero_di_telefonate (conteggio di quante volte
# lo stesso "nome" appare nella lista), e restituisce questo dizionario.
# Usa json.load per leggere il file.
def esercizio2(nome_file_json: str) -> Dict[str, int]:
    # TODO: leggi il file JSON, scorri i contatti e conta le occorrenze di ciascun "nome"
    pass


print(esercizio2("agenda_piccola.json"))             # caso base: pochi contatti
print(esercizio2("agenda_grande.json"))              # caso estremo 1: molti contatti ripetuti
print(esercizio2("agenda_vuota.json"))               # caso estremo 2: lista vuota -> dict vuoto atteso


# ESERCIZIO 3
# Scrivi una funzione che, data una URL che restituisce un JSON con una chiave "items"
# contenente una lista di oggetti, scarica il JSON usando requests.get(url).json(),
# calcola quante volte compare ciascun valore della chiave "type" all'interno di ogni item,
# e restituisce un dizionario type -> conteggio.
# Se un item non contiene la chiave "type", ignoralo.
def esercizio3(url: str) -> Dict[str, int]:
    # TODO: fai la richiesta HTTP con requests, estrai items, poi conta i valori di "type"
    pass


print(esercizio3("https://api.esempio.it/risorse"))  # caso base: pochi item con type diversi
print(esercizio3("https://api.esempio.it/moltissimi"))  # caso estremo 1: molti item
print(esercizio3("https://api.esempio.it/vuoto"))    # caso estremo 2: nessun item -> dict vuoto atteso