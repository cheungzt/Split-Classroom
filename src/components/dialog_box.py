import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import *

class DialogBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        try:
            self.font = pygame.font.Font(CHINESE_FONT, FONT_SIZE)
        except Exception as e:
            print(f"警告：对话框加载字体出错 - {e}")
            self.font = pygame.font.Font(None, FONT_SIZE)
        
    def draw(self, screen, text):
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        
        # 修改文本换行处理，支持中文
        text_width = self.rect.width - DIALOG_PADDING * 2
        x = self.rect.x + DIALOG_PADDING
        y = self.rect.y + DIALOG_PADDING
        
        # 按字符分割文本
        chars = list(text)
        current_line = ""
        
        for char in chars:
            test_line = current_line + char
            text_surface = self.font.render(test_line, True, BLACK)
            
            if text_surface.get_width() > text_width:
                # 当前行已满，绘制当前行并开始新行
                line_surface = self.font.render(current_line, True, BLACK)
                screen.blit(line_surface, (x, y))
                y += line_surface.get_height() + 5
                current_line = char
            else:
                current_line += char
        
        # 绘制最后一行
        if current_line:
            line_surface = self.font.render(current_line, True, BLACK)
            screen.blit(line_surface, (x, y))