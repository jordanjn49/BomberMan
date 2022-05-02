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
                if event.key == pygame.K_UP:
                    afficherCase(x,y)
                    if plateau[y-1][x]<2 :
                        y -= 1                                     #Deplacement vers le haut
                    img = pygame.image.load('image/up2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    afficherCase(x,y)
                    if plateau[y+1][x]<2 :
                        y += 1                                     #Deplacement vers le bas
                    img = pygame.image.load('image/down2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    afficherCase(x,y)
                    if plateau[y][x+1]<2 :
                        x += 1                                     #Deplacement vers la droite
                    img = pygame.image.load('image/right2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    afficherCase(x,y)
                    if plateau[y][x-1]<2 :
                        x -= 1                                     #Deplacement vers la gauche
                    img = pygame.image.load('image/left2.png')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bombes.add([x,y,100])



            perso(x*50,y*50,img)
            pygame.display.update()


########################################################################################################################

                                            # Affichage du plateau de jeu

plateau= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
            surface.blit(img2, [x*50,y*50])



########################################################################################################################

                                                # Fin du jeu

def game_over():
    messages("GAME OVER")



########################################################################################################################

                                        # Partie principale du jeu

pygame.init()

surfaceW = 1150
surfaceH = 700
persoW = 50
persoH = 50

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("BomberMan")
son = pygame.mixer.Sound("audio/music.wav")

plateau_de_jeu()
son.play(loops=100)
joueur()
pygame.quit()
quit()