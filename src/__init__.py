import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

from .hud import *
from .var import *
from .menu import Menu

pygame.init()
pygame.font.init()
