# import the pygame module
import pygame
import random
import time

pygame.init()
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
screen = pygame.display.set_mode((width, height))

# Set the caption of the screen
pygame.display.set_caption('Flappybird')

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True
playing = True

def game_over():
    global playing
    game_over_screen_fade = pygame.Surface((width, height))
    game_over_screen_fade.fill((0, 0, 0))
    game_over_screen_fade.set_alpha(160)
    screen.blit(game_over_screen_fade, (0, 0))

    font = pygame.font.Font(None, 75)
    text = font.render("GAME OVER", True, (255,255,255))
    text_rect = text.get_rect(center=(width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.update()
    playing = False

def refresh_screen():
    screen.fill(background_colour)
def draw_tile(tile_x, tile_y, color):
    pygame.draw.rect(screen, color, pygame.Rect(tile_x, tile_y, tile_width, tile_height))

def draw_pipe(x, top_height, bottom_height):
    for bI in range(0,top_height):
        draw_tile(x, bI*tile_height, pipe_colour)

    for tI in range(bottom_height,tiles_height):
        draw_tile(x, tI*tile_height, pipe_colour)

def draw_bird(height):
    draw_tile(screen.get_width()/2, height, (248, 255, 59))

# x,top_height,gap
pipes = []

def add_pipe():
    gap = random.randint(5,10)
    add_score = 1
    if len(pipes) == 0:
        pipes.append((width, 5, 5+gap, add_score))
    else:
        last_pipe = pipes[len(pipes)-1]

        bottom_height = random.randint(last_pipe[1]-15, last_pipe[1]+15)
        if bottom_height < 3:
            bottom_height = 3

        top_height = bottom_height+gap

        pipes.append((width, bottom_height, top_height, add_score))


delta_time = 0
last_time = time.time()
pipe_timer = time.time()
bird_height = screen.get_height()/2
bird_velocity = -160
score = 0
# game loop
while running:
    if playing:
        refresh_screen()

        font = pygame.font.Font(None, 40)
        text = font.render(str(score), True, (0, 0, 0))
        screen.blit(text, (10, 10))

        if bird_velocity > -160:
            bird_velocity -= 4.5

        draw_bird(bird_height)

        bird_height = bird_height - (bird_velocity * delta_time)

        if (time.time() - pipe_timer) > 4:
            add_pipe()
            pipe_timer = time.time()

        for i in range(0, len(pipes)-1):
            pipes[i] = (pipes[i][0] + (-90 * delta_time), pipes[i][1], pipes[i][2], pipes[i][3])
            draw_pipe(pipes[i][0], pipes[i][1], pipes[i][2])

            if bird_height < pipes[i][1] * tile_height and abs(pipes[i][0] - screen.get_width()/2) < 0.25:
                game_over()
            elif bird_height > pipes[i][2] * tile_height and abs(pipes[i][0] - screen.get_width()/2) < 0.25:
                game_over()
            elif bird_height > screen.get_height():
                game_over()
            elif bird_height < 0:
                game_over()
            elif abs(pipes[i][0] - screen.get_width()/2) < 1:
                score += pipes[i][3]
                pipes[i] = (pipes[i][0], pipes[i][1], pipes[i][2], 0)

            print(bird_height)

            if pipes[i][0] < -tile_width:
                pipes.remove(pipes[i])

    pygame.display.update()

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = bird_velocity + 160 + 800



    delta_time = time.time()-last_time
    last_time = time.time()
