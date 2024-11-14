import random

"""
Déplacement : Le code commence par compacter les éléments vers la direction souhaitée, en retirant les '*'.

Fusion : Ensuite, il vérifie les paires d'éléments adjacents pour voir s'ils sont égaux et,
si c'est le cas, les fusionne en doublant la valeur de l'un et en remplaçant l'autre par '*'.
Compléter les vides : Enfin, il ajoute des '*' aux endroits appropriés pour que chaque ligne ou colonne ait toujours 4 éléments.
"""

print("Bienvenue dans 2048")
print()

def deplacer_gauche(plateau):
    for i in range(4):
        nouvelle_ligne = [val for val in plateau[i] if val != "*"]  # Retirer les "*" de la ligne, permet de mettre tous les nombres a gauche sans fusionner 
        nouvelle_ligne += ["*"] * (4 - len(nouvelle_ligne))  # Ajouter des "*" à la fin pour compléter la ligne
        for j in range(3):  # Fusionner les cases adjacentes identiques
            if nouvelle_ligne[j] == nouvelle_ligne[j + 1] and nouvelle_ligne[j] != "*":
                nouvelle_ligne[j] *= 2
                nouvelle_ligne[j + 1] = "*"
        nouvelle_ligne = [val for val in nouvelle_ligne if val != "*"]  # Retirer à nouveau les "*" après la fusion
        nouvelle_ligne += ["*"] * (4 - len(nouvelle_ligne))  # Compléter la ligne
        plateau[i] = nouvelle_ligne  # Mettre à jour la ligne du plateau
    return plateau

def deplacer_droite(plateau):
    for i in range(4):
        nouvelle_ligne = [val for val in plateau[i] if val != "*"]
        nouvelle_ligne = ["*"] * (4 - len(nouvelle_ligne)) + nouvelle_ligne  # Ajout des "*" au début pour le déplacement à droite
        for j in range(3, 0, -1):
            if nouvelle_ligne[j] == nouvelle_ligne[j - 1] and nouvelle_ligne[j] != "*":
                nouvelle_ligne[j] *= 2
                nouvelle_ligne[j - 1] = "*"
        nouvelle_ligne = ["*"] * (4 - len([val for val in nouvelle_ligne if val != "*"])) + [val for val in nouvelle_ligne if val != "*"]
        plateau[i] = nouvelle_ligne
    return plateau

def deplacer_haut(plateau):
    for j in range(4):
        nouvelle_colonne = [plateau[i][j] for i in range(4) if plateau[i][j] != "*"]
        nouvelle_colonne += ["*"] * (4 - len(nouvelle_colonne))
        for i in range(3):
            if nouvelle_colonne[i] == nouvelle_colonne[i + 1] and nouvelle_colonne[i] != "*":
                nouvelle_colonne[i] *= 2
                nouvelle_colonne[i + 1] = "*"
        nouvelle_colonne = [val for val in nouvelle_colonne if val != "*"]
        nouvelle_colonne += ["*"] * (4 - len(nouvelle_colonne))
        for i in range(4):
            plateau[i][j] = nouvelle_colonne[i]
    return plateau

def deplacer_bas(plateau):
    for j in range(4):
        nouvelle_colonne = [plateau[i][j] for i in range(4) if plateau[i][j] != "*"]
        nouvelle_colonne = ["*"] * (4 - len(nouvelle_colonne)) + nouvelle_colonne
        for i in range(3, 0, -1):
            if nouvelle_colonne[i] == nouvelle_colonne[i - 1] and nouvelle_colonne[i] != "*":
                nouvelle_colonne[i] *= 2
                nouvelle_colonne[i - 1] = "*"
        nouvelle_colonne = ["*"] * (4 - len([val for val in nouvelle_colonne if val != "*"])) + [val for val in nouvelle_colonne if val != "*"]
        for i in range(4):
            plateau[i][j] = nouvelle_colonne[i]
    return plateau

def main():
    plateau = [["*" for _ in range(4)] for _ in range(4)]

    x = y = 2  # Les deux 2 présents au début de chaque game 2048

    r = random.randint(0, 3)  # Deux random pour placer un x = 2 aléatoirement sur la grille (random sur les lignes et colonnes)
    s = random.randint(0, 3)

    t = random.randint(0, 3)  # Deux random pour placer un y = 2 aléatoirement sur la grille (random sur les lignes et colonnes)
    u = random.randint(0, 3)

    while r == t and s == u:
        t = random.randint(0, 3)
        u = random.randint(0, 3)

    plateau[r][s] = x
    plateau[t][u] = y

    for ligne in plateau:
        print(*ligne)
    print()

    while True:

        print("q = gauche")
        print("d = droite")
        print("z = haut")
        print("s = bas")
        print()

        move = input("Choisissez un mouvement: ")

        if move == "q":
            plateau = deplacer_gauche(plateau)
        elif move == "d":
            plateau = deplacer_droite(plateau)
        elif move == "z":
            plateau = deplacer_haut(plateau)
        elif move == "s":
            plateau = deplacer_bas(plateau)

        # Générer un nouveau 2 quelque part sur la grille, uniquement là où les cellules sont vides
        a = random.randint(0, 3)
        b = random.randint(0, 3)

        while plateau[a][b] != "*":
            a = random.randint(0, 3)
            b = random.randint(0, 3)

        plateau[a][b] = 2

        for ligne in plateau:
            print(*ligne)
        print()


main()
