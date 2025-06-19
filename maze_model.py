# === maze_model.py ===
# Représentation et affichage ASCII du labyrinthe

# Définition d'une cellule dans le labyrinthe
class Cellule:
    def __init__(self, x, y):
        self.x = x  # Coordonnée X de la cellule
        self.y = y  # Coordonnée Y de la cellule
        self.murs = {'N': True, 'S': True, 'E': True, 'O': True}  # Murs présents
        self.visite = False  # Booléen pour vérifier si la cellule a été visitée
        self.marque = False  # Booléen pour savoir si la cellule fait partie du chemin solution

# Crée une grille de n lignes et m colonnes de cellules
def creer_grille(n, m):
    grille = []  # Liste principale pour stocker la grille
    for i in range(n):  # Parcours des lignes
        ligne = []  # Nouvelle ligne vide
        for j in range(m):  # Parcours des colonnes
            ligne.append(Cellule(i, j))  # Ajouter une cellule à la ligne
        grille.append(ligne)  # Ajouter la ligne complète à la grille
    return grille  # Retourner la grille construite

# Affiche le labyrinthe avec ses murs et les cellules marquées '*'
def afficher_lab(grille):
    n = len(grille)  # Nombre de lignes
    m = len(grille[0])  # Nombre de colonnes
    txt = ''  # Chaîne de texte finale à afficher

    txt += '+' + '---+' * m + '\n'  # Première ligne du haut du labyrinthe

    for i in range(n):  # Parcourir les lignes
        ligne1 = '|'  # Contenu visuel de la ligne (haut des cellules)
        ligne2 = '+'  # Contenu des murs inférieurs

        for j in range(m):  # Parcourir les colonnes
            c = grille[i][j]  # Cellule actuelle

            # Afficher une étoile si la cellule fait partie du chemin solution
            if c.marque:
                ligne1 += ' * ' if not c.murs['E'] else ' * |'  # Chemin marqué + mur Est si nécessaire
            else:
                ligne1 += '   ' if not c.murs['E'] else '   |'  # Cellule vide + mur Est si nécessaire

            ligne2 += '   +' if not c.murs['S'] else '---+'  # Mur Sud ou vide

        txt += ligne1 + '\n' + ligne2 + '\n'  # Ajouter les deux lignes au texte final

    print(txt)  # Afficher le labyrinthe complet dans le terminal
