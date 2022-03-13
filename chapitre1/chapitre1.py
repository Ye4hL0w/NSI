#Chapitre 1

#Exercice 1

def extraire(UnTexte):
    x=[]
    for e in UnTexte:
        x.insert(0,e)
    return x

def voyelle(UneListe):
    v=["a","e","i","o","u","y"]
    for element in UneListe:
        if element in v:
            print(element)

def plusgrande(UneListe):
    x=[]
    for e in UneListe:
        if e!=" ":
            x.insert(0,e)
    minimum=x.pop(-1)
    for element in x:
        if ord(element)>=65:
            if ord(minimum)>ord(element):
                minimum=element
    print(minimum)

#10 Exercice:

def extraire2(UnTexte):
    longueur=len(UnTexte)
    liste = [None]*longueur
    for i in range(longueur):
        liste[i]=UnTexte[i]
    return liste

def occurence(UneListe):
    longueur=len(UneListe)
    liste=[None]*(2*longueur)
    pointeur=0
    for caractere in UneListe:
        if caractere in liste:
            trouve=False
            i=0
            while not(trouve):
                if liste[i]==caractere:
                    liste[i+1]+=1
                    trouve=True
                else:
                    i+=1
        else:
            liste[pointeur]=caractere
            liste[pointeur+1]=1
            pointeur+=2
    if pointeur!=longueur*2:
        liste2=[None]*pointeur
        for i in range(pointeur):
            liste2[i]=liste[i]
        return liste2
    else:
        return liste

#11 Exercice:
#1.

import random
def listealea(n):
    liste=[None]*n
    for i in range(n):
        liste[i] = random.randint(-20,20)
    return liste

#2.

def paire(liste):
    liste2=[None]*len(liste)    #on créé une liste vide de la même taille
    pointeur=0                  #désigne l'emplacemùent à écrire
    for i in range(len(liste)): #on boucle sur les éléments de la liste
        if liste[i]%2==0:       # si le nombre est pair
            liste2[pointeur]=liste[i]   #on remplit liste2
            pointeur+=1         #on décale le pointeur
    liste3=[None]*pointeur      #liste3 contiendra les nombres pairs sans les None
    for i in range(pointeur):
        liste3[i]=liste2[i]     #on asocie les éléments entre liste2 et liste3
    return liste3               #fini!





























