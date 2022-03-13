
"""Chapitre 5"""

#Exercice 12 :

arbre=["Toto",["Tantan",["Titi",None,None],["Tutu",None,None]], ["Tintin",["Furfur",None,None],["Teïteï",["Tojtoj",None,None],["têtê",None,None]]]]

def ajoutfeuillegauche(arbre,valeur):
    assert type(arbre)==list
    assert len(arbre)==3
    arbre[1]=[valeur,None,None]
    return arbre

def ajoutfeuilledroit(arbre,valeur):
    assert type(arbre)==list
    assert len(arbre)==3
    arbre[2]=[valeur,None,None]
    return arbre
def taille(arbre):
    if arbre==None:
        return 0
    elif arbre[1]==None and arbre[2]==None:
        return 1
    else:
        return 1+taille(arbre[1])+taille(arbre[2])
def hauteur(arbre):
    if arbre==None:
        return 0
    elif arbre[1]==None and arbre[2]==None:
        return 1
    else:
        return 1+max(hauteur(arbre[1]),hauteur(arbre[2]))

def nombrefeuille(arbre):
    if arbre==None:
        return 0
    elif arbre[1]==None and arbre[2]==None:
        return 1
    else:
        return nombrefeuille(arbre[1])+nombrefeuille(arbre[2])

#Exercice 19 :

def lectureprefixe(arbre):
    if arbre==None:
        pass
    else:
        print(arbre[0])
        lectureprefixe(arbre[1])
        lectureprefixe(arbre[2])

def lectureinfixe(arbre):
    if arbre==None:
        pass
    else:
        lectureinfixe(arbre[1])
        print(arbre[0])
        lectureinfixe(arbre[2])

def lecturepostfixe(arbre):
    if arbre==None:
        pass
    else:
        lecturepostfixe(arbre[1])
        lecturepostfixe(arbre[2])
        print(arbre[0])