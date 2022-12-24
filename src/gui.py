import pygame
from .gui_element import Label, ButtonLabel, ButtonRect
from .gui_basic import key_in_dict
from .var import BLACK, m5x7


class Gui:
    def __init__(self, display_size, font_path=m5x7):
        self.display = pygame.Surface(display_size, pygame.SRCALPHA)
        self.font_path = font_path
        self.labels = {}
        self.buttons = {}

    def resize(self, new_display_size):
        self.display = pygame.Surface(new_display_size, pygame.SRCALPHA)

        for label in self.labels:
            self.labels[label].resize(self.display)

        for button in self.buttons:
            self.buttons[button].resize(self.display)

    def create_button_from_label(self, button_name, label_name, action=None):
        if not key_in_dict(label_name, self.labels):
            raise KeyError("Label name {} not attributed.".format(label_name))
        if key_in_dict(button_name, self.buttons):
            raise KeyError("Button name {} already attributed.".format(button_name))

        label = self.labels[label_name]
        self.buttons[button_name] = ButtonLabel(label, action=action)

    def create_button_from_rect(self, button_name, rect, action=None):
        if key_in_dict(button_name, self.buttons):
            raise KeyError("Button name {} already attributed.".format(button_name))

        self.buttons[button_name] = ButtonRect(rect, self.display, action=action)

    def label(self, name, pos, text, size, color=BLACK, fonts=None, center=False):
        if key_in_dict(name, self.labels):
            raise KeyError("Label name {} already attributed.".format(name))

        if fonts is None:
            fonts = self.font_path

        label = Label(pos, text, size, self.display, color=color, fonts=fonts, center=center)
        self.labels[name] = label

    def label_update_text(self, label_name, text):
        self.labels[label_name].update_text(text)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            self.buttons[button].update(mouse_pos)

    def draw(self, display):
        self.display.fill((0, 0, 0, 0))
        for key in self.labels:
            self.labels[key].draw()

        for key in self.buttons:
            self.buttons[key].draw()

        display.blit(self.display, (0, 0))
