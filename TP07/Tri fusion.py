def Fusion(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    if lst1[0] <= lst2[0]:
        return [lst1[0]] + Fusion(lst1[1:], lst2)
    if lst2[0] <= lst1[0]:
        return [lst2[0]] + Fusion(lst2[1:], lst1)


def Decouper(lst):
    n = len(lst)
    moitie = n//2
    return lst[0:moitie], lst[moitie:n]


def Expo(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return Expo(a*a, n/2)
    else:
        return a*Expo(a*a, (n-1)/2)


def TriFusion(lst):
    if len(lst) == 1:
        return lst
    else:
        a1, a2 = Decouper(lst)
        return Fusion(TriFusion(a1), TriFusion(a2))
def jeutest(fonction):
    assert fonction([27,10,12,8,11])== [8,10,11,12,27],"Erreur nombres normaux"
    assert fonction([-27,-10,-12,-8,-11])== [-27,-12,-11,-10,-8],"Erreur nombres négatifs"
    assert fonction([5,4,3,3,1,0])== [0,1,3,3,4,5],"Erreur nombres similaires"
    assert fonction([-1,-2,0,1,2])== [-2,-1,0,1,2],"Erreur nombres négatifs et positif"
    assert fonction([2,1.1,1.2])==[1.1,1.2,2],"Erreur nombres décimaux"
    return print("Aucune erreur, BRAVO!")

print(Decouper([5,4,3,3,1,0]))
print(TriFusion([1,3,4,5,6,2]))
jeutest(TriFusion)