import time

class Catcheur:#ajt catcheur legendaire genre class priovée et systele argent et aussi ne pas choisir le meme mode 2 fois

    def __init__(self):
        nom=self.choixperso()
        self.nom=nom
        #self.pv=pv
        #self.atk=atk
        #self.vitesse=vitesse
        if nom=="JohnCena":
            self.pv=1200
            self.atk=800
            self.vitesse=2
            self.endurance=1000
        elif nom=="RandyOrton":
            self.pv=1300
            self.atk=700
            self.vitesse=2
            self.endurance=1000
        elif nom=="BigShow":
            self.pv=1500
            self.atk=500
            self.vitesse=1
            self.endurance=1000
        elif nom=="ReyMysterio":
            self.pv=1100
            self.atk=900
            self.vitesse=3
            self.endurance=1000

    def choixperso(self):
        print()
        print("1-John Cena")
        print("2-Randy Orton")
        print("3-Big Show")
        print("4-Rey Mysterio")
        print()
        choix=input("Quel catcheur souhaites-tu choisir ?")
        if choix == "1" or choix=="John Cena":
            p="JohnCena"
        elif choix == "2" or choix=="Randy Orton":
            p="RandyOrton"
        elif choix == "3" or choix=="Big Show":
            p="BigShow"
        elif choix == "4" or choix=="Rey Mysterio":
            p="ReyMysterio"
        else:
            print("erreur")
        return p

    def recup_perso(self,joueur,catcheur):
        joueur.pv=catcheur.pv
        joueur.atk=catcheur.atk
        joueur.vitesse=catcheur.vitesse

    def recup_pseudo(self):
        return self.nom

    def recup_pv(self):
        print(self.pv)

    def recup_endurance(self):
        print(self.endurance)

    def recup_atk(self):
        return self.atk

    def recup_vitesse(self):
        return self.vitesse

