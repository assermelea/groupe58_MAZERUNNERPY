# === bfs_solver_visualizer.py ===
# Résolution du labyrinthe avec l’algorithme BFS (plus court chemin)

from collections import deque  # Pour utiliser une file FIFO (First-In First-Out)

# Fonction qui résout le labyrinthe avec BFS
def resoudre_bfs(grille, x1, y1, x2, y2):
    n, m = len(grille), len(grille[0])  # Taille de la grille
    file = deque()  # Créer une file pour stocker les cellules à visiter
    file.append((x1, y1))  # Ajouter le point de départ à la file
    pred = {}  # Dictionnaire pour stocker les prédécesseurs de chaque cellule
    grille[x1][y1].visite = True  # Marquer la cellule de départ comme visitée

    # Directions de déplacement : Nord, Sud, Est, Ouest
    dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'O': (0, -1)}

    # Tant qu’il y a des cellules à visiter
    while file:
        x, y = file.popleft()  # Prendre la première cellule de la file

        # Si on est arrivé à la cellule d’arrivée
        if (x, y) == (x2, y2):
            chemin = []  # Initialiser le chemin trouvé
            while (x, y) != (x1, y1):  # Revenir en arrière jusqu’au départ
                chemin.append((x, y))  # Ajouter chaque cellule au chemin
                x, y = pred[(x, y)]  # Remonter au prédécesseur
            chemin.append((x1, y1))  # Ajouter la cellule de départ
            chemin.reverse()  # Inverser pour avoir le chemin dans le bon sens
            return chemin  # Retourner le chemin complet

        c = grille[x][y]  # Cellule actuelle

        for d, (dx, dy) in dirs.items():  # Parcourir les 4 directions
            if not c.murs[d]:  # S’il n’y a pas de mur dans cette direction
                nx, ny = x + dx, y + dy  # Calculer la nouvelle position
                voisin = grille[nx][ny]  # Récupérer la cellule voisine
                if not voisin.visite:  # Si elle n’a pas été visitée
                    voisin.visite = True  # Marquer comme visitée
                    file.append((nx, ny))  # L’ajouter à la file
                    pred[(nx, ny)] = (x, y)  # Mémoriser le prédécesseur

    return None  # Si aucun chemin trouvé

# Fonction pour afficher visuellement le chemin dans la grille
def afficher_chemin_ascii(grille, chemin):
    for x, y in chemin:
        grille[x][y].marque = True  # Marquer les cellules du chemin avec *
