while True:
    print("Nouveau joueur ?")
    if input() == "non":
        print("Au revoir !")
        break
    else:
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        age = int(input("Âge : "))

        print("Vous voulez créer une boulangerie ou un café ?")
        choix = input()
        if choix == "boulangerie":
            argent = 50000
        elif choix == "café":
            argent = 100000
        else:
            print("Choix invalide !")
            continue

        print("Veuillez déterminer vos performances, le nombre d'employés et le nombre de machines.")
        performances = int(input("Performances : "))
        nb_employes = int(input("Nombre d'employés : "))
        nb_machines = int(input("Nombre de machines : "))
        salaire_employe = 1000
        prix_matiere_premiere = 2100
        prix_equipement = 15000

        print("Veuillez déterminer le nombre de matières premières.")
        nb_farine = int(input("Nombre de farine : "))
        nb_graine = int(input("Nombre de grains de café : "))
        nb_fruits = int(input("Nombre de fruits : "))
        nb_viande = int(input("Nombre de viande : "))
        nb_matieres_premieres = nb_farine + nb_graine + nb_fruits + nb_viande
        print("Nombre de matières premières :", nb_matieres_premieres)

        fonds = argent - performances - nb_employes*salaire_employe - nb_machines*prix_equipement - nb_matieres_premieres*prix_matiere_premiere
        print("Actuellement, vos fonds sont de :", fonds)

        for i in range(3):
            print("Le jeu commence maintenant ! Veuillez sélectionner l'événement 01, 02 ou 03")
            evenement = input()
            if evenement == "01":
                print("Cet événement est la diminution des prix des matières premières")
                fonds += 6000
                print("Nouveaux fonds :", fonds)
            elif evenement == "02":
                print("Cet événement est l’augmentation des prix de l’énergie")
                fonds -= 100
                print("Nouveaux fonds :", fonds)
            elif evenement == "03":
                print("Cet événement est nouveaux adversaires")
                fonds -= 50
                print("Nouveaux fonds :", fonds)
            else:
                print("Choix invalide !")
                continue

        score = fonds - 30000
        print("Score :", score)
        if score > 0:
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu !")

