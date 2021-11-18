def jeutest(fonction):
    assert fonction([27,10,12,8,11])== [8,10,11,12,27],"Erreur nombres normaux"
    assert fonction([-27,-10,-12,-8,-11])== [-27,-12,-11,-10,-8],"Erreur nombres négatifs"
    assert fonction([5,4,3,3,1,0])== [0,1,3,3,4,5],"Erreur nombres similaires"
    assert fonction([-1,-2,0,1,2])== [-2,-1,0,1,2],"Erreur nombres négatifs et positif"
    assert fonction([2,1.1,1.2])==[1.1,1.2,2],"Erreur nombres décimaux"
    return print("Aucune erreur, BRAVO!")
