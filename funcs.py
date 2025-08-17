import pygame
import random
import variables

#functions
def restart_game():
    # we don't need the global keyword here
    variables.playerX = 360
    variables.playerY = 500
    variables.playerX_change = 0
    variables.bulletX = variables.playerX
    variables.bulletY = 500
    variables.bullet_state = "ready"
    variables.score_val = 0
    variables.enemyX_change_mult = 1
    for i in range(variables.enemy_count):
        variables.enemyX[i] = random.randint(0 , 736)
        variables.enemyY[i] = random.randint(50 , 150)
        variables.enemyX_change[i] = 0.2*variables.enemyX_change_mult
        variables.enemyY_change[i] = 40

def show_score(x, y):
    score = variables.font.render("Score: " + str(variables.score_val), True, (0, 255, 255))
    variables.screen.blit(score, (x, y))

def show_lives(x, y):
    lives = variables.lives_font.render("Lives: " + str(variables.player_lives), True, (255, 0, 0))
    variables.screen.blit(lives, (x, y))

def player(x , y):
    variables.screen.blit(variables.playerImg, (x , y))

def enemy(x , y, i):
    variables.screen.blit(variables.enemyImg[i], (x , y))

def fire_bullet(x,y,flag = False):
    if flag == True:
        variables.screen.blit(variables.BeamImg, (x, y))
    else:
        variables.bullet_state = "fire"
        variables.screen.blit(variables.bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2) ** 0.5
    #"27" is from trial and error
    return distance < 27