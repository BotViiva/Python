import pygame;
from sys import exit

#pistetaulun luonti
def score ():
    score_p1_text = text_font_big.render(f'{scoreboard[1]}', False, (255, 255, 255))
    score_p1_rect = score_p1_text.get_rect(center = (window_size[0] // 2 - 70, 50))
    score_p2_text = text_font_big.render(f'{scoreboard[0]}', False, (255, 255, 255))
    score_p2_rect = score_p2_text.get_rect(center = (window_size[0] // 2 + 70, 50))
    window.blit(score_p1_text, score_p1_rect)
    window.blit(score_p2_text, score_p2_rect)
    

#aloitusnäyttö
def start_screen ():
    window.fill((0,0,0))
    
    window.blit(title_text, title_rect)
    window.blit(start_text, start_rect)
    window.blit(controls_text, controls_rect)
    window.blit(controls_info_text, controls_info_rect)
    window.blit(start_space_text, start_space_rect)
    

pygame.init()


window_size = (800,600)
window = pygame.display.set_mode((window_size))
pygame.display.set_caption('Pong')
FPS = pygame.time.Clock()
run = True
game_active = False
text_font_big = pygame.font.Font('assets/Grand9K.ttf', 70)
text_font_medium = pygame.font.Font('assets/Grand9K.ttf', 30)
text_font_small = pygame.font.Font('assets/Grand9K.ttf', 10)
scoreboard = [0, 0]

#aloitusnäytön muuttujat
title_text = text_font_big.render('Bong!', False, (255, 255, 255))
title_rect = title_text.get_rect(center = (window_size[0] // 2, window_size[1] // 8))
start_text = text_font_medium.render('START', False, (255, 255, 255))
start_rect = start_text.get_rect(center = (window_size[0] // 2, window_size[1] - 100))
start_space_text = text_font_small.render('Push space to start', False , (255, 255, 255))
start_space_rect = start_space_text.get_rect( center = (window_size[0] // 2, window_size[1] - 140))
controls_text = text_font_medium.render('Controls:', False, (255, 255, 255))
controls_rect = controls_text.get_rect( center = (window_size[0] // 2, window_size[1] // 3))
controls_info_text = text_font_small.render('W = up, S = down           ArrowUp = up, ArrowDown = down', False, (255, 255, 255))
controls_info_rect = controls_info_text.get_rect(center = (window_size[0] // 2, controls_rect[2] + 100))

#peliobjektit
paddle_width, paddle_height = (10,100)
ball_size = (16)
ball_speed_x = (3)
ball_speed_y = (2)
p1_paddle = pygame.Rect(window_size[0] - paddle_width, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
p2_paddle = pygame.Rect(0, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)


while run:

    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and start_rect.collidepoint(pygame.mouse.get_pos()) :
            game_active = True


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

    

    #tarkista osuiko pallo pohjaan 
    if ball.bottom > window_size[1]:
        ball = pygame.Rect(ball.x, window_size[1] - ball_size, ball_size, ball_size)
        ball_speed_y = -ball_speed_y

    #tarkista osuiko pallo kattoon
    if ball.top <= 0 :
        ball_speed_y = -ball_speed_y
        ball = pygame.Rect(ball.x, 0 + ball_size , ball_size, ball_size)

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
        
        #muuttuja osuman sijainnille (tulos = -5/-4/-3/-2/-1/0/1/2/3/4/5/6)
        collision_area = (ball.centery - p1_paddle.top + ball_size // 2 -50) // 10
        #muuta suuntaa
        ball_speed_x = -ball_speed_x
        
        #muuta nopeutta
        ball_speed_y = collision_area + ball_speed_y
        print(collision_area, ball_speed_x, ball_speed_y)
        
        #tarkista maksiminopeus
        if ball_speed_y > 10:
            ball_speed_y = 10
        if ball_speed_y < -10:
            ball_speed_y = -10
        if ball_speed_x > 6:
            ball_speed_x = 6
        if ball_speed_x < -6:
            ball_speed_x = -6
    #tarkista osuuko pallo vasempaan mailaan
    if ball.colliderect(p2_paddle):
        
        #muuttuja osuman sijainnille
        collision_area = (ball.centery - p2_paddle.top + ball_size // 2 -50) // 10
        # muuta suuntaa
        ball_speed_x = -ball_speed_x
        # muuta nopeutta
        ball_speed_y = collision_area + ball_speed_y
        print(collision_area, ball_speed_x, ball_speed_y)
    
        #tarkista maksiminopeus
        if ball_speed_y > 10:
            ball_speed_y = 10
        if ball_speed_y < -10:
            ball_speed_y = -10
        if ball_speed_x > 6:
            ball_speed_x = 6
        if ball_speed_x < -6:
            ball_speed_x = -6

    #päivitä näyttö
    pygame.display.flip()

    if game_active == False:
        
        scoreboard = [0,0]
        
        start_screen()

        if keys[pygame.K_SPACE] :
            game_active = True
        
        

    #piirrä elementit
    if game_active:

        
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        window.fill((0, 0, 0))
        pygame.draw.line(window, (255, 255, 255), (window_size[0] // 2, 0), (window_size[0] // 2, window_size[1]))
        pygame.draw.rect(window, (255, 255, 255), p2_paddle)
        pygame.draw.rect(window, (255, 255, 255), p1_paddle)
        pygame.draw.ellipse(window, (255, 255, 255), ball)
        score()
    
    if scoreboard[0] == 3:
        game_active = False
    if scoreboard[1] == 3:
        game_active = False

    #rajoittaa framet 60:een
    FPS.tick(60)

pygame.quit()