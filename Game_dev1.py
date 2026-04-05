import pygame
import random
import math
import sys

pygame.init()

window = pygame.display.set_mode((800, 600))



pygame.display.set_caption("space invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

space_img = pygame.image.load('space-invaders.png')

spaceX = 370
spaceY = 480
spaceX_change = 0


ghost_img = pygame.image.load('ghost.png')

ghostX = random.randint(0,735)
ghostY = random.randint(50,150)
ghostX_change = 0.3
ghostY_change = 40

bulletimg = pygame.image.load('bullet.png')
bulletimg = pygame.transform.scale(bulletimg, (40, 60))
bulletX = 0
bulletY = 480
bulletX_change = 5
bulletY_change = 5
bullet_state = "ready"

score = 0








def draw_player():
    window.blit(space_img, (spaceX, spaceY))

def draw_ghost():
    window.blit(ghost_img, (ghostX, ghostY))

def fire_bullet(X,Y):
    global bullet_state
    bullet_state= "fire"
    window.blit(bulletimg, (X+16, Y+10))


def iscollision(ghostX, ghostY, bulletX, bulletY):
    distance = math.sqrt(math.pow(ghostX-bulletX,2)+ math.pow(ghostY-bulletY,2))
    if distance <=27 :
        return True
    else:
        return False

running = True
while running:
    window.fill((0,0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceX_change = -0.5

            elif event.key == pygame.K_RIGHT:
                spaceX_change = 0.5

            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = spaceX
                    bulletY = 480
                    fire_bullet(bulletX, bulletY)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                spaceX_change = 0
            
            elif event.key == pygame.K_RIGHT:
                spaceX_change = 0

     
    spaceX += spaceX_change
    if spaceX <= 0:
        spaceX = 0
    elif spaceX > 735:
        spaceX = 735

    ghostX += ghostX_change
    if ghostX <= 0:
        ghostX_change = 0.3
        ghostY += ghostY_change
    elif ghostX >= 735:
        ghostX_change = -0.3
        ghostY += ghostY_change
    
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    collision = iscollision(ghostX, ghostY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        ghostX = random.randint(0, 735)
        ghostY = random.randint(50, 150)
        score += 1
        print("score:", score)

    

    draw_player()
    draw_ghost()
    pygame.display.update()







