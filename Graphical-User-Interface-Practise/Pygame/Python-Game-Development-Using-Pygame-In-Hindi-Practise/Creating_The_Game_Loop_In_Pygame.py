 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : Creating The Game Loop In Pygame
 #    Input     : none
 #    Output    : Creating The Game Loop In Pygame
 #    ------------------------------------------------------------------------------------------


import pygame
x = pygame.init()
print(x)    #  check pygame version and imported module

gameWindow = pygame.display.set_mode((600, 400))  #   display game window, set mode take a tuple as input, weidth and height
pygame.display.set_caption("My First Game")  #   give a caption of the game at the starting of the game

#   game specific variable
exitGame = False  #    when user decide to exit the game it will be true and will exit the game
gameOver = False  #   when used won or computer won or game is tie, then it will be true and will exit the game

#   game loop will run untill game is on. it run game, take input, update position etc
#   creating game loop
while not exitGame:
    pass


#   when outside of game loop. exit the game
pygame.quit()
quit()

#   this program will run some time and after running some time it will go in the infinite while loop. so game window will hang