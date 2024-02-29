# import the pygame module
import pygame
import random

width = 1000
height = 1000

tile_width = 20
tile_height = 20

tiles_height = int(height / tile_height)
tiles_width = int(width / tile_width)

# Define the background colour
# using RGB color coding.
background_colour = (71, 237, 255)
pipe_colour = (0, 191, 41)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((750, 750))

# Set the caption of the screen
pygame.display.set_caption('Flappybird')

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

def refresh_screen():
    screen.fill(background_colour)
def draw_tile(tile_x, tile_y, color):
    pygame.draw.rect(screen, color, pygame.Rect(tile_x, tile_y, tile_width, tile_height))

def draw_pipe(x, top_height, gap):
    print(str(tiles_height) + "-(" + str(top_height) + "+" + str(gap) + ")")
    bottom_height = tiles_height-(top_height+gap)

    for bI in range(0,top_height):
        draw_tile(x, bI*tile_height, pipe_colour)
    for tI in range(top_height+gap,tiles_height):
        draw_tile(x, tI*tile_height, pipe_colour)


# x,top_height,gap
pipes = []

def add_pipe():
    pipes.append((width+tile_width, random.randint(0, tiles_height-5), random.randint(3,7)))

# game loop
while running:
    refresh_screen()
    for pipe in pipes:
        draw_pipe(pipe[0], pipe[1], pipe[2])

    pygame.display.update()

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
