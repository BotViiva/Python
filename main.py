import pygame;

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

image = pygame.image.load("lentokone.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = pygame.time.Clock()
run = True

#koneen koko
width = 17
height = 9

#koneen alkusijainti
xpos = 400
ypos = 300
#liikkumisnopeus (1px/frame)
vel = 1

while run:
    #tyhjentää ruudun edellisen framen muutokset
    screen.fill((0,0,0))

    screen.blit(image, (xpos,ypos))

    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #tarkistaa onko kone ruudulla. jos ei, vaihtaa suuntaa
    keys = pygame.key.get_pressed() 
      
    # vasen nuoli painettuna
    if keys[pygame.K_LEFT] and xpos>0: 
          
        # vähennys x-koordinaattiin 
        xpos -= vel 
          
    # oikea nuoli painettuna 
    if keys[pygame.K_RIGHT] and xpos<800-width: 
          
        # lisäys x-koordinaattiin 
        xpos += vel 
         
    # ylös nuoli painettuna    
    if keys[pygame.K_UP] and ypos>0: 
          
        # vähennys y-koordinaattiin 
        ypos -= vel 
          
    # alas nuoli painettuna    
    if keys[pygame.K_DOWN] and ypos<600-height: 
        # lisäys y-koordinaattiin 
        ypos += vel 

    #laittaa muutokset näytölle
    pygame.display.update()

    #rajoittaa framet 60:een
    FPS.tick(60)

pygame.quit()

#https://dr0id.bitbucket.io/legacy/pygame_tutorials.html