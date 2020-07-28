import pygame
import sys
from board import Board
from automata import Blinker
import messages
from public_UI import *


pygame.init()

board = Board(0, WINDOW_WIDTH, WINDOW_HEIGHT, 7)
cell_size = board.cell_size()
board_size = board.size()
line = Blinker()
pause = False
def paused():
    global pause
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        pause_line_1 = messages.message_display("Paused".upper(), SCREEN, Position(board_size.width//2, board_size.height//2), RED)
        #line 2
        messages.message_display("(press 'p' to continue)", SCREEN, Position(board_size.width//2, board_size.height//2 + pause_line_1.height), CYAN)
        pygame.display.update()
        CLOCK.tick(15)

def unpause():
    global pause
    pause = False

def handle_events():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
                paused()
        if event.type == pygame.MOUSEBUTTONDOWN and pause == True:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    board.get_cell_num_for_pos(0, Position(mouse_pos[0], mouse_pos[1]))._draw_circle()
                    

while True:
    # TODO: use dt to control movement speed of objects?
    dt = CLOCK.tick(FPS)
    SCREEN.fill(WHITE)
    board.draw_grid(board.active_grid)
    
    #capture events (mouse clicks, closing the game, etc)
    handle_events()    
    pygame.display.flip()


# MARK: Reference (unused)

#animation x value wrap around - x is an iterator
    # x = cell_size.width//2
    # if x >= board_size.width:
    #     x = cell_size.width//2
    # else:
    #     x += cell_size.width