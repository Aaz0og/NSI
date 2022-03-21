Nvilles = 6
L0 = [0,3,1,0,0,0] # la matrice d'adjacence est mise en place de façon très simple ici
L1 = [3,0,1,2,0,0] # la méthode append est utilisée dans la suite
L2 = [1,1,0,3,5,0]
L3 = [0,2,3,0,1,3]
L4 = [0,0,5,1,0,1]
L5 = [0,0,0,3,1,0]
m_adjac = [L0,L1,L2,L3,L4,L5] # m_adjac[4][2] contient la valeur 5, etc. 
DIJ=list() # la liste DIJ mémorise les données du tableau 
for i in range (Nvilles): #création de la ligne du tableur
  DIJ.append([1000000,"X","N"]) #représenter l'infini
ville_select=0 # numéro de la ville sélectionnée; 0 = ville de départ
dist_interm=0 # distance pour arriver à la ville sélectionnée; 0 au départ
while ville_select != Nvilles-1:
  minimum=1000000
  for n in range(1,Nvilles):
    if DIJ[n][2]=="N":
      dist= 
      dist_totale=
      if dist != 0 and dist_totale < DIJ[n][0]:
        DIJ[n][0]=
        DIJ[n][1]=
      if DIJ[n][0]<minimum:
        minimum=
        pville_select=
  ville_select=pville_select # pville_select = numéro de la prochaine ville sélectionnée
  DIJ[ville_select][2]=
  dist_interm=
  for i in range(1,Nvilles):
    print( DIJ[i])
  print ("\n")
chemin=list() # reconstitution du plus court chemin, en partant de la ville d'arrivée
ville=Nvilles-1
chemin.append(ville)
while ville != 0:
  ville=DIJ[ville][1]
  chemin.append(ville)

print ("plus court chemin, à lire à l'envers : ",chemin)
print ("distance totale : ",DIJ[Nvilles-1][0])
