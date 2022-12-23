from .var import WHITE, templates
from .gui import text_objects, draw_text_objects, draw_button, get_outline, button_is_active
import sys
import pygame


class Menu:
    """Simplify the creation of menu. Posses color template & auto layout.
    """

    font_size = 45
    outline = 1
    outline_color = (121, 85, 74)
    background_color = (179, 190, 196)
    screen_color = (42, 64, 84)

    def __init__(self, font_color=WHITE):
        self.labels = []
        self.buttons = []
        self.font_color = font_color
        self.run = True

    @classmethod
    def properties(cls, font_size=font_size, outline_color=outline_color,
                   outline=outline, background_color=background_color, screen_color=screen_color):
        cls.font_size = font_size
        cls.outline = outline
        cls.outline_color = outline_color
        cls.background_color = background_color
        cls.screen_color = screen_color

    def template(self, template_key):
        """Update the menu coloring to a templates.

        Args:
            template_key (str): Different coloring options. "vaporwave", "default", "vibrant". They're all equally ugly.
        """
        self.font_color = templates[template_key]["font_color"]
        self.properties(outline_color=templates[template_key]["outline_color"],
                        background_color=templates[template_key]["background_color"],
                        screen_color=templates[template_key]["screen_color"])

    def add_label(self, x, y, text, size=font_size, color=None):
        """Summary

        Args:
            x (int): x coordinate
            y (int): y coordinate
            text (str): text string
            size (int, optional): font size
            color (int tuple, optional): color
        """
        if color is None:
            color = self.font_color
        text_surf, text_rect = text_objects(text, size, color=color)
        x -= text_rect.w / 2
        y -= text_rect.h / 2
        element = [[x, y], text_surf]
        self.labels.append(element)

    def add_button(self, x, y, text, action=None, size=font_size, color=None):
        """Add a button to the menu

        Args:
            x (int): x coordinate
            y (int): y coordinate
            text (str): text string
            action (None, optional): Function to do when button is clicked. Default is None.
            size (int, optional): font size
            color (int tuple, optional): color.
        """
        if color is None:
            color = self.font_color
        text_surf, text_rect = text_objects(text, size, color=color)
        text_rect.x, text_rect.y = x, y
        rect = get_outline(text_rect, outline=self.outline)
        element = [[x, y], text_surf, rect, action]
        self.buttons.append(element)

    def auto_layout(self, display, axis="horizontal"):
        """Automatically adjust x & y coordinate of all button to space them on the screen.

        Args:
            display (pygame.Surface): Surface to draw on. x & y coordinate are calculated based on its size.
            axis (str, optional): Ether "horizontal" or "vertical". Choose wether button are put on x-axis or y-axis.
        """
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
                if element[3] is not None:
                    if element[3] == "quit":
                        self.run = False
                    else:
                        element[3]()

    def draw(self, display):
        display.fill(self.screen_color)
        if len(self.labels) > 0:
            for element in self.labels:
                draw_text_objects(display, element[0], element[1])

        if len(self.buttons) > 0:
            for element in self.buttons:
                draw_button(display, element[0], element[1], element[2], outline=self.outline,
                            outline_color=self.outline_color, background_color=self.background_color)

    def mainloop(self, display, fps=15):
        """Create a loop for the menu. Handle event, update & rendering

        Args:
            display (pygame.Surface): Surface to draw on
            fps (int, optional): FPS, default is 15
        """
        clock = pygame.time.Clock()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            display.fill(WHITE)

            pos = pygame.mouse.get_pos()
            self.update(pos)
            self.draw(display)

            pygame.display.update()
            clock.tick(fps)
