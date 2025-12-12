# esercizio1: data una quantità di secondi (intero), restituisci QUANTE MINUTI INTERI COMPLETI ci sono
#             Usa solo operazioni aritmetiche viste (//, %, *, +, -) e NESSUNA funzione pronta.
def esercizio1(secondi):
    return secondi // 60

print(esercizio1(0))        # caso_base: 0 secondi
print(esercizio1(59))       # caso_estremo1: meno di 1 minuto
print(esercizio1(3605))     # caso_estremo2: più di un'ora


# esercizio2: data una spesa totale (float) e il numero di persone (int),
#             restituisci QUANTO PAGA OGNI PERSONA come float.
#             Usa la divisione normale / e fai attenzione ai casi limite (es. 0 persone).
def esercizio2(spesa_totale, numero_persone):
    return None if numero_persone == 0 else spesa_totale / numero_persone

print(esercizio2(100.0, 4))   # caso_base
print(esercizio2(0.0, 3))     # caso_estremo1: spesa zero
print(esercizio2(50.0, 0))    # caso_estremo2: persone zero (decidi tu come gestirlo)


# esercizio3: data una base (int) e un esponente (int >= 0),
#             restituisci base**esponente SENZA usare l'operatore **,
#             ma solo moltiplicazioni ripetute e un ciclo while o for (li userai dopo, ora pensa solo alla logica).
def esercizio3(base, esponente):
    risultato = base
    if esponente == 0:
        return 1
    for _ in range(esponente - 1):
        risultato *= base
    return risultato

print(esercizio3(2, 0))     # caso_base: qualunque numero alla 0
print(esercizio3(2, 10))    # caso_estremo1: potenza grande
print(esercizio3(0, 5))     # caso_estremo2: base zero, esponente positivo