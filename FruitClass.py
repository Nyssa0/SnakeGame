import random
import numpy
import pygame


class Fruit:

    def __init__(self, x, y, img):
        image_size = (10, 10)
        self.img = img
        # Changing the size of the image
        self.img = pygame.transform.scale(self.img, image_size)

        self.img.convert()

        self.position = [random.randrange(1, (x // 10)) * 10,
                         random.randrange(1, (y // 10)) * 10]
        self.spawn = True

    def new_position(self, x, y):
        self.position = [random.randrange(1, (x // 10)) * 10,
                         random.randrange(1, (y // 10)) * 10]

    def show_fruit(self, screen, color):
        rect = self.img.get_rect()
        position = numpy.add(self.position, 5)
        rect.center = position
        screen.blit(self.img, rect)
        pygame.draw.rect(screen, color, rect, 1)

    def get_bonus(self, score, difficulty, speed):
        if difficulty == 1:
            score = score + 5
        if difficulty == 2:
            score += 10
            speed *= 1.25
        if difficulty == 3:
            score += 15
            speed *= 1.5
        self.spawn = False
        return score, speed

    def get_malus(self, score, difficulty, speed):
        if difficulty == 1:
            score -= 5
            speed *= 1.5
        elif difficulty == 2:
            score -= 10
            speed *= 1.75
        elif difficulty == 3:
            score -= 15
            speed *= 2
        self.spawn = False
        return score, speed

    def get_health(self, hp):
        hp += 1
        self.spawn = False
        return hp

    def fruit_spawn(self, x, y):
        if not self.spawn:
            self.new_position(x, y)
        self.spawn = True
