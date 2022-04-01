import random,sys,time
try: 
    import bext 
except ImportError:
    print("Module bext non trouvé. Essayez 'pip3 install bext'")
    sys.exit()

# Définition des constantes    
DUREE_PAUSE = 0.2
#TODO Essayer de changer ça de 0 à 100:
CHANCE_TOMBER_LARGEUR = 50
LARGEUR_ECRAN = 79
HAUTEUR_ECRAN = 25
X = 0
Y = 1
SABLE = chr(9617)
MUR = chr(9608)

# Faire les murs de l'horloge
HORLOGE = set()
for i in range(18,37):
    HORLOGE.add((i,1)) 
    HORLOGE.add((i,23)) 
for i in range(1,5):
    HORLOGE.add((18,i)) 
    HORLOGE.add((36,i)) 
    HORLOGE.add((18, i+19)) 
    HORLOGE.add((36, i+19)) 
for i in range(8):
    HORLOGE.add((19+i,5+i)) 
    HORLOGE.add((35-i,5+i))
    HORLOGE.add((25-i,13+i))
    HORLOGE.add((29+i,13+i))
    
# Faire les murs au dessus de l'horloge
SABLE_INITIAL = set()
for y in range(8):
    for x in range(19+y,36-y):
        SABLE_INITIAL.add((x,y+4))
        
def main():
    bext.fg('yellow')
    bext.clear()
    
    
    # Faire le message d'arrêt
    bext.goto(0,0)
    print('Ctrl-C pour arrêter',end='')
    
    # Montrer les murs de l'horloge
    for mur in HORLOGE:
        bext.goto(mur[X],mur[Y])
        print(MUR,end='')
    
    while True: # Boucle du programme
        toutSable = list(SABLE_INITIAL)
        # Dessiner le sable initial
        for sable in toutSable:
            bext.goto(sable[X],sable[Y])
            print(SABLE,end='')
        runhourglasssimulation(toutSable)
        
def runhourglasssimulation(toutSable):
    '''Faire tourner la simulation jusqu'a 
    ce que le sable ne bouge plus'''
    while True: # Loop tant que le sable existe
        random.shuffle(toutSable)
        sableBougeCetteEtape = False
        for i, sable in enumerate(toutSable):
            if sable[Y] == HAUTEUR_ECRAN-1:
                continue
            # Si rien n'est en dessous du sable il bouge
            pasSableEnDessous = (sable[X],sable[Y]+1) not in toutSable
            pasMurEnDessous = (sable[X],sable[Y]+1) not in HORLOGE
            peutTomber = pasSableEnDessous and pasMurEnDessous
            
            if peutTomber:
                # Draw the sand in its new position down one space:
                bext.goto(sable[X], sable[Y])
                print(' ', end='') # Clear the old position.
                bext.goto(sable[X], sable[Y] + 1)
                print(SABLE, end='')
                # Set the sand in its new position down one space:
                toutSable[i] = (sable[X], sable[Y] + 1)
                sableBougeCetteEtape = True
            
            else:
                # Check if the sand can fall to the left:
                dessousGauche = (sable[X] - 1, sable[Y] + 1)
                pasSableDessousGauche = dessousGauche not in toutSable
                pasMurDessousGauche = dessousGauche not in HORLOGE
                gauche = (sable[X] - 1, sable[Y])
                pasMurGauche = gauche not in HORLOGE
                pasSurBordGauche = sable[X] > 0
                peutTomberGauche = (pasSableDessousGauche and pasMurDessousGauche and pasMurGauche and pasSurBordGauche)
                # Check if the sand can fall to the right:
                dessousDroite = (sable[X] + 1, sable[Y] + 1)
                pasSableDessousDroite = dessousDroite not in toutSable
                noWallBelowRight = dessousDroite not in HORLOGE
                droite = (sable[X] + 1, sable[Y])
                pasMurDroite = droite not in HORLOGE
                pasSurBordDroite = sable[X] < LARGEUR_ECRAN - 1
                peutTomberDroite = (pasSableDessousDroite and noWallBelowRight and pasMurDroite and pasSurBordDroite)
                
                # Gérer la direction ou le sable tombe
            directionChute = None
            if peutTomberGauche and not peutTomberDroite:
                directionChute = -1 # Sable tombe a gauche
            elif not peutTomberGauche and peutTomberDroite:
                directionChute = 1 # Sable tombe a droite
            elif peutTomberGauche and peutTomberDroite:
                # Les deux sont possibles alors on fait de l'aléatoire
                directionChute = random.choice((-1,1))
                    
            # Regarde si le sable peut faire une "grosse" chute a droite ou a gauche
            if random.random() * 100 < CHANCE_TOMBER_LARGEUR:
                dessousDeuxGauche = (sable[X] - 2, sable[Y] + 1)
                pasSableDessousDeuxGauche = dessousDeuxGauche not in toutSable
                pasMurDessousDeuxGauche = dessousDeuxGauche not in HORLOGE
                pasSurDeuxiemeBordGauche = sable[X] > 1
                peutTomberDeuxGauche = (peutTomberGauche and pasSableDessousDeuxGauche and pasMurDessousDeuxGauche and pasSurDeuxiemeBordGauche)
                
                dessousDeuxDroite = (sable[X] + 2, sable[Y] + 1)
                pasSableDessousDeuxDroite = dessousDeuxDroite not in toutSable
                pasMurDessousDeuxDroite = dessousDeuxDroite not in HORLOGE
                pasSurDeuxiemeBordGauche = sable[X] < LARGEUR_ECRAN - 2
                peutTomberDeuxDroite = (peutTomberDroite and pasSableDessousDeuxDroite and pasMurDessousDeuxDroite and pasSurDeuxiemeBordGauche)
                
                if peutTomberDeuxGauche and not peutTomberDeuxDroite:
                    directionChute = -2
                
                elif not peutTomberDeuxGauche and peutTomberDeuxDroite:
                    directionChute = 2
                
                elif peutTomberDeuxGauche and peutTomberDeuxDroite:
                    directionChute = random.choice((-2, 2))
            if directionChute == None:
                # This sand can't fall, so move on.
                continue
            # Draw the sand in its new position:
            bext.goto(sable[X], sable[Y])
            print(' ', end='') # Erase old sand.
            bext.goto(sable[X] + directionChute, sable[Y] + 1)
            print(SABLE, end='') # Draw new sand.
            
            # Move the grain of sand to its new position:
            toutSable[i] = (sable[X] + directionChute, sable[Y] + 1)
            sableBougeCetteEtape = True
            
        sys.stdout.flush() # (Required for bext-using programs.)
        time.sleep(DUREE_PAUSE) # Pause after this
    # If no sand has moved on this step, reset the hourglass:
    if not sableBougeCetteEtape:
        time.sleep(2)
        # Erase all of the sand:
        for sable in toutSable:
            bext.goto(sable[X], sable[Y])
            print(' ', end='')
#        break # Break out of main simulation loop.

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-C is pressed, end the program.

for i in range