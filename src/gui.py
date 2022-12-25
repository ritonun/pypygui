import pygame
from .gui_element import Label, ButtonLabel, ButtonRect, ButtonImage
from .gui_basic import key_in_dict
from .var import BLACK, m5x7


class Gui:
    """Global Gui class to handle all gui elements

    Attributes:
        buttons (dict): Contains all button element
        display (pygame.Surface): Surface to draw all gui elements on
        font_path (str): relative path to font
        labels (dict): Contains all label element
    """

    def __init__(self, display_size, font_path=m5x7):
        """Init Gui

        Args:
            display_size (pygame.Surface): Surface to draw all gui elements on
            font_path (str, optional): relative path to font
        """
        self.display = pygame.Surface(display_size, pygame.SRCALPHA)
        self.font_path = font_path
        self.labels = {}
        self.buttons = {}

    def resize(self, new_display_size):
        """Handle resize events

        Args:
            new_display_size (int tuple): new display size after resize
        """
        self.display = pygame.Surface(new_display_size, pygame.SRCALPHA)

        for label in self.labels:
            self.labels[label].resize(self.display)

        for button in self.buttons:
            self.buttons[button].resize(self.display)

    def create_button_from_label(self, button_name, label_name, action=None):
        """Create a button based on a text label. Will resize automatically.

        Args:
            button_name (str): Name to reference button in a dict
            label_name (str): Name of label to base the button around
            action (None, optional): Function to execute when the button is clicked

        Raises:
            KeyError
        """
        if not key_in_dict(label_name, self.labels):
            raise KeyError("Label name {} not attributed.".format(label_name))
        if key_in_dict(button_name, self.buttons):
            raise KeyError("Button name {} already attributed.".format(button_name))

        label = self.labels[label_name]
        self.buttons[button_name] = ButtonLabel(label, action=action)

    def create_button_from_rect(self, button_name, rect, action=None):
        """Create a button from a rect.

        Args:
            button_name (str): Key to be used in buttons dict
            rect (pygame.Rect): Pygame rect object
            action (None, optional): Function to execute when the button is clicked

        Raises:
            KeyError
        """
        if key_in_dict(button_name, self.buttons):
            raise KeyError("Button name {} already attributed.".format(button_name))

        self.buttons[button_name] = ButtonRect(rect, self.display, action=action)

    def create_button_from_image(self, button_name, img, pos, display, resize_img=1, action=None):
        """Create a button from an image (a pygame Surface).

        Args:
            button_name (str): Key to be used in buttons dict
            img (pygame.Surface): Button image
            pos (int tuple): Position to draw image
            display (pygame.Surface): Surface to draw the button on
            resize_img (int, optional): Change image size by multipliyng current size by resize_img
            action (None, optional): Function to execute when the button is clicked

        Raises:
            KeyError
        """
        if key_in_dict(button_name, self.buttons):
            raise KeyError("Button name {} already attributed.".format(button_name))

        self.buttons[button_name] = ButtonImage(img, pos, display, resize_img=resize_img, action=action)

    def label(self, name, pos, text, size, color=BLACK, fonts=None, center=False):
        """Create a text label.

        Args:
            name (str): Key to be used in labels dict
            pos (int tuple): Position to draw label on surface
            text (str): Text to show
            size (int): Font size
            color (int tuple, optional): Text color
            fonts (None, optional): Text font
            center (bool, optional): If true, text is centered around pos, else it is draw at pos.

        Raises:
            KeyError
        """
        if key_in_dict(name, self.labels):
            raise KeyError("Label name {} already attributed.".format(name))

        if fonts is None:
            fonts = self.font_path

        label = Label(pos, text, size, self.display, color=color, fonts=fonts, center=center)
        self.labels[name] = label

    def label_update_text(self, label_name, text):
        """Update label text

        Args:
            label_name (str): Key to access label in labels dict
            text (str): New text

        Raises:
            KeyError: Raise error if label name doesn't exist
        """
        if not key_in_dict(label_name, self.labels):
            raise KeyError("Label name {} does not exist.".format(label_name))

        self.labels[label_name].update_text(text)

    def update(self):
        """Update all gui element. All buttons are checked wether they are active or not.
        """
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            self.buttons[button].update(mouse_pos)

    def draw(self, display):
        """Draw gui surface on display

        Args:
            display (pygame.Surface): Display to draw on Gui surface
        """
        self.display.fill((0, 0, 0, 0))
        for key in self.labels:
            self.labels[key].draw()

        for key in self.buttons:
            self.buttons[key].draw()

        display.blit(self.display, (0, 0))
