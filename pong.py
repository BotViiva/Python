from random import randint
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
    
#pelaajien nimeäminen
def player_naming_box():
    
    p1_name_text = text_font_medium.render (p1_name, False, (255, 255, 255))
    p2_name_text = text_font_medium.render (p2_name, False, (255, 255, 255))
    p1_name_rect.w = max(100, p1_name_text.get_width()+10)
    p2_name_rect.w = max(100, p2_name_text.get_width()+10)
    
    pygame.draw.rect(window, p1_color, p1_name_rect)
    pygame.draw.rect(window, p2_color, p2_name_rect)

    window.blit(p1_name_text, (p1_name_rect.x+5, p1_name_rect.y-8))    
    window.blit(p2_name_text, (p2_name_rect.x+5, p2_name_rect.y-8))
    
    pygame.display.flip()

#aloitusnäyttö
def start_screen ():
    window.fill((0,0,0))
    
    window.blit(title_text, title_rect)
    window.blit(start_text, start_rect)
    window.blit(controls_text, controls_rect)
    window.blit(p1_controls_info_text, p1_controls_info_rect)
    window.blit(p2_controls_info_text, p2_controls_info_rect)
    window.blit(start_space_text, start_space_rect)


#pelin aloitus
def game_start():
    countdown = [3, 2, 1, "GO!"]
    

    for index in countdown:
        window.fill((0, 0, 0,))
        score()
        countdown_surf = text_font_big.render(str(index), False, (255, 255, 255))
        countdown_rect = countdown_surf.get_rect(center = (window_size[0] // 2, window_size[1] // 2))
        window.blit(countdown_surf, countdown_rect)
        pygame.draw.line(window, (255, 255, 255), (window_size[0] // 2, 0), (window_size[0] // 2, window_size[1]))
        pygame.draw.rect(window, (255, 255, 255), p2_paddle)
        pygame.draw.rect(window, (255, 255, 255), p1_paddle)
        pygame.draw.ellipse(window, (255, 255, 255), ball)
        pygame.display.update()
        pygame.time.wait(1000)
        print(index)
        if index == "GO!":
            break
#maaliäänet
def goal_sound():
    goal_1 = pygame.mixer.Sound("assets/goal_1.wav")
    goal_2 = pygame.mixer.Sound("assets/goal_2.wav")
    goal_3 = pygame.mixer.Sound("assets/goal_3.wav")
    goal_4 = pygame.mixer.Sound("assets/goal_4.wav")
    goal = [goal_1, goal_2, goal_3, goal_4]

    goal[randint(0,3)].play()

#voittoruutu
def win_screen():
    #voittoruudun näyttöaika millisekunteina
    current_time = 5000
    while current_time > 0:
        current_time -=1

        winner_text = text_font_big.render(f'{winner}' " wins!", False, (255,255,255))
        winner_rect = winner_text.get_rect(center = (window_size[0] // 2, window_size[1] // 2))

        window.fill ((0, 0, 0))
        window.blit(winner_text, winner_rect)
        pygame.display.flip()

pygame.init()


window_size = (800,600)
window = pygame.display.set_mode((window_size))
window_rect = pygame.Rect(0,0,window_size[0],window_size[1])
pygame.display.set_caption('BonK')
FPS = pygame.time.Clock()


run = True
game_active = False
text_font_big = pygame.font.Font('assets/Grand9K.ttf', 70)
text_font_medium = pygame.font.Font('assets/Grand9K.ttf', 30)
text_font_small = pygame.font.Font('assets/Grand9K.ttf', 20)
scoreboard = [0, 0]

#aloitusnäytön muuttujat

p1_controls = "ArrowUp = up, ArrowDown = down"
p2_controls = "W = up, S = down"

title_text = text_font_big.render('BonK!', False, (255, 255, 255))
title_rect = title_text.get_rect(center = (window_size[0] // 2, window_size[1] // 8))

start_text = text_font_medium.render('START', False, (255, 255, 255))
start_rect = start_text.get_rect(center = (window_size[0] // 2, window_size[1] - 100))

start_space_text = text_font_small.render('Push space to start', False , (255, 255, 255))
start_space_rect = start_space_text.get_rect( center = (window_size[0] // 2, window_size[1] - 140))

controls_text = text_font_medium.render('Controls:', False, (255, 255, 255))
controls_rect = controls_text.get_rect( center = (window_size[0] // 2, window_size[1] // 3))

p1_controls_info_text = text_font_small.render(p1_controls, False, (255, 255, 255))
p2_controls_info_text = text_font_small.render(p2_controls, False, (255, 255, 255))
p1_controls_info_rect = p1_controls_info_text.get_rect(center = (window_size[0] // 2 + 200, controls_rect[2] + 100))
p2_controls_info_rect = p2_controls_info_text.get_rect(center = (window_size[0] // 2 - 220, controls_rect[2] + 100))

#pelaajan nimeämisen muuttujat
p1_name = "Player 1" #Oikea
p2_name = "Player 2" #Vasen

p1_name_rect = pygame.Rect(window_size[0] // 2 + 200, window_size[1] // 2, 300, 36)
p2_name_rect = pygame.Rect(window_size[0] // 2 - 300, window_size[1] // 2, 300, 36)

p1_active = False
p2_active = False
p1_color_active = (100, 100, 100)
p2_color_active = (100, 100, 100)
p1_color_passive = (150, 150, 150)
p2_color_passive = (150, 150, 150)


#peliobjektit
ball_size = 16
ball_speed_x = 3
ball_speed_y = 2
ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)
ball_hit_times = 0
hit_sound_1 = pygame.mixer.Sound('assets/paddle_1.wav')
hit_sound_2 = pygame.mixer.Sound('assets/paddle_2.wav')
paddle_width, paddle_height = (10,100)
p1_paddle = pygame.Rect(window_size[0] - paddle_width, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
p2_paddle = pygame.Rect(0, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)

winner = ""

while run:

    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and start_rect.collidepoint(pygame.mouse.get_pos()) and game_active == False and p2_name !="" and p1_name !="" : #lisää tähän ehto: pelaajilla tulee olla nimet
            game_active = True
            game_start()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            
            if p1_name_rect.collidepoint(event.pos):
                p1_name = ""
                p1_active = True
            else: 
                p1_active = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            
            if p2_name_rect.collidepoint(event.pos): 
                p2_name = ""
                p2_active = True
            else: 
                p2_active = False
        if p1_active:
            if event.type == pygame.KEYDOWN: 
            
                # tarkista backspace
                if event.key == pygame.K_BACKSPACE: 
                
                    # tyhjennä nimi 
                    p1_name = p1_name[:-1] 
                #unicode palauttaa painetun näppäimen string-muodossta
                else: 
                    p1_name += event.unicode
        if p2_active:
            if event.type == pygame.KEYDOWN: 
            
                # tarkista backspace
                if event.key == pygame.K_BACKSPACE: 
                
                    # tyhjennä nimi 
                    p2_name = p2_name[:-1] 
                #unicode palauttaa painetun näppäimen string-muodossta
                else: 
                    p2_name += event.unicode
                
        if p1_active: 
            p1_color = p1_color_active
            p2_color = p2_color_passive
            if event.type == pygame.K_KP_ENTER:
                p1_active = False
        elif p2_active:
            p2_color = p2_color_active
            p1_color = p1_color_passive
            if event.type == pygame.K_KP_ENTER:
                p2_active = False
        else:
            p1_color = p1_color_passive
            p2_color = p2_color_passive
        
        

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
        ball = pygame.Rect(ball.x, 0 + ball_size // 2 , ball_size, ball_size)

    #tarkista osuiko pallo maaliin
    
    #oikea maali
    if ball.x > window_size[0] - ball_size:
        scoreboard[1] = scoreboard[1] + 1
        ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)

        ball_hit_times = 0
        ball_speed_x = 3
        ball_speed_y = randint(-4,4)
        goal_sound()

        timer = 2000
        while timer >0:
            timer -=1
            pygame.display.flip()

        if  scoreboard[1] < 3:
            winner = p2_name
            game_start()

    #vasen maali
    if ball.x < 0 :
        scoreboard[0] = scoreboard[0] + 1
        ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)

        ball_hit_times = 0
        ball_speed_x = -3
        ball_speed_y = randint(-4,4)
        goal_sound()

        timer = 2000
        while timer >0:
            timer -=1
            pygame.display.flip()

        if scoreboard[0] < 3:
            winner = p1_name
            game_start()

    #tarkista osuuko pallo oikeaan mailaan
    if ball.colliderect(p1_paddle):
        
        ball_hit_times += 1
        if ball_hit_times == 2 :
            ball_speed_x -= 1
            ball_hit_times = 0
        if ball_hit_times == -2:
            ball_speed_x -= 1
            ball_hit_times = 0
        print(ball_hit_times, ball_speed_x)

        #ääni
        hit_sound_1.play()
        
        #muuttuja osuman sijainnille (tulos = -5/-4/-3/-2/-1/0/1/2/3/4/5/6)
        collision_area = (ball.centery - p1_paddle.top + ball_size // 2 -50) // 10
        
        #muuta suuntaa
        ball_speed_x = -ball_speed_x
        
        #muuta nopeutta
        ball_speed_y = collision_area + ball_speed_y
        
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
        
        ball_hit_times += 1
        if ball_hit_times == 2:
            ball_speed_x -= 1
            ball_hit_times = 0
        if ball_hit_times == -2:
            ball_speed_x -= 1
            ball_hit_times = 0
        print(ball_hit_times, ball_speed_x)

        #ääni
        hit_sound_2.play()

        #muuttuja osuman sijainnille
        collision_area = (ball.centery - p2_paddle.top + ball_size // 2 -50) // 10
        # muuta suuntaa
        ball_speed_x = -ball_speed_x
        # muuta nopeutta
        ball_speed_y = collision_area + ball_speed_y
    
        #tarkista maksiminopeus
        if ball_speed_y > 10:
            ball_speed_y = 10
        if ball_speed_y < -10:
            ball_speed_y = -10
        if ball_speed_x > 8:
            ball_speed_x = 8
        if ball_speed_x < -8:
            ball_speed_x = 8

    #päivitä näyttö
    pygame.display.flip()









    #piirrä aloitusnäyttö
    if game_active == False:
        
        #nollaa edellisen pelin tapahtumat
        p1_paddle = pygame.Rect(window_size[0] - paddle_width, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
        p2_paddle = pygame.Rect(0, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
        scoreboard = [0,0]
        ball_speed_x = 3
        ball_speed_y = 2
        

        
        start_screen()
        player_naming_box()

        if p1_active or p2_active :
            player_naming_box()

        if keys[pygame.K_SPACE] :
            game_active = True
            game_start()

    #piirrä peli
    if game_active:
        
        

        window.fill((0, 0, 0))
        pygame.draw.line(window, (255, 255, 255), (window_size[0] // 2, 0), (window_size[0] // 2, window_size[1]))
        pygame.draw.rect(window, (255, 255, 255), p2_paddle)
        pygame.draw.rect(window, (255, 255, 255), p1_paddle)
        pygame.draw.ellipse(window, (255, 255, 255), ball)
        score()
        ball.x += ball_speed_x
        ball.y += ball_speed_y
    
    if scoreboard[0] == 3 or scoreboard[1] == 3:
        win_screen()
        game_active = False

    
    
    
    #rajoittaa framet 60:een
    FPS.tick(60)

pygame.quit()