import pygame
import sys
from board import Board
from messages import message_display
from public_UI import *
import webbrowser

pygame.init()
cell_count = 50
board = Board(0, WINDOW_WIDTH, WINDOW_HEIGHT, 1, cell_count)

# MARK: Run Loop
i=0
def run():
    global i
    while True:
        # TODO: use dt to control movement speed of objects? (if implementing particles)
        if pause:
            if i == 0:                                
                i+=1
                paused()        
        board.increase_generation()
        SCREEN.fill(FILL_COLOR)        
        board.draw_grid(board.active_grid)
        handle_events()                 
        pygame.display.flip()
        CLOCK.tick(FPS)

# MARK: View Lifecycle
def display_pause_message():
    board_size = board.size()
    pause_line_1 = message_display("Paused".upper(), SCREEN, Position(board_size.width//2, board_size.height//2), WHITE)
    message_display("(Click to draw, press 'p' to continue, 'h' for rules/about)", SCREEN, Position(board_size.width//2, board_size.height//2 + pause_line_1.height), WHITE)

def unpause():
    global pause
    pause = False
    board._is_user_interaction_enabled = False

def paused():
    global pause
    pause = True      
    board._is_user_interaction_enabled = True
    display_pause_message()        
    while pause == True:
        board.draw_rects(board.active_grid)
        handle_events()
        pygame.display.update()
    board.clear_rects(board.active_grid)

def toggle_pause():
    if pause == True:
        unpause()
    else:
        paused()

def clear_board():
    board.clear()
    if pause:
        display_pause_message()

def randomize_board():
    global board
    board.clear()
    board = Board(0, WINDOW_WIDTH, WINDOW_HEIGHT, board_style=None, num_cells=cell_count)
    if pause:
        display_pause_message()
    board._is_user_interaction_enabled = pause

def handle_events():
    #global pause
    pause_button = board.pauseBtn
    clear_button = board.clearBtn
    random_button = board.randomizeBtn
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                toggle_pause()                
            if event.key == pygame.K_h:
                webbrowser.open('https://conways-game-of-life.webflow.io/')

        if event.type == pygame.MOUSEBUTTONDOWN:
            #handle events on the status bar with new_location and events on the entire screen with mouse_pos
            mouse_pos = pygame.mouse.get_pos()
            new_location = (mouse_pos[0], mouse_pos[1]-board.size().height)

            if pause_button.collidepoint(new_location):
                toggle_pause()

            if clear_button.collidepoint(new_location):
                clear_board()
            
            if random_button.collidepoint(new_location):
                randomize_board()

            if board._is_user_interaction_enabled == True:                
                pygame.key.set_repeat()
                board_rect = pygame.Rect(0, 0, WINDOW_WIDTH, board.size().height)
                if event.button == 1 and board_rect.collidepoint(mouse_pos):                    
                    cell = board.get_cell_for_pos(board.active_grid, Position(mouse_pos[0], mouse_pos[1]))[0]
                    if cell.is_alive():
                        cell._clear_circle()
                        cell.draw()
                    else:                            
                        cell._draw_circle()
                        cell.draw()
            CLOCK.tick(7)
            pygame.display.update()

# MARK: Run the game!
run()