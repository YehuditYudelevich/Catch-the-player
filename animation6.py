import pygame
import sys
import random
import math
pygame.init()

WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation6")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

gray=(255,182,193)
radios = 40
# טעינת התמונה של השחקן
image = pygame.image.load("im.png")
image = pygame.transform.scale(image, (200, 200)) 
im=pygame.image.load("images.png")
im = pygame.transform.scale(im,(int(radios*1.7),int(radios*1.7))) 

player_x, player_y = WIDTH // 2, HEIGHT // 2
balls = []
speed = 2
new_ball_timer = 0  
def move():
    screen.fill(gray)
    screen.blit(image, (player_x, player_y))
    for b in balls:
        pygame.draw.circle(screen, WHITE, (int(b[0]), int(b[1])), radios)
        screen.blit(im,(int(b[0] - im.get_width() // 2), int(b[1] - im.get_height() // 2))) 

    pygame.display.flip()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5 
    for b in balls:
        dx = player_x - b[0]
        dy = player_y - b[1]
        dist = math.sqrt(dx**2 + dy**2)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        b[0] += dx * speed
        b[1] += dy * speed
        
        for other in balls:
            if other != b:
                distance = math.sqrt((b[0] - other[0])**2 + (b[1] - other[1])**2)
                if distance < 2 * radios:  
                    overlap = 2 * radios - distance
                    angle = math.atan2(b[1] - other[1], b[0] - other[0])
                    b[0] += overlap * math.cos(angle) / 2
                    b[1] += overlap * math.sin(angle) / 2
                    other[0] -= overlap * math.cos(angle) / 2
                    other[1] -= overlap * math.sin(angle) / 2
    
    
    new_ball_timer += 1
    if new_ball_timer >= 60:
        new_ball_timer = 0
        if len(balls) > 30:
            font=pygame.font.Font(None,80)
            text=font.render("You are the cutest student ever!!",True,RED)
            screen.blit(text,(0,100))
            pygame.display.flip()
            pygame.time.wait(4000)
            running=False
        a = random.randint(radios, WIDTH - radios)
        b = random.randint(radios, HEIGHT - radios)
        while any(math.sqrt((a - bx)**2 + (b - by)**2) < 2 * radios for bx, by in balls):
            a = random.randint(radios, WIDTH - radios)
            b = random.randint(radios, HEIGHT - radios)
        balls.append([a, b])
    move()
    clock.tick(120)
