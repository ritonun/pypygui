import pygame
from .var import m5x7, WHITE, BLACK


def rect_is_clicked(rect, mouse_pos):
    if rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            return True
    return False


def key_in_dict(key, checked_dict):
    if key in checked_dict:
        return True
    else:
        return False


def center_surface(surface, pos):
    """Get pos for a surface based on the center pos

    Args:
        surface (pygame.Surface): surface to center
        pos (int tuple): center position

    Returns:
        int tuple: top left corner pos to draw surface
    """
    w, h = surface.get_size()
    x = pos[0] - int(w / 2)
    y = pos[1] - int(h / 2)
    return (x, y)


def center_rect(rect, pos):
    w, h = rect.w, rect.h
    x = pos[0] - int(w / 2)
    y = pos[1] - int(h / 2)
    return (x, y)


def text_objects(text, size, color=WHITE, fonts=m5x7):
    """Create obj

    Args:
        text (str): text string
        size (int): font size
        color (tuple, optional): text color, default is WHITE

    Returns:
        pygame.surface: containt the text & font
        pygame.rect: rect of surface size
    """
    font = pygame.font.Font(fonts, size)
    text_surf = font.render(str(text), False, color)
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


def draw_text_objects(display, pos, surf):
    """Draw a text object

    Args:
        display (pygame.Surface): Surface to draw on
        pos (int tuple): Position to draw text
        surf (pygame.Surface): Surface containg the text
    """
    display.blit(surf, pos)


def button_is_active(rect, pos):
    """Check if the mouse is hovering on the button

    Args:
        rect (pygame.Rect): button rect
        pos (int tuple): mouse coordinate

    Returns:
        bool: True if mouse is hovering on the button
    """
    if rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0]:
            return True
    return False


def get_outline(rect, outline):
    """Create a new bigger/smaller rect base on a rect. The two rects share the same center.

    Args:
        rect (pygame.Rect): Base rect
        outline (int): Factor of diminution/augmentation of the rect size

    Returns:
        pygame.Rect: New rect outlined
    """
    rect.x -= outline
    rect.y -= outline
    rect.w += 2 * outline
    rect.h += 2 * outline
    return rect


def draw_button(display, pos, surf, rect, outline=1, outline_color=BLACK, background_color=WHITE):
    """Summary

    Args:
        display (pygame.Surface): Surface to draw on
        pos (int tuple): Coordinate of the button
        surf (pygame.Surface): button surface
        rect (pygame.Rect): button rect
        outline (int, optional): Size of the outline
        outline_color (int tuple, optional): Color of the outline
        background_color (int tuple, optional): Color of the background in the button
    """
    # background color
    pygame.draw.rect(display, background_color, rect)
    # outline
    pygame.draw.rect(display, outline_color, rect, outline)
    # text
    text_pos = [pos[0] + outline + ((rect.w - (outline * 2) - surf.get_rect().w) / 2),
                pos[1] + outline]
    draw_text_objects(display, text_pos, surf)


def label(display, x, y, text, size, color=WHITE):
    """Display a string of text

    Args:
        display (pygame.Surface): Surface to draw on
        x (int): x coordinate
        y (int): y coordinate
        text (str): text string
        size (int): font size
        color (int tuple, optional): font color, default is white
    """
    text_surf, text_rect = text_objects(text, size, color=color)
    display.blit(text_surf, (x, y))


def button(display, x, y, text, size, pos, action=None, font_color=WHITE, outline_color=BLACK, outline=3):
    """Display a button

    Args:
        display (pygame.Surface): Surface to draw on
        x (int): x coordinate
        y (int): y coordinate
        text (str): text string
        size (int): font size
        pos (int tuple): mouse coordinate
        action (None, optional): Function to run if button is clicked
        font_color (int tuple, optional): font color, default is white
        outline_color (int tuple, optional): outline color, default is black
        outline (int, optional): outline size, default is 3
    """
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
