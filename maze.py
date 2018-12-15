# =======================================================================================================
"""MAZE : Algorithme générant un labyrinthe texte partie 1"""
# =======================================================================================================
__author__  = "DELAR Emmalito"
__version__ = "2.1" 
__date__    = "2018-03-28"
# =======================================================================================================
from random import *
from tkinter import *
# -------------------------------------------------------------------------------------------------------
def direction(position,nb_ligne,nb_colonne):
    """Cherche les directions accessibles (NORD, SUD, EST, OUEST) et en choisit une aléatoirement"""

    NORD = -nb_colonne
    EST = 1
    OUEST = -1
    SUD = nb_colonne
    direction = [NORD,EST,OUEST,SUD]

    #On marque les directions inaccessible à l'aide de caractères a ou b
    a,b = 'a','b'
    if 0 <= position < nb_colonne :
        a = NORD                        
    if ((nb_ligne*nb_colonne)-nb_colonne)-1<position<nb_ligne*nb_colonne:
        a = SUD
    if position%nb_colonne == 0:
        b = OUEST
    if position % nb_colonne == nb_colonne-1:
        b = EST
    #On supprime ces directions marquéees de la liste de directions
    if a != 'a':
        direction.remove(a)
    if b != 'b':
        direction.remove(b)
    #On choisit aléatoirement une des directions
    i = randint(0,len(direction)-1)
    #Puis on retourne la liste de direction, la direction choisie et la nouvelle position  // ambigue
    return position+direction[i],direction[i],direction

# --------------------------------------------------------------------------------------------------------
def chemin_(nb_ligne,nb_colonne):
    """Crée le chemin du labyrinthe et retourne l'ordre des cases et des directions empruntées"""

    chemin, case_visite, direct, case_visite_beta, i = [],[],[],[],1           
    grille = [0]*nb_ligne*nb_colonne                                                    
    # On commence la construction du labyrinthe à une position aléatoire de la grille
    case = randint(0,len(grille)-1)                                           
    #Liste, allant être modifiée, qui enregistre les cases visitées 
    case_visite_beta.append(case)
    #Liste qui enregistre les cases visitées
    case_visite = case_visite_beta[:]
    #On marque la case de départ
    grille[case]=1
    #Tant que toute les cases n'ont pas été marquées, case1 = voisin(case)
    while i<len(grille):                                                                  
        case1,new_dir,liste_dir = direction(case,nb_ligne,nb_colonne)                               
        case1,new_dir = verification(grille,case1,new_dir,liste_dir,case_visite_beta,nb_ligne,nb_colonne,chemin) 
        case = case1
        grille[case] = 1
        case_visite.append(case)
        case_visite_beta.append(case)                                                  
        chemin.append(new_dir)                                                            
        i +=1
     #On retourne la listes des cases visitées et le chemin emprunté
    return(case_visite,chemin)

# --------------------------------------------------------------------------------------------------------
def verification(grille,case1,new_dir,liste_dir,case_visite,nb_ligne,nb_colonne,chemin):
    """On va vérifier si la case peut être choisie"""

    #Si la case n'est pas marquée on la renvoie
    if grille[case1] != 1:                                                                
        return case1,new_dir
    #Si elle l'est, on choisit une des cases voisines
    if len(liste_dir) > 1:                                             
        liste_dir.remove(new_dir)
        nvx = len(liste_dir)-1
        new_dir = liste_dir[randint(0,nvx)]
        case1 = case_visite[-1]+new_dir
        #Et on la vérifie 
        return verification(grille,case1,new_dir,liste_dir,case_visite,nb_ligne,nb_colonne,chemin)
    #Sinon on sélectionne la case visitée précédente et on change de direction
    else :                                                                             
        del case_visite[-1]
        case1 = case_visite[-1]
        case1,new_dir,liste_dir = direction(case1,nb_ligne,nb_colonne)
        case1 = case1 - new_dir
        new_dir = 'a'
        liste_dir.append('a')
        chemin.append('a')
        #Puis on la vérifie 
        return verification(grille,case1,new_dir,liste_dir,case_visite,nb_ligne,nb_colonne,chemin)    
