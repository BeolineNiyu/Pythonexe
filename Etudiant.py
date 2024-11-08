
etudiants = []


def ajouter_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    etudiants.append(nom)
    print(f"Étudiant '{nom}' ajouté avec succès.")


def afficher_etudiants():
    if etudiants:
        print("Liste des étudiants :")
        for i, etudiant in enumerate(etudiants, 1):
            print(f"{i}. {etudiant}")
    else:
        print("Aucun étudiant trouvé.")


def supprimer_etudiant():
    nom = input("Entrez le nom de l'étudiant à supprimer : ")
    if nom in etudiants:
        etudiants.remove(nom)
        print(f"Étudiant '{nom}' supprimé avec succès.")
    else:
        print(f"L'étudiant '{nom}' n'existe pas dans la liste.")


def rechercher_etudiant():
    nom = input("Entrez le nom de l'étudiant à rechercher : ")
    if nom in etudiants:
        print(f"L'étudiant '{nom}' a été trouvé.")
    else:
        print(f"L'étudiant '{nom}' n'existe pas dans la liste.")


def menu():
    while True:
        print("\nMenu :")
        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Supprimer un étudiant")
        print("4. Rechercher un étudiant")
        print("5. Quitter")
        
        choix = input("Choisissez une option (1-5) : ")
        
        if choix == '1':
            ajouter_etudiant()
        elif choix == '2':
            afficher_etudiants()
        elif choix == '3':
            supprimer_etudiant()
        elif choix == '4':
            rechercher_etudiant()
        elif choix == '5':
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 5.")


menu()
