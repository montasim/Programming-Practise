 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : display game window
 #    Input     : none
 #    Output    : game window
 #    ------------------------------------------------------------------------------------------


import pygame
x = pygame.init()
print(x)    #  check pygame version and imported module

gameWindow = pygame.display.set_mode((600, 400))    #   display game window, set mode take a tuple as input, weidth and height