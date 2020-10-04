import pygame
import random
import time


WIDTH = 600
HEIGHT = 600
FPS = 30

# pygame window set up 
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Generator')
clock = pygame.time.Clock()

# colours
BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)
BLUE =  (0,   0,   255)
RED =   (255, 0,   0  )
GREEN = (0,   255, 0  )

# initial grid settings
cell_size = 20
grid_size = WIDTH // cell_size 

grid = []
stack = []
visited = []
path = {}



def build_grid(cell_size, grid_size):
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(SCREEN, WHITE, (i * (cell_size), 
                                            j * (cell_size), 
                                            cell_size, cell_size), 1)
            grid.append((i * (cell_size), j * (cell_size)))

def create_maze(x, y):
    visited.append((x,y))
    stack.append((x,y))
    draw_nose(x,y)
    
    while stack:
        # check for neighbours
        neighbours = check_neighbourhood(x, y)

        if neighbours:
            cell_x, cell_y = random.choice(neighbours)
            print(f'trying neighbour cell: x = {cell_x}, y = {cell_y}')
            # draw progression
            if cell_x == x and cell_y > y:
                grow_down(x,y)
            elif cell_x == x and cell_y < y:
                grow_up(x,y)
            elif cell_y == y and cell_x > x:
                grow_right(x,y)
            else:
                grow_left(x,y)    
            time.sleep(0.1)

            create_maze(cell_x, cell_y)

        else:
            new_x, new_y = stack.pop()
            draw_backtrack(x, y)
            print(f'trying new cell: x = {new_x}, y = {new_y}')
            create_maze(new_x, new_y)

def check_neighbourhood(x,y):
    neighbours = []
    if (x + cell_size, y) in grid and (x + cell_size, y) not in visited:
        neighbours.append((x + cell_size, y))
    if (x - cell_size, y) in grid and (x - cell_size, y) not in visited:
        neighbours.append((x - cell_size, y))
    if (x, y + cell_size) in grid and (x, y + cell_size) not in visited:
        neighbours.append((x, y + cell_size))
    if (x, y - cell_size) in grid and (x, y - cell_size) not in visited:
        neighbours.append((x, y - cell_size))

    return neighbours

def draw_nose(x, y):
    pygame.draw.rect(SCREEN, RED, (x + 1, y + 1, cell_size - 2, cell_size - 2))
    pygame.display.update()
    time.sleep(0.1) 

def draw_backtrack(x, y):
    pygame.draw.rect(SCREEN, GREEN, (x + 1, y + 1, cell_size - 2, cell_size - 2))
    pygame.display.update()
    time.sleep(0.1)

# draw maze movemenet:
def grow_right(x, y):
    pygame.draw.rect(SCREEN, BLUE, (x + 1, y + 1,  2 * cell_size - 2, cell_size - 2))
    pygame.display.update()

def grow_down(x, y):
    pygame.draw.rect(SCREEN, BLUE, (x + 1, y + 1, cell_size - 2, 2 * cell_size - 2))
    pygame.display.update()

def grow_left(x, y):
    pygame.draw.rect(SCREEN, BLUE, (x - cell_size + 1, y + 1,  2 * cell_size - 2, cell_size - 2))
    pygame.display.update()

def grow_up(x, y):
    pygame.draw.rect(SCREEN, BLUE, (x + 1, y - cell_size + 1, cell_size - 2, 2 * cell_size - 2))
    pygame.display.update()


build_grid(cell_size, grid_size)
create_maze(0,0)


# pygame loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
