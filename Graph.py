# =======================================================================================================
"""GRAPH : Algorithme générant une interface graphique à un labyrinthe texte"""
# =======================================================================================================
__author__  = "DELAR Emmalito"
__version__ = "3.1" 
__date__    = "2018-04-29"
# =======================================================================================================
from maze_2 import *
import tkinter.font as tkFont 
# -------------------------------------------------------------------------------------------------------
def scrole():
    """Renvoie les dimensions du labyrinthe choisi par l'utilisateur"""

    #On crée une fenêtre graphique
    win = Tk()                                                                              
    win['bg'] = 'white'
    t = ("Helvetica", "11", "bold")
    #Les 2 scroles permettant de choisir les dimensions et un bouton entrer
    scrole_1 = Scale(win,orient = "horizontal",bg ='white', label="Ligne",font=t,           
                     from_=3, to=100)
    scrole_2 = Scale(win,orient = "horizontal",bg ='white', label="Colonne",font=t,         
                     from_=3, to=100)
    bouton_1 = Button(win,text='Entrer',command= win.quit)                                  
    
    scrole_1.pack(), scrole_2.pack(), bouton_1.pack(pady=6)
    win.mainloop()
    #On récupère la valeur des scroles et ferme la fenêtre
    nb_ligne,nb_colonne = scrole_1.get(),scrole_2.get()                                                     
    win.destroy()
    #On retourne les valeurs des scroles
    return nb_ligne,nb_colonne                                                                             
# -------------------------------------------------------------------------------------------------------
def graph():
    """Génération du labyrinthe graphique"""

    #On récupère les dimensions du labyrinthe et la liste de tuile le formant
    nb_ligne,nb_colonne = scrole()                                                                          
    graph = sauvegarde(nb_ligne,nb_colonne)                                                                

    #On crée une fenêtre en pleine écran, une zone de texte, un dictionnaire et le widget contenant le labyrinthe
    win = Tk()
    can = Canvas(win,bg='white')                                                           
    frame = Frame(win,bg='white')
    win['bg']='white'
    win.attributes('-fullscreen',True )                                                                           
    texte = 'Labyrinthe %s * %d'%(nb_ligne,nb_colonne)
    tms30 = tkFont.Font(family='Times', size=30, weight='bold')
    label = Label(frame,text = texte,bg='white',font=tms30)
    x,y,compteur = 0,10,0
    gifsdict={}

    #Pour chaque case de la grille
    for ligne in range(nb_ligne+1):                                                                
        for colonne in range(nb_colonne+1):                                                          

            #On insère l'image de la tuile 
            tuile = PhotoImage(file=graph[compteur])                                        
            item = can.create_image(x,y,image=tuile)                                        
            can.photo=tuile
            gifsdict[tuile]= graph[compteur]
            compteur += 1
            x+=16                                                                          
        y+=16                                                                              
        x = 0
        
    #On crée les scrolls vertical et horizontal de la fenêtre
    scrollbar = Scrollbar(win,orient='vertical',command = can.yview)                        
    scrollbar_2 = Scrollbar(win, orient='horizontal',command = can.xview)
    #Et un bouton servant à fermer la fenêtre
    Button(frame,text='Quitter',command=win.destroy).pack(side=RIGHT)                       
    
    scrollbar.pack(side = RIGHT,fill=Y),scrollbar_2.pack(side = BOTTOM,fill=X)
    frame.pack(side = TOP),label.pack(),can.pack(fill='both',expand=1)
    win.mainloop()
# =======================================================================================================    
if __name__ == "__main__":
  graph()
# =======================================================================================================
