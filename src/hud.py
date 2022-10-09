import pygame
from .var import m5x7, WHITE, BLACK


def text_objects(text, size, color=WHITE):
    font = pygame.font.Font(m5x7, size)
    text_surf = font.render(str(text), False, color)
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


def draw_text_objects(display, pos, surf):
    display.blit(surf, pos)


def button_is_active(rect, pos):
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0]:
            return True
    return False


def get_outline(rect, outline):
    rect.x -= outline
    rect.y -= outline
    rect.w += 2 * outline
    rect.h += 2 * outline
    return rect


def draw_button(display, pos, surf, rect, outline=1, outline_color=BLACK, background_color=WHITE):
    # background color
    pygame.draw.rect(display, background_color, rect)
    # outline
    pygame.draw.rect(display, outline_color, rect, outline)
    # text
    text_pos = [pos[0] + outline + (rect.w / 2) - (surf.get_rect().w / 2), pos[1]]
    draw_text_objects(display, text_pos, surf)
    

def label(display, x, y, text, size, color=WHITE):
    text_surf, text_rect = text_objects(text, size, color=color)
    display.blit(text_surf, (x, y))


def button(display, x, y, text, size, pos, action=None, font_color=WHITE, outline_color=BLACK, outline=3):
    text_surf, text_rect = text_objects(text, size, color=font_color)
    text_rect.x, text_rect.y = x, y
    text_rect.x -= outline
    text_rect.y -= outline
    text_rect.w += 2 * outline
    text_rect.h += 2 * outline

    if button_is_active(text_rect, pos) and action is not None:
        action() 

    display.blit(text_surf, (x, y))
    pygame.draw.rect(display, outline_color, text_rect, outline)
