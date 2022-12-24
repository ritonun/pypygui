import pygame
from .gui_element import Label
from .var import BLACK, m5x7


class Gui:
    def __init__(self, display_size):
        self.display = pygame.Surface(display_size, pygame.SRCALPHA)
        self.labels = {}

    def resize(self, new_display_size):
        self.display = pygame.Surface(new_display_size, pygame.SRCALPHA)

        for label in self.labels:
            self.labels[label].resize(self.display)

    def label(self, name, pos, text, size, color=BLACK, fonts=m5x7, center=False):
        if name in self.labels:
            raise KeyError("Label name '{}' already in use.".format(name))

        label = Label(pos, text, size, self.display, color=color, fonts=fonts, center=center)
        self.labels[name] = label

    def label_update_text(self, label_name, text):
        self.labels[label_name].update_text(text)

    def update(self):
        pass

    def draw(self, display):
        self.display.fill((0, 0, 0, 0))
        for key in self.labels:
            self.labels[key].draw()

        display.blit(self.display, (0, 0))
