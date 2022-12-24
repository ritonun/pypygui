import pygame
from .gui_basic import center_surface, text_objects
from .var import BLACK, m5x7


class Label:
    def __init__(self, pos, text, size, display, color=BLACK, fonts=m5x7, center=False):
        self.display = display
        w, h = self.display.get_size()

        self.text = text
        self.size_ratio = size / h
        self.color = color
        self.fonts = fonts
        self.center = center
        self.surf, rect = text_objects(self.text, size, color=self.color, fonts=self.fonts)

        if self.center:
            self.pos = center_surface(self.surf, pos)
            self.pos_ratio = (pos[0] / w, pos[1] / h)
        else:
            self.pos = pos
            self.pos_ratio = (pos[0] / w, pos[1] / h)

    def resize(self, new_display):
        self.display = new_display
        w, h = self.display.get_size()

        size = int(self.size_ratio * h)
        self.surf, rect = text_objects(self.text, size, color=self.color, fonts=self.fonts)

        pos = (int(self.pos_ratio[0] * w), int(self.pos_ratio[1] * h))
        self.pos = center_surface(self.surf, pos)

    def update_text(self, text):
        self.text = text
        size = int(self.size_ratio * self.display.get_height())
        self.surf, rect = text_objects(self.text, size, color=self.color, fonts=self.fonts)

        if self.center:
            w, h = self.display.get_size()
            pos = (int(self.pos_ratio[0] * w), int(self.pos_ratio[1] * h))
            self.pos = center_surface(self.surf, pos)

    def draw(self):
        self.display.blit(self.surf, self.pos)


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
