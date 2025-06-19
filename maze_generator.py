# === maze_generator.py ===
# Génère un labyrinthe parfait en cassant les murs entre cellules avec une méthode récursive (DFS)

import random  # Pour mélanger les voisins de façon aléatoire

# Retourne la liste des voisins non visités autour de la cellule donnée
def voisins_non_visites(grille, c):
    vois = []  # Liste vide pour stocker les voisins valides
    n, m = len(grille), len(grille[0])  # Récupérer les dimensions de la grille
    x, y = c.x, c.y  # Position actuelle de la cellule

    # Vérifie s’il y a un voisin en haut non visité
    if x > 0 and not grille[x - 1][y].visite:
        vois.append(('N', grille[x - 1][y]))  # Ajouter voisin nord

    # Vérifie s’il y a un voisin en bas non visité
    if x < n - 1 and not grille[x + 1][y].visite:
        vois.append(('S', grille[x + 1][y]))  # Ajouter voisin sud

    # Vérifie s’il y a un voisin à gauche non visité
    if y > 0 and not grille[x][y - 1].visite:
        vois.append(('O', grille[x][y - 1]))  # Ajouter voisin ouest

    # Vérifie s’il y a un voisin à droite non visité
    if y < m - 1 and not grille[x][y + 1].visite:
        vois.append(('E', grille[x][y + 1]))  # Ajouter voisin est

    return vois  # Retourner tous les voisins valides non visités

# Casse les murs entre deux cellules dans une direction donnée
def casser_murs(c1, c2, direction):
    opp = {'N': 'S', 'S': 'N', 'E': 'O', 'O': 'E'}  # Dictionnaire des directions opposées
    c1.murs[direction] = False  # Supprimer le mur de la première cellule
    c2.murs[opp[direction]] = False  # Supprimer le mur opposé de la cellule voisine

# Fonction principale pour générer le labyrinthe en partant d'une cellule
def generer_lab(grille, c):
    c.visite = True  # Marquer la cellule comme visitée

    vois = voisins_non_visites(grille, c)  # Obtenir ses voisins non visités
    random.shuffle(vois)  # Mélanger les voisins pour rendre le labyrinthe aléatoire

    for dir, voisin in vois:  # Parcourir les voisins
        if not voisin.visite:  # Si le voisin n’a pas été visité
            casser_murs(c, voisin, dir)  # Casser le mur entre la cellule actuelle et le voisin
            generer_lab(grille, voisin)  # Appel récursif sur le voisin pour continuer la génération
