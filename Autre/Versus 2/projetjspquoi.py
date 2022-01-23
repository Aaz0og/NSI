argent = 0

def placements(durée,montant,pourcentage):
    return montant * (((1 + ((pourcentage/100.0)/12)) ** (12*durée)))

def percentage(pourcent, sur):
  return 100 * float(pourcent)/float(sur)

print(percentage(1500,2))

print(placements(5,1500,5))

P = int(input("Enter starting principle please. "))
n = int(input("Enter number of compounding periods per year. "))
r = float(input("Enter annual interest rate. e.g. 15 for 15% "))
y = int(input("Enter the amount of years. "))

FV = P * (((1 + ((r/100.0)/n)) ** (n*y)))

print ("The final amount after", y, "years is", FV)