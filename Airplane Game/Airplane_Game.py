import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((900, 700))
finished = False
start = False
health = 5
score = 0
level = 1
fonts = pygame.font.SysFont('Arial', 30)
fontsed = pygame.font.SysFont('Arial', 50)
pygame.display.set_caption("Matthias's Airplane Game")

    
playerBack = pygame.image.load("Background.png")
playerBack = pygame.transform.scale(playerBack, (900, 700))
playerBack = playerBack.convert()
playerBack = playerBack.convert_alpha()
screen.blit(playerBack,(0,0))
pygame.display.flip()

playerWin = pygame.image.load("you_win.png")
playerWin = pygame.transform.scale(playerWin, (900,700))
playerWin = playerWin.convert()
playerWin = playerWin.convert_alpha()

def startScreen():
    instructions = fonts.render("Avoid the fireballs and get as many as dollar bills as you can!", True, (255,255,255))
    for i in range(10, 0, -1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        startTime = fontsed.render(f"Game starts in {i} seconds", True, (255,255,255))
        screen.blit(playerBack,(0,0))
        screen.blit(instructions,(56, 100))
        screen.blit(startTime, (190, 200))
        pygame.display.flip()
        pygame.time.wait(1000)

sound = pygame.mixer.music.load("gamesound.mp3")
pygame.mixer.music.play(100,0)

scoreT = pygame.image.load("treasure.png")
scoreT = pygame.transform.scale(scoreT, (150, 50))
scoreT = scoreT.convert()
scoreT = scoreT.convert_alpha()
xc = random.randint(30,600)
yc = random.randint(30,600)
screen.blit(scoreT,(xc,yc))


playerImage = pygame.image.load("isolated-plane-details.png")
playerImage = pygame.transform.scale(playerImage, (200, 100))
playerImage = playerImage.convert()
playerImage = playerImage.convert_alpha()
x = 600
y = 50
screen.blit(playerImage,(x,y))
pygame.display.set_icon(playerImage)


fireball = pygame.image.load("2211.w018.n002.1487B.p15.1487.png")
fireball = pygame.transform.scale(fireball, (300, 150))
fireball = fireball.convert()
fireball = fireball.convert_alpha()
q = -240
w = 30
screen.blit(fireball,(q,w))

fireball2 = pygame.image.load("2211.w018.n002.1487B.p15.1487 copy.png")
fireball2 = pygame.transform.scale(fireball2, (300, 150))
fireball2 = fireball2.convert()
fireball2 = fireball2.convert_alpha()
e = -400
r = 300
screen.blit(fireball2,(e,r))

fireball3 = pygame.image.load("2211.w018.n002.1487B.p15.1487 copy.png")
fireball3 = pygame.transform.scale(fireball3, (300, 150))
fireball3 = fireball3.convert()
fireball3 = fireball3.convert_alpha()
t = -560
u = 600
screen.blit(fireball3,(t,u))
startScreen()
start = True

while finished == False:
    for s in range(3, 0, -1):
        levelUpTime = fontsed.render(f"Game starts in {s} seconds", True, (0, 0, 0))
        if 20 <= score <= 29:
            q += 3
            e += 3
            t += 3
            level = 2
        elif 30 <=score <= 39:
            q += 4
            e += 4
            t += 4
            level = 3
        elif 30 <=score <= 49:
            q += 5
            e += 5
            t += 5
            level = 4
        elif score >= 50:
            finished = True
            
            level = 5
        else:
            q += 2
            e += 2
            t += 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True        
                
        if (x >= q-20 and x <= q+20) and (y >= w-20 and y <= w+20):
            health -= 1
            q = -240
            wl = random.randint(30,600)
            w = wl
        if (x >= e-20 and x <= e+20) and (y >= r-20 and y <= r+20):
            health -= 1
            e = -240
            rl = random.randint(30,600)
            r = rl
        if (x >= t-20 and x <= t+20) and (y >= u-20 and y <= u+20):
            health -= 1
            t = -240
            ul = random.randint(30,600)
            u = ul
        if (x >= xc-20 and x <= xc+20) and (y >= yc-20 and y <= yc+20):
            score += 1
            xc = random.randint(30,600)
            yc = random.randint(30,600)
        if health <= 0:
            finished = True
        pressedKeys = pygame.key.get_pressed()
        
        if pressedKeys[pygame.K_UP] == 1:
            y -= 2.6
        if pressedKeys[pygame.K_DOWN] == 1:
            y += 2.6
        if pressedKeys[pygame.K_LEFT] == 1:
            x -= 2.6
        if pressedKeys[pygame.K_RIGHT] == 1:
            x += 2.6
        if x >= 700:
            x = 700
        if y >= 600:
            y = 600
        if x <= 0:
            x = 0
        if y <= 0:
            y = 0
            screen.blit(playerImage,(600,50))
        if q >= 700:
            q = -240
            wl = random.randint(0,600)
            w = wl
        if e >= 700:
            e = -240 
            rl = random.randint(0,600)
            r = rl
        if t >= 700:
            t = -240 
            ul = random.randint(0,600)
            u = ul
        if finished == True:
            if score <= 49:
                print("Game over!")
                print("You highest level was", level)
                print("You highest score was", score)     
                playerEnd = pygame.image.load("gameover.png")
                playerEnd = pygame.transform.scale(playerEnd, (900, 700))
                playerEnd = playerEnd.convert()
                playerEnd = playerEnd.convert_alpha()
                screen.blit(playerEnd,(0,0))
                pygame.display.flip()
            else:
                screen.blit(playerWin,(0,0))
                pygame.display.flip()
                print("You Win!")
                print("You highest level was", level)
                print("You highest score was", score)
            
        else:
            screen.blit(playerBack,(0,0))
            screen.blit(scoreT,(xc,yc))
            screen.blit(fireball, (q,w))
            screen.blit(fireball2, (e,r))
            screen.blit(fireball3,(t,u))
            screen.blit(playerImage,(x,y))
            font = pygame.font.SysFont('Arial', 30)
            textHealth = font.render("Your health is", True, (255,255,255))
            textHealthI = font.render(str(health), True, (255,255,255))
            screen.blit(textHealth, (10,10))
            screen.blit(textHealthI, (200, 10))
            textScore = font.render("Your score is", True, (255,255,255))
            textScoreI = font.render(str(score), True, (255,255,255))
            screen.blit(textScore, (10,50))
            screen.blit(textScoreI, (190, 50))
            textLevel = font.render("Your level is", True, (255,255,255))
            textLevelI = font.render(str(level), True, (255,255,255))
            screen.blit(textLevel, (10,90))
            screen.blit(textLevelI, (180, 90))
            pygame.display.flip()


pygame.quit()
