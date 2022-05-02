import pygame
from pygame.locals import*


dark = (000,000,000)
blue = (0,129,204)

pygame.init()

surfaceW = 1150
surfaceH = 650
persoW = 50
persoH = 50

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("BomberMan")
son = pygame.mixer.Sound("audio/music.wav")

def perso(x,y,image):
    surface.blit(image,(x,y))

def joueur():
    img = pygame.image.load('image/down.png')
    x = 200
    y = 350
    ymouv = 0
    xmouv = 0

    game_over = False

    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ymouv = -2
                    img = pygame.image.load('image/up2.png')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ymouv = 0
                    img = pygame.image.load('image/up.png')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ymouv = +2
                    img = pygame.image.load('image/down2.png')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    ymouv = 0
                    img = pygame.image.load('image/down.png')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xmouv = -2
                    img = pygame.image.load('image/left2.png')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    xmouv = 0
                    img = pygame.image.load('image/left.png')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xmouv = +2
                    img = pygame.image.load('image/right2.png')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    xmouv = 0
                    img = pygame.image.load('image/right.png')

        x = x + xmouv
        y = y + ymouv

        surface.fill(blue)
        perso(x,y,img)

        if y > surfaceH:
            y = y - surfaceH + 0
        if x > surfaceW:
            x = x - surfaceW
        if y - 10 < 0:
            y = y + surfaceH - 0
        if x + 10 < 0:
            x = x + surfaceW

        pygame.display.update()

plateau= [[3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,1,1,2,2,2,2,2,2,2,2,2,3],
[3,1,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,2,3],
[3,2,2,2,2,2,2,2,2,2,2,2,3],
[3,2,3,2,3,2,3,2,3,2,3,1,3],
[3,2,2,2,2,2,2,2,2,2,1,1,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3]]

x=0
y=0
for ligne in plateau :
    x=0
    for case in ligne:
        if case==3 :
            img2 = pygame.image.load('image/bloc2.png')
            #img2 = pygame.image.set_mode((640, 480))
            surface.blit(img2, [x,y])
        x=x+50
    y = y+50
    pygame.display.update()

def obj(texte, Police):
    texteaffiche = Police.render(texte,True,white)
    return texteaffiche, texteindex.get_rect()

def messages_debut(texte):
    fontscore = pygame.font.Font("font.ttf",50)
    fonttemps = pygame.font.Font("font.ttf",60)

    scoreaffiche, score_index = obj(texte, fontscore)
    score_index.center = ((surfaceW/2)+500),((surfaceH/2)-290)
    surface.blit(scoreaffiche,score_index)

    tempsaffiche, temps_index = obj(texte, fonttemps)
    temps_index.center = surfaceW/2, ((surfaceH/2)-280)
    surface.blit(tempsaffiche,temps_index)

    pygame.display.update()

def message_fin(texte):
    fontgame_over = pygame.font.Font("font.ttf",90)
    fontresume = pygame.font.Font("font.ttf",40)

    game_overaffiche, game_over_index = obj(texte, fontgame_over)
    game_over_index_index.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(game_overaffiche,game_over_index)

    resumeaffiche, resume_index = obj("Appuyer sur Entrer pour recommancer", fontresume)
    resume_index.center = surfaceW/2, (surfaceH/2)
    surface.blit(resumeaffiche, resume_index)

    pygame.display.update()

def game_over():
    messages("GAME OVER")


son.play(loops=100)
#joueur()
pygame.quit()
quit()