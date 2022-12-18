import time
import pygame


class Rules:
    def __init__(self):
        return

    # game over function
    def game_over(self, score, color, x, y, screen):
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render('Your Score is : ' + str(score), True, color)

        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()

        # setting position of the text
        game_over_rect.midtop = (x / 2, y / 4)

        # blit will draw the text on screen
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # after 2 seconds we will quit the
        # program
        time.sleep(2)

        # deactivating pygame library
        pygame.quit()

        # quit the program
        quit()