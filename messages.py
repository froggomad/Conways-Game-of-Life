#message_display helper
import pygame
from public_UI import Position, BLACK

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, surface, position=Position(0,0), color=BLACK):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText, color)
    # I don't really want to manipulate the center property, but couldn't figure out how to access x and y directly
    # So, use the center, but adjust so it's actually using the x,y passed in to position the text rectangle
    if position.x > surface.get_rect().width//2:
        text_x = position.x - (TextRect.width//2)
    elif position.x < surface.get_rect().width//2:
        text_x = position.x + (TextRect.width//2)
    else:
        text_x = position.x

    if position.y > surface.get_rect().height//2:
        text_y = position.y - (TextRect.height//2)
    elif position.y < surface.get_rect().height//2:
        text_y = position.y + (TextRect.height//2)
    else:
        text_y = position.y
    TextRect.center = (text_x, text_y)
    # draw it
    surface.blit(TextSurf, TextRect)
    return TextRect

def Button(text, coords, surface, border_color=BLACK, text_color=BLACK, fill_color=None, padding=20, border=True):
    """color will be the color of the button's border/outer rectangle"""
    if fill_color == None:
        fill_color = surface.fill_color
    
    largeText = pygame.font.Font('freesansbold.ttf',20)
    text_objs = text_objects(text, largeText, text_color)
    text_surface = text_objs[0]
    text_rect = text_objs[1]
    rect = pygame.Rect(coords, (text_rect.width + int(padding), text_rect.height))

    #draw border
    if border == True:
        pygame.draw.rect(surface, border_color, rect, 1)
    pygame.draw.rect(surface, fill_color, rect)
    surface.blit(text_surface, (coords[0] + padding//2, coords[1]))
    return (rect)

