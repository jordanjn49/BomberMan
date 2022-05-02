import pygame
from pygame.locals import*

def perso(x,y,image):
    surface.blit(image,(x,y))


def score(compte) :
    texte = police.render("Player 1 : " + str(compte), True, black)
    texte2 = police.render("Player 2 : " + str(compte), True, black)
    time = police2.render("TIME : " + str(compte), True, brown)
    surface.blit(texte, [10,10])
    surface.blit(texte2, [1020, 10])
    surface.blit(time, [500, 5])


def plateau_de_jeu():
    y=0
    x=0
    for ligne in plateau :
        x=0
        for case in ligne:
            afficherCase(x,y)
            x=x+1
        y = y+1

def afficherCase(x,y):
            if plateau[y][x]==3 :
                img2 = pygame.image.load('image/bloc3.png')
            elif plateau[y][x]==2 :
                    img2 = pygame.image.load('image/bloc2.png')
            elif plateau[y][x]==1 :
                    img2 = pygame.image.load('image/bloc1.png')
            elif plateau[y][x]==0 :
                    img2 = pygame.image.load('image/bloc0.png')
            elif plateau[y][x]==0.1:
                img2 = pygame.image.load('image/bloc0right.png')
            elif plateau[y][x]==0.2:
                img2 = pygame.image.load('image/bloc0left.png')

            surface.blit(img2, [x*50,y*50])

def joueur():
    img = pygame.image.load('image/right.png')
    image = pygame.image.load('image/stay.png')
    x = 1
    y = 2
    a = 21
    b = 12

    bombes = []
    bombes2 = []

    game_over = False

    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                          #Quitter le jeu avec la croix
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:                       #Quitter le jeu de maniere forcee
                    game_over = True
                if event.key == pygame.K_F2:                       #Couper la musique
                    son.stop()
                if event.key == pygame.K_F1:                       #Lancer la musique
                    son.play(60)


###############################################  DEPLACEMENTS  #########################################################


### JOUEUR 1 ###

                if event.key == pygame.K_z:
                    afficherCase(x,y)
                    if plateau[y-1][x]<2:
                        y -= 1                                     #Deplacement vers le haut
                    img = pygame.image.load('image/up2.png')
                if event.key == pygame.K_s:
                    afficherCase(x,y)
                    if plateau[y+1][x]<2:
                        y += 1                                     #Deplacement vers le bas
                    img = pygame.image.load('image/down2.png')
                if event.key == pygame.K_d:
                    afficherCase(x,y)
                    if plateau[y][x+1]<2:
                        x += 1                                     #Deplacement vers la droite
                    img = pygame.image.load('image/right2.png')
                if event.key == pygame.K_q:
                    afficherCase(x,y)
                    if plateau[y][x-1]<2:
                        x -= 1                                     #Deplacement vers la gauche
                    img = pygame.image.load('image/left2.png')
                if event.key == pygame.K_f:                    #Poser une bombe
                    if len(bombes) == 0:
                        bombes.append([x,y,10000])



### JOUEUR 2 ###



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        afficherCase(a,b)
                        if plateau[b-1][a]<2:
                            b -= 1                                     #Deplacement vers le haut
                        image = pygame.image.load('image/haut.png')
                    if event.key == pygame.K_DOWN:
                        afficherCase(a,b)
                        if plateau[b+1][a]<2:
                            b += 1                                     #Deplacement vers le bas
                        image = pygame.image.load('image/bas.png')
                    if event.key == pygame.K_RIGHT:
                        afficherCase(a,b)
                        if plateau[b][a+1]<2:
                            a += 1                                     #Deplacement vers la droite
                        image = pygame.image.load('image/droite.png')
                    if event.key == pygame.K_LEFT:
                        afficherCase(a,b)
                        if plateau[b][a-1]<2:
                            a -= 1                                     #Deplacement vers la gauche
                        image = pygame.image.load('image/gauche.png')
                    if event.key == pygame.K_SPACE:                    #Poser une bombe
                        if len(bombes2) == 0:
                            bombes2.append([a,b,10000])

                perso(x * 50, y * 50, img)
                perso(a*50,b*50,image)
                pygame.display.update()

#####################################################  BOMBES  #########################################################

        #Principe :
            # bombes[0]: bombe 1
                # bombes[0][0]: valeur de x
                # bombes[0][1]: valeur de y
                # bombes[0][2]: nb de seconces avant explosion
                # bombes[0][3]: numero du joueur


