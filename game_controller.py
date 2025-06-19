# === game_controller.py ===
# Contrôle l’exécution du labyrinthe : génération, résolution, affichage

# Importer les fonctions nécessaires des autres modules
from maze_model import creer_grille, afficher_lab  # Pour créer et afficher la grille
from maze_generator import generer_lab  # Pour générer le labyrinthe
from dfs_solver import resoudre_dfs, marquer_solution  # Pour résoudre avec DFS
from bfs_solver_visualizer import resoudre_bfs, afficher_chemin_ascii  # Pour résoudre avec BFS

# Fonction pour réinitialiser l’état des cellules (avant une nouvelle résolution)
def reinitialiser_visites(grille):
    for ligne in grille:  # Pour chaque ligne
        for c in ligne:  # Pour chaque cellule
            c.visite = False  # Réinitialiser la visite
            c.marque = False  # Réinitialiser le marquage du chemin

# Fonction principale qui lance l'application
def lancer():
    print("=== MazeRunnerPy ===")  # Message d'accueil

    n = int(input("Nombre de lignes : "))  # Demander le nombre de lignes
    m = int(input("Nombre de colonnes : "))  # Demander le nombre de colonnes

    g = creer_grille(n, m)  # Créer la grille vide
    generer_lab(g, g[0][0])  # Générer le labyrinthe depuis la cellule (0,0)

    print("\nLabyrinthe généré :")  # Afficher le labyrinthe
    afficher_lab(g)

    # Demander les coordonnées de départ et d’arrivée
    x1, y1 = map(int, input("Point de départ (x y) : ").split())
    x2, y2 = map(int, input("Point d'arrivée (x y) : ").split())

    # Choisir l’algorithme de résolution
    print("\nMéthode de résolution :")
    print("1 - DFS récursif")
    print("2 - BFS (chemin le plus court)")
    choix = input("Choix (1/2) : ")

    reinitialiser_visites(g)  # Nettoyer la grille

    if choix == '1':  # Résolution avec DFS
        chemin = []  # Initialiser une liste vide
        trouve = resoudre_dfs(g, x1, y1, x2, y2, chemin)  # Appel DFS
        if trouve:
            marquer_solution(g, chemin)  # Marquer les cellules du chemin avec *
            print("\nChemin trouvé avec DFS :")
            afficher_lab(g)  # Affichage du labyrinthe avec étoiles
        else:
            print("Aucun chemin trouvé.")

    elif choix == '2':  # Résolution avec BFS
        chemin = resoudre_bfs(g, x1, y1, x2, y2)  # Appel BFS
        if chemin:
            afficher_chemin_ascii(g, chemin)  # Marquer les cellules du chemin
            print("\nChemin trouvé avec BFS :")
            afficher_lab(g)
        else:
            print("Aucun chemin trouvé.")

    else:
        print("Choix invalide.")  # Si l'utilisateur ne tape pas 1 ou 2
#point d'entree du programme
if __name__ == "__main__":
    lancer() #appel a la fonction principale

