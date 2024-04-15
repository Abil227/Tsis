import pygame


pygame.init()
screen = pygame.display.set_mode((600,500))
x = 25
y = 25

run = True
clock = pygame.time.Clock()
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20
    
    if x < 25:
        x = 25
    if y < 25:
        y = 25
    if x > 600 - 25:
        x = 600 - 25
    if y > 500 - 25:
        y = 500 - 25
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,'Red',(x,y),25)
    clock.tick(500)
    pygame.display.update()
    