Projet : Labyrinthe
----------------------------------------------------------------------------------------------------------------------------------------

Version 1 :

Pour générer le labyrinthe, nous l'avons d'abord crée via un algorithme. Pour cela, nous nous sommes inspirés de la méthode d'exploration exhaustive. Nous avons donc fait 6 programmes pour.

Direction : Ce programme retourne les directions possible que le chemin peut emprunter, la case d'arrivé et la direction prise ( qui a été choisit aléatoirement).

Chemin : Celui ci va générer la totalité du chemin et va retourner les cases visitées(de la 1ère à la dernière) et les directions prises.

Verification : Il va indiquer si la direction choisit peut être prise et sinon renvoi une direction possible.

Recuperation : Sert à transformer la tuple de 2 éléments renvoyée par le programme Chemin en une liste de m*n nombres.

Recup_mur : Va retourner deux listes de valeurs booléennes, indiquant l'une et l'autre les murs horizontaux et verticaux restant après avoir tracé le chemin. 

Laby : Il va retourner deux listes de valeurs booléennes, indiquant l'une et l'autre les murs horizontaux et verticaux restant après avoir tracé le chemin.

Scrole : Interface graphique permettant à l'utilisateur de rentrer les dimensions du labyrinthe.

Graph : Pas encore commencé mais devrais générer graphiquement le labyrinthe obtenu.

----------------------------------------------------------------------------------------------------------------------------------------

Version 2 :

On a amélioré les programmes Maze, Maze_2 et Graph :

Maze : Programme Chemin :On a remplacer la tuples qui enregistrait les cases visitées par une liste. Les dimensions maximum du labyrinthe ont été agrandit.

Maze_2 : Programme recup_mur : On a utilisé des tableaux à deux dimensions pour représenter les murs verticaux et horizontaux. 
	 Programme laby      : Avec les tableaux, on va récupérer la liste de tuiles représentant le labyrinthes.

Graph : Programme graph      : On représente graphiquement le labyrinthe grâce à la liste de tuile.


----------------------------------------------------------------------------------------------------------------------------------------

Version 3 :

On a amélioré la "lisibilité" du code (nom de variable plus significative, commentaire plus claire,...).
On a généré le labyrinthe dans un canvas.
On a rajouté des scrolles à la fenêtre.
On a essayé d'implémenter le solveur à l'aide de l'algorithme A* sans succès.







