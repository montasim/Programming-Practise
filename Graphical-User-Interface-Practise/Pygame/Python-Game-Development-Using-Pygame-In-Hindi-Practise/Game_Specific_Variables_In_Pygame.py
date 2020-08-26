 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : Game Specific Variables In Pygame
 #    Input     : none
 #    Output    : Game Specific Variables In Pygame
 #    ------------------------------------------------------------------------------------------


import pygame
x = pygame.init()
print(x)    #  check pygame version and imported module

gameWindow = pygame.display.set_mode((600, 400))  #   display game window, set mode take a tuple as input, weidth and height
pygame.display.set_caption("My First Game")  #   give a caption of the game at the starting of the game

#   game specific variable
exit_game = False  #    when user decide to exit the game it will be true and will exit the game
game_over = False  #   when used won or computer won or game is tie, then it will be true and will exit the game
