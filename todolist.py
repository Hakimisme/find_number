# La liste va stocker nos tâches
taches = []

# Fonction qui va nous permettre d'ajouter des tâches à la liste
def ajout_taches(tache):
    taches.append(tache)
    print("Tâche ajoutée avec succès !")

# Fonction pour afficher toutes les tâches
def affiche_taches():
    if taches:
        print("Liste des tâches :")
        for index, tache in enumerate(taches, start=1):
            print(f"{index}. {tache}")
    else:
        print("Aucune tâche n'est enregistrée.")

# Fonction pour supprimer une tâche
def supprimer_taches(index):
    if index > 0 and index <= len(taches):
        del taches[index - 1]
        print("Tâche supprimée avec succès !")
    else:
        print("Index invalide.")

def main():
    while True:
        print("\nMenu :")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        
        choice = input("Choisissez une option : ")

        if choice == "1":
            tache = input("Entrez la tâche à ajouter : ")
            ajout_taches(tache)
        elif choice == "2":
            affiche_taches()
        elif choice == "3":
            index = int(input("Entrez le numéro de la tâche à supprimer : "))
            supprimer_taches(index)
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir à nouveau.")

if __name__ == "__main__":
    main()
