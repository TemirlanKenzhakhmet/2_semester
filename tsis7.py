import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
let1 = pygame.font.SysFont('serif', 15)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #графики косинуса и синуса 
    for x in range(100, 700):
        sy1 = 240 * math.sin((x - 100) / 100 * math.pi)
        sy2 = 240 * math.sin((x - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, red, False, [(x, 280 + sy1), ((x + 1), 280 + sy2)])
    for x in range(100, 700, 2):
        cy1 = 240 * math.cos((x - 100) / 100 * math.pi)
        cy2 = 240 * math.cos((x - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, blue, False, [(x, 280 + cy1), ((x + 1), 280 + cy2)])
    #линии в таблице
    for x in range(100, 701, 100):
        pygame.draw.line(screen, black, [x, 20], [x, 540], 1)
        if x == 400:
            pygame.draw.line(screen, black, [400, 20], [400, 540], 2)
    for y in range(40, 521, 60):
        pygame.draw.line(screen, black, [80, y], [720, y], 1)
        if y == 280:
            pygame.draw.line(screen, black, [80, 280], [720, 280], 2)
    #черточки
    for x in range(150, 651, 100):
        pygame.draw.line(screen, black, [x, 20], [x, 35], 1)
        pygame.draw.line(screen, black, [x, 525], [x, 540], 1)
    for x in range(125, 676, 50):
        pygame.draw.line(screen, black, [x, 20], [x, 30], 1)
        pygame.draw.line(screen, black, [x, 530], [x, 540], 1)
    for x in range(112, 688, 25):
        pygame.draw.line(screen, black, [x, 20], [x, 25], 1)
        pygame.draw.line(screen, black, [x, 535], [x, 540], 1)
    for y in range(70, 491, 60):
        pygame.draw.line(screen, black, [80, y], [90, y], 1)
        pygame.draw.line(screen, black, [710, y], [720, y], 1)
    for y in range(55, 506, 30):
        pygame.draw.line(screen, black, [80, y], [85, y], 1)
        pygame.draw.line(screen, black, [715, y], [720, y], 1)
    #значения
    screen.blit(let1.render('-3п', False, black), (95, 550))
    screen.blit(let1.render('-5п/2', False, black), (145, 550))
    screen.blit(let1.render('-2п', False, black), (195, 550))
    screen.blit(let1.render('-3п/2', False, black), (245, 550))
    screen.blit(let1.render('-п', False, black), (295, 550))
    screen.blit(let1.render('-п/2', False, black), (345, 550))
    screen.blit(let1.render('0', False, black), (395, 550))
    screen.blit(let1.render('п/2', False, black), (445, 550))  
    screen.blit(let1.render('п', False, black), (495, 550)) 
    screen.blit(let1.render('3п/2', False, black), (545, 550))
    screen.blit(let1.render('2п', False, black), (595, 550))
    screen.blit(let1.render('5п/2', False, black), (645, 550))
    screen.blit(let1.render('3п', False, black), (695, 550))

    screen.blit(let1.render('1.00', False, black), (40, 30))
    screen.blit(let1.render('0.75', False, black), (40, 90))
    screen.blit(let1.render('0.50', False, black), (40, 150))
    screen.blit(let1.render('0.25', False, black), (40, 210))
    screen.blit(let1.render('0.00', False, black), (40, 270))
    screen.blit(let1.render('-0.25', False, black), (40, 330))
    screen.blit(let1.render('-0.50', False, black), (40, 390))
    screen.blit(let1.render('-0.75', False, black), (40, 450))  
    screen.blit(let1.render('-1.00', False, black), (40, 510)) 
    screen.blit(let1.render('sin x', False, black), (510, 50))
    screen.blit(let1.render('cos x', False, black), (510, 65))
    
    pygame.draw.line(screen, red, [550, 60], [565, 60], 3)
    pygame.draw.line(screen, blue, [550, 75], [565, 75], 3)

    screen.blit(let1.render('-3', False, black), (110, 320)) 
    screen.blit(let1.render('-2', False, black), (180, 320))
    screen.blit(let1.render('-1', False, black), (260, 320))
    
    pygame.draw.rect(screen, black, pygame.Rect(80, 20, 640, 520), 2)
    pygame.display.flip()