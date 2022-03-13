class Pile:
    def __init__(self):
        self.tablo = []


    def push(self, data):
        self.tablo.append(data)


    def pop(self):
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

class Tableau:
    def __init__(self,taille):
        self.tablo = [None]*taille

    def toutvide(self):
        for element in self.liste:
            if element!=None:
                return False
            return True

    def change(self,i,data):
        self.liste[i]=data

    def effacer(self,i):
        self.liste[i]=None

    def connaitre(self,i):
        return self.liste[i]

    def affichetout(self):
        return self.liste

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