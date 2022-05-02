import pygame
from pygame.locals import*

########################################################################################################################

                                            # Parametrage des personnages

def perso(x,y,image):
    surface.blit(image,(x,y))

def joueur():
    img = pygame.image.load('image/right.png')
    x = 1
    y = 2

    bombes = []

    game_over = False

    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:                       #Quitter le jeu de maniere forcee
                    game_over = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    afficherCase(x,y)
                    if plateau[y-1][x]<2:
                        y -= 1                                     #Deplacement vers le haut
                    img = pygame.image.load('image/up2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    afficherCase(x,y)
                    if plateau[y+1][x]<2:
                        y += 1                                     #Deplacement vers le bas
                    img = pygame.image.load('image/down2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    afficherCase(x,y)
                    if plateau[y][x+1]<2:
                        x += 1                                     #Deplacement vers la droite
                    img = pygame.image.load('image/right2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    afficherCase(x,y)
                    if plateau[y][x-1]<2:
                        x -= 1                                     #Deplacement vers la gauche
                    img = pygame.image.load('image/left2.png')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(bombes) < 1:
                        bombes.append([x,y,100])
                        img = pygame.image.load('image/bomb.png')
                        if bombes[0]==plateau[x] and bombes[1]==plateau[y]:
                            plateau == 4
                        print(plateau[1][2])


            print(bombes)
            perso(x*50,y*50,img)
            pygame.display.update()

def score(compte) :
    clock = pygame.time.Clock()
    police = pygame.font.Font('font.otf', 30)
    police2 = pygame.font.Font('font.otf', 40)
    texte = police.render("Player 1 : " + str(compte), True, black)
    texte2 = police.render("Player 2 : " + str(compte), True, black)
    time = police2.render("TIME : " + str(clock.tick()), True, brown)
    surface.blit(texte, [10,10])
    surface.blit(texte2, [1020, 10])
    surface.blit(time, [500, 5])

########################################################################################################################
                                            # Affichage du plateau de jeu

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


def plateau_de_jeu():
    y=0
    x=0
    for ligne in plateau :
        x=0
        for case in ligne:
            afficherCase(x,y)
            x=x+1
        y = y+1


    score_actuel = 0
    score2_actuel = 0
    score(score_actuel)
    score(score2_actuel)
    pygame.display.update()

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



########################################################################################################################

                                                # Fin du jeu

def game_over():
    messages("GAME OVER")

########################################################################################################################

                                        # Partie principale du jeu

pygame.init()
pygame.font.init()

black = (0,0,0)
brown = (133, 74, 0)
surfaceW = 1150
surfaceH = 700
surface = pygame.display.set_mode((surfaceW,surfaceH),RESIZABLE)
persoW = 50
persoH = 50

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