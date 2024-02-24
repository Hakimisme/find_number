import random

def lanceur_de():
    nb = input("Trouve le chiffre entre 0 et 10 : ")
    x = str(random.randint(0,10))

    if nb == x:
        print("Bravo vous avez trouvé le bon résultat qui est : " + nb)
    else: 
        print("Malheureusement vous n'avez pas trouvé le bon chiffre, le chiffre qui était à deviner est " + x + " mais vous vous avez dis : " + nb)

lanceur_de()