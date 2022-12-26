import os  # noqa
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"  # noqa
import pygame  # noqa

from .gui import *  # noqa
from .gui_element import *  # noqa
from .var import *  # noqa
from .menu import Menu  # noqa
from .gui_basic import *  # noqa
from .button_property import *  # noqa

pygame.init()
pygame.font.init()
