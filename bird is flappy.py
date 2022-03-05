import pygame
import random as r
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 80)

imgBG = pygame.image.load("background.png")
imgBird = pygame.image.load("bird.png")
imgBird2 = pygame.image.load("bird_Skin2.png")
imgPT = pygame.image.load("pipe_top.png")
imgPB = pygame.image.load("pipe_bottom.png")
imgBG_night = pygame.image.load("background_night.png")
fon = imgBG
bird = imgBird

py, sy, ay = HEIGHT // 2, 0, 0
player = pygame.Rect(WIDTH // 3, py, 34, 24)
frame = 0
dscores = 0

state = "start"
timer = 60

pipes = []
bges = []

bges.append(pygame.Rect(0, 0, 288, 600))

lives = 3
scores = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = press[0] or keys[pygame.K_SPACE]
    
    if timer > 0:
        timer -= 1

    frame = (frame + 0.2) % 4

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

        if pipe.x == WIDTH // 3:
            scores += 1
            dscores += 1

        if dscores // 2 == 5:
            fon = imgBG_night
            bird = imgBird2
        if dscores // 2 == 10:
            fon = imgBG
            bird = imgBird
            dscores = 0

        if pipe.right < 0:
            pipes.remove(pipe)

    if state == "start":
        if click and timer == 0 and len(pipes) == 0:
            state = "play"

        py += (HEIGHT // 2 - py) * 0.1
        player.y = py
    elif state == "play":
        if click:
            ay = -2
        else:
            ay = -0.3

        py += sy
        sy = (sy + ay + 1) * 0.98
        player.y = py

        m = r.randrange(0, 200)

        if len(pipes) == 0 or pipes[len(pipes)-1].x < WIDTH - 300:
            pipes.append(pygame.Rect(WIDTH, m, 52, 200))
            pipes.append(pygame.Rect(WIDTH, m + 350, 52, 200))

        if player.top < 0 or player.bottom > HEIGHT:
            state = "fall"
            lives -= 1

        for pipe in pipes:
            if player.colliderect(pipe):
                state = "fall"
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

    image = bird.subsurface(34 * int(frame), 0 , 34, 24)
    image = pygame.transform.rotate(image, -sy * 2)
    window.blit(image, player)

    text = font1.render("Очки: " + str(scores // 2), 1, pygame.Color("black"))
    window.blit(text, (10, 10))

    text = font1.render("HP: " + str(lives), 1, pygame.Color("red"))
    window.blit(text, (10, HEIGHT - 30))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
