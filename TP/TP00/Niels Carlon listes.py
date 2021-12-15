# Exercice 1
def somme_liste(l):
    r=0
    for elements in l:
        r+= elements
    return r
print(somme_liste([1,3,4]))

#-----
# Exercice 2
def produit_liste(l):
    r=1
    for elements in l:
        r*= elements
    return r
print(produit_liste([2,3,4]))

#-----
# Exercice 3
def echanger(l,i,j):
    l[i], l[j] = l[j], l[i]
    return l
print(echanger([1,2,3,4,5],2-1,3-1))

#-----
# Exercice 4  
def occurrence(x,l):
    ite=0
    for elements in l:
        if elements == x:
            ite+=1
    return ite
print(occurrence(2,[1,2,3,2]))

#-----
# Exercice 5
def concatener_liste(l,p):
    l += p
    return l
concatener_liste([1,2],[3,4])

#-----
# Exercice 6
def fibonacci(n):
    a=0
    b=1
    l=[0]
    if n<0:
        print("Impossible")
    elif n==0:
        return 0
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            l.append(b)
            c=a+b
            a=b
            b=c
        return l
print(fibonacci(12))

#-----
# Excercice 7
import random
def generer_listee(l):
    l=[]
    for _ in range(100):
        a = random.randint(0,10000)
        l.append(a)
    #l=[for _ in range(100): l.append(random.randint(0,10000))]
    return l
print(generer_listee(0))

# Partie 2

def generer_l(n,x):
    l=[]
    for _ in range(n):
        a = random.randint(0,x)
        l.append(a)
    #l=[for _ in range(100): l.append(random.randint(0,10000))]
    return l
print(generer_l(4,4))

# Partie 3

def generer_liste(n,x):
    l=[]
    if x<n:
        b = n-x
        x+=b+1
    for _ in range(n):
        a = random.randint(0,x)
        if a in l:
            while a in l: 
                a = random.randint(0,x)
        l.append(a)
    return l
print(generer_liste(4,3))

#-----
# Exercice 8
def fusion_liste(ly,p):
    for element in p:
        if element not in ly:
            ly.append(element)
    return ly
print(fusion_liste([1,2,5],[2,3,4,1,2]))

#-----
# Exercice 9
def max_liste(l):
    max=0
    for element in l:
        if element>max:
            max=element
    return max
max_liste([1,4,3,5,6,5,8,9,23])

# Niels Carlon-Mismer