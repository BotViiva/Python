import pygame;
from sys import exit

#pistetaulun luonti
def score ():
    score_p1 = text_font.render(f'{scoreboard[1]}', False, (255, 255, 255))
    score_p1_rect = score_p1.get_rect(center = (window_size[0] // 2 - 70, 50))
    score_p2 = text_font.render(f'{scoreboard[0]}', False, (255, 255, 255))
    score_p2_rect = score_p2.get_rect(center = (window_size[0] // 2 + 70, 50))
    window.blit(score_p1, score_p1_rect)
    window.blit(score_p2, score_p2_rect)


pygame.init()


window_size = (800,600)
window = pygame.display.set_mode((window_size))
pygame.display.set_caption('Pong')
FPS = pygame.time.Clock()
run = True
game_active = False
text_font = pygame.font.Font('assets/Grand9K.ttf', 50)
scoreboard = [0, 0]


#peliobjektit
paddle_width, paddle_height = (20,100)
ball_size = (16)
ball_speed_x = (3)
ball_speed_y = (2)
p1_paddle = pygame.Rect(window_size[0] - paddle_width, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
p2_paddle = pygame.Rect(0, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)

#score_p1 = text_font.render(f'{scoreboard[0]}', False, (255, 255, 255))
#score_p2 = text_font.render(f'{scoreboard[1]}', False, (255, 255, 255))



while run:

    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()


    #keys muuttuja (key.get_pressed() tarkkailee kaikkia painettuja nappeja) 
    keys = pygame.key.get_pressed()    
    
    #vastustajan liikuttaminen
    if keys[pygame.K_UP] and p1_paddle.top > 0:
        p1_paddle.y -= 5
    if keys[pygame.K_DOWN] and p1_paddle.bottom < window_size[1]:
        p1_paddle.y += 5
         
    #pelaajan liikuttaminen    
    if keys[pygame.K_w] and p2_paddle.top > 0:
        p2_paddle.y -= 5
    if keys[pygame.K_s] and p2_paddle.bottom < window_size[1]:
        p2_paddle.y += 5

    # Liikuta palloa
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #tarkista osuiko pallo pohjaan 
    if ball.bottom > window_size[1]:
        ball = pygame.Rect(ball.x, window_size[1] - ball_size, ball_size, ball_size)
        ball_speed_y = -ball_speed_y

    #tarkista osuiko pallo kattoon
    if ball.top < 0 :
        ball = pygame.Rect(ball.x, 0 + ball_size , ball_size, ball_size)
        ball_speed_y = -ball_speed_y

    #tarkista osuiko pallo maaliin
    if ball.x >= window_size[0] - ball_size:
        ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)
        scoreboard[1] = scoreboard[1] + 1
        print(scoreboard)

    if ball.x <= 0 :
        ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)
        scoreboard[0] = scoreboard[0] + 1
        print(scoreboard)
        
    #tarkista osuuko pallo oikeaan mailaan
    if ball.colliderect(p1_paddle):
        
        #muuttuja osuman sijainnille
        collision_area = ball.y - p1_paddle.top + ball_size // 2
        
        #tarkista osuman sijainti ja muuta suunta ja nopeus
        if collision_area >=20 and collision_area < 35:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y - 0.5
        elif collision_area >=0 and collision_area < 20:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y - 1        
        elif collision_area < 0:
            ball_speed_x = -ball_speed_x
            if ball_speed_y > 0:    
                ball_speed_y = -ball_speed_y
            else:
                ball_speed_y = ball_speed_y + 1
        elif collision_area >65 and collision_area <= 80:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y + 0.5
        elif collision_area >80 and collision_area <= 100:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y + 1        
        elif collision_area > 100:
            ball_speed_x = -ball_speed_x
            if ball_speed_y < 0:    
                ball_speed_y = -ball_speed_y
            else:
                ball_speed_y = ball_speed_y -1
        else:
            ball_speed_x = -ball_speed_x
    
    #tarkista osuuko pallo vasempaan mailaan
    if ball.colliderect(p2_paddle):
        
        #muuttuja osuman sijainnille
        collision_area = ball.y - p2_paddle.top
        
        #tarkista osuman sijainti ja muuta nopeutta
        if collision_area >=20 and collision_area < 35:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y - 0.5
        elif collision_area >=0 and collision_area < 20:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y - 1        
        elif collision_area < 0:
            ball_speed_x = -ball_speed_x
            if ball_speed_y < 0:
                ball_speed_y = ball_speed_y - 1.5
            else:
                ball_speed_y = -ball_speed_y     
        elif collision_area >65 and collision_area <= 80:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y + 0.5
        elif collision_area >80 and collision_area <= 100:
            ball_speed_x = -ball_speed_x
            ball_speed_y = ball_speed_y + 1        
        elif collision_area > 100:
            ball_speed_x = -ball_speed_x
            if ball_speed_y > 0:
                ball_speed_y = ball_speed_y + 1.5
            else:
                ball_speed_y = -ball_speed_y       
        else:
            ball_speed_x = -ball_speed_x
        
    
    #päivitä näyttö
    pygame.display.flip()

    #piirrä elementit
    window.fill((0, 0, 0))
    pygame.draw.line(window, (255, 255, 255), (window_size[0] // 2, 0), (window_size[0] // 2, window_size[1]))
    pygame.draw.rect(window, (255, 255, 255), p2_paddle)
    pygame.draw.rect(window, (255, 255, 255), p1_paddle)
    pygame.draw.ellipse(window, (255, 255, 255), ball)
    score()
    

    #rajoittaa framet 60:een
    FPS.tick(60)

pygame.quit()