class JeuVideo:
    def __str__(self):
        texteAffichage = self.titre + "\n"
        texteAffichage += "Multijoueur : " + str(self.isMultijoueur()) + "\n"
        texteAffichage += "Plateformes : " + str(self.plateformes) + "\n"
        return texteAffichage

    def __init__(self, titre, plateformes, multijoueur):
        self.titre = titre
        self.plateformes = plateformes
        self.multijoueur = multijoueur

    def addPlateforme(self, console):
        if not(console in self.plateformes):
            self.plateformes.append(console)

    def removePlateforme(self, console):
        if console in self.plateformes:
            self.plateformes.remove(console)

    def isOnPlateforme(self, console):
        return console in self.plateformes

    def isMultijoueur(self):
        return self.multijoueur


mario64 = JeuVideo("Mario 64", ["N64", "DS", "Switch"], False)
mario64.titre
mario64.isMultijoueur()
mario64.addPlateforme("PS4")
mario64.isOnPlateforme("Switch")
mario64.removePlateforme("PS4")
mario64.isOnPlateforme("PS4")
mario64 = JeuVideo("Mario 64", ["N64", "DS", "Switch"], False)
print(mario64)
