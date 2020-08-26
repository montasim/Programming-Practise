 #    ------------------------------------------------------------------------------------------
 #    Author    : Mohammad Montasim -Al- Mamun Shuvo
 #    Copyright : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
 #    Credits   : https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww
 #    Email     : montasimmamun@gmail.com
 #    Github    : https://github.com/montasimmamun/

 #    Date      : Created on 
 #    Version   : 1.0.1
 #    Purpose   : Snakes Game: Length Increment Logic
 #    Input     : none
 #    Output    : Snakes Game: Length Increment Logic
 #    ------------------------------------------------------------------------------------------

import pygame  #    import pygame module
import random   #   for food location

pygame.init()  #   start pygame

#   screen size input
screen_width = 300
screen_height = 400

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
snake_height = 10
snake_width = 10
snake_velocity_x = 0    #   snake velocity in x axis
snake_velocity_y = 0  #   snake velocity in y axis
init_velocity = 5

clock = pygame.time.Clock()  #   update game state with time
fps = 60  #   frame per second for game, change in a second

font = pygame.font.SysFont(None, 40)  #   get system font, set font size

#   show score to window
def screen_score(text, color, x, y):    #   set font style
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

#   game score
score = 0

#   food property
food_x = 80
food_y = 80

#   snake length
snake_list = []
snake_length = 1

def plot_snake(game_window, color, snake_list, snake_height, snake_weight):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x,
        y, snake_height, snake_width])

#   game loop
while not exit_game:
    for event in pygame.event.get():    #   get event from the game
        print(event)  #   display event
        
        if event.type == pygame.QUIT:   #   check if user tried to quit
            exit_game = True  #   if, then exit game
            
        if event.type == pygame.KEYDOWN:    #   check if any key is pressed
            if event.key == pygame.K_RIGHT: #   if right arraw key is pressed it will execute the statement inside it
                print("You have pressed right arrow key")
                snake_velocity_x = init_velocity
                snake_velocity_y = 0

            if event.key == pygame.K_LEFT: #   if left arraw key is pressed it will execute the statement inside it
                print("You have pressed left arrow key")
                snake_velocity_x = - init_velocity
                snake_velocity_y = 0
            
            if event.key == pygame.K_UP: #   if right arraw key is pressed it will execute the statement inside it
                print("You have pressed up arrow key")
                snake_velocity_y = - init_velocity
                snake_velocity_x = 0

            if event.key == pygame.K_DOWN: #   if left arraw key is pressed it will execute the statement inside it
                print("You have pressed down arrow key")
                snake_velocity_y = init_velocity
                snake_velocity_x = 0

        #   snake position
        snake_x += snake_velocity_x #   update position of snake in x axis
        snake_y += snake_velocity_y  #   update position of snake in y axis
        
        #   snake length after eating food
        snake_length += 5   #   determine snake length initially

        #   determine score, if snake collaps food update score
        if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
            score += 1
            print("Score:", score * 10)

            #   food property
            food_x = random.randint(10, screen_width/2)    #   generate random x axis location for food, food is so close to border, so move from border
            food_y = random.randint(10, screen_height/2)   #   generate random y axis location for food, food is so close to border, so move from border

        
        print(event)  #   prints all event in the game

    #   set game window color to white    
    game_window.fill(white)

    #   print score to screen
    screen_score("Score: " + str(score * 10), red, 5, 5)

    #   display food to game window
    pygame.draw.rect(game_window, red, food_x, food_y, snake_height, snake_width)


    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    #   display snake to game window
    #   

    plot_snake(game_window, black, snake_list, snake_height, snake_width)
        

    #   update display changes
    pygame.display.update()

    #   set game fps
    clock.tick(fps)

#   quit game
pygame.quit()
quit ()