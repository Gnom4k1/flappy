import pygame
import random as r
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 80)

kastil = 698

imgBG = pygame.image.load("background.png")
imgBird = pygame.image.load("bird_Skin.png")
imgBird2 = pygame.image.load("bird_Skin2.png")
imgPT = pygame.image.load("pipe_top2.png")
imgPB = pygame.image.load("pipe_bottom2.png")
imgBG_night = pygame.image.load("background_night.png")
imgHEAR_DIE = pygame.image.load("HEART_DIE.png")
imgMenu = pygame.image.load("Menu.png")
MULTIVERSE = pygame.image.load("MULTIVERSE.png")
imgRESET = pygame.image.load("RESET.png")
imgSETTING = pygame.image.load("SETTING.png")
imgOFF = pygame.image.load("Menu_SOUND_OFF.png")
imgLIGHT = pygame.image.load("LIGHT_THEME.png")
imgDARK = pygame.image.load("DARK_THEME.png")
imgBACK = pygame.image.load("BACK.png")
imgApple = pygame.image.load("apple.png")
imgBOMB = pygame.image.load("BOMB.png")
imgPineapple = pygame.image.load("pineapple.png")
imgWatermelon = pygame.image.load("WATERMELON.png")
fon = imgBG
bird = imgBird
FpS = r.randrange(1,2)
Menu = imgMenu
ExitMenu = 1
mode = 1

p = r.randrange(0, 200)
pr = p + 380
pt = r.randrange(p, pr)

