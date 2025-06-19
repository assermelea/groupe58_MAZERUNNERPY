# === dfs_solver.py ===
# Résolution du labyrinthe avec l’algorithme DFS récursif

# Fonction de résolution par parcours en profondeur (DFS)
def resoudre_dfs(grille, x1, y1, x2, y2, chemin=[]):
    c = grille[x1][y1]  # Prendre la cellule de départ
    c.visite = True  # Marquer la cellule comme visitée
    chemin.append((x1, y1))  # Ajouter la cellule actuelle au chemin

    if (x1, y1) == (x2, y2):  # Si on a atteint la cellule d’arrivée
        return True  # Chemin trouvé

    # Dictionnaire des directions et des déplacements (delta x et y)
    dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'O': (0, -1)}

    # Parcourir les directions possibles
    for d, (dx, dy) in dirs.items():
        if not c.murs[d]:  # Si le mur dans cette direction est ouvert
            nx, ny = x1 + dx, y1 + dy  # Coordonnées du voisin
            voisin = grille[nx][ny]  # Obtenir la cellule voisine

            if not voisin.visite:  # Si elle n’a pas encore été visitée
                if resoudre_dfs(grille, nx, ny, x2, y2, chemin):  # Appel récursif
                    return True  # Si la solution est trouvée dans ce chemin

    chemin.pop()  # Si aucun chemin ne mène à la fin, retour arrière
    return False  # Aucun chemin trouvé depuis cette cellule

# Fonction pour marquer les cellules du chemin trouvé avec une étoile
def marquer_solution(grille, chemin):
    for x, y in chemin:
        grille[x][y].marque = True  # Active l’affichage de l’étoile dans afficher_lab()
