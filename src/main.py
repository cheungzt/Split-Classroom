import pygame
import sys
from game import Game
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, TITLE

def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    game = Game(screen)
    
    game.teacher_text_bounds = {
        'width': 350,
        'height': 269,
        'left': 857,
        'top': 359
    }
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_event(event)
            
        game.update()
        game.draw()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main() 