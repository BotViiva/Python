import pygame;

pygame.init()
window_size = (800,600)

window = pygame.display.set_mode((window_size))
pygame.display.set_caption('Pong')
FPS = pygame.time.Clock()
run = True
xpos = 400
ypos = 300

paddle_width, paddle_height = (20,100)
ball_size = (15)
ball_speed_x = (3)
ball_speed_y = (3)


player_paddle = pygame.Rect(0, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(window_size[0] - paddle_width, window_size[1] // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)

while run:

    #tapa poistua loopista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #keys muuttuja
    keys = pygame.key.get_pressed()    
    
    #vastustajan liikuttaminen
    if keys[pygame.K_UP] and opponent_paddle.top > 0:
        opponent_paddle.y -= 5
    if keys[pygame.K_DOWN] and opponent_paddle.bottom < window_size[1]:
        opponent_paddle.y += 5
         
    #pelaajan liikuttaminen    
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_s] and player_paddle.bottom < window_size[1]:
        player_paddle.y += 5

    # Liikuta palloa
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #tarkista osuiko pallo maaliin
    if ball.x <= 0 or ball.x >= window_size[0] - ball_size:
        ball = pygame.Rect(window_size[0] // 2 - ball_size // 2, window_size[1] // 2 - ball_size // 2, ball_size, ball_size)

  
    #tarkista osuuko pallo vastustajan mailaan
    if ball.colliderect(opponent_paddle):
        
        #tarkista osuman sijainti ja muuta nopeutta
        if ball.y >= opponent_paddle.top and ball.y <= opponent_paddle.top + 20:
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y
            print("osui yläkulmaan")
        elif ball.y >= opponent_paddle.top and ball.y <= opponent_paddle.top + 40:
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y
            print("osui keskiylä")
        elif ball.y <= opponent_paddle.bottom and ball.y >= opponent_paddle.bottom - 20:
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y
            print("osui alakulmaan")
        elif ball.y <= opponent_paddle.bottom and ball.y >= opponent_paddle.bottom - 40:
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y
            print("osui keskiala")
        else:
            ball_speed_x = -ball_speed_x
            print("osui keskelle")
        
    
    #tarkista osuuko pallo pelaajan mailaan
    if ball.colliderect(player_paddle):
        
        #tarkista osuman sijainti ja muuta nopeutta
        if ball.y >= player_paddle.top and ball.y <= player_paddle.top + 20:
            ball_speed_x = -ball_speed_x
            print("osui yläkulmaan")
        elif ball.y >= player_paddle.top and ball.y <= player_paddle.top + 40:
            ball_speed_x = -ball_speed_x
            print("osui keskiylä")
        elif ball.y <= player_paddle.bottom and ball.y >= player_paddle.bottom - 20:
            ball_speed_x = -ball_speed_x
            print("osui alakulmaan")
        elif ball.y <= player_paddle.bottom and ball.y >= player_paddle.bottom - 40:
            ball_speed_x = -ball_speed_x
            print("osui keskiala")
        else:
            ball_speed_x = -ball_speed_x
            print("osui keskelle")
        
    #tarkista osuuko pallo ylä- tai alarajaan
    if ball.top <= 0 or ball.bottom >= window_size[1]:
        ball_speed_y = -ball_speed_y

    #päivitä näyttö
    pygame.display.flip()

    #piirrä elementit
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), player_paddle)
    pygame.draw.rect(window, (255, 255, 255), opponent_paddle)
    pygame.draw.ellipse(window, (255, 255, 255), ball)

    #rajoittaa framet 60:een
    FPS.tick(60)

pygame.quit()