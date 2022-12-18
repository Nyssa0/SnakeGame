import pygame


class Score:

    def __init__(self):
        # initial score
        self.point = 0

    # displaying Score function
    def show_score(self, choice, color, font, size, score, screen):
        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)

        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)

        # create a rectangular object for the
        # text surface object
        score_rect = score_surface.get_rect()

        # displaying text
        screen.blit(score_surface, score_rect)