def combat(finish,objspec1,choixatk,choixdef,c1,c2):
    if finish==True:
        c2.pv-=c2.pv
        c1.endurance-=100
        print()
        print()
        print(c1.nom,"sort du ring..")
        time.sleep(2)
        print()
        print(c1.nom,"va sous le ring..")
        print()
        time.sleep(2)
        print(c1.nom,"remonte..")
        print()
        time.sleep(0.5)
        print(c1.nom,"possède quelque chose dans les mains😲")
        print()
        time.sleep(2)
        print()
        time.sleep(1)
        item=""
        if objspec1=="1" or objspec1=="Chaise":
            item="UNE CHAISE"
        elif objspec1=="2" or objspec1=="Table":
            item="UNE TABLE"
        elif objspec1=="3" or objspec1=="Echelle":
            item="UNE ECHELLE"
        elif objspec1=="4" or objspec1=="Escabeau":
            item="UN ESCABEAU"
        else:
             item="UNE CHAISE"
        print(" il charge AVEC",item,"...")
        time.sleep(2)
        print("vous avez mis",c2.nom,"KO")
        time.sleep(2)
        print()
        print()
        c2.pv=0
        print(c2.nom,"a donc 0 pv")
        print()
        print()
        if c1.pv==0 or c2.pv==0:
            print("Le round est terminé")
            scorec1=0
            scorec2=0
            if c1.pv<c2.pv:
                print("Bravo à",c2.nom)
                print("Vous avez mis K-O",c1.nom)
                scorec1+=1
            else:
                print("Bravo à",c1.nom)
                print("Vous avez mis K-O",c2.nom)
                scorec1+=1
            if scorec1>scorec2:
                print(c1.nom,"gagne,voici le score:")
                print(scorec1,"-",scorec2)
            else:
                print(c2.nom,"gagne, voici le score")
                print(scorec2,"-",scorec1)
            rejouer=input("Souhaitez-vous relancer une partie ?")
            if rejouer=="Oui" or rejouer=="oui":
                jouer()
            else:
                print("Au revoir, à bientôt")
    else:
        if choixatk=="1" or choixatk=="2" or choixatk=="DirectDroit" or choixatk=="DirectGauche" :
            if choixdef=="3" or choixdef=="Aucun":
                c2.pv-=c1.atk//4*c1.vitesse
                c1.endurance-=100
                print()
                print()
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//4*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                print(c2.nom)
                print("a donc",c2.pv,"pv")
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
            elif choixdef=="1" or choixdef=="Poing":
                c2.pv-=c1.atk//5*c1.vitesse
                c1.endurance-=100
                c2.endurance-=200
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//5*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                dimi=c1.atk//4*c1.vitesse-c1.atk//5*c1.vitesse
                print(c2.nom)
                print("a diminué l'effet de l'attaque de",dimi,"grâce aux poings" )
                time.sleep(2)
                print("il a donc",c2.pv,"pv")
                time.sleep(1)
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
            elif choixdef=="2" or choixdef=="Esquive":
                if c2.endurance>=499:
                    if c2.vitesse<=1:
                        c2.pv-=c1.atk//6*c1.vitesse
                        c1.endurance-=100
                        c2.endurance-=499
                        print()
                        print(c1.nom,"attaque..")
                        print()
                        time.sleep(2)
                        print(c2.nom,"esquive")
                        time.sleep(1)
                        print()
                        print("vous avez infligé",c1.atk//6*c1.vitesse,"dégâts")
                        time.sleep(2)
                        print()
                        print()
                        dimi=c1.atk//4*c1.vitesse-c1.atk//6*c1.vitesse
                        print(c2.nom)
                        print("a diminué l'effet de l'attaque de",dimi,"grâce à l'esquive" )
                        time.sleep(2)
                        print()
                        print("Il a donc",c2.pv,"pv")
                        time.sleep(1)
                        print()
                        print()
                        if c1.pv<0 or c2.pv<0:
                            jeu=False
                    elif c2.vitesse>=2:
                        c1.endurance-=100
                        c2.endurance-=499
                        print()
                        print(c1.nom,"attaque..")
                        print()
                        time.sleep(2)
                        print(c2.nom,"esquive")
                        time.sleep(1)
                        print()
                        print("vous avez infligé",0,"dégat" )
                        print()
                        print()
                        dimi=c1.atk//4*c1.vitesse
                        print(c2.nom)
                        print("a diminué l'effet de l'attaque de",dimi,"grâce à l'esquive" )
                        time.sleep(2)
                        print()
                        print("Il a donc",c2.pv,"pv")
                        time.sleep(1)
                        print()
                        print()
                        if c1.pv<0 or c2.pv<0:
                            jeu=False
                else:
                    print("Désolé",c2.nom,"ton endurance est insuffisante pour effuctuer une esquive")
            else:
                c2.pv-=c1.atk//4*c1.vitesse
                c1.endurance-=100
                print()
                print()
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//4*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                print(c2.nom)
                print("a donc",c2.pv,"pv")
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
        elif choixatk=="2" or choixatk=="3" or choixatk=="KickDroit" or choixatk=="KickGauche":
            if choixdef=="3" or choixdef=="Aucun":
                c2.pv-=c1.atk//2*c1.vitesse
                c1.endurance-=250
                print()
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//2*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                print(c2.nom)
                print("a donc",c2.pv,"pv")
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
            elif choixdef=="1" or choixdef=="Poing":
                c2.pv-=c1.atk//3*c1.vitesse
                c1.endurance-=250
                c2.endurance-=200
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//3*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                dimi=c1.atk//2*c1.vitesse-c1.atk//3*c1.vitesse
                print(c2.nom)
                print("a diminué l'effet de l'attaque de",dimi,"grâce aux poings" )
                time.sleep(2)
                print("il a donc",c2.pv)
                time.sleep(1)
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
            elif choixdef=="2" or choixdef=="Esquive":
                if c2.endurance>=499:
                    if c2.vitesse<=1:
                        c2.pv-=c1.atk//6*c1.vitesse
                        c1.endurance-=100
                        c2.endurance-=499
                        print(c1.nom,"attaque..")
                        print()
                        time.sleep(2)
                        print(c2.nom,"esquive")
                        time.sleep(1)
                        print()
                        print("vous avez infligé",c1.atk//6*c1.vitesse,"dégâts car vous n'avez pas assez de points de vitesse pour esquiver la totalité du coup")
                        time.sleep(4)
                        print()
                        print()
                        dimi=c1.atk//2*c1.vitesse-c1.atk//6*c1.vitesse
                        print(c2.nom)
                        print("a diminué l'effet de l'attaque de",dimi,"grâce à l'esquive" )
                        time.sleep(2)
                        print("il a donc",c2.pv,"pv")
                        time.sleep(1)
                        print()
                        print()
                        if c1.pv<0 or c2.pv<0:
                            jeu=False
                    elif c2.vitesse>=2:
                        c1.endurance-=100
                        c2.endurance-=499
                        print(c1.nom,"attaque..")
                        print()
                        time.sleep(2)
                        print(c2.nom,"esquive")
                        time.sleep(1)
                        print()
                        print("vous avez infligé",0,"dégat" )
                        print()
                        print()
                        dimi=c1.atk//2*c1.vitesse
                        print(c2.nom)
                        print("a diminué l'effet de l'attaque de",dimi,"grâce à l'esquive" )
                        time.sleep(2)
                        print("il a donc",c2.pv,"pv")
                        time.sleep(1)
                        print()
                        print()
                        if c1.pv<0 or c2.pv<0:
                            jeu=False
                else:
                    print("Désolé",c2.nom,"il ton endurance est insuffisante pour effuctuer une esquive")
            else:
                c2.pv-=c1.atk//2*c1.vitesse
                c1.endurance-=250
                print()
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//2*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                print(c2.nom)
                print("a donc",c2.pv,"pv")
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
        else:
            if choixdef=="3" or choixdef=="Aucun":
                c2.pv-=c1.atk//4*c1.vitesse
                c1.endurance-=100
                print()
                print()
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//4*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                print(c2.nom)
                print("a donc",c2.pv,"pv")
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
            elif choixdef=="1" or choixdef=="Poing":
                c2.pv-=c1.atk//5*c1.vitesse
                c1.endurance-=100
                c2.endurance-=200
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//5*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                dimi=c1.atk//4*c1.vitesse-c1.atk//5*c1.vitesse
                print(c2.nom)
                print("a diminué l'effet de l'attaque de",dimi,"grâce aux poings" )
                time.sleep(2)
                print("il a donc",c2.pv,"pv")
                time.sleep(1)
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False
            elif choixdef=="2" or choixdef=="Esquive":
                if c2.endurance>=499:
                    if c2.vitesse<=1:
                        c2.pv-=c1.atk//6*c1.vitesse
                        c1.endurance-=100
                        c2.endurance-=499
                        print()
                        print(c1.nom,"attaque..")
                        print()
                        time.sleep(2)
                        print(c2.nom,"esquive")
                        time.sleep(1)
                        print()
                        print("vous avez infligé",c1.atk//6*c1.vitesse,"dégâts")
                        time.sleep(2)
                        print()
                        print()
                        dimi=c1.atk//4*c1.vitesse-c1.atk//6*c1.vitesse
                        print(c2.nom)
                        print("a diminué l'effet de l'attaque de",dimi,"grâce à l'esquive" )
                        time.sleep(2)
                        print()
                        print("Il a donc",c2.pv,"pv")
                        time.sleep(1)
                        print()
                        print()
                        if c1.pv<0 or c2.pv<0:
                            jeu=False
                    elif c2.vitesse>=2:
                        c1.endurance-=100
                        c2.endurance-=499
                        print()
                        print(c1.nom,"attaque..")
                        print()
                        time.sleep(2)
                        print(c2.nom,"esquive")
                        time.sleep(1)
                        print()
                        print("vous avez infligé",0,"dégat" )
                        print()
                        print()
                        dimi=c1.atk//4*c1.vitesse
                        print(c2.nom)
                        print("a diminué l'effet de l'attaque de",dimi,"grâce à l'esquive" )
                        time.sleep(2)
                        print()
                        print("Il a donc",c2.pv,"pv")
                        time.sleep(1)
                        print()
                        print()
                        if c1.pv<0 or c2.pv<0:
                            jeu=False
                else:
                    print("Désolé",c2.nom,"ton endurance est insuffisante pour effuctuer une esquive")
            else:
                c2.pv-=c1.atk//4*c1.vitesse
                c1.endurance-=100
                print()
                print()
                print(c1.nom,"attaque..")
                time.sleep(2)
                print()
                print("vous avez infligé",c1.atk//4*c1.vitesse,"dégâts")
                time.sleep(2)
                print()
                print()
                print(c2.nom)
                print("a donc",c2.pv,"pv")
                print()
                print()
                if c1.pv<0 or c2.pv<0:
                    jeu=False




def jouer():
    finish=False
    jeu=True
    print("     ---Bienvenue dans la WWE---")
    regles=input("Souhaitez-vous (re)lire les règles ?")
    if regles=="oui" or regles=="Oui":
        print("Voici les règles du jeux :")
        print()
        print()
        print("C'est un jeu de 1v1, les deux joueurs devront choisir le catcheur de leur choix en début de partie.")
        print()
        time.sleep(4)
        print("- Chaque personnage à 2000 pts qui sont attribués différemment entre les points d'attaque et les points de vie.")
        print()
        print("- La vitesse varie de 1 à 3, le résultat de l’attaque est multiplié par la vitesse.")
        print()
        print("- Chaque personnage a 1000 pts d’endurance.")
        print()
        time.sleep(10)
        print("- Les compétences sont :")
        print("                         -Pv")
        print("                         -Puissance")
        print("                         -Vitesse")
        print("                         -Endurance")
        print()
        print()
        time.sleep(4)
        print("Voici les caractéristiques des peronnages :")
        print()
        time.sleep(2)
        print("-John Cena :")
        print()
        print("             -Pv : 1200")
        print("             -Puissance : 800")
        print("             -Vitesse : 2")
        print("             -Endurance : 1000")
        print()
        time.sleep(2)
        print("-Randy Orton :")
        print()
        print("             -Pv : 1300")
        print("             -Puissance : 700")
        print("             -Vitesse : 2")
        print("             -Endurance : 1000")
        print()
        time.sleep(2)
        print("-Big Show :")
        print()
        print("             -Pv : 1500")
        print("             -Puissance : 500")
        print("             -Vitesse : 1")
        print("             -Endurance : 1000")
        print()
        time.sleep(2)
        print("-ReyMysterio :")
        print()
        print("             -Pv : 1100")
        print("             -Puissance : 900")
        print("             -Vitesse : 3")
        print("             -Endurance : 1000")
        print()
        print()
        time.sleep(2)
        print("Voici les différents types d'attaques et de défenses :")
        print()
        time.sleep(4)
        print("Les attaques :")
        print("-Poings :")
        print("         -Direct Droit")
        print("         -Direct Gauche")
        print("-Jambes :")
        print("         -Kick Droit")
        print("         -Kick Gauche")
        print()
        time.sleep(4)
        print("Les défenses :")
        print("         -Contre des poings :")
        print("         -Esquive")
        print("         -Aucun")
        time.sleep(3)
        print()
        print("A partir du round 3, le catcheur ayant le plus de points d'endurance se verra capable d'infliger un coup spécial qui finira son adversaire !")
        time.sleep(4)
        print()
        print()
    print("Vous pouvez commencer !")
    c1=Catcheur()
    c2=Catcheur()
    print()
    print("1-Chaise")
    print("2-Table")
    print("3-Echelle")
    print("4-Escabeau")
    print()
    print(c1.nom)
    objspec1=input("Veuillez choisir votre objet ! ")
    print()
    print(c2.nom)
    objspec2=input("Veuillez choisir votre objet ! ")
    i=0
    while jeu:
        i+=1
        print("Round",i)
        if i==3:
            finish=True
            if c1.endurance>=c2.endurance:
                combat(finish,objspec1,choixatk,choixdef,c1,c2)
            elif c2.endurance<c2.endurance:
                combat(finish,objspec1,choixatk,choixdef,c2,c1)
        else:
            finish=False
        print()
        print("C'est au tour de",c1.nom,"veuillez choisir votre attaque")
        print()
        choixatk=input("1-DirectDroit, 2-DirectGauche, 3-KickDroit, 4-KickGauche")
        print()
        print(c2.nom,"Veuillez choisir votre défense")
        time.sleep(1)
        print()
        conseil=input("voulez-vous des conseils concernant votre défense ?")
        if conseil=="oui" or conseil=="Oui":
            print()
            guider_defense(choixatk,c1,c2)
        print()
        choixdef=input("1-Poing 2-Esquive 3-Aucun")
        combat(finish,objspec1,choixatk,choixdef,c1,c2)
        print(c1.nom)
        dmdpv=input("Voulez-vous voir vos pv ?")
        if dmdpv=="Oui" or dmdpv=="oui":
            Catcheur.recup_pv(c1)
        print()
        dmded=input("et votre endurance ?")
        if dmdpv=="Oui" or dmdpv=="oui":
            Catcheur.recup_endurance(c1)
        print()
        print(c2.nom)
        dmdpv=input("Voulez-vous voir vos pv ?")
        if dmdpv=="Oui" or dmdpv=="oui":
            Catcheur.recup_pv(c2)
        print()
        dmded=input("et votre endurance ?")
        if dmdpv=="Oui" or dmdpv=="oui":
            Catcheur.recup_endurance(c2)
        print()
        if c1.pv<0 or c2.pv<0 or c1.endurance<0 and c2.endurance<0:
            jeu=False
            break
        print()
        print("C'est au tour de",c2.nom,"veuillez choisir votre attaque")
        print()
        choixatk=input("1-DirectDroit, 2-DirectGauche, 3-KickDroit, 4-KickGauche")
        print(c1.nom)
        print()
        print(c1.nom,"Veuillez choisir votre défense")
        time.sleep(1)
        print()
        conseil=input("voulez-vous des conseils concernant votre défense ?")
        if conseil=="oui" or conseil=="Oui":
            print()
            guider_defense(choixatk,c2,c1)
        print()
        choixdef=input("1-Poing 2-Esquive 3-Aucun")
        combat(finish,objspec2,choixatk,choixdef,c2,c1)
        print(c1.nom)
        if c1.pv<0 or c2.pv<0 or c1.endurance<0 and c2.endurance<0:
            jeu=False
            break
    print("Le combat est terminé")
    scorec1=0
    scorec2=0
    if c1.pv<c2.pv:
        print("Bravo à",c1.nom)
        print("Vous avez mis K-O",c2.nom)
        scorec1+=1
    else:
        print("Bravo à",c2.nom)
        print("Vous avez mis K-O",c1.nom)
        scorec1+=1
    if scorec1>scorec2:
        print(c1.nom,"gagne,voici le score:")
        print(scorec1,"-",scorec2)
    else:
        print(c2.nom,"gagne, voici le score")
        print(scorec2,"-",scorec1)
    rejouer=input("Souhaitez-vous relancer une partie ?")
    if rejouer=="Oui" or rejouer=="oui":
        jouer()
    else:
        print("Au revoir, à bientôt")


def guider_defense(choixatk,c1,c2):
    if choixatk=="1" or choixatk=="2" or choixatk=="DirectDroit" or choixatk=="DirectGauche" :
        print(c1.nom,"s'apprête à infliger :")
        print(c1.atk//4*c1.vitesse,"dégâts si",c2.nom)
        print("ne défend pas.")
        print()
        print("si",c2.nom,"esquive il perdra :")
        if c2.vitesse<=1:
            print(c1.atk//6*c1.vitesse,"pv et 499 d'endurance")
        elif c2.vitesse>=2:
            print("0 pv et 499 d'endurance")

        print("si",c2.nom,"contre avec ses points il perdra :")
        print(c1.atk//5*c1.vitesse,"pv et 200 d'endurance")
    elif choixatk=="2" or choixatk=="3" or choixatk=="KickDroit" or choixatk=="KickGauche":
        print(c1.nom,"s'apprête à infliger :")
        print(c1.atk//2*c1.vitesse,"dégâts si",c2.nom)
        print("ne défend pas.")

        print("si",c2.nom,"esquive il perdra :")
        if c2.vitesse<=1:
            print(c1.atk//6*c1.vitesse,"pv et 499 d'endurance")
        elif c2.vitesse>=2:
            print("0 pv et 499 d'endurance")
        print()
        print("si",c2.nom,"contre avec ses points il perdra :")
        print(c1.atk//3*c1.vitesse,"pv et 200 d'endurance")