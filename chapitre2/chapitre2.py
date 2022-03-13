'''Chapitre 2:'''

#exercice 2
def diviseur(n):
    if type(n)!=int:
        return False
    if n<1:
        return False
    liste=[]
    for i in range(1,n+1):
        if n%i==0:
            liste.append(i)
    return liste

#exercice 5

"""
Programme PGCD qui prend en argument deux nombres entiers et qui ne bug pas
"""

def pgcdOpti(m,n):
    assert type(m)==int                 #assertion que m est un int
    assert type(n)==int                 #assertion que n est un int
    assert m>=1                         #assertion que m>=1
    assert n>=1                         #assertion que n>=1
    sortie=1                            #sortie contiendra le PGCD
    for i in range(2,min(m,n)+1):       #pour les nombres de 2 à min(m,n)
        if m%i==0 and n%i==0:           #si i est un diviseur de m et n
            sortie=i                    #on stocke i dans sortie
    return sortie

#exercice 6

"""
fonction retournant la decomposition en facteur premier d'un integer n>=2 sous
forme d'une liste d'int
"""

def decompFacteurPremiers(n):
    assert type(n)==int
    assert n>=2
    liste=[]
    diviseur=2
    while not(EstPremier(n)):
        if n%diviseur==0:
            liste.append(diviseur)
            n=n//diviseur+=1
        else:
            diviseur+=1


























