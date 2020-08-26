 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : Event Types and Key Press Handling In Pygame
 #    Input     : none
 #    Output    : Event Types and Key Press Handling In Pygame
 #    ------------------------------------------------------------------------------------------


import pygame
x = pygame.init()
print(x)    #  check pygame version and imported module

gameWindow = pygame.display.set_mode((600, 400))  #   display game window, set mode take a tuple as input, weidth and height
pygame.display.set_caption("My First Game")  #   give a caption of the game at the starting of the game

#   game specific variable
exit_Game = False  #    when user decide to exit the game it will be true and will exit the game
gameOver = False  #   when used won or computer won or game is tie, then it will be true and will exit the game

#   game loop will run untill game is on. it run game, take input, update position etc
#   creating game loop
while not exit_Game:
    #   this will stable game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_Game == True  #   when user quit. quit the game
            #   when outside of game loop. exit the game
            pygame.quit()
            quit()

            
        if event.type == pygame.KEYDOWN:    #   check if any key is pressed
            if event.key == pygame.K_RIGHT: #   if right arraw key is pressed it will execute the statement inside it
                print("You have pressed right arrow key")
        print(event)    #   prints all event in the game


