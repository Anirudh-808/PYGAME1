import pygame
import random

#other stuff
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Practice")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

#score
score_val = 0
font = pygame.font.Font("freesansbold.ttf", 30)

#player stuff
playerImg = pygame.image.load("battleship.png")
playerX = 360
playerY = 500
playerX_change = 0

#enemy stuff
#using lists for more than one enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_count = 8

for i in range(enemy_count):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0 , 736))
    enemyY.append(random.randint(50 , 150))
    enemyX_change.append(0.2)
    enemyY_change.append(40)

#bullet stuff
bulletImg = pygame.image.load("laser.png")
bulletX = playerX
bulletY = 500
bulletY_change = 0.9
bullet_state = "ready"  # "ready" - you can't see the bullet, "fire" - the bullet is moving