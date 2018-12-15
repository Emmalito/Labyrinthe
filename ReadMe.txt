Projet : Labyrinthe
----------------------------------------------------------------------------------------------------------------------------------------

Version 1 :

Pour g�n�rer le labyrinthe, nous l'avons d'abord cr�e via un algorithme. Pour cela, nous nous sommes inspir�s de la m�thode d'exploration exhaustive. Nous avons donc fait 6 programmes pour.

Direction : Ce programme retourne les directions possible que le chemin peut emprunter, la case d'arriv� et la direction prise ( qui a �t� choisit al�atoirement).

Chemin : Celui ci va g�n�rer la totalit� du chemin et va retourner les cases visit�es(de la 1�re � la derni�re) et les directions prises.

Verification : Il va indiquer si la direction choisit peut �tre prise et sinon renvoi une direction possible.

Recuperation : Sert � transformer la tuple de 2 �l�ments renvoy�e par le programme Chemin en une liste de m*n nombres.

Recup_mur : Va retourner deux listes de valeurs bool�ennes, indiquant l'une et l'autre les murs horizontaux et verticaux restant apr�s avoir trac� le chemin. 

Laby : Il va retourner deux listes de valeurs bool�ennes, indiquant l'une et l'autre les murs horizontaux et verticaux restant apr�s avoir trac� le chemin.

Scrole : Interface graphique permettant � l'utilisateur de rentrer les dimensions du labyrinthe.

Graph : Pas encore commenc� mais devrais g�n�rer graphiquement le labyrinthe obtenu.

----------------------------------------------------------------------------------------------------------------------------------------

Version 2 :

On a am�lior� les programmes Maze, Maze_2 et Graph :

Maze : Programme Chemin :On a remplacer la tuples qui enregistrait les cases visit�es par une liste. Les dimensions maximum du labyrinthe ont �t� agrandit.

Maze_2 : Programme recup_mur : On a utilis� des tableaux � deux dimensions pour repr�senter les murs verticaux et horizontaux. 
	 Programme laby      : Avec les tableaux, on va r�cup�rer la liste de tuiles repr�sentant le labyrinthes.

Graph : Programme graph      : On repr�sente graphiquement le labyrinthe gr�ce � la liste de tuile.


----------------------------------------------------------------------------------------------------------------------------------------

Version 3 :

On a am�lior� la "lisibilit�" du code (nom de variable plus significative, commentaire plus claire,...).
On a g�n�r� le labyrinthe dans un canvas.
On a rajout� des scrolles � la fen�tre.
On a essay� d'impl�menter le solveur � l'aide de l'algorithme A* sans succ�s.







