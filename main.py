#### Imports et définition des variables globales
"""importation du module sys"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples avec un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    c=[s[0]]
    o=[1]
    n=len(s)
    if not s :
        return []
    for k in range(1,n):
        if s[k] == s[k-1]:
            o[-1] += 1
        else :
            c.append(s[k])
            o.append(1)
    return list(zip(c,o))


def artcode_r(s):
    """retourne la liste de tuples avec un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    if not s :
        return []
    n = 1
    # recherche nombre de caractères identiques au premier
    while n < len(s) and s[n]==s[0]:
        n+=1
    # appel récursif
    return [(s[0], n)] + artcode_r(s[n:])


#### Fonction principale
def main():
    """fonction principale pour afficher le résultat"""
    s = 'MMMMaaacXolloMM'
    print("Itératif :", artcode_i(s))
    print("Récursif :", artcode_r(s))

if __name__ == "__main__":
    main()
