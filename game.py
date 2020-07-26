import pygame
import sys
from board import Board
from automata import Line_Three

pygame.init()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
CLOCK = pygame.time.Clock()
FPS = 5
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)

board = Board(0, WINDOW_WIDTH, 25)
cell_size = board.cell_size()
board_size = board.size()
x = cell_size//2
line = Line_Three()
while True:
    # TODO: use dt to control movement speed of objects?
    dt = CLOCK.tick(FPS)
    SCREEN.fill(WHITE)
    board.draw_grid()
    line.draw(SCREEN, x, cell_size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if x >= board_size:
        x = cell_size//2
    else:
        x += cell_size
    # double buffers by default
    pygame.display.flip()

    