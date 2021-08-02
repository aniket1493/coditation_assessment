import sys
import pygame
import numpy as np                                           # use for creating 2-D array
from file_1 import Game

pygame.init()
pygame.display.set_caption("Assignment")

WIDTH = 500
HEIGHT = 500

# sample_input = 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1


entries = list(map(int, input("Enter the cells: ").split())) # taking input from the user in a form of list
grid = np.array(entries).reshape(10, 10)                     # reshaping the aaray in a gird of 10 X 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))            # create the screen of size 500x500 pixel resolution

prog = Game(screen, grid)

clock = pygame.time.Clock()
fps = 5                                                       # setting frames per second

while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))                                      # filling the black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    prog.run()

    pygame.display.update()