py, sy, ay = HEIGHT // 2, 0, 0
player = pygame.Rect(WIDTH // 3, py, 34, 24)
clock_item = pygame.Rect(650, 132, 50, 50)
SETTING_BUTTON = pygame.Rect(700, 25, 50, 50)
RESET = pygame.Rect(30,132, 50, 50)
DARK_TEM = pygame.Rect(275,244, 50, 50)
BACK = pygame.Rect(650,136,50,50)
WHITE = (255,255,255)
MULTIVERSE.set_colorkey(WHITE)
frame = 0
dscores = 0
Menu2 = pygame.Rect(70, 100, 650, 450)
MenuOFF = pygame.Rect(70, 100, 650, 450)
spawn_F = r.randrange(1, 4)

RED = (255, 0, 0)
imgMenu.set_colorkey(RED)

WHITE2 = (255,255,255)
imgBird.set_colorkey(WHITE2)

imgBACK.set_alpha(0)

imgBOMB.set_alpha(0)
imgWatermelon.set_alpha(0)
imgApple.set_alpha(0)
imgPineapple.set_alpha(0)

state = "start"
timer = 60
timerV2 = 120
timerV3 = 300
pipes = []
bges = []
hard = 200
theme = 1

bges.append(pygame.Rect(0, 0, 288, 600))

lives = 3
scores = 0
maxs = 0

Up = -2
Down = -0.5
HEARTS = []
show_heart = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    press = pygame.mouse.get_pressed()
    START = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = press[0] or keys[pygame.K_SPACE]
    SPEED1 = keys[pygame.K_q]
    SPEED2 = keys[pygame.K_e]
    SPEED3 = keys[pygame.K_w]
    Up2 =keys[pygame.K_UP]
    Down2 = keys[pygame.K_DOWN]
    RESET_b = keys[pygame.K_r]
    CLOSE = keys[pygame.K_ESCAPE]
    BOMB = pygame.Rect(750, 200, 50, 50)
    Watermmelon = pygame.Rect(750, 300, 50, 50)
    Apple = pygame.Rect(730, 400, 70, 70)
    Pineapple = pygame.Rect(750, 100, 50, 50)
    timerV3 = 60


    if timer > 0:
        timer -= 1
    if timerV2 > 0:
        timerV2 -= 1
    if timerV2 == 0:
        timerV2 = 600
        show_heart = r.randint(2,2)
    if timerV3 > 0:
        timerV3 -= 1
    if timerV3 == 0:
        timerV3 = 300

    frame = (frame + 0.2) % 4

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pos = pygame.mouse.get_pos()
            if ExitMenu == 1:
                if pos[1] > 386 and pos[1] < 468 and pos[0] > 116 and pos[0] < 303:
                    ExitMenu = 0
                    imgMenu.set_alpha(0)
                    MULTIVERSE.set_alpha(0)
            if ExitMenu == 1:
                if pos[1] > 384 and pos[1] < 469 and pos[0] > 501 and pos[0] < 707:
                    play = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pos2 = pygame.mouse.get_pos()
            if ExitMenu == 1:
                if pos[1] > 148 and pos[1] < 181 and pos[0] > 659 and pos[0] < 685:
                    fon = imgBG_night
                    MULTIVERSE.set_alpha(0)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pos4 = pygame.mouse.get_pos()
            if pos[1] > 25 and pos[1] < 75 and pos[0] > 700 and pos[0] < 750:
                ExitMenu = 3

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pos3 = pygame.mouse.get_pos()
            if ExitMenu == 1:
                if pos[1] > 129 and pos[1] < 181 and pos[0] > 30 and pos[0] < 80:
                    pipes.remove(pipe)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pos6 = pygame.mouse.get_pos()
            if ExitMenu == 3:
                if pos[1] > 134 and pos[1] < 184 and pos[0] > 650 and pos[0] < 698:
                    ExitMenu = 1
                    imgBACK.set_alpha(0)
                    imgBird.set_alpha(300)

    if CLOSE:
        play = False

    for i in range(len(bges)-1, -1, -1):
        bg = bges[i]
        bg.x -= 1

        if bg.right < 0:
            bges.remove(bg)

        if bges[len(bges)-1].right <= WIDTH:
            bges.append(pygame.Rect(bges[len(bges)-1].right, 0, 288, 600))

    for i in range(len(pipes)-1, -1, -1):
        pipe = pipes[i]
        pipe.x -= 3
        for h in HEARTS:
            h[0] -= 1

        if SPEED1:
            FPS = 30
        if SPEED2:
            FPS = 80
        if SPEED3:
            FPS = 60

        if state == "play" or state == "bonus":
            if pipe.x == WIDTH // 3:
                scores += 1
                dscores += 1

        if pipe.right < 0:
            pipes.remove(pipe)

        if show_heart == 2:
            HEARTS.append([600, py])
            show_heart = 0
        for k,h in enumerate(HEARTS):
            if h[0] < 0:
                HEARTS.remove(h)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                pos3 = pygame.mouse.get_pos()
                if pos[1] > 129 and pos[1] < 181 and pos[0] > 30 and pos[0] < 80:
                    pipes.remove(pipe)
                    state = "fall"
                    lives = 3
                    scores = 0
                    dscores = 0

        if RESET_b:
            pipes.remove(pipe)
            state = "fall"
            lives = 3
            scores = 0
            dscores = 0

        if scores == 20:
            state = "bonus"


        if state == "bonus":
            BOMB = pygame.Rect(750, 200, 50, 50)
            Watermmelon = pygame.Rect(750, 300, 50, 50)
            Apple = pygame.Rect(730, 400, 70, 70)
            Pineapple = pygame.Rect(750, 100, 50, 50)
            if spawn_F == 1:
                imgBOMB.set_alpha(300)
                spawn_F = r.randrange(1, 4)
            if spawn_F == 2:
                imgWatermelon.set_alpha(300)
                spawn_F = r.randrange(1, 4)
            if spawn_F == 3:
                imgApple.set_alpha(300)
                spawn_F = r.randrange(1, 4)
            if spawn_F == 4:
                imgPineapple.set_alpha(300)
                spawn_F = r.randrange(1, 4)


        if lives <= 0:
                lives = 3
                scores = 0

        if scores > maxs:
            maxs = scores

    if state == "start":
        if click and timer == 0 and len(pipes) == 0 and ExitMenu == 0:
            state = "play"

        py += (HEIGHT // 2 - py) * 0.1
        player.y = py

    elif state == "play" and mode == 1 or state == "bonus":
        if click:
            ay = -2
        else:
            ay = -0.5

        py += sy
        sy = (sy + ay + 1) * 0.98
        player.y = py

        p = r.randrange(0, 100)
        pr = p + 380
        pt = r.randrange(p, pr)

        if state == "play":
            if len(pipes) == 0 or pipes[len(pipes)-1].x < WIDTH - 300:
                pipes.append(pygame.Rect(WIDTH, p, 52, hard))
                pipes.append(pygame.Rect(WIDTH, p + 380, 52, hard))

        if player.top < 0 or player.bottom > HEIGHT:
            state = "fall"
            lives -= 1

        for pipe in pipes:
            if player.colliderect(pipe):
                state = "fall"
                lives -= 1

        for h in HEARTS:
            if player.colliderect(pygame.Rect(h[0]+1, h[1]+1, 30, 30)):
                HEARTS.remove(h)
                lives -= 1

    elif state == "fall":
        sy, ay = 0, 0
        state = "start"
        timer = 60
    else:
        pass
    



    window.fill(pygame.Color("black"))
    for bg in bges:
        window.blit(fon, bg)


    for pipe in pipes:
        if pipe.y < 350:
            rect = imgPT.get_rect(bottomleft = pipe.bottomleft)
            window.blit(imgPT, rect)
        else:
            rect = imgPB.get_rect(topleft = pipe.topleft)
            window.blit(imgPB, rect)

    image2 = imgHEAR_DIE
    Clocks = MULTIVERSE
    RESETBUTT = imgRESET
    Menushka = imgMenu
    for h in HEARTS:
        window.blit(image2, pygame.Rect(h[0], h[1], 34, 34))
    window.blit(Menushka, Menu2)
    if theme == 1:
        THEME = imgLIGHT
    if theme == 2:
        THEME = imgDARK
    if state == "start":
        if ExitMenu == 3:
            Menushka = imgOFF
            window.blit(Menushka, Menu2)
            imgBird.set_alpha(0)
            window.blit(THEME, DARK_TEM)
            MULTIVERSE.set_alpha(0)
            imgBACK.set_alpha(300)

    if event.type == pygame.MOUSEBUTTONDOWN:        
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pos5 = pygame.mouse.get_pos()
            print(pos5)
            if pos[1] > 229 and pos[1] < 294 and pos[0] > 265 and pos[0] < 331:
                if fon == imgBG:
                    theme = 2
                    fon = imgBG_night
                else:
                    theme = 1
                    fon = imgBG

    window.blit(Clocks, clock_item)
    if ExitMenu == 0:
        window.blit(RESETBUTT, RESET)
    window.blit(imgSETTING, SETTING_BUTTON)

    window.blit(imgBOMB, BOMB)
    window.blit(imgWatermelon, Watermmelon)
    window.blit(imgApple, Apple)
    window.blit(imgPineapple, Pineapple)


    image = bird.subsurface(34 * int(frame), 0 , 34, 24)
    image = pygame.transform.rotate(image, -sy * 2)
    window.blit(image, player)

    imgBack = imgBACK
    window.blit(imgBack, BACK)




    if ExitMenu == 0:
        text = font1.render("Очки: " + str(scores // 2), 1, pygame.Color("black"))
        window.blit(text, (10, 10))

        text = font1.render("Макс Очки: " + str(scores // 2), 1, pygame.Color("black"))
        window.blit(text, (10, 70))

        text = font1.render("HP: " + str(lives), 1, pygame.Color("red"))
        window.blit(text, (10, HEIGHT - 30))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
