# Exercice 2 :

def facRECUR(n):
    assert type(n)==int #on vérifie que n est un int
    assert n>0 # on vérifie que n>0
    if n==1: #condition d'arret
        return 1
    else:
        return n*facRECUR(n-1) #on lance fac(n-1)

def facITERA(n):
    assert type(n)==int
    assert n>0
    produit=1
    for i in range(1,n+1):
        produit=produit*1
    return produit

# Exercice 3 :

def fiboRECUR(n):
    assert type(n)==int
    assert n>0
    if n==1 or n==2:
        return 1
    else:
        return fiboRECUR(n-2)+fiboRECUR(n-1)

def fiboITERA(n):
    assert type(n)==int
    assert n>0
    if n==1 or n==2:
        return 1
    avant_dernier=1
    dernier=1
    fibo_n=2
    for i in range(3,n):
        avant_dernier=dernier
        dernier=fibo_n
        fibo_n=avant_dernier+dernier
    print(fibo_n)

# Exercice 4 :

def compteVoyelleRECUR(texte):
    assert type(texte)==str
    if texte =="":
        return 0
    voyelle["a","e","i","o","u","y","é","è","ê","à","â","î","ï"]
    if len(texte)==1:
        if texte[0].lower() in voyelle:
            return 1
        else:
            return 0
    else:
        caractere=texte[0]
        if caractere.lower() in voyelle:
            return 1+compteVoyelleRECUR(texte[1:])
        else:
            return compteVoyelleRECUR(texte[1:])

def compteVoyelleITERA(texte):
    assert type(texte)==str
    if texte =="":
        return 0
    voyelle["a","e","i","o","u","y","é","è","ê","à","â","î","ï"]
    somme=0
    for caractere in texte:
        if caractere.lower() in voyelle:
            somme+=1
        return somme

# Exercice 5 :

def lapinRECUR(n,adulte=2.,ado=0,enfant=0,fin=True):
    assert type(n)==int
    assert n>=0
    if fin:
        (adulte,ado,enfant)=lapinRECUR(n,adulte,ado,enfant,False)
        return adulte+ado+enfant
    else:
        if n==0:
            return (adulte,edo,enfant)
        else:
            return lapinRECUR(n-1,adulte+ado,enfant,adulte,False)

def lapinITERA(n):
    assert type(n)==int
    assert n>=0
    adulte=2
    ado=0
    enfant=0
    for i in range(n):
        ancien_adulte=adulte
        adulte=adulte+ado
        ado=enfantenfant=ancien_adulte
    return adulte+ado+enfant

# Exercice 6 :

def coeffBinomRECUR(n,p):
    assert type(n)==int
    assert type(p)==int
    assert n>=1 and p>=0 and p<=n
    if n==1:
        return 1
    elif p==0:
        return 1
    elif p==n:
        return 1
    else:
        return coeffBinomRECUR(n-1,p-1)+coeffBinomRECUR(n-1,p)

def coeffBinomITERA(n):
    assert type(n)==int and type(p)==int
    assert n>=1 and p>=0 and p<=n
    return int(factoITERA(n)/(factoITERA(p)*factoITERA(n-p)))











































































































