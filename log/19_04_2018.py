import pygame
from pygame.locals import*

def displayer(x, y, image):
    surface.blit(image,(x*50,y*50))

def score_player1(number) :
    text = font_score.render("Player 1 : " + str(int(number)), True, black)
    surface.blit(text, [20,10])

def score_player2(number) :
    text = font_score.render("Player 2 : " + str(int(number)), True, black)
    surface.blit(text, [1000, 10])

def timer(number) :
    text = font_timer.render("TIME : " + str(int(number)) + "sec", True, brown)
    white_img = pygame.image.load('image/center.png')
    surface.blit(white_img,[500,0])
    surface.blit(text, [500, 5])

def board_displayer():
    x=0
    y=0
    for line in game_board :
        x=0
        for case in line:
            case_selection(x, y)
            x=x+1
        y = y+1
    score_player1(score1)
    score_player2(score2)

def case_selection(x, y):
    if game_board[y][x] == 3:
        case_image = pygame.image.load('image/bloc3.png')
    elif game_board[y][x] == 2:
        case_image = pygame.image.load('image/bloc2.png')
    elif game_board[y][x] == 1:
        case_image = pygame.image.load('image/bloc1.png')
    elif game_board[y][x] == 0:
        case_image = pygame.image.load('image/bloc0.png')
    elif game_board[y][x] == 0.1:
        case_image = pygame.image.load('image/bloc0right.png')
    elif game_board[y][x] == 0.2:
        case_image = pygame.image.load('image/bloc0left.png')

    displayer(x, y, case_image)

def start():
    persist = True
    while persist:
        text = font_start.render("Press SPACE to start", True, white)
        wallpaper = pygame.image.load('image/wallpaper.png')
        surface.blit(wallpaper,(0,0))
        surface.blit(text, [100, 500])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    persist = False
                    main()



def main():
    board_displayer()
    global score2, score1, time
    player1_image = pygame.image.load('image/player1_stay.png')
    player2_image = pygame.image.load('image/player2_stay.png')
    x_player1 = 1
    y_player1 = 2
    x_player2 = 21
    y_player2 = 12

    bomb_player1 = []
    bomb_player2 = []

    game_over = False

    while not game_over :
        #if time <= 0 :
        pygame.display.update()
        time -= 0.0025
        timer(time)
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


###################################################  MOVEMENT  #########################################################


### PLAYER 1 ###

                if event.key == pygame.K_w:
                    case_selection(x_player1, y_player1)
                    if game_board[y_player1 - 1][x_player1]<2:
                        y_player1 -= 1                                     #Deplacement vers le haut
                    player1_image = pygame.image.load('image/player1_up.png')
                if event.key == pygame.K_s:
                    case_selection(x_player1, y_player1)
                    if game_board[y_player1 + 1][x_player1]<2:
                        y_player1 += 1                                     #Deplacement vers le bas
                    player1_image = pygame.image.load('image/player1_down.png')
                if event.key == pygame.K_d:
                    case_selection(x_player1, y_player1)
                    if game_board[y_player1][x_player1 + 1]<2:
                        x_player1 += 1                                     #Deplacement vers la droite
                    player1_image = pygame.image.load('image/player1_right.png')
                if event.key == pygame.K_a:
                    case_selection(x_player1, y_player1)
                    if game_board[y_player1][x_player1 - 1]<2:
                        x_player1 -= 1                                     #Deplacement vers la gauche
                    player1_image = pygame.image.load('image/player1_left.png')
                if event.key == pygame.K_f:                    #Poser une bombe
                    if len(bomb_player1) == 0:
                        bomb_player1.append([x_player1,y_player1,10000])



### PLAYER 2 ###



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        case_selection(x_player2, y_player2)
                        if game_board[y_player2 - 1][x_player2]<2:
                            y_player2 -= 1                                     #Deplacement vers le haut
                        player2_image = pygame.image.load('image/player2_up.png')
                    if event.key == pygame.K_DOWN:
                        case_selection(x_player2, y_player2)
                        if game_board[y_player2 + 1][x_player2]<2:
                            y_player2 += 1                                     #Deplacement vers le bas
                        player2_image = pygame.image.load('image/player2_down.png')
                    if event.key == pygame.K_RIGHT:
                        case_selection(x_player2, y_player2)
                        if game_board[y_player2][x_player2 + 1]<2:
                            x_player2 += 1                                     #Deplacement vers la droite
                        player2_image = pygame.image.load('image/player2_right.png')
                    if event.key == pygame.K_LEFT:
                        case_selection(x_player2, y_player2)
                        if game_board[y_player2][x_player2 - 1]<2:
                            x_player2 -= 1                                     #Deplacement vers la gauche
                        player2_image = pygame.image.load('image/player2_left.png')
                    if event.key == pygame.K_SPACE:                    #Poser une bombe
                        if len(bomb_player2) == 0:
                            bomb_player2.append([x_player2,y_player2,1000])

                displayer(x_player1,y_player1,player1_image)
                displayer(x_player2,y_player2,player2_image)


######################################################  BOMBS  #########################################################

        #Principe :
            # bombes[0]: bombe 1
                # bombes[0][0]: valeur de x
                # bombes[0][1]: valeur de y
                # bombes[0][2]: nb de seconces avant explosion
                # bombes[0][3]: numero du main


