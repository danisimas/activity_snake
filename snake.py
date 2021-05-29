from pygame.locals import *
from random import randint
from control.constantes import *
import time
import pygame

# Lists to store the coordinates of the snake's body parts

x_snake_position = [0]
y_snake_position = [0]
score_temp = 0

# Increasing the size of the list to potentially have 1000 sections for the snake

for i in range(0, 1000):
    x_snake_position.append(-100)
    y_snake_position.append(-100)


# Function to check if the snake hits something like fruits or itself

def collision(x_coordinates_1, y_coordinates_1, x_coordinates_2, y_coordinates_2, size_snake, size_fruit):
    if ((x_coordinates_1 + size_snake >= x_coordinates_2) or (
            x_coordinates_1 >= x_coordinates_2)) and x_coordinates_1 <= x_coordinates_2 + size_fruit:
        if ((y_coordinates_1 >= y_coordinates_2) or (
                y_coordinates_1 + size_snake >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + size_fruit:
            return True
        return False


# Function to display the player's score

def text_score(score_temp):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score_temp), True, (0, 0, 0))
    window.blit(text, (500, 0))


def life():
    pass


def bonus():
    pass


pygame.init()

# Creating the main window and giving it a name

window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")

# Blitting an image on the main window

cover = pygame.Surface(window.get_size())
cover = cover.convert()
cover.fill((144, 238, 144))
window.blit(cover, (0, 0))

# Refreshing the screen to display everything

pygame.display.flip()

# Loading the main images on the game window

head = pygame.image.load("assets/body_snake_arthur.png").convert_alpha()  # The head
head = pygame.transform.scale(head, (25, 25))

body_part_1 = pygame.image.load("assets/body_snake_arthur.png").convert_alpha()  # The body
body_part_1 = pygame.transform.scale(body_part_1, (25, 25))

fruit = pygame.image.load("assets/apple_arthur.png").convert_alpha()  # The fruit
fruit = pygame.transform.scale(fruit, (25, 25))

# Storing the head and fruit's coordinates in variables

position_1 = head.get_rect()
position_fruit = fruit.get_rect()

# Storing the variables in the list variables created before

x_snake_position[0] = position_1.x
y_snake_position[0] = position_1.y

# Giving random coordinates to the first fruit of the game

position_fruit.x = randint(2, 10) * STEP
position_fruit.y = randint(2, 10) * STEP

# Main loop for the game

while PLAYING:

    # Collecting all the events

    for event in pygame.event.get():

        # Checking if the user quits the game

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            PLAYING = False

        # Checking if the user presses a key

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                if MOVE_UP == False and MOVE_INIT == True:
                    if MOVE_DOWN == True:
                        MOVE_UP = False

                    else:

                        MOVE_DOWN = MOVE_RiGHT = MOVE_LEFT = False
                        MOVE_UP = MOVE_INIT = True

            if event.key == pygame.K_DOWN:

                if MOVE_DOWN == False:
                    if MOVE_UP == True:
                        MOVE_DOWN = False

                    else:

                        MOVE_RiGHT = MOVE_LEFT = MOVE_UP = False
                        MOVE_DOWN = MOVE_INIT = True

            if event.key == pygame.K_RIGHT:

                if MOVE_RiGHT == False:
                    if MOVE_LEFT == True:
                        MOVE_RiGHT = False

                    else:

                        MOVE_LEFT = MOVE_UP = MOVE_DOWN = False
                        MOVE_RiGHT = MOVE_INIT = True

            if event.key == pygame.K_LEFT:

                if MOVE_LEFT == False:
                    if MOVE_RiGHT == True:  # Empêchement d'aller dans la direction opposée
                        MOVE_LEFT = False

                    else:

                        MOVE_RiGHT = MOVE_DOWN = MOVE_UP = False  # Changement de la variable de déplacement
                        MOVE_LEFT = MOVE_INIT = True

    window.blit(body_part_1, (-50, 50))
    window.blit(head, (0, 0))

    # Moving each part of the body by giving them new coordinates

    for i in range(SNAKE - 1, 0, -1):
        x_snake_position[i] = x_snake_position[(i - 1)]

        y_snake_position[i] = y_snake_position[(i - 1)]

    # Filling the window with white to erase the different parts of the snake

    cover.fill((144, 238, 144))

    for i in range(1, SNAKE):
        cover.blit(body_part_1, (x_snake_position[i], y_snake_position[i]))

    # Moving the snake in a certain direction if the user presses a key

    if MOVE_UP:
        y_snake_position[0] = y_snake_position[0] - STEP
        window.blit(cover, (0, 0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if MOVE_DOWN:
        y_snake_position[0] = y_snake_position[0] + STEP
        window.blit(cover, (0, 0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if MOVE_RiGHT:
        x_snake_position[0] = x_snake_position[0] + STEP
        window.blit(cover, (0, 0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if MOVE_LEFT:
        x_snake_position[0] = x_snake_position[0] - STEP
        window.blit(cover, (0, 0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    # Calling the collision function to check if the snake hits the edges of the window

    if x_snake_position[0] < window_rect.left:
        pass

    if x_snake_position[0] + 35 > window_rect.right:
        pass

    if y_snake_position[0] < window_rect.top:
        pass

    if y_snake_position[0] + 35 > window_rect.bottom:
        pass

    # Calling the collision function to check if the snake hits itself

    if collision(x_snake_position[0], y_snake_position[0], x_snake_position[i], y_snake_position[i], 0, 0) and (
            MOVE_INIT == True):
        PLAYING = False

    window.blit(fruit, position_fruit)

    if collision(x_snake_position[0], y_snake_position[0], position_fruit.x, position_fruit.y, 35, 25):

        position_fruit.x = randint(1, 20) * STEP
        position_fruit.y = randint(1, 20) * STEP

        for j in range(0, SNAKE):

            while collision(position_fruit.x, position_fruit.y, x_snake_position[j], y_snake_position[j], 35, 25):
                position_fruit.x = randint(1, 20) * STEP
                position_fruit.y = randint(1, 20) * STEP

        # Increasing the size of the snake and the score

        SNAKE = SNAKE + 1
        score_temp = score_temp + 1

    # Displaying the score

    text_score(score_temp)

    # Flipping to add everything on the board

    pygame.display.flip()

    # Delaying the game to make the snake move fluently

    time.sleep(SPEED / 1000)

# Exiting the game if the main loop is done

pygame.quit()
exit()
