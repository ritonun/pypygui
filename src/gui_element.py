import pygame
from .var import BLACK


class Slider:
    def __init__(self, display, x, y, w, h, min_value=0, max_value=100):
        self.display = display
        self.slider_rect = pygame.Rect(x, y, w, h)

        self.circle_radius = h * 2
        self.circle_pos = [x, y + self.slider_rect.h / 2]

        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value

    def is_active(self, mouse_pos):
        w_ratio = 1.25
        h_ratio = 4
        w = self.slider_rect.w * w_ratio
        h = self.slider_rect.h * h_ratio
        x = self.slider_rect.x - (self.slider_rect.w * w_ratio - self.slider_rect.w) / 2
        y = self.slider_rect.y - (self.slider_rect.h * h_ratio - self.slider_rect.h) / 2

        rect = pygame.Rect(x, y, w, h)
        # pygame.draw.rect(self.display, GREEN, rect, 1)

        if rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False

    def update_slider(self, mouse_pos):
        mouse_pos = list(mouse_pos)
        a = (self.max_value - self.min_value) / self.slider_rect.w
        b = a * self.slider_rect.x

        if mouse_pos[0] < self.slider_rect.x:
            mouse_pos[0] = self.slider_rect.x
        elif mouse_pos[0] > self.slider_rect.x + self.slider_rect.w:
            mouse_pos[0] = self.slider_rect.x + self.slider_rect.w

        self.circle_pos[0] = mouse_pos[0]
        self.value = a * mouse_pos[0] - b

    def get_value(self):
        return self.value

    def update(self, mouse_pos):
        if self.is_active(mouse_pos):
            self.update_slider(mouse_pos)
        self.render()

    def render(self):
        pygame.draw.rect(self.display, BLACK, self.slider_rect, 1)
        pygame.draw.circle(self.display, BLACK, self.circle_pos, self.circle_radius)
