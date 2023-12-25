# Créé par Isaac, le 14/10/2021 en Python 3.7

class Marienbad(object):
    """ 
    Attributs : 
        --> tas de type tuple d'entiers
        --> allumettes de type liste d'entiers
        --> joueurs de type tuple de chaînes de caractères
        --> tour des joueurs
    Méthodes :  
        --> constructeur des valeurs (joueur1, joueur2)
        --> affiche l'état du jeu
        --> renvoie un booléen si c'est possible d'enlever n allumettes
        --> met à jour les tas en enlevant n allumettes dans le tas
        --> renvoie un booléen si le jeu est fini
    """
    def __init__(self, joueurs):
        """Constructeur avec valeurs par défaut."""
        self.tas = (1, 2, 3, 4, 5, 6)
        self.allumettes = [1, 3, 5, 7, 9, 11]  
        self.joueurs = joueurs
        self.tour = 0

    def __str__(self):
        """Affiche l'état du jeu."""
        return (f"\n{'~'*25}\n"
                f"rangée : {self.tas}\n"
                f"allumettes : {self.allumettes}\n"  
                f"{'~'*25}\n"
                f"C'est à {self.joueurs[self.tour]} de jouer :")

    def verifie(self, tas, nombre_allumettes):
        """Retourne True si le coup proposé est valide, sinon False."""
        return True if self.allumettes[tas - 1] >= nombre_allumettes else False  

    def enlever(self, tas, nombre_allumettes):
        """Met à jour les tas d'allumettes."""
        if self.verifie(tas, nombre_allumettes):
            self.allumettes[tas - 1] -= nombre_allumettes  
            self.tour = 1 if self.tour % 2 == 0 else 0
            print(f"\tLa rangée {tas} ne comporte que {self.allumettes[tas - 1]} allumette(s) !")

    def termine(self):
        """Retourne True si le jeu est terminé, sinon False."""
        return sum(self.allumettes) == 0

# PROGRAMME PRINCIPAL
joueurs = input("Noms des deux joueurs : ").split()  
marienbad = Marienbad(joueurs)
print(marienbad)
while not marienbad.termine():
    numero_tas = int(input("\tNuméro de la rangée : "))
    nombre_allumettes = int(input("\tNombre d'allumettes à enlever : "))
    marienbad.enlever(numero_tas, nombre_allumettes)
    print(marienbad)

print(f"\n*** {marienbad.joueurs[1 - marienbad.tour]} gagne ! ***")  