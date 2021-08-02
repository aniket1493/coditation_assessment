import pygame
import numpy as np

class Game:
    def __init__(self, surface, grid, active_color=(255, 255, 255), inactive_color=(0, 0, 0)):
        self.surface = surface                                                                  # passing the screen to surface
        self.active_color = active_color                                                        # alive cell colour is set to white
        self.inactive_color = inactive_color                                                    # dead cell is set to black
        self.columns = 10                                                                       # number of columns
        self.rows = 10                                                                          # number of rows
        self.grid = np.array(grid,dtype=bool)                                                   # converting input data to boolean type

    # running the program
    def run(self):                                                                              
        self.draw_grid()
        self.update_grid()

    # drawing the grid
    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(self.surface, self.active_color, [row * 50, col * 50, 1000, 1000])
                else:
                    pygame.draw.rect(self.surface, self.inactive_color, [row * 50, col * 50, 1000, 1000])

    # updating the grid
    def update_grid(self):
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid

    # updating the cell
    def update_cell(self, x, y):
        current_state = self.grid[x, y]
        alive_neighbors = 0

        # In 3 X 3 grid, we check here how many number of alive neighbours are present for every node with 8 neighbours
        for i in range(-1, 2):
            if ((x + i) < 0 or ((x + i) >= self.grid.shape[0])):
                continue
            for j in range(-1, 2):
                if ((y + j) < 0 or (y + j) >= self.grid.shape[1]):
                    continue
                if i == 0 and j == 0:
                        continue
                elif self.grid[x + i, y + j]:
                    alive_neighbors += 1

        # Updating the cell's state
        if current_state and alive_neighbors < 2:                                       # dies as it is underpopulates
            return False
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3):          # lives to the next generation
            return True
        elif current_state and alive_neighbors > 3:                                     # dies as it is overpopulates
            return False
        elif ~current_state and alive_neighbors == 3:                                   # becomes alive
            return True
        else:
            return current_state


