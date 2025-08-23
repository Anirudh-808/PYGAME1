import pygame
import random

from pygame import mixer

pygame.init()

import variables
from funcs import *

# to make sure the speedup is gradual
last_speedup_score = 0

#to check if game is over
game_over = False

#background
mixer.music.load("BackOnTrack.mp3")
mixer.music.set_volume(0.5)  # Set volume to 50%
mixer.music.play(-1)  # -1 means loop indefinitely

#game loop
running = True
while running:
    variables.screen.fill((0,0,0))

    #exit logic and keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                variables.playerX_change = -0.4
            if event.key == pygame.K_d:
                variables.playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                #to make sure bullet can only be shot is it is READY
                if variables.bullet_state == "ready":
                    variables.bulletX = variables.playerX
                    variables.bulletY = variables.playerY
                    variables.bullet_state = "fire"
                    mixer.Sound("laser2.mp3").play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                variables.playerX_change = 0

    #player boundary logic and motion
    variables.playerX += variables.playerX_change

    if variables.playerX <= 0:
        variables.playerX = 0
    elif variables.playerX >= 736:
        variables.playerX = 736

    #enemy boundary logic and collision check and motion
    if not game_over:
        for i in range(variables.enemy_count):
            #game over logic
            if variables.enemyY[i] > 440:
                variables.player_lives -= 1
                print("Player lives left:", variables.player_lives)
                #resetting the enemy
                variables.enemyX[i] = random.randint(0 , 736)
                variables.enemyY[i] = random.randint(50 , 150)

                if variables.player_lives == 0:
                    mixer.music.stop()
                    for j in range(variables.enemy_count):
                        variables.enemyY[j] = 2000  # move enemy off screen
                    game_over = True  # Set game over flag   

            variables.enemyX[i] += variables.enemyX_change[i]*variables.enemyX_change_mult

            if variables.enemyX[i] <= 0:
                variables.enemyX_change[i] = abs(variables.enemyX_change[i])
                variables.enemyY[i] += variables.enemyY_change[i]
            elif variables.enemyX[i] > 736:
                variables.enemyX_change[i] = -(variables.enemyX_change[i])
                variables.enemyY[i] += variables.enemyY_change[i]

            #collision check
            if variables.bullet_state == "fire" and isCollision(variables.enemyX[i], variables.enemyY[i], variables.bulletX, variables.bulletY):
                variables.score_val += 1
                variables.bulletY = 500
                variables.bullet_state = "ready"
                #respawn enemy
                variables.enemyX[i] = random.randint(0 , 736)
                variables.enemyY[i] = random.randint(50 , 150)

            enemy(variables.enemyX[i], variables.enemyY[i], i)

    else:
        game_over_font = pygame.font.Font("freesansbold.ttf", 64)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        new_game_text = variables.font.render("Press 'N' to Restart", True, (255, 255, 255))
        variables.screen.blit(game_over_text, (200, 250))
        variables.screen.blit(new_game_text, (210, 320))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    #restart game
                    restart_game()
                    mixer.music.play(-1)
                    game_over = False #reset the game over flag
            else:
                break

    #check if bullet hits the boundary
    #if so send it back to ready state
    if variables.bulletY < 0:
        variables.bulletY = 500
        variables.bullet_state = "ready"
    #bullet motion
    if variables.bullet_state == "fire":
        fire_bullet(variables.bulletX, variables.bulletY)
        variables.bulletY -= variables.bulletY_change

    # enemy speedup
    if variables.score_val % 5 == 0 and variables.score_val >= 5 and variables.score_val != last_speedup_score:
        #increase enemy speed
        variables.enemyX_change_mult += 0.1
        last_speedup_score = variables.score_val

    player(variables.playerX, variables.playerY)
    show_score(10, 10)
    show_lives(650, 10)
    pygame.display.update()