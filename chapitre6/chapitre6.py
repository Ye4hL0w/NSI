class ArbreBinaire:
    def __init__(self,valeur):
        self.valeur=valeur
        self.gauche=None
        self.droit=None

    def ajoutgauche(self,valeur):
        self.gauche=ArbreBinaire(valeur)

    def supprgauche(self):
        self.gauche=None

    def ajoutdroit(self,valeur):
        self.droit=ArbreBinaire(valeur)

    def supprdroit(self):
        self.droit=None

class File:
    def __init__(self):
        self.tablo=[]

    def pousse(self,nb):
        self.tablo.insert(0,nb)

    def pop(self):
        return self.tablo.pop()

    def non_vide(self):
        return self.tablo!=[]

arbre=ArbreBinaire(30)
arbre.ajoutgauche(20)
arbre.gauche.ajoutgauche(10)
arbre.gauche.gauche.ajoutgauche(5)
arbre.gauche.gauche.ajoutdroit(11)
arbre.gauche.ajoutdroit(22)
arbre.gauche.droit.ajoutdroit(27)
arbre.ajoutdroit(60)
arbre.droit.ajoutgauche(45)
arbre.droit.gauche.ajoutgauche(40)
arbre.droit.gauche.ajoutdroit(50)
arbre.droit.ajoutdroit(100)
arbre.droit.droit.ajoutgauche(80)
arbre.droit.droit.ajoutdroit(200)


def rechercheValeur(unarbre,valeur):
    if unarbre==None:
        return False
    else:
        if unarbre.valeur==valeur:
            return True
        elif valeur<unarbre.valeur:
            return rechercheValeur(unarbre.gauche,valeur)
        else:
            return rechercheValeur(unarbre.droit,valeur)


#Supposons qu'il n'y ait que des valeurs distinctes:
def ajoutValeur(unarbre,valeur):
    if valeur<unarbre.valeur:
        if unarbre.gauche==None:
            unarbre.ajoutgauche(valeur)
        else:
            ajoutValeur(unarbre.gauche,valeur)
    else:
        if unarbre.droit==None:
            unarbre.ajoutdroit(valeur)
        else:
            ajoutValeur(unarbre.droit,valeur)

def taille(arbre):
    if arbre==None:
        return 0
    else:
        return 1+taille(arbre.gauche)+taille(arbre.droit)

def hauteur(arbre):
    if arbre==None:
        return 0
    else:
        return 1+max(hauteur(arbre.gauche),hauteur(arbre.droit))


def creaarbrerechercheIDIOT(liste):
    if liste==[]:
        return None
    unarbre=ArbreBinaire(liste.pop())
    while liste!=[]:
        ajoutValeur(unarbre,liste.pop())
    return unarbre


def creaArbreRechercheSmart(liste):
    assert type(liste)==list        #on verifie que c'est une liste
    assert liste!=[]
    if len(liste)==1:               #on traite le cas où il n'y a qu'une valeur
        return ArbreBinaire(liste[0])
    elif len(liste)==2:             #on traite le cas où il y a deux valeurs
        arbre=ArbreBinaire(liste[0])
        ajoutValeur(arbre,liste[1])
        return arbre
    else:                           # il y a au moins 3 valeurs
        liste.sort()                #on trie la liste
        longueur=len(liste)
        indice_milieu=len(liste)//2 # marche pour les cas pairs et impairs
        arbre=ArbreBinaire(liste[indice_milieu])    #on créé l'arbre
        file=File()                                 #on mettra a l'interieur les bouts de liste à traiter
        file.pousse(liste[:indice_milieu])          #on pousse la partie à gauche du milieu
        file.pousse(liste[indice_milieu+1:])        #on pousse la partie à droite du milieu
        while file.non_vide():                      #tant qu'il reste des listes à vider
            liste_traitee=file.pop()                #on selectionne une file
            longueur=len(liste_traitee)
            if longueur==0:                         # si la liste est vide
                pass
            elif longueur==1:                       #il n'y a qu'une valeur
                ajoutValeur(arbre,liste_traitee.pop())
            elif longueur==2:                       #il n'y a que deux valeurs
                ajoutValeur(arbre,liste_traitee.pop())
                ajoutValeur(arbre,liste_traitee.pop())
            else:                                   #il y a au moins trois valeurs donc un milieu
                indice_milieu=len(liste_traitee)//2 #marche pour pairs et impairs
                ajoutValeur(arbre,liste_traitee[indice_milieu])  #on met la valeur centrale
                file.pousse(liste_traitee[:indice_milieu])       #on pousse partie à gauche
                file.pousse(liste_traitee[indice_milieu+1:])     #on pousse partie à droite
    return arbre  #gg