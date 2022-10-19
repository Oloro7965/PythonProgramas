import time,pygame,random
pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('snake game in python')
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
font_style = pygame.font.SysFont(None,50)
font_style_score=pygame.font.SysFont(None,25)
record=0
def game():
    clock = pygame.time.Clock()
    game_over = False
    game_close = False
    score=0
    x = 300
    y = 300
    x1_change = 0
    y1_change = 0
    snake_sizex = 10
    snake_sizey = 10
    snake_list = []
    length_snake = 1
    x_food = (random.randrange(1,800) // 10.0) * 10.0
    y_food = (random.randrange(1,600) // 10.0) * 10.0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
        x += x1_change
        y += y1_change
        if x >= 800 or y >= 600 or x < 0 or y < 0:
            message('you lost',red,350,100)
            pygame.display.update()
            time.sleep(2)
            game_over = True
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]
        for block in snake_list[:-1]:
            if block == snake_head:
                message('You lost',red,350,100)
                pygame.display.update()
                time.sleep(2)
                game_over=True
        dis.fill(white)
        pygame.draw.rect(dis,red,[x_food,y_food,10,10])
        draw_snake(snake_list)
        score_message("Score:",20,20)
        score_message(str(score),75,20)
        pygame.display.update()
        if x == x_food and y == y_food:
            x_food = (random.randrange(1,800) // 10.0) * 10.0
            y_food = (random.randrange(1,600) // 10.0) * 10.0
            print(x_food)
            print(y_food)
            length_snake += 1
            score += 1
            print(score)
            print('bakiades')
        pygame.display.update()
        clock.tick(30)
    message('Your Score',red,350,250)
    message(str(score),red,420,300)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()
def score_message(msg,x,y):
    mesg=font_style_score.render(msg,True,red)
    dis.blit(mesg,[x,y])
def message(msg, color,x,y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y]) #350 e 100 para aviso de perdeu
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,blue,[x[0],x[1],10,10])
game()
