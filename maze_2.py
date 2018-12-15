# =======================================================================================================
"""MAZE : Algorithme générant un labyrinthe texte partie 2"""
# =======================================================================================================
__author__  = "DELAR Emmalito"
__version__ = "3.1" 
__date__    = "2018-04-29"
# =======================================================================================================
from maze import *
import os
# -------------------------------------------------------------------------------------------------------
def laby(nb_ligne,nb_colonne):
    """Retourne la liste des tuiles formant le labyrinthe"""
    
    
    tuiles_h, tuiles_v, tuiles = [],[],[]                                          
    case_visite, chemin = chemin_(nb_ligne,nb_colonne)
    case_save =  case_visite[:]
    chemin_save = chemin[:]
    
    #On récupère l'état (ouvert ou fermé) des murs horizontaux et verticaux du labyrinthe
    mur_h = [[0 for i in range(nb_colonne)]for j in range(nb_ligne+1)]                     
    mur_v = [[0 for i in range(nb_colonne + 1)]for j in range(nb_ligne)]
    
    mur_h,mur_v = recup_mur(mur_h,mur_v,case_visite,chemin,0,0,nb_ligne,nb_colonne)
    
    #On parcour le tableau des murs horizontaux et marque dans une liste son état
    for liste in mur_h:
        for i in liste:
            if i == 0:
                tuiles_h.append('B')                                         
            else:
                tuiles_h.append('R')
        #A chaque liste du tableau on ajoute 'R' 
        tuiles_h.append('R')
        
    #On fait de même avec le tableau des murs verticaux dans une autre liste
    for liste in mur_v:                                                         
        for i in liste:
            if i == 0:
                tuiles_v.append('C')
            else:
                tuiles_v.append('R')
    #Pour  finir on rempli la fin de la liste avec 'R'
    for i in range(nb_colonne+1):                                                    
        tuiles_v.append('R')
        
    #Puis on réunit les 2 listes pour avoir la liste final 
    for z in range(len(tuiles_h)):                                            
        if tuiles_h[z] == 'B' and tuiles_v[z] == 'R':
            tuiles.append('B.gif')
        elif tuiles_h[z] == 'R' and tuiles_v[z] == 'C':
            tuiles.append('C.gif')
        elif tuiles_h[z] == 'B' and tuiles_v[z] == 'C':
            tuiles.append('D.gif')
        elif tuiles_h[z] == 'R' and tuiles_v[z] == 'R':
            tuiles.append('A.gif')
            
    #On termine en ajoutant une entrée et une sortie choisie aléatoire                                               
    indice,nb = 0,0
    while nb <2:
        entre = randint(1,(nb_ligne-2))
        for i in range(entre+1):
            for j in range(nb_colonne+1):
                indice += 1
        tuiles[indice] = 'E.gif'
        indice = -1
        nb+=1
        
    #On retourne la liste des tuiles du labyrinthe
    return tuiles

# -------------------------------------------------------------------------------------------------------
def recup_mur(mur_h,mur_v,case_visite,list_chemin,i,compt,nb_ligne,nb_colonne):
    """Crée 2 tableaux indiquant l'état des murs verticaux et horizontaux du labyrinthe"""


    NORD,SUD,EST,OUEST,CASE_PRECEDENTE = -nb_colonne, nb_colonne,1,-1,'a'
    #On parcours la liste list_chemins
    while i < (nb_ligne*nb_colonne)-1:
        #On calcul les indices pour chaque élément [e][a]
        indice_tab = int(case_visite[compt]/nb_colonne)                                  
        indice_list = case_visite[compt]%nb_colonne
        
        #On marque le mur correspondant au déplacement
        if list_chemin[i] == NORD:                                                
            mur_h[indice_tab][indice_list] = 1                                  
        elif list_chemin[i] == SUD:                                               
            mur_h[indice_tab+1][indice_list] = 1
        elif list_chemin[i] == OUEST:                                              
            mur_v[indice_tab][indice_list] = 1
        elif list_chemin[i] == EST:                                               
            mur_v[indice_tab][indice_list+1] = 1
        elif list_chemin[i] == CASE_PRECEDENTE:                                             
            while list_chemin[i] == CASE_PRECEDENTE:
                del list_chemin[i]
                del case_visite[compt]
                compt -=1
            return recup_mur(mur_h,mur_v,case_visite,list_chemin,i,compt,nb_ligne,nb_colonne)       
        compt += 1
        i += 1
    #On retourne les tableaux des murs horizontaux et verticaux        
    return mur_h,mur_v

# -------------------------------------------------------------------------------------------------------
def sauvegarde(nb_ligne,nb_colonne):
    """Sauvegarde dans un fichier texte la liste des tuiles formant le labyrinthe"""

    tuiles = laby(nb_ligne,nb_colonne)
    labyrinthe_text = tuiles[:]
    #On transforme la liste en chaîne de caractères
    labyrinthe_text = ','.join(labyrinthe_text)
    #On ouvre ou crée le fichier texte Labyrinthe
    fichier = open("Labyrinthe.txt","a")
    #On ajoute le texte 
    fichier.write("[")
    fichier.write(labyrinthe_text)
    fichier.write("]")
    #On le ferme
    fichier.close()
    #Puis on renvoie la liste de tuiles
    return tuiles
