import pygame;

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = pygame.Rect((300, 250, 50, 50))
run = True

while run:
    #tyhjentää ruudun edellisen framen muutokset
    screen.fill((0,0,0))
    #piirtää pelaajan
    pygame.draw.rect(screen, (255, 0, 0), player)
    #liikuttaa pelaajaa
    key = pygame.key.get_pressed()
    if key [pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key [pygame.K_d] == True:
        player.move_ip(1, 0)
    if key [pygame.K_s] == True:
        player.move_ip(0, 1)
    if key [pygame.K_w] == True:
        player.move_ip(0, -1)
    
    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick(60)

pygame.quit()