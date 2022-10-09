from .var import BLACK, WHITE, RED, BLUE, GREEN
from .hud import text_objects, draw_text_objects, draw_button, get_outline, button_is_active


class Menu:
    font_color = RED
    font_size = 35
    outline = 1
    outline_color = BLACK
    background_color = WHITE

    def __init__(self):
        self.labels = []
        self.buttons = []

    def set_properties(self, font_color=font_color, font_size=font_size, outline_color=outline_color,
                       outline=outline, background_color=background_color):
        self.font_color = RED
        self.font_size = 35
        self.outline = 1
        self.outline_color = BLACK
        self.background_color = BLUE

    def add_label(self, x, y, text, size=font_size, color=font_color):
        text_surf, text_rect = text_objects(text, size, color=color)
        element = [[x, y], text_surf]
        self.labels.append(element)

    def add_button(self, x, y, text, action=None, size=font_size, color=font_color):
        text_surf, text_rect = text_objects(text, size, color=color)
        text_rect.x, text_rect.y = x, y
        text_rect = get_outline(text_rect, outline=self.outline)
        element = [[x, y], text_surf, text_rect, action]
        self.buttons.append(element)

    def auto_layout(self, display, axis="horizontal"):
        # 1. get biggest width element
        # 2. impose width on all element
        # 3. x = display.w / nb element - rect.w
        
        max_width = 0
        for button in self.buttons:
            if button[2].w > max_width:
                max_width = button[2].w

        for button in self.buttons:
            button[2].w = max_width

        w, h = display.get_size()

        if axis == "horizontal":
            x_incr = w / (len(self.buttons) + 1)
            y = h * (3 / 4)

            index = 1
            for button in self.buttons:
                pos = [x_incr * index - (button[2].w / 2), y]
                button[0] = pos
                button[2].x, button[2].y = pos
                index += 1

        elif axis == "vertical":
            x = (w * (1 / 2)) - (max_width / 2)
            y_incr = h / (len(self.buttons) + 1)

            index = 1
            for button in self.buttons:
                pos = [x, y_incr * index - (button[2].h / 2)]
                button[0] = pos
                button[2].x, button[2].y = pos
                index += 1

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
                draw_button(display, element[0], element[1], element[2], outline=self.outline, 
                            outline_color=self.outline_color, background_color=self.background_color)
