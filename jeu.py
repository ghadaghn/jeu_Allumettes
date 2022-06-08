def jeu_ordi(nb_allum, prise_max):
    prise=0
    s = prise_max + 1
    t = (nb_allum - s) % (prise_max + 1)
    while (t != 0):
        s -= 1
        t = (nb_allum - s) % (prise_max + 1)
        prise = s - 1
    if (prise == 0):
        prise = 1
    print("l'ordi en prend : ", prise)
    return prise









#le nombre d'allumettes que je prend
def jeu_moi(nb_allu_max,nb_allu_rest):
    prise = 0
    if(nb_allu_max>nb_allu_rest):#si le nombre d'allumete restante est inférieure au nombre max on pourra pas tirer le nombre max
        nbr=nb_allu_rest
    else:
        nbr=nb_allu_max
    while (prise <= 0 or prise > nb_allu_max or prise>nb_allu_rest):
        try:
            print("Vous pouvez tirer entre 1 et ",nbr," allumettes")
            prise = int(input("combien d'allumette voulez-vous tirer ?"))
        except:
            print("saisie incorrecte")
    return prise





# afficher n allumettes
def afficher_allumettes(n):
    a = n
    print("il reste ",n," allumettes")
    while (a != 0):
        a -= 1
        if a == 0:
            print("o")
        else:
            print("o", end=' ')

    a = n
    while (a != 0):
        a -= 1
        print("|", end=' ')
    print("")



#nb_allu_rest le nombre d'allumettes restantes
#nb_allu_max le maximum d'allumette qu'on peut tirer
#qui celui qui commence le jeu
def jeu(nb_allu_rest,nb_allu_max,qui):
    while (nb_allu_rest != 0):
        if(qui==0):
            qui = 1
            nb_allu_rest-=jeu_moi(nb_allu_max,nb_allu_rest)
            if(nb_allu_rest==0):
                print("le pc a gangé")
            else:
                afficher_allumettes(nb_allu_rest)

        else:
            qui = 0
            nb_allu_rest -= jeu_ordi(nb_allu_rest, nb_allu_max)
            if (nb_allu_rest == 0):
                print("j'ai gangé")
            else:
                afficher_allumettes(nb_allu_rest)


def main():
    nb_max_d = 0
    nb_allu_max = 0
    nb_allu_rest = 0
    prise = 0
    qui = -1
    while (nb_max_d < 10 or nb_max_d > 60):
        try:
            nb_max_d = int(input("Entrez un nombre max d'allumette au depart entre 10 et 50."))
        except:
            print("saisie incorrecte")
    nb_allu_rest = nb_max_d


    while (nb_allu_max <= 0 or nb_allu_max > nb_max_d):
        try:
            print("nombre d'allumettes max doit etre entre 1 et ",nb_max_d, "allumettes")
            nb_allu_max = int(input("Entrez un nombre max d'allumette que l'on peut tirer dans un tours"))
        except:
            print("saisie incorrecte")

    print("")
    qui = int(input("Qui commence? 1=PC   0=moi"))
    print("")

    afficher_allumettes(nb_allu_rest)
    jeu(nb_allu_rest,nb_allu_max,qui)


if __name__ == "__main__":
    main()