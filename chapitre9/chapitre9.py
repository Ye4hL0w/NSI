#DIVISER POUR REGNER

# Exercice 2 :

def listealea(taille,petit,grand):
    liste=[]
    for i in range(taille):
        liste.append(randint(petit,grand))
    return liste

# def recherche(liste,valeur):
#     if len(liste)==1:
#         return liste[0]==valeur
#     else:
#         return recherche(liste[:len(liste)//2],valeur)+recherche(liste[len(liste)//2:],valeur)

def recherche(liste,valeur):
    if len(liste)==1:
        if liste[0]==valeur:
            return 1
        else:
            return 0
    else:
        milieu=len(listealea)//2    #indice du milieu de la liste
        partiegauche=liste[:milieu] #indice du milieu de la liste
        partiedroite=liste[milieu:] #première moitié de la liste
        nbAGauche=recherche(partiegauche,valeur)    #on compte le nombre de fois ou le nb est présent dans la première moitié gauche
        nbADroite=recherche(partiedroite,valeur)     #on compte le nombre de fois ou le nb est présent dans la première moitié droite
        return nbAGauche+nbADroite#on retourne la somme

#Exercice 4 fusion :

import random

def listealea(n,mini,maxi):
    liste=[]
    for i in range(n):
        liste.append(random.randint(mini,maxi))
    return liste

def fusion(liste1,liste2):#APPRENDRE PAR COEUR
    assert type(liste1)==list
    assert type (liste2)==list
    listefinale=[]                  #liste qui sera retournée 
    while liste1!=[] and liste2!=[]:#tant qu'il y a des éléments dans les 2 listes
        if liste1[0]<liste2[0]:     #si c'est bien dans la liste 1 qu'il y a l'élément le plus petit
            mini=liste1.pop(0)
        else:                       #si c'est bien dans la liste 2 qu'il y a l'élément le plus petit
            mini=liste2.pop(0)
        listefinale.append(mini)    #on ajoute à la liste retournée
    if liste1==[]:                  #s'il reste des éléments dans la liste2
        while liste2!=[]:           #on la vide
            mini=liste2.pop(0)
            listefinale.append(mini)
    else:                           #s'il reste des éléments dans la liste1
        while liste1!=[]:           #on la vide
            mini=liste1.pop(0)
            listefinale.append(mini)
    return listefinale              #fini

def fusionCurseur(liste1,liste2):
    assert type(liste1)==list
    assert type(liste2)==list
    listefinale=[] #liste qui sera retournée
    curseur1=0 #curseur pour la liste 1
    curseur2=0 #curseur pour la liste 2
    while curseur1<len(liste1) and curseur2<len(liste2): # tant qu'on est pas arrivé au bout d'une liste
        if liste1[curseur1]<liste2[curseur2]: #si c'est dans la liste 1 qu'il y a l'élément le plus petit 
            mini=liste1[curseur1]
            curseur1+=1
        else: #si c'est dans la liste 2 qu'il y a l'élément le plus petit 
            mini=liste2[liste2]
            curseur2+=1
        listefinale.append(mini) #on ajoute à la liste retournée
    if curseur1==len(liste1):  # s'il reste des éléments à mettre dans la liste 2
        while curseur2<len(liste2):
            curseur+=1
            listefinale.append(mini)
    else: #s'il reste des éléments à mettre dans la liste 1
        while curseur1<len(liste1):
            mini=liste1[curseur1]
            curseur1+=1
            listefinale.append(mini)
    return listefinale #fini

#Exercice 5 tri fusion :

def triparfusion(liste): #APPRENDRE PAR COEUR BAC
    if len(liste)<=1:
        return liste
    else:
        moitie=len(liste)//2 # curseur milieu
        gauche=triparfusion(liste[:moitie]) # relance moitié gauche
        droite=triparfusion(liste[moitie:]) # relance moitié droite
        return fusion(gauche,droite) # on fusionne

def triFusionUP(liste):
    while len(liste)!=1 or liste!=[]:
        liste1=liste[0:len(liste)//2]
        liste2=liste[len(liste)//2:len(liste)]
        return fusion(triFusion(liste1),triFusion(liste2))
    return liste
        
def triparfusionVersionHARDMODE(liste):
    if len(liste)<=1:
        return liste
    else:
        moitié=len(liste)//2
        return fusion(triparfusion(liste[:moitié]),triparfusion(liste[moitié:]))        

def triparfusionVersionVeryHARDMODE(liste):
    if len(liste)<=1:
        return liste
    else:
        return fusion(triparfusion(liste[:len(liste)//2]),triparfusion(liste[len(liste)//2:]))    

def triparfusionVersionGODMODE(liste):
    return liste if len(liste)<=1 else fusion(triparfusion(liste[:len(liste)//2]),triparfusion(liste[len(liste)//2:])) 
