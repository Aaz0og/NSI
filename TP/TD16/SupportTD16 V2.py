""" Programmes pour réaliser le TD16"""

def addition(a,b):
    """ renvoie le rapport des deux nombres passés en paramètre"""
    return a+b

def soustraction(a,b):
    """ renvoie la différence des deux nombres a et b : a-b"""
    return a-b

def produit(a,b):
    """ renvoie le résultat de la multiplication des nombres a et b"""
    return a*b

def division(a,b):
    """ renvoie le quotient des nombres a et b : a/b"""
    return a/b

def testOperation1():
    assert operation1(2,3,4)==20
    assert operation1(2,3,0)==0
    assert operation1(2,-3,4.0)==-4.0

def operation1(a,b,c):
	return produit(c,addition(a,b))
	
def operation2(a,b,c,d):
	assert c!=-d, "Division par 0"
	return division(soustraction(a,b),addition(c,d))
	
def testOperation2():
    assert operation2(10,2,4,4)==1
    assert operation2(15,5,8,2)==1
    assert operation2(58,35,18,5)==1
    
testOperation2()
