 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : Creating Ground For Our Snakes Game
 #    Input     : none
 #    Output    : Creating Ground For Our Snakes Game
 #    ------------------------------------------------------------------------------------------

import pygame  # import pygame module

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

running = True
#   game loop
while running:
    for event in pygame.event.get():    #   get event from the game
        print(event)  #   display event
        
        if event.type == pygame.QUIT:
            exit_game = True
            running = False
    
    game_window.fill(white)
    pygame.display.update()
