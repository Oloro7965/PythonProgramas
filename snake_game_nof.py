import time
import pygame
pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('snake game in python')
# game_over = False
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
x = 300
y = 300
x1_change = 0
y1_change = 0
font_style = pygame.font.SysFont(None,50)
clock = pygame.time.Clock()
game_over = False
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
    if x >= 800 or y >= 600 or x <= 0 or y <= 0:
        game_over = True
    dis.fill(white)
    pygame.draw.rect(dis, blue, [x, y, 10, 10])
    pygame.display.update()
    clock.tick(30)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [300, 300])
# message('You lost', red)
pygame.display.update()
# time.sleep(10)
pygame.quit()
quit()