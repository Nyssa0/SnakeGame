import pygame


class Player:

    def __init__(self):
        self.difficulty = int(input("Choose difficulty ( type 1 for easy, 2 for medium and 3 for hard ) : "))
        if self.difficulty == 1:
            self.hp = 6
        if self.difficulty == 2:
            self.hp = 4
        if self.difficulty == 3:
            self.hp = 2

    # displaying Score function
    def show_hp(self, choice, color, font, size, hp, screen, x, y):
        # creating font object score_font
        hp_font = pygame.font.SysFont(font, size)

        # create the display surface object
        # score_surface
        hp_surface = hp_font.render('HP : ' + str(hp), True, color)

        # create a rectangular object for the
        # text surface object
        hp_rect = hp_surface.get_rect()

        hp_rect.topright = (x,y)

        # displaying text
        screen.blit(hp_surface, hp_rect)
