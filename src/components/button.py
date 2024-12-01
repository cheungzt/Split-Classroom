import pygame
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import *

class Button:
    def __init__(self, rect, color=(255, 255, 255), is_circle=False):
        self.rect = rect
        self.color = color
        self.text = ""
        self.text_color = (0, 0, 0)
        self.image = None
        try:
            self.font = pygame.font.Font(CHINESE_FONT, FONT_SIZE_SMALL)
        except:
            print("警告：无法加载中文字体，使用默认字体")
            self.font = pygame.font.Font(None, FONT_SIZE_SMALL)
        self.is_hovered = False
        self.is_circle = is_circle

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        elif self.color:
            pygame.draw.rect(screen, self.color, self.rect)
        
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
        