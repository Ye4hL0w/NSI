
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

#Exercice 21 :

arbre=ArbreBinaire("toto")
arbre.ajoutgauche("tantan")
arbre.gauche.ajoutgauche("titi")
arbre.gauche.ajoutdroit("tutu")
arbre.ajoutdroit("tintin")
arbre.droit.ajoutgauche("furfur")
arbre.droit.ajoutdroit("teïteï")
arbre.droit.droit.ajoutgauche("tojtoj")
arbre.droit.droit.ajoutdroit("têtê")

#Exercice 22 :

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

def nombrefeuille(arbre):
    if arbre==None:
        return 0
    elif arbre.gauche==None and arbre.droit==None:
        return 1
    else:
        return nombrefeuille(arbre.gauche)+nombrefeuille(arbre.droit)

def lectureprefixe(arbre):
    if arbre==None:
        pass
    else:
        print(arbre.valeur)
        lectureprefixe(arbre.gauche)
        lectureprefixe(arbre.droit)

def lectureinfixe(arbre):
    if arbre==None:
        pass
    else:
        lectureinfixe(arbre.gauche)
        print(arbre.valeur)
        lectureinfixe(arbre.droit)

def lecturepostfixe(arbre):
    if arbre==None:
        pass
    else:
        lecturepostfixe(arbre.gauche)
        lecturepostfixe(arbre.droit)
        print(arbre.valeur)

#Exercice 30 :

def evaluer(arbre):
    if arbre.valeur=="+":
        return evaluer(arbre.gauche)+evaluer(arbre.droit)
    elif arbre.valeur=="-":
        return evaluer(arbre.gauche)-evaluer(arbre.droit)
    elif arbre.valeur=="*":
        return evaluer(arbre.gauche)*evaluer(arbre.droit)
    elif arbre.valeur=="/":
        return evaluer(arbre.gauche)/evaluer(arbre.droit)
    elif arbre.valeur=="**" or arbre.valeur=="^":
        return evaluer(arbre.gauche)**evaluer(arbre.droit)
    else:
        return arbre.valeur

arbre2=ArbreBinaire("/")
arbre2.ajoutgauche(10)
arbre2.ajoutdroit("-")
arbre2.droit.ajoutgauche(8)
arbre2.droit.ajoutdroit(6)

#Exercice 32 :

class File:
    def __init__(self):
        self.tablo = []

    def pousse(self, data):
        self.tablo.insert(0,data)

    def extraire(self):
        return self.tablo.pop()

    def vide(self):
        if self.tablo==[]:
            return True
        else:
            return False

    def nonvide(self):
        if self.tablo!=[]:
            return True
        else:
            return False

def parcourslargeur(arbre):
    if arbre==None:
        pass
    else:
        file=File()
        file.pousse(arbre)
        while file.nonvide():
            element=file.extraire()
            if element!=None:
                print(element.valeur)
                file.pousse(element.gauche)
                file.pousse(element.droit)


























