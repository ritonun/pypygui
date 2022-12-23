import pygame
from .gui_basic import text_objects
from .var import BLACK


class Gui:
    def __init__(self, display_size):
        self.display = pygame.Surface(display_size, pygame.SRCALPHA)
        self.labels = {}

    def center_surface(self, surface, pos):
        w, h = surface.get_size()
        x = pos[0] - int(w / 2)
        y = pos[1] - int(h / 2)
        return (x, y)

    def resize(self, new_display_size):
        self.display = pygame.Surface(new_display_size, pygame.SRCALPHA)
        w, h = self.display.get_size()

        for key in self.labels:
            label = self.labels[key]
            size = int(label["size_ratio"] * w)
            pos = (int(label["pos_ratio"][0] * w), int(label["pos_ratio"][1] * h))

            text_surf, text_rect = text_objects(label["text"], size, color=label["color"])
            self.labels[key]["surface"] = text_surf
            self.labels[key]["pos"] = pos
            print(key, size)

    def label(self, name, pos, text, size, color=BLACK, center=False):
        if name in self.labels:
            raise KeyError("Label name '{}' already in use.".format(name))

        # calculate size ratio
        size_ratio: float = size / self.display.get_height()
        pos_ratio = (float(pos[0] / self.display.get_width()), float(pos[1] / self.display.get_height()))
        text_surf, text_rect = text_objects(text, size, color=color)
        self.labels[name] = {"surface": text_surf, "pos": pos, "pos_ratio": pos_ratio, "text": text,
                             "size_ratio": size_ratio, "color": color}
        print(name, size)

    def update(self):
        pass

    def draw(self, display):
        self.display.fill((0, 0, 0, 0))

        for key in self.labels:
            label = self.labels[key]
            self.display.blit(label["surface"], label["pos"])

        display.blit(self.display, (0, 0))
