def Fusion(lst1,lst2):
    if len(lst1)==0:
        return lst2
    if len(lst2)==0:
        return lst1
    if lst1[0]<lst2[0]:
        return [lst1[0],Fusion(lst1[1:],lst2)]
    if lst2[0]<lst1[0]:
        return [lst2[0],Fusion(lst2[1:],lst1)]
def Decouper(lst):
    n = len(lst)
    ct=n//2
    return lst[0:ct-1],lst[ct:n-1]

fus = Fusion(Decouper([27,10,12,8,11]))
print(fus)