import pygame
from pygame.locals import *
import random, time

pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Cars")
clock = pygame.time.Clock()

FPS = 60
speed = 5
score = 0
total_score = 0

font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game over", True, (0, 0, 0))
congratulation = small_font.render("Congratulations, you completed the game!", True, (0, 0, 0))

# background = pygame.image.load()

class enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (random.randint(100, 450), 0))

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 750:
            self.rect.top = 0
            self.rect.center = (random.randint(90, 440), 0)

class enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load()
        self.surf = pygame.Surface((50, 75))
        self.surf.fill((255, 50, 0))
        self.rect = self.surf.get_rect(center = (random.randint(550, 900), 0))

    def move(self):
        self.rect.move_ip(0, speed + 3)
        if self.rect.bottom > 750:
            self.rect.top = 0
            self.rect.center = (random.randint(540, 890), 0)

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load()
        self.surf = pygame.Surface((50, 75))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(center = (700 / 2, 750 - 150))

    def move(self):
        press = pygame.key.get_pressed()
        if self.rect.left > 0:
            if press[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 1000:
            if press[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if press[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 720:
            if press[K_DOWN]:
                self.rect.move_ip(0, 5)

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 215, 0))
        self.rect = self.surf.get_rect(center = (random.randint(50, 950), 0))

    def move(self):
        global score
        global total_score
        self.rect.move_ip(0, speed + 1)
        if self.rect.bottom > 750:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 940), 0)

p1 = player()
e1 = enemy1()
e2 = enemy2()
c1 = coin()
enemies = pygame.sprite.Group()
enemies.add(e1)
enemies.add(e2)
coins = pygame.sprite.Group()
coins.add(c1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(e2)
all_sprites.add(c1)

Inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(Inc_speed, 5000)

while True:
    for event in pygame.event.get():
        if event.type == Inc_speed:
            speed += 1
        if event.type == pygame.QUIT:
            exit()

    # screen.blit(background, (0, 0))

    scores = small_font.render(str(score), True, (255, 255, 255))
    total = small_font.render("Your total score is: " + str(total_score), True, (0, 0, 0))
    screen.blit(scores, (10, 10))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(p1, coins):
        score += 1
        total_score = score
        for entities in coins:
            entities.rect.center = (2000, 2000)
        if score == 1:
            screen.fill((40, 230, 225))
            screen.blit(congratulation, (700 / 2 - 150, 750 / 2))

            pygame.display.update()
        
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            exit()

    if pygame.sprite.spritecollideany(c1, enemies):
        c1.rect.center = (random.randint(100, 900), 0) 

    if pygame.sprite.spritecollideany(p1, enemies):
        # pygame.mixer.sound().play()
        # time.sleep(0,5)

        screen.fill((212, 212, 212))
        screen.blit(game_over, (700 / 2 - 150, 750 / 2))
        screen.blit(total, (700 / 2 - 140, 750 / 2 + 100))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        exit()

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(FPS)