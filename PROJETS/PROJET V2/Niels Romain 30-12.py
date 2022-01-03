jeux=[]

# jeu 1
x = [ 0, 2, 5, 10]
y = [ 0, 3, 5]
sol = 4
jeux.append([x,y,sol])

for ax in x:
    for bx in x:
        for ay in y:
            for by in y:
                if carrestest(ax,bx,by,ay)== True:
                    sol+=1
                    print(sol)
                    