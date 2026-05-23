import pygame
from sys import exit

# --------------------
# CONSTANTS
# --------------------
GAME_WIDTH = 900
GAME_HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
PLAYER_SPEED = 5
JUMP_SPEED = -13
GRAVITY = 0.5
FLOOR_Y = 440

# --------------------
# INIT
# --------------------
pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Matthias's Platformer Game")
clock = pygame.time.Clock()

# --------------------
# IMAGES
# --------------------
background_image = pygame.image.load("platformer.png").convert()
background_image = pygame.transform.scale(background_image, (900, 600))

player_image_right = pygame.image.load("playerR.png")
player_image_right = pygame.transform.scale(player_image_right, (60, 60))
pygame.display.set_icon(player_image_right)

player_image_left = pygame.image.load("playerL.png")
player_image_left = pygame.transform.scale(player_image_left, (60, 60))

player_image_jumpR = pygame.image.load("playerJR.png")
player_image_jumpR = pygame.transform.scale(player_image_jumpR, (80, 80))

player_image_jumpL = pygame.image.load("playerJL.png")
player_image_jumpL = pygame.transform.scale(player_image_jumpL, (80, 80))

playerBullet_img = pygame.image.load("kirbyBullet.png")
playerBullet_img = pygame.transform.scale(playerBullet_img, (40, 40))

enemy_img = pygame.image.load("kirby_enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (60, 50))

playershootR = pygame.image.load("kirbyAttackR.png")
playershootR = pygame.transform.scale(playershootR, (60, 60))

playershootL = pygame.image.load("kirbyAttackL.png")
playershootL = pygame.transform.scale(playershootL, (60, 60))

health_tower = pygame.image.load("tower.png")
health_tower = pygame.transform.scale(health_tower, (600, 600))

# --------------------
# SPRITE GROUPS
# --------------------
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# --------------------
# CLASSES
# --------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image_right
        self.rect = self.image.get_rect(topleft=(245, FLOOR_Y - PLAYER_HEIGHT))

        self.vel_x = 0
        self.vel_y = 0
        self.direction = "right"
        self.jumping = False

    def update(self):
        # Gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Horizontal movement
        self.rect.x += self.vel_x

        # Floor collision
        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.vel_y = 0
            self.jumping = False

        # Screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GAME_WIDTH:
            self.rect.right = GAME_WIDTH

        self.update_image()

    def update_image(self):
        if self.jumping:
            self.image = player_image_jumpR if self.direction == "right" else player_image_jumpL
        else:
            self.image = player_image_right if self.direction == "right" else player_image_left

    def shoot(self):
        bullet = Bullet(self)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = playerBullet_img
        self.rect = self.image.get_rect(center=player.rect.center)

        self.speed = 8 if player.direction == "right" else -8

    def update(self):
        self.rect.x += self.speed

        if self.rect.right < 0 or self.rect.left > GAME_WIDTH:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = -3

    def update(self):
        self.rect.x += self.speed

        # Bounce off walls
        if self.rect.left <= 0 or self.rect.right >= GAME_WIDTH:
            self.speed *= -1

# --------------------
# CREATE OBJECTS
# --------------------
player = Player()
enemy1 = Enemy(700, FLOOR_Y - 50)

all_sprites.add(player, enemy1)
enemies.add(enemy1)

# --------------------
# GAME LOOP
# --------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.direction == "right":
                player.image = playershootR
                window.blit(player.image, (player))
                player.update_image()
                player.shoot()
            if event.key == pygame.K_SPACE and player.direction == "left":
                player.image = playershootL
                window.blit(player.image, (player))
                player.update_image()
                player.shoot()
            if event.key in (pygame.K_UP, pygame.K_w) and not player.jumping:
                player.vel_y = JUMP_SPEED
                player.jumping = True

    # INPUT
    keys = pygame.key.get_pressed()
    player.vel_x = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.vel_x = -PLAYER_SPEED
        player.direction = "left"

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.vel_x = PLAYER_SPEED
        player.direction = "right"

    # UPDATE
    all_sprites.update()

    # Player ↔ Enemy collision → reverse enemy
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            enemy.speed *= -1

    # DRAW
    window.blit(background_image, (0, 0))
    window.blit(health_tower, (-170, -60))

    for sprite in all_sprites:
        window.blit(sprite.image, sprite.rect)

    pygame.display.update()
    clock.tick(FPS)
