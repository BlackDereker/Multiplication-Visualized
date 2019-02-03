import pygame
import math

pygame.init()

size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Math")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 30)

Z = 0
K = 250
radius = size[0] / 2.1

def calculate_points():
    points = [[0,0] for i in range(K)]
    angle = 0
    for i in range(K):
        x = int(math.cos(math.radians(angle)) * radius + size[0] / 2)
        y = int(math.sin(math.radians(angle)) * radius + size[1] / 2)
        points[i] = [x, y]
        angle += 360 / K
    return points

def draw():
    screen.fill((0,0,0))
    for point in points:
        pygame.draw.circle(screen, (255,0,0), point, 1)
    for i in range(K):
        target = int((i * Z)) % K
        pygame.draw.line(screen, (255,255,255), points[i], points[target])
    z_info = font.render('Z: {0:.3f}'.format(Z), True, (255,255,255))
    k_info = font.render('K: {0}'.format(K), True, (255,255,255))
    screen.blit(z_info, (0,0))
    screen.blit(k_info, (0,30))

points = calculate_points()

draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Z += 0.005
        draw()
    elif keys[pygame.K_DOWN]:
        Z -= 0.005
        draw()
    if keys[pygame.K_LEFT] and K > 0:
        K -= 1
        points = calculate_points()
        draw()
    elif keys[pygame.K_RIGHT]:
        K += 1
        points = calculate_points()
        draw()
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