### JOUEUR 1 ###

        for bombe in bombes:
            if bombe[2]>5000 :
                img2 = pygame.image.load('image/bomb.png')
                surface.blit(img2, [bombe[0]*50,bombe[1]*50])
                bombe[2] -= 1

            elif bombe[2]>0:
                if(bombe[2]==5000):
                    explose = pygame.image.load('image/bomb_center.png')
                    surface.blit(explose, [bombe[0]*50,bombe[1]*50])
                    pygame.display.update()

                if plateau[bombe[1]][bombe[0]+1] < 3:
                    explose = pygame.image.load('image/bomb_right2.png')
                    surface.blit(explose, [(bombe[0] +1) * 50, bombe[1] * 50])
                    pygame.display.update()
                    plateau[bombe[1]][bombe[0] + 1] = 1

                if plateau[bombe[1]-1][bombe[0]] < 3:
                    explose = pygame.image.load('image/bomb_up2.png')
                    surface.blit(explose, [(bombe[0]) * 50, (bombe[1]-1) * 50])
                    pygame.display.update()
                    plateau[bombe[1]-1][bombe[0]] = 1

                if plateau[bombe[1]][bombe[0]-1] < 3:
                    explose = pygame.image.load('image/bomb_left2.png')
                    surface.blit(explose, [(bombe[0] -1) * 50, bombe[1] * 50])
                    pygame.display.update()
                    plateau[bombe[1]][bombe[0] - 1] = 1

                if plateau[bombe[1]+1][bombe[0]] < 3:
                    explose = pygame.image.load('image/bomb_down2.png')
                    surface.blit(explose, [(bombe[0]) * 50, (bombe[1]+1) * 50])
                    pygame.display.update()
                    plateau[bombe[1]+1][bombe[0]] = 1

                if bombe[0] == x and bombe[1] == y \
                        or bombe[0]+1 == x and bombe[1] == y \
                        or bombe[0]-1 == x and bombe[1] == y \
                        or bombe[0] == x and bombe[1]-1 == y \
                        or bombe[0] == x and bombe[1]+1 == y:
                    game_over = True

                if bombe[0] == a and bombe[1] == b \
                        or bombe[0]+1 == a and bombe[1] == b \
                        or bombe[0]-1 == a and bombe[1] == b \
                        or bombe[0] == a and bombe[1]-1 == b \
                        or bombe[0] == a and bombe[1]+1 == b:
                    game_over = True

                bombe[2] -= 300


            else:
                plateau[bombe[1]][bombe[0]] = 1
                plateau_de_jeu()
                perso(a * 50, b * 50, image)
                perso(x*50,y*50,img)
                pygame.display.update()
                bombes.remove(bombe)

### JOUEUR 2 ###


        for bombe in bombes2:
            if bombe[2]>5000 :
                img2 = pygame.image.load('image/bomb.png')
                surface.blit(img2, [bombe[0]*50,bombe[1]*50])
                bombe[2] -= 1

            elif bombe[2]>0:
                if(bombe[2]==5000):
                    explose = pygame.image.load('image/bomb_center.png')
                    surface.blit(explose, [bombe[0]*50,bombe[1]*50])
                    pygame.display.update()

                if plateau[bombe[1]][bombe[0]+1] < 3:
                    explose = pygame.image.load('image/bomb_right2.png')
                    surface.blit(explose, [(bombe[0] +1) * 50, bombe[1] * 50])
                    pygame.display.update()
                    plateau[bombe[1]][bombe[0] + 1] = 1

                if plateau[bombe[1]-1][bombe[0]] < 3:
                    explose = pygame.image.load('image/bomb_up2.png')
                    surface.blit(explose, [(bombe[0]) * 50, (bombe[1]-1) * 50])
                    pygame.display.update()
                    plateau[bombe[1]-1][bombe[0]] = 1

                if plateau[bombe[1]][bombe[0]-1] < 3:
                    explose = pygame.image.load('image/bomb_left2.png')
                    surface.blit(explose, [(bombe[0] -1) * 50, bombe[1] * 50])
                    pygame.display.update()
                    plateau[bombe[1]][bombe[0] - 1] = 1

                if plateau[bombe[1]+1][bombe[0]] < 3:
                    explose = pygame.image.load('image/bomb_down2.png')
                    surface.blit(explose, [(bombe[0]) * 50, (bombe[1]+1) * 50])
                    pygame.display.update()
                    plateau[bombe[1]+1][bombe[0]] = 1

                if bombe[0] == a and bombe[1] == b \
                        or bombe[0]+1 == a and bombe[1] == b \
                        or bombe[0]-1 == a and bombe[1] == b \
                        or bombe[0] == a and bombe[1]-1 == b \
                        or bombe[0] == a and bombe[1]+1 == b:
                    game_over = True

                if bombe[0] == x and bombe[1] == y \
                        or bombe[0]+1 == x and bombe[1] == y \
                        or bombe[0]-1 == x and bombe[1] == y \
                        or bombe[0] == x and bombe[1]-1 == y \
                        or bombe[0] == x and bombe[1]+1 == y:
                    game_over = True

                bombe[2] -= 300


            else:
                plateau[bombe[1]][bombe[0]] = 1
                plateau_de_jeu()
                perso(x*50,y*50,img)
                perso(a*50,b*50,image)
                pygame.display.update()
                bombes2.remove(bombe)


########################################################################################################################

                                        # Partie principale du jeu

pygame.init()
pygame.font.init()

plateau= [[0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,1,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,1,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]

time = 10000
police = pygame.font.Font('font.otf', 30)
police2 = pygame.font.Font('font.otf', 40)
black = (0,0,0)
brown = (133, 74, 0)
surfaceW = 1150
surfaceH = 700
surface = pygame.display.set_mode((surfaceW,surfaceH),RESIZABLE)
persoW = 50
persoH = 50

score_player1 = 0
score_player2 = 0

icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("BomberMan")
son = pygame.mixer.Sound("audio/music.wav")
son.play(loops=100)
pygame.mouse.set_visible(False)


plateau_de_jeu()
joueur()

pygame.quit()
quit()


##  while i <= 10000 :
#       time -= 1
#       texte = police.render("Player 1 : " + str(time), True, black)
#       surface.blit(texte, [10, 10])
#       i += 1
#       pygame.display.update()