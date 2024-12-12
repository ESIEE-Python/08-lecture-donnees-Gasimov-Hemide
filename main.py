"""
programme de lecture complet et de calcul d'un fichier csv possedant des lignes d'entiers.
    Fonction secondaires :
    - read_data(filename)  : retourne le contenu du fichier 
    - get_list_k(data, k)  
    - get_first(l)          
    - get_last(l)           
    - get_max(l)            
    - get_min(l)           
    - get_sum(l)           

    Fonction principale :
    - main() : fait des appels de tests
"""
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,mode='r',encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        s = list(r)
        l = [list(map(int, sublist)) for sublist in s]
    return l

def get_list_k(data, k):
    """
    retourne la liste d'indice k de la liste data

    Args:
        data (list): la liste d'étude
        k (int): l'indice de la liste à retourner 

        Returns:
        l (list): le contenu du fichier (1 list par ligne)
    """
    l = data[k]
    return l

def get_first(l):
    """
     retourne le premier élément de la liste l
        Args:
        l (list): liste à étudier

        Returns:
        int : le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    retourne le dernier élément de la liste l
        Args:
        l (list): liste à étudier

        Returns:
        int : le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    retourne la valeur maximum de la liste l
        Args:
        l (list): liste à étudier

        Returns:
        int : la valeur maximum de la liste
    """
    return max(l)

def get_min(l):
    """
    retourne la valeur minimum de la liste l
        Args:
        l (list): liste à étudier

        Returns:
        int : la valeur minimum de la liste
    """
    return min(l)

def get_sum(l):
    """
    retourne la somme des valeurs de la liste l
        Args:
        l (list): liste à étudier

        Returns:
        int : la somme des valeurs de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    permet de faire les tests des fonctions secondaires
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
