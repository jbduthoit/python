from random import *

val = ['as','r','d','v','10','9','8','7']
coul = ['coeur','carreau','trefle','pique']

def tirage():
    '''tirage d'une carte dans un jeu de 32 cartes'''
    a = randint(0,7)
    b = randint(0,3)
    return (val[a],coul[b])

def gain():
    '''On tire une carte dans un jeu de 32 cartes.​
Si la carte tirée est un as, on gagne 3 jetons.​
Si c’est un cœur, on gagne 2 jetons.​
Pour toutes les autres cartes, on perd un jeton.​
Éventuellement, les gains se cumulent.​
On appelle $X$ la variable aléatoire égale au gain en jetons.​
Déterminer la loi de probabilité de $X​$'''
    carte_tiree = tirage()
    gain = 0
    if carte_tiree[0] == 'as':
        gain += 3
    if carte_tiree[1] == 'coeur':
        gain += 2
    if carte_tiree[0] != 'as' and carte_tiree[1] != 'coeur':
        gain += -2
    return gain


def pourcentage_pour_100000_lancers():
    c = [0,0,0]
    for i in range (100000):
        gain_partie = gain()
        if gain_partie == 5:
            c[0] = c[0] + 1
        if gain_partie == 3:
            c[1] = c[1] +1
        if gain_partie == -2:
            c[2] = c[2] + 1
    c[0] = c[0] / 100000
    c[1] = c[1] / 100000
    c[2] = c[2] / 100000
    return c


def gain_moyen():
    c = 0
    for i in range (100000):
        gain_partie = gain()
        c = c + gain_partie
    return c/100000

            
    
    