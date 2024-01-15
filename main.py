import pygame;

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

image = pygame.image.load("lentokone.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

#koneen alkusijainti
xpos = 50
ypos = 50
#liikkumisnopeus (2px/frame)
step_x = 2
step_y = 2

while run:
    #tyhjentää ruudun edellisen framen muutokset
    screen.fill((0,0,0))

    screen.blit(image, (xpos,ypos))

    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #tarkistaa onko kone ruudulla. jos ei, vaihtaa suuntaa
    if xpos>SCREEN_WIDTH-20 or xpos<0:
        step_x = -step_x
    if ypos>SCREEN_HEIGHT-10 or ypos<0:
        step_y = -step_y
    #päivittää koneen sijainnin
    xpos += step_x #liikuttaa oikealle
    ypos += step_y #liikuttaa vasemmalle

    #laittaa muutokset näytölle
    pygame.display.flip()

    #rajoittaa framet 60:een
    clock.tick(60)

pygame.quit()