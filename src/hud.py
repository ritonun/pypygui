import pygame
from .locals import m5x7, WHITE, BLACK


def text_objects(text, size, color=WHITE):
    font = pygame.font.Font(m5x7, size)
    text_surf = font.render(str(text), False, color)
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


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

    if text_rect.collidepoint(pos) and action is not None:
        if pygame.mouse.get_pressed()[0]:
            action()

    display.blit(text_surf, (x, y))
    pygame.draw.rect(display, outline_color, text_rect, outline)
