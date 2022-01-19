# Exercice 1
def R(V, aff):
    if aff == 1:
        return print("Distance parcourue par le véhicule en 1sec (temps de réaction donné par l'exrcice)", V / 3.6, "m a", V, "km/h")
    else:
        return V / 3.6


def F(V, aff, mouille):
    if aff == 1 and mouille == False:
        return print("Distance parcourue pendant le temps de freinage", V**2/200, "m a", V, "km/h")

    if aff == 1 and mouille == True:
        return print("Distance parcourue pendant le temps de freinage", (V**2/200)*2, "m a", V, "km/h")

    if aff == 0 and mouille == True:
        return (V**2/200)*2

    if aff == 0 and mouille == False:
        return V**2/200


def A(V, aff, mouille):
    if aff == 1 and mouille == False:
        return print("Distance totale de l'arrêt a", V, "km/h", R(V, 0)+F(V, 0), "m")

    if aff == 1 and mouille == True:
        return print("Distance totale de l'arrêt a", V, "km/h", R(V, 0)+F(V, 0, True), "m")

    if aff == 0 and mouille == True:
        return int(R(V, 0)+F(V, 0, True))

    if aff == 0 and mouille == False:
        return int(R(V, 0)+F(V, 0, False))

# Exercice 2


def demande():
    vitesse = int(input("Quelle est la vitesse du véhicule ?: "))
    mouille = bool(input("La route est-elle mouillée ? (Boolean, 1 = True, 0 = False): "))
    Distance = int(input("A quelle distance se trouve l'obstacle?: "))
    if int(A(vitesse, 0, mouille)) < Distance:
        freiner = str("Oui il pourra")
    else:
        freiner = str("Non il ne pourra pas")
    R(vitesse, 1), F(vitesse, 1, mouille), A(vitesse, 1, mouille), print(
        "Le conducteur pourra t'il freiner a temps ?", freiner)


demande()
