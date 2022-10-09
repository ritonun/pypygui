from .var import RED, BLACK, WHITE
from .hud import text_objects, draw_text_objects, draw_button, get_outline, button_is_active


class Menu:
    font_color = RED
    font_size = 35
    outline = 1
    outline_color = BLACK

    def __init__(self):
        self.labels = []
        self.buttons = []

    def add_label(self, x, y, text, size=font_size, color=font_color):
        text_surf, text_rect = text_objects(text, size, color=color)
        element = [(x, y), text_surf]
        self.labels.append(element)

    def add_button(self, x, y, text, action=None, size=font_size, color=font_color):
        text_surf, text_rect = text_objects(text, size, color=color)
        text_rect = get_outline(text_rect, outline=self.outline)
        element = [(x, y), text_surf, text_rect, action]
        self.buttons.append(element)

    def update(self, mouse_pos):
        for element in self.buttons:
            if button_is_active(element[2], mouse_pos):
                if element[3]() is not None:
                    element[3]()

    def draw(self, display):
        if len(self.labels) > 0:
            for element in self.labels:
                draw_text_objects(display, element[0], element[1])

        if len(self.buttons) > 0:
            for element in self.buttons:
                draw_button(display, element[0], element[1], element[2], outline=self.outline, outline_color=self.outline_color)
