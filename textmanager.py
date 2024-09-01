import pygame.font


class TextManager:
    def __init__(self,screen):
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Arial',25)
        self.screen = screen

    def create_label(self, label, COLOR, x, y):
        self.text_surface = self.my_font.render(label,False,COLOR)
        self.screen.blit(self.text_surface, (x,y))
