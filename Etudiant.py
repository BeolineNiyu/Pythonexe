
etudiants = []

def ajouter_etudiant():
    id = int(input("Entrez l'ID de l'étudiant : "))
    nom = input("Entrez le nom de l'étudiant : ")
    prenom = input("Entrez le prénom de l'étudiant : ")
    email = input("Entrez l'email de l'étudiant : ")
    etudiant = {"id": id, "nom": nom, "prenom": prenom, "email": email}
    etudiants.append(etudiant)
    print("Étudiant ajouté avec succès.")


def afficher_etudiants():
    if etudiants:
        print("\nListe des étudiants :")
        for etudiant in etudiants:
            print(f"ID : {etudiant['id']}, Nom : {etudiant['nom']}, Prénom : {etudiant['prenom']}, Email : {etudiant['email']}")
    else:
        print("\nAucun étudiant dans la liste.")


def rechercher_etudiant():
    critere = input("Rechercher par (id/nom) : ")
    valeur = int(input("Entrez la valeur à rechercher : "))
    if critere == "id":

        etudiant_resultat = [ etudiant for etudiant in etudiants if etudiant['id'] == valeur ]
        print(f"Étudiant trouvé : {etudiant_resultat}")
        return
    # print("Étudiant non trouvé.")

    if rechercher_etudiant:
         input("Le nom doit commencer par une majuscule." )
         print(" ce n'est pas Le nom doit commencer par une majuscule : ")

    else:
        print("Le nom de l'étudiant est valide.")


def supprimer_etudiant():
    critere = input("Supprimer par (id/nom) : ")
    valeur = input("Entrez la valeur à supprimer : ")
    if critere == "id":
                 
            etudiant_supprimer = [ etudiant for etudiant in etudiants if etudiant['id'] == valeur ]
            print("Étudiant supprimé avec succès.")
            return
   # print("Étudiant non trouvé.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Supprimer un étudiant")
        print("5. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == '1':
            ajouter_etudiant()
        elif choix == '2':
            afficher_etudiants()
        elif choix == '3':
            rechercher_etudiant()
        elif choix == '4':
            supprimer_etudiant()
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")


menu()

    



    
