 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : Creating Food For Snake To Eat
 #    Input     : none
 #    Output    : Creating Food For Snake To Eat
 #    ------------------------------------------------------------------------------------------

import pygame  #    import pygame module
import random   #   for food location

pygame.init()  #   start pygame

#   screen size input
screen_width = int(input("Enter Game Width: "))
screen_height = int(input("Enter Game Height: "))

#   colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

game_window = pygame.display.set_mode((screen_width, screen_height))  #   set game window size to 600 x 400

pygame.display.set_caption("Snake Game")    #   set game name to Snake Game
pygame.display.update()

#   game specific variable
exit_game = False
game_over = False

#   snake property
snake_x = 40
snake_y = 50
snake_length = 10
snake_width = 10
snake_velocity_x = 0    #   snake velocity in x axis
snake_velocity_y = 0  #   snake velocity in y axis

clock = pygame.time.Clock()  #   update game state with time
fps = 30  #   frame per second for game, change in a second

#   food property
food_x = random.randint(0, screen_width)    #   generate random x axis location for food
food_y = random.randint(0, screen_height)   #   generate random y axis location for food

#   game loop
while not exit_game:
    for event in pygame.event.get():    #   get event from the game
        print(event)  #   display event
        
        if event.type == pygame.QUIT:   #   check if user tried to quit
            exit_game = True  #   if, then exit game
            
        if event.type == pygame.KEYDOWN:    #   check if any key is pressed
            if event.key == pygame.K_RIGHT: #   if right arraw key is pressed it will execute the statement inside it
                print("You have pressed right arrow key")
                snake_velocity_x = 10
                snake_velocity_y = 0

            if event.key == pygame.K_LEFT: #   if left arraw key is pressed it will execute the statement inside it
                print("You have pressed left arrow key")
                snake_velocity_x = -10
                snake_velocity_y = 0
            
            if event.key == pygame.K_UP: #   if right arraw key is pressed it will execute the statement inside it
                print("You have pressed up arrow key")
                snake_velocity_y = -10
                snake_velocity_x = 0

            if event.key == pygame.K_DOWN: #   if left arraw key is pressed it will execute the statement inside it
                print("You have pressed down arrow key")
                snake_velocity_y = 10
                snake_velocity_x = 0

        snake_x += snake_velocity_x #   update position of snake in x axis
        snake_y += snake_velocity_y #   update position of snake in y axis

        print(event)    #   prints all event in the game
    
    game_window.fill(white)
    pygame.draw.rect(game_window, red, [food_x, food_y, snake_length, snake_width])
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_length, snake_width])
    pygame.display.update()

    clock.tick(fps)

pygame.quit()
quit ()