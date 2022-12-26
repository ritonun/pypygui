import pygame
from .gui_basic import rect_is_clicked
from .var import BLACK


class Outline:
    def __init__(self, base_rect, display, outline_size=1, outline_color=BLACK):
        self.base_rect = base_rect
        self.display = display
        self.outline_size = outline_size
        self.outline_size_ratio = outline_size / self.display.get_height()
        self.outline_color = outline_color

        self.get_outline_rect(self.base_rect)

    def get_outline_rect(self, rect):
        x = rect.x - self.outline_size
        y = rect.y - self.outline_size
        w = rect.w + 2 * self.outline_size
        h = rect.h + 2 * self.outline_size
        self.outline_rect = pygame.Rect(x, y, w, h)

    def resize(self, new_base_rect, new_display):
        self.display = new_display
        self.base_rect = new_base_rect
        self.outline_size = int(self.outline_size_ratio * self.display.get_height())
        self.get_outline_rect(new_base_rect)

    def outline_is_active(self, mouse_pos):
        if rect_is_clicked(self.outline_rect, mouse_pos):
            return True
        return False

    def draw(self):
        pygame.draw.rect(self.display, self.outline_color, self.outline_rect, self.outline_size)
