
#6. Exercice:

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

def caractereDansPile(texte):
    assert type(texte)==str
    p=Pile()
    for caractere in texte:
        p.push(caractere)
    return p

def nbEspace(texte):
    resultat=0
    while texte.nonvide():
        x=texte.pop()
        if x==" ":
            resultat+=1
    return resultat

#7. Exercice:

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

#8. Exercice:

def extraire(un_texte):
    assert type(un_texte)==str
    f=File()
    for caractere in un_texte:
        f.pousse(caractere)
    return f

def voyelle(une_file):
    while une_file.nonvide():
        x=une_file.extraire()
        if x.lower() in ["a","e","i","o","u","y"]:
            print(x)

def plusGrande(une_file):             #on vérifie qu'une_file est nonvide
    assert une_file.nonvide()         #nouvelle_file contiendra les carac. sans espace
    nouvelle_file=File()              #on extrait carac. d'une_file pour mettre dans une nouvelle file
    while une_file.nonvide():
        x=une_file.extraire()
        if x !=" ":
            nouvelle_file.pousse(x)
    meilleur=nouvelle_file.extraire() #on commence en disant que le premier est le meilleur
    while nouvelle_file.nonvide():    #on défile tous les éléments pour trouver le meilleur
        x=nouvelle_file.extraire()
        if ord(x)>=65 and ord(x)<ord(meilleur):
                minimum=x
    print(meilleur)

#10. Exercice:

class Tableau:

    def __init__(self,taille):
        self.tablo = [None]*taille

    def toutvide(self):
        for element !=None:
            return False
        return True

    def change(self,i,data):
        self.liste[i]=data

    def effacer(self,i):
        self.liste(i)=None

    def connaitre(self,i):
        return self.liste[i]

    def affichetout(self):
        return self.liste

#11. Exercice:

def extraire2(unTexte):
    t=Tableau(len(unTexte))
    for i in range(len(unTexte)):
        t.change(i,unTexte[i])
    return t

def occurence(tablo):




















