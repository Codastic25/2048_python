import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill(color="white")
pygame.display.set_caption("2048")

pygame.mixer.init()
pygame.mixer.music.load("prism.mp3")
pygame.mixer.music.play(-1) #pour jouer la musique en boucle


#choix des couleurs pour chaque puissance de 2 jusqu'à 2048

couleurs = {
    2: (238, 228, 218),   # beige tres clair
    4: (237, 224, 200),   # beige clair
    8: (242, 177, 121), # orange clair
    16: (245, 149, 99),  # orange
    32: (246, 124, 95),    # orange foncé
    64: (246, 94, 59),    # rouge orangé
    128: (237, 207, 114),  # jaune
    256: (237, 204, 97), # jaune foncé
    512: (237, 200, 80),  # doré
    1024: (237, 197, 63),  # jaune doré
    2048: (237, 194, 46),  # jaune tres doré
}

#fonctions de déplacements

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

def tour_2():

    # Générer un nouveau 2 quelque part sur la grille, uniquement là où les cellules sont vides
    a = random.randint(0, 3)
    b = random.randint(0, 3)

    while plateau[a][b] != "*":
        a = random.randint(0, 3)
        b = random.randint(0, 3)

    plateau[a][b] = 2


#créer la grille de NB_COL par NB_LIGNES

def afficher_grille(plateau):

    NB_COL = 4
    NB_LIGNES = 4
    DIM_CELL = 600//4

    for i in range (0,NB_COL):
        for j in range (0,NB_LIGNES):
            rect = pygame.Rect(i*DIM_CELL, j*DIM_CELL, DIM_CELL, DIM_CELL)
            pygame.draw.rect(screen, pygame.Color("black"), rect, width=1)

            if plateau[i][j] == "*":
                rect = pygame.Rect(i*DIM_CELL, j*DIM_CELL, DIM_CELL, DIM_CELL)
                pygame.draw.rect(screen, pygame.Color("black"), rect, width=1)
            else:
                # Définir la police et la taille du texte
                font = pygame.font.Font(None, 70)

                # Rendre le texte '2' en surface
                text_surface = font.render(str(plateau[i][j]), True, (0,0,0))

                # Créer un Rect pour le texte
                rect = pygame.Rect(j*DIM_CELL, i*DIM_CELL, DIM_CELL, DIM_CELL)

                # Centrer le texte à l'intérieur du rect
                text_rect = text_surface.get_rect(center=rect.center)

                #colorer les cases de différentes couleurs et mettre des contours
                
                couleur = couleurs.get(plateau[i][j], (200, 200, 200))
                pygame.draw.rect(screen, couleur, rect)
                pygame.draw.rect(screen, pygame.Color("black"), rect, width=1)
                
                screen.blit(text_surface, text_rect)
            
                # Vérifiez les conditions de victoire/défaite après avoir dessiné toute la grille
                if any(2048 in row for row in plateau):
                    victoire()
                elif est_jeu_termine(plateau):
                    defaite()


def le_tableau():
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

    return plateau

plateau = le_tableau()

#fonctions ci_dessous de menu du jeu
def text_title(text, font, color, x, y):
    draw_text(text, font, color, x, y)

font_2 = pygame.font.Font(None, 100)
font = pygame.font.Font(None, 50)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    on = True
    while on:
        screen.fill(pygame.Color("dark blue"))
        text_title("2048", font_2, pygame.Color("yellow"), 600//2, 600//6)
        draw_text("Press ENTER for START", font, pygame.Color("white"), 600//2, 600//2.5)
        draw_text("Q for EXIT", font, pygame.Color("white"), 600//2, 600//2)
        draw_text("By Marvilliers Aurian", font, pygame.Color("white"), 600//2, 600//1.5)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    on = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    

main_menu()

#ecran de victoire
def victoire():
    screen.fill(color="green")
    draw_text("WIN", font_2, pygame.Color("white"), 600//2, 600//2)
    pygame.display.update()
    pygame.time.delay(6000)
    main_menu()

#condition de jeu terminé
def est_jeu_termine(plateau):
    # Vérifier s'il y a des cases vides
    if any("*" in ligne for ligne in plateau):
        return False
    
    # Vérifier s'il y a des mouvements possibles horizontalement
    for i in range(4):
        for j in range(3):
            if plateau[i][j] == plateau[i][j+1]:
                return False
    
    # Vérifier s'il y a des mouvements possibles verticalement
    for i in range(3):
        for j in range(4):
            if plateau[i][j] == plateau[i+1][j]:
                return False
    
    # Si aucun mouvement n'est possible, le jeu est terminé
    return True


#ecran de defaite
def defaite():
    screen.fill(color="red")
    draw_text("LOSE", font_2, pygame.Color("white"), 600//2, 600//2)
    pygame.display.update()
    pygame.time.delay(6000)
    main_menu()


#boucle de jeu 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deplacer_gauche(plateau)
                tour_2()
            if event.key == pygame.K_RIGHT:
                deplacer_droite(plateau)
                tour_2()
            if event.key == pygame.K_UP:
                deplacer_haut(plateau)
                tour_2()
            if event.key == pygame.K_DOWN:
                deplacer_bas(plateau)
                tour_2()

    screen.fill(pygame.Color("white"))

    afficher_grille(plateau)

    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()

#texte a mettre en évidence pour éviter les pb de plagiat de musique :
"""
Music: Bensound.com/royalty-free-music
License code: DMYZRXXIHVMUFX4I
"""