### PLAYER 1 ###

        for bomb in bomb_player1:
            if bomb[2]>500 :
                bomb_image = pygame.image.load('image/bomb.png')
                displayer(bomb[0],bomb[1],bomb_image)
                bomb[2] -= 1

            elif bomb[2]>0:
                if(bomb[2]==500):
                    explose = pygame.image.load('image/bomb_center.png')
                    displayer(bomb[0], bomb[1], explose)

                if game_board[bomb[1]][bomb[0] + 1] < 3:
                    explose = pygame.image.load('image/bomb_right.png')
                    displayer(bomb[0]+1, bomb[1], explose)
                    game_board[bomb[1]][bomb[0] + 1] = 1

                if game_board[bomb[1] - 1][bomb[0]] < 3:
                    explose = pygame.image.load('image/bomb_up.png')
                    displayer(bomb[0], bomb[1]-1, explose)
                    game_board[bomb[1] - 1][bomb[0]] = 1

                if game_board[bomb[1]][bomb[0] - 1] < 3:
                    explose = pygame.image.load('image/bomb_left.png')
                    displayer(bomb[0]-1, bomb[1], explose)
                    game_board[bomb[1]][bomb[0] - 1] = 1

                if game_board[bomb[1] + 1][bomb[0]] < 3:
                    explose = pygame.image.load('image/bomb_down.png')
                    displayer(bomb[0], bomb[1]+1, explose)
                    game_board[bomb[1] + 1][bomb[0]] = 1

                if bomb[0] == x_player1 and bomb[1] == y_player1 \
                        or bomb[0]+1 == x_player1 and bomb[1] == y_player1 \
                        or bomb[0]-1 == x_player1 and bomb[1] == y_player1 \
                        or bomb[0] == x_player1 and bomb[1]-1 == y_player1 \
                        or bomb[0] == x_player1 and bomb[1]+1 == y_player1:
                    score2 += 1/16

                if bomb[0] == x_player2 and bomb[1] == y_player2 \
                        or bomb[0]+1 == x_player2 and bomb[1] == y_player2 \
                        or bomb[0]-1 == x_player2 and bomb[1] == y_player2 \
                        or bomb[0] == x_player2 and bomb[1]-1 == y_player2 \
                        or bomb[0] == x_player2 and bomb[1]+1 == y_player2:
                    score1 += 1/16

                bomb[2] -= 30


            else:
                game_board[bomb[1]][bomb[0]] = 1
                board_displayer()
                displayer(x_player2,y_player2,player2_image)
                displayer(x_player1,y_player1,player1_image)
                bomb_player1.remove(bomb)

### PLAYER 2 ###


        for bomb in bomb_player2:
            if bomb[2]>500 :
                bomb_image = pygame.image.load('image/bomb.png')
                displayer(bomb[0], bomb[1], bomb_image)
                bomb[2] -= 1

            elif bomb[2]>0:
                if(bomb[2]==500):
                    explose = pygame.image.load('image/bomb_center.png')
                    displayer(bomb[0], bomb[1], explose)

                if game_board[bomb[1]][bomb[0] + 1] < 3:
                    explose = pygame.image.load('image/bomb_right.png')
                    displayer(bomb[0] + 1, bomb[1], explose)
                    game_board[bomb[1]][bomb[0] + 1] = 1

                if game_board[bomb[1] - 1][bomb[0]] < 3:
                    explose = pygame.image.load('image/bomb_up.png')
                    displayer(bomb[0], bomb[1] - 1, explose)
                    game_board[bomb[1] - 1][bomb[0]] = 1

                if game_board[bomb[1]][bomb[0] - 1] < 3:
                    explose = pygame.image.load('image/bomb_left.png')
                    displayer(bomb[0] - 1, bomb[1], explose)
                    game_board[bomb[1]][bomb[0] - 1] = 1

                if game_board[bomb[1] + 1][bomb[0]] < 3:
                    explose = pygame.image.load('image/bomb_down.png')
                    displayer(bomb[0], bomb[1] + 1, explose)
                    game_board[bomb[1] + 1][bomb[0]] = 1

                if bomb[0] == x_player2 and bomb[1] == y_player2 \
                        or bomb[0]+1 == x_player2 and bomb[1] == y_player2 \
                        or bomb[0]-1 == x_player2 and bomb[1] == y_player2 \
                        or bomb[0] == x_player2 and bomb[1]-1 == y_player2 \
                        or bomb[0] == x_player2 and bomb[1]+1 == y_player2:
                    score1 += 1/16

                if bomb[0] == x_player1 and bomb[1] == y_player1 \
                        or bomb[0]+1 == x_player1 and bomb[1] == y_player1 \
                        or bomb[0]-1 == x_player1 and bomb[1] == y_player1 \
                        or bomb[0] == x_player1 and bomb[1]-1 == y_player1 \
                        or bomb[0] == x_player1 and bomb[1]+1 == y_player1:
                    score2 += 1/16

                bomb[2] -= 30


            else:
                game_board[bomb[1]][bomb[0]] = 1
                board_displayer()
                displayer(x_player1,y_player1,player1_image)
                displayer(x_player2,y_player2,player2_image)
                bomb_player2.remove(bomb)



########################################################################################################################

                                        # Partie principale du jeu

pygame.init()
pygame.font.init()

icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("BomberMan")
son = pygame.mixer.Sound("audio/music.wav")
son.play(loops=100)
pygame.mouse.set_visible(False)

game_board= [[0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1],
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


time = 180
score1 = 0
score2 = 0

font_start = pygame.font.Font('font.otf', 50)
font_score = pygame.font.Font('font.otf', 30)
font_timer = pygame.font.Font('font.otf', 40)
black = (0,0,0)
brown = (133, 74, 0)
white = (255,255,255)
surfaceW = 1150
surfaceH = 700
surface = pygame.display.set_mode((surfaceW,surfaceH),RESIZABLE)
player_W = 50
player_H = 50


board_displayer()
start()



pygame.quit()
quit()
