#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from math import sqrt
from tree import BinaryTree
from nary_tree import NaryTree

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
"""
nome = "hide"
cognome = "matsumoto"
matricola = "5050"

################################################################################
################################################################################
################################################################################
# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 4 punti
Implementate la funzione ex1(N) che, dato un intero N positivo o nullo, 
restituisce l'N-esimo termine della successione di Lucas del primo tipo, U(N, P, Q), definita come segue:
    U(0, *, *) = 0
    U(1, *, *) = 1
    U(n, P, Q) = P * U(n-1, P, Q) - Q * U(n-2, P, Q) per n >= 2.

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
"""
def lucas_U_recursive(n, P, Q, memo):
    if n in memo:
        return memo[n]

    result = (P * lucas_U_recursive(n - 1, P, Q, memo) -
              Q * lucas_U_recursive(n - 2, P, Q, memo))

    memo[n] = result
    return result
def ex1(N, P, Q):
    memo = {0: 0, 1: 1}
    return lucas_U_recursive(N, P, Q, memo)

# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 8 punti

Implementa la funzione ex2(root) che riceve in ingresso root, un'istanza di albero binario, così come definito
nella classe BinaryTree del modulo tree. La funzione deve trovare e restituire la differenza minima in valore assoluto 
tra la somma dei valori dei nodi nella coppia di sottoalberi sinistro e destro di un nodo qualsiasi dell'albero, 
radice inclusa. Per un nodo foglia, la differenza è 0. 

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
'''


def calculate_sum_and_diff(node, min_abs_diff):
    """
    Esegue un post-order traversal, calcolando la somma di ogni sottoalbero
    e aggiornando la differenza minima globale.
    Ritorna: la somma totale dei valori nel sottoalbero radicato in 'node'.
    """
    if node is None:
        return 0

    sum_left = calculate_sum_and_diff(node.left, min_abs_diff)
    sum_right = calculate_sum_and_diff(node.right, min_abs_diff)

    current_diff = abs(sum_left - sum_right)

    min_abs_diff[0] = min(min_abs_diff[0], current_diff)

    return node.value + sum_left + sum_right

def ex2(root):
    min_abs_diff = [float('inf')]
    calculate_sum_and_diff(root, min_abs_diff)
    return min_abs_diff[0] if min_abs_diff[0] != float('inf') else 0


import os


# %% ----------------------------------- EX.3 ----------------------------------- #
'''
Ex3: 8 points 
Implementa la funzione ex3(dirin, K, extensions) che, dato il percorso di una directory dirin, 
un intero K e una lista di estensioni target (es. ['txt', 'pdf']), deve trovare tutte 
le directory che contengono un numero sufficiente di file con una delle estensioni specificate.

Restituisci un dizionario che ha:
  - Come chiavi: il path completo (stringa) di ogni directory (usando '/' come separatore).
  - Come valori: il numero totale di file (conteggiati ricorsivamente in tutti i sottolivelli) 
    la cui estensione è presente nella lista extensions.
Il dizionario deve includere solo le directory in cui il conteggio totale di tali file è strettamente maggiore di K.

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
'''


def get_dir_file_count_recursive(current_path, K, extensions, result):
    current_dir_valid_count = 0
    total_valid_count_in_subtree = 0

    try:
        for entry in os.listdir(current_path):
            full_path = current_path + '/' + entry

            if os.path.isfile(full_path):
                ext = os.path.splitext(entry)[1].lower().lstrip('.')

                if ext in extensions:
                    current_dir_valid_count += 1

            elif os.path.isdir(full_path):
                total_valid_count_in_subtree += get_dir_file_count_recursive(full_path, K, extensions, result)

    except OSError:
        return 0

    total_valid_count_in_subtree += current_dir_valid_count

    if total_valid_count_in_subtree > K:
        result[current_path] = total_valid_count_in_subtree

    return total_valid_count_in_subtree


def ex3(dirin, K, extensions):
    result = {}
    extensions = [ext.lower() for ext in extensions]
    get_dir_file_count_recursive(dirin, K, extensions, result)
    return result


# %% ---------------------------- EX 4 ---------------------------- #
'''
Esercizio 4 (10 punti): 

Trova il nodo che soddisfa la seguente condizione e ha la profondità maggiore.
La condizione è che il valore del nodo sia uguale al più piccolo numero primo (positivo) 
presente nel percorso dalla radice a quel nodo (radice esclusa). 
Restituire il percorso (lista di valori) dalla radice a questo nodo.
In caso di parità di valore minimo, considera prima il nodo con la massima profondità, poi il suo ordine di visita 
in pre-order.

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
'''


def is_prime(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


def dfs(node: NaryTree, current_path: list, primes_on_path: set, best_match, pre_order_counter):

    if node is None:
        return

    current_path.append(node.value)
    current_depth = len(current_path) - 1

    new_primes_on_path = primes_on_path.copy()
    if current_depth > 0 and is_prime(node.value):
        new_primes_on_path.add(node.value)

    min_prime = min(new_primes_on_path) if new_primes_on_path else None

    if min_prime is not None and node.value == min_prime:

        if current_depth > best_match[1]:
            best_match[0] = current_path.copy()
            best_match[1] = current_depth
            best_match[2] = pre_order_counter[0]  # Aggiorna la posizione pre-order

        elif current_depth == best_match[1] and pre_order_counter[0] < best_match[2]:
            best_match[0] = current_path.copy()
            best_match[2] = pre_order_counter[0]

    pre_order_counter[0] += 1

    for child in node.children:
        dfs(child, current_path, new_primes_on_path, best_match, pre_order_counter)

    current_path.pop()


def ex4(root: NaryTree):
    best_match = [None, -1, float('inf')]
    pre_order_counter = [0]

    dfs(root, [], set(), best_match, pre_order_counter)

    return best_match[0]


######################################################################################

if __name__ == '__main__':
    # Puoi provare qui le tue implementazioni senza che interferiscano con il grader

    pass