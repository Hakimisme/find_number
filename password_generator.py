import random

alphabet_minuscule = "abcdefghijklmnopqrstuvwxyz"
alphabet_majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombre = "0123456789"
caractere = "!#$%&()*+,-./:;<=>?@][^_`{|}~"

def generate():
    longueur_minuscule = int(input("Donner la longueur de lettre minuscule que vous souhaitez : "))
    longueur_majuscule = int(input("Donner la longueur de lettre majuscule que vous souhaitez : "))
    longueur_nombre = int(input("Donner la longueur de nombre que vous souhaitez : "))
    longueur_caractere = int(input("Donner la longueur de carctere spéciaux que vous souhaitez : "))

    lettre_minuscule = "".join(random.sample(alphabet_minuscule, longueur_minuscule))
    lettre_majuscule = "".join(random.sample(alphabet_majuscule, longueur_majuscule))
    lettre_nombre = "".join(random.sample(nombre, longueur_nombre))
    lettre_caractere = "".join(random.sample(caractere, longueur_caractere))



    print(lettre_minuscule+lettre_majuscule+lettre_nombre+lettre_caractere)

generate()