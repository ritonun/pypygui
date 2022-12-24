import pygame
from .gui_element import Label, Button
from .var import BLACK, m5x7


class Gui:
    def __init__(self, display_size, font_path=m5x7):
        self.display = pygame.Surface(display_size, pygame.SRCALPHA)
        self.font_path = font_path
        self.labels = {}
        self.buttons = {}

    def key_in_use(self, key):
        if key in self.labels:
            raise KeyError("Label key '{}' already in use.".format(key))
        if key in self.buttons:
            raise KeyError("Buttons key '{}' already in use.".format(key))

    def resize(self, new_display_size):
        self.display = pygame.Surface(new_display_size, pygame.SRCALPHA)

        for label in self.labels:
            self.labels[label].resize(self.display)

        for button in self.buttons:
            self.buttons[button].resize(self.display)

    def button(self, name, pos, text, size, color=BLACK, fonts=None, center=False, action=None):
        self.key_in_use(name)

        if fonts is None:
            fonts = self.font_path

        button = Button(pos, text, size, self.display, color=color, fonts=fonts, center=center,
                        action=action)
        self.buttons[name] = button

    def label(self, name, pos, text, size, color=BLACK, fonts=None, center=False):
        self.key_in_use(name)

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
