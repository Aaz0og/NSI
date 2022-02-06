from random import choice


def jeu():
    actions = ["Pierre", "Papier", "Sciseaux"]
    repactions = ["r", "R", "S", "s", "p", "P"]
    clean = 0
    rep = input("Qu'elle action ? R-P-S: ")
    while rep not in repactions:
        rep = input("Qu'elle action (Tu sais pas lire?)? R-P-S: ")
    bot = str(choice(actions))
    if rep == "R" or "r":
        if bot == "Sciseaux":
            return print("Vous avez gagné ! Le robot à fait", bot)
        if bot == "Papier":
            return print("Vous avez perdu le robot a fait", bot)
        if bot == "Pierre":
            return print("Egalité")
    if rep == "P" or "p":
        if bot == "Sciseaux":
            return print("Vous avez perdu ! Le robot à fait", bot)
        if bot == "Pierre":
            return print("Vous avez gagné le robot a fait", bot)
        if bot == "Papier":
            return print("Egalité")
    if rep == "S" or "s":
        if bot == "Papier":
            return print("Vous avez gagné ! Le robot à fait", bot)
        if bot == "Pierre":
            return print("Vous avez perdu le robot a fait", bot)
        if bot == "Papier":
            return print("Egalité")


jeu()
