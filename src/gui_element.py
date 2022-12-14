import pygame
from .gui_basic import center_surface, center_rect, text_objects, rect_is_clicked
from .var import BLACK, RED, m5x7
from .button_property import Outline


class Label:
    def __init__(self, pos, text, size, display, color=BLACK, fonts=m5x7, center=False):
        self.display = display
        w, h = self.display.get_size()

        self.text = text
        self.size_ratio = size / h
        self.color = color
        self.fonts = fonts
        self.center = center
        self.surf, self.rect = text_objects(self.text, size, color=self.color, fonts=self.fonts)

        if self.center:
            self.pos = center_surface(self.surf, pos)
            self.pos_ratio = (pos[0] / w, pos[1] / h)
        else:
            self.pos = pos
            self.pos_ratio = (pos[0] / w, pos[1] / h)

        self.need_resize = False

    def resize(self, new_display):
        self.display = new_display
        w, h = self.display.get_size()

        size = int(self.size_ratio * h)
        self.surf, self.rect = text_objects(self.text, size, color=self.color, fonts=self.fonts)

        pos = (int(self.pos_ratio[0] * w), int(self.pos_ratio[1] * h))
        self.pos = center_surface(self.surf, pos)

    def update_text(self, text):
        self.text = text
        size = int(self.size_ratio * self.display.get_height())
        self.surf, self.rect = text_objects(self.text, size, color=self.color, fonts=self.fonts)

        if self.center:
            w, h = self.display.get_size()
            pos = (int(self.pos_ratio[0] * w), int(self.pos_ratio[1] * h))
            self.pos = center_surface(self.surf, pos)
        self.need_resize = True

    def draw(self):
        self.display.blit(self.surf, self.pos)


class Button:
    debug = True
    color = RED

    def __init__(self, rect, display, action=None):
        self.rect = rect
        self.display = display
        w, h = self.display.get_size()
        self.rect_ratio = (self.rect.x / w, self.rect.y / h, self.rect.w / w, self.rect.h / h)

        self.action = action
        self.is_active = False

        self.propertys = {}

    def resize(self, new_display):
        self.display = new_display
        w, h = self.display.get_size()
        self.rect = pygame.Rect(int(self.rect_ratio[0] * w), int(self.rect_ratio[1] * h),
                                int(self.rect_ratio[2] * w), int(self.rect_ratio[3] * h))

        if "outline" in self.propertys:
            self.propertys["outline"].resize(self.rect, self.display)

    def check_is_active(self, mouse_pos):
        if "outline" in self.propertys:
            if self.propertys["outline"].outline_is_active(mouse_pos) is True:
                self.is_active = True
                if self.action is not None:
                    self.action()

        elif rect_is_clicked(self.rect, mouse_pos):
            self.is_active = True
            if self.action is not None:
                self.action()
        else:
            self.is_active = False

    def draw(self):
        if "outline" in self.propertys:
            self.propertys["outline"].draw()

        if self.debug:
            pygame.draw.rect(self.display, self.color, self.rect, 1)

    def add_outline(self, outline_size=1, outline_color=BLACK):
        self.propertys["outline"] = Outline(self.rect, self.display, outline_size=outline_size,
                                            outline_color=outline_color)


class ButtonLabel(Button):
    def __init__(self, label, display, action=None):
        self.label = label

        rect = self.label.rect
        rect.x = self.label.pos[0]
        rect.y = self.label.pos[1]
        super().__init__(rect, display, action=action)

    def resize(self, new_display):
        self.display = new_display
        self.rect = self.label.rect
        self.rect.x = self.label.pos[0]
        self.rect.y = self.label.pos[1]

        if "outline" in self.propertys:
            self.propertys["outline"].resize(self.rect, self.display)

    def update(self, mouse_pos):
        self.check_is_active(mouse_pos)

        if self.label.need_resize is True:
            self.resize(self.label.display)
            self.label.need_resize = False


class ButtonRect(Button):
    def __init__(self, rect, display, action=None):
        super().__init__(rect, display, action=action)

    def update(self, mouse_pos):
        super().check_is_active(mouse_pos)

    def draw(self):
        pygame.draw.rect(self.display, BLACK, self.rect, 1)


class ButtonImage(Button):
    def __init__(self, img, pos, display, resize_img=1, action=None, center=False):
        self.img_original = img
        self.img = img

        self.center = center

        rect = self.img.get_rect()
        super().__init__(rect, display, action=action)
        self.pos = pos
        if self.center:
            self.rect.x, self.rect.y = center_rect(rect, pos)
        else:
            self.rect.x, self.rect.y = self.pos

        self.pos_ratio = (self.pos[0] / self.display.get_width(), self.pos[1] / self.display.get_height())

        self.resize_img = resize_img
        self.resize_ratio = self.img.get_width() / self.display.get_width()
        self.image_ratio = self.img.get_width() / self.img.get_height()

    def resize(self, new_display):
        super().resize(new_display)

        self.rect.w = self.image_ratio * self.rect.h
        self.img = pygame.transform.scale(self.img_original, (self.rect.w, self.rect.h))

        self.pos = (self.pos_ratio[0] * self.display.get_width(), self.pos_ratio[1] * self.display.get_height())
        if self.center:
            self.pos = center_rect(self.rect, self.pos)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def update(self, mouse_pos):
        super().check_is_active(mouse_pos)

    def draw(self):
        self.display.blit(self.img, (self.rect.x, self.rect.y))
        super().draw()


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
