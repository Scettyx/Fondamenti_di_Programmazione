# esercizio1
# Scrivi una classe ColoreEsteso che estende Colore aggiungendo un metodo
# 'clippa()' che modifica l'oggetto stesso portando R,G,B dentro [0,255],
# e un metodo 'inverti()' che restituisce un nuovo ColoreEsteso che è
# l'inverso (tipo "negativo": 255 - canale) del colore corrente.
# Usa operatori, ereditarietà e __repr__ per stampare bene gli oggetti.

def esercizio1():
    pass

print(esercizio1())          # caso_base
print(esercizio1())          # caso_estremo1
print(esercizio1())          # caso_estremo2


# esercizio2
# Definisci una classe FiltroMediaColore che ESTENDE FiltroPixel e che, data
# una lista di Colore in __init__, calcola nel costruttore il colore medio
# (media semplice dei canali) e, nel metodo nuovopixel, restituisce sempre
# questo colore medio, ignorando il pixel originale. Prova il filtro su
# una piccola Immagine fatta a mano.

def esercizio2():
    pass

print(esercizio2())          # caso_base
print(esercizio2())          # caso_estremo1
print(esercizio2())          # caso_estremo2


# esercizio3
# Crea una gerarchia di figure minimale: FiguraBase, PuntoColorato, RettangoloOrizzontale.
# - FiguraBase ha solo colore e un metodo astratto disegna.
# - PuntoColorato disegna un singolo pixel.
# - RettangoloOrizzontale disegna un rettangolo allineato agli assi dato
#   il punto in alto a sinistra, larghezza e altezza.
# Usa Immagine, setpixel e ereditarietà. Fai in modo che esercizio3
# crei una piccola Immagine, disegni un punto e un rettangolo e ritorni
# la matrice di triple RGB tramite asTriples().

def esercizio3():
    pass

print(esercizio3())          # caso_base
print(esercizio3())          # caso_estremo1
print(esercizio3())          # caso_estremo2